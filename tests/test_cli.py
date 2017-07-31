import sys
import yaml
from os import path
from specsynthase.cli import main


def test_cli():
    base_dir = path.join(path.abspath(path.dirname(__file__)), "fixtures", "petstore")
    full = path.join(base_dir, "full.yml")
    sys.argv[1] = full
    main()