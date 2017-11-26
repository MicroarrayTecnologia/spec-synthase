import yaml
from collections import OrderedDict
from swagger_spec_validator.validator20 import validate_spec


class SpecBuilder(OrderedDict):
    def __init__(self, *args, **kwargs):
        OrderedDict.__init__(self, *args, **kwargs)
        self._mergeable_keys = ["definitions", "parameters", "paths", "responses", "securityDefinitions"]

    def _load_spec(self, file_name):
        with open(file_name, 'r') as spec_file:
            return yaml.load(spec_file)

    def _merge_part(self, key, part_dict):
        if part_dict:
            if key not in self:
                self[key] = {}
            self._merge_dict(self[key], part_dict)

    def _merge_dict(self, main_dict, part_dict):
        self._test_merge(main_dict, part_dict)
        main_dict.update(part_dict)

    def _test_merge(self, main_dict, part_dict):
        for k, v in part_dict.items():
            if k in main_dict:
                raise ValueError("Key {} already exists in spec file.".format(k))

    def _cut_part(self, spec, key):
        part = {}
        if key in spec:
            part = spec[key]
            del spec[key]
        return part

    def _cut_parts(self, spec):
        parts = []
        for merg_key in self._mergeable_keys:
            parts.append((merg_key, self._cut_part(spec, merg_key)))
        return parts

    def add_spec(self, file_name):
        spec = self._load_spec(file_name)
        parts = self._cut_parts(spec)
        self._merge_dict(self, spec)
        for merg_key, spec_part in parts:
            self._merge_part(merg_key, spec_part)
        return self

    def dump(self, *args, **kwargs):
        return yaml.safe_dump(dict(**self), *args, **kwargs)

    def validate(self):
        validate_spec(self)
        return self
