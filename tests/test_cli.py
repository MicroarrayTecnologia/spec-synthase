from mock import patch
import pytest

from os import path
from swagger_spec_validator import SwaggerValidationError
from specsynthase.cli import main


def test_cli():
    base_dir = path.join(path.abspath(path.dirname(__file__)), "fixtures", "petstore")
    full = path.join(base_dir, "full.yml")
    with patch('sys.argv', [__name__, full]):
        main()


def test_validation_fail():
    base_dir = path.join(path.abspath(path.dirname(__file__)), "fixtures", "petstore")
    with pytest.raises(SwaggerValidationError):
        base = path.join(base_dir, "base.yml")
        with patch('sys.argv', [__name__, base]):
            main()
