"""
Unit tests for Github.py
"""
import mock
import os
import pytest
import unittest

from pyghub.github import Github # pylint: disable=import-error

class TestConstructor(unittest.TestCase):
    """
    Tests for Github:Github Constructor
    """
    def setup(self):
        pass

    def test_constructor_fails_without_api_token(self):
        with pytest.raises(Exception):
            Github()

    def test_constructor_does_not_fail_with_api_token_as_arg(self):
        gh = Github("fake_token")
        assert gh is not None

    @mock.patch.dict(os.environ, {"GH_TOKEN": "fake_token"})
    def test_constructor_does_not_fail_with_api_token_as_env_var(self):
        gh = Github()
        assert gh is not None
