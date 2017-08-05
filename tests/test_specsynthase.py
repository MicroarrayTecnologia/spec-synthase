import pytest
import yaml

from os import path
from swagger_spec_validator import SwaggerValidationError
from specsynthase.specbuilder import SpecBuilder


def _get_base_dir():
    return path.join(path.abspath(path.dirname(__file__)), "fixtures", "petstore")


def _check_dicts(l, r):
    for k, v in l.items():
        assert (k in r)
        if isinstance(v, dict):
            _check_dicts(v, r[k])


def test_build_fluent():
    base_dir = _get_base_dir()
    full = yaml.load(open(path.join(base_dir, "full.yml")).read())
    spec = SpecBuilder().add_spec(path.join(base_dir, "security.yml"))\
                        .add_spec(path.join(base_dir, "base.yml"))\
                        .add_spec(path.join(base_dir, "definitions.yml"))\
                        .add_spec(path.join(base_dir, "paths.yml"))
    _check_dicts(full, spec)
    _check_dicts(spec, full)


def test_build_existing_key():
    base_dir = _get_base_dir()
    with pytest.raises(ValueError):
        SpecBuilder().add_spec(path.join(base_dir, "base.yml"))\
                     .add_spec(path.join(base_dir, "definitions.yml"))\
                     .add_spec(path.join(base_dir, "definitions.yml"))


def test_dump():
    base_dir = _get_base_dir()
    parts = ["base.yml", "definitions.yml", "paths.yml", "security.yml"]
    full = yaml.load(open(path.join(base_dir, "full.yml")).read())

    spec = SpecBuilder()
    for p in parts:
        spec.add_spec(path.join(base_dir, p))

    # Dumping and reloading the yaml is slow, but we can't compare dumped
    # strings because of potential key ordering differences.
    assert full == yaml.load(spec.dump())


def test_validation_fail():
    base_dir = _get_base_dir()
    with pytest.raises(SwaggerValidationError):
        SpecBuilder().add_spec(path.join(base_dir, "base.yml")).validate()
