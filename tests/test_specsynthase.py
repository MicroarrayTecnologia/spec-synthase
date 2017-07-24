import os
from os import path
import yaml

from specsynthase.specbuilder import SpecBuilder


def test_main():
    spec = SpecBuilder()


def test_dump():
    base_dir = path.join(path.abspath(path.dirname(__file__)), "fixtures", "petstore")
    parts = ["base.yml", "definitions.yml", "paths.yml"]
    full = yaml.load(open(path.join(base_dir, "full.yml")).read())

    spec = SpecBuilder()
    for p in parts:
        spec.add_spec(path.join(base_dir, p))

    assert full == spec
