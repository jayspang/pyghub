"""
Unit tests for github.py
"""
import mock
import os
import pytest
import unittest

from requests import RequestException
from pyghub.providers.github import Github # pylint: disable=import-error

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

class TestGetRepos(unittest.TestCase):
    """
    Tests for Github.get_repos
    """
    def setup(self):
        pass

    @mock.patch("requests.get")
    def test_get_repos_raises_on_failure(self, mock_get):
        gh = Github("fake_token")
        mock_get.side_effect = RequestException("Failure to launch!")
        with pytest.raises(Exception):
            gh.get_repos()

    @mock.patch("requests.get")
    def test_get_repos_succeeds(self, mock_get):
        gh = Github("fake_token")
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = "foo"
        result = gh.get_repos()
        assert result is not None

class TestGetRepo(unittest.TestCase):
    """
    Tests for Github.get_repo
    """
    def setup(self):
        pass

    @mock.patch("requests.get")
    def test_get_repo_raises_on_failure(self, mock_get):
        gh = Github("fake_token")
        mock_get.side_effect = RequestException("Failure to launch!")
        with pytest.raises(Exception):
            gh.get_repo("fake_owner", "fake_repo")
        
    @mock.patch("requests.get")
    def test_get_repo_fails_if_repo_not_found(self, mock_get):
        gh = Github("fake_token")
        mock_get.return_value.status_code = 404
        with pytest.raises(Exception):
            gh.get_repo("fake_owner", "fake_repo")

    @mock.patch("requests.get")
    def test_get_repo_succeeds(self, mock_get):
        gh = Github("fake_token")
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = "foo"
        result = gh.get_repo("fake_owner", "fake_repo")
        assert result is not None