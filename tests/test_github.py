import mock
import pytest
import unittest

from pyghub.github import Github # pylint: disable=import-error

class TestGithub(unittest.TestCase):
    def setup(self):
        pass

    def test_fails_without_api_token(self):
        with pytest.raises(Exception):
            Github()

    def test_does_not_fail_with_api_token(self):
        gh = Github('fake_auth_token')
        assert gh is not None
