import mock
import pytest
import unittest

from pyghub.github import *

class TestGithub(unittest.TestCase):
    def setup(self):
        pass

    def test_fails_without_api_token(self):
        with pytest.raises(Exception):
            Github()
