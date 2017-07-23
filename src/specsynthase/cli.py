from __future__ import print_function
import sys
import yaml

from .specbuilder import SpecBuilder


def main():
    spec = SpecBuilder()
    for f in sys.argv[1:]:
        spec.add_spec(f)
    print(yaml.dump(spec))
