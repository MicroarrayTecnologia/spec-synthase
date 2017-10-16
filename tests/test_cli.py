import sys
import pytest

from os import path
from swagger_spec_validator import SwaggerValidationError
from specsynthase.cli import main


def test_cli():
    base_dir = path.join(path.abspath(path.dirname(__file__)), "fixtures", "petstore")
    full = path.join(base_dir, "full.yml")
    sys.argv[1] = full
    main()


def test_validation_fail():
    base_dir = path.join(path.abspath(path.dirname(__file__)), "fixtures", "petstore")
    with pytest.raises(SwaggerValidationError):
        base = path.join(base_dir, "base.yml")
        sys.argv[1] = base
        main()
