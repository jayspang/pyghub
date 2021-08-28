"""
Unit tests for git.py
"""
import mock
import pytest
import unittest

from pyghub.providers.git import Git # pylint: disable=import-error
from git import GitCommandError


class TestConstructor(unittest.TestCase):
    """
    Tests for git:Git Constructor
    """
    def setup(self):
        pass

    def test_constructor_does_not_raise(self):
        Git()

class TestCloneRepo(unittest.TestCase):
    """
    Tests for git.clone_repo
    """
    def setup(self):
        pass

    @mock.patch("os.path.exists")
    def test_fails_if_path_exists(self, mock_path_exists):
        g = Git()
        mock_path_exists.return_value = True
        with pytest.raises(Exception):
            g.clone_repo("https://fake_repo", "c:\\fake_dir")

    @mock.patch("git.Repo.clone_from")
    def test_clones_valid_repo_successfully(self, mock_clone_from):
        g = Git()
        mock_clone_from.return_value = 0
        g.clone_repo("https://fake_repo", "c:\\fake_dir")

    @mock.patch("git.Repo.clone_from")
    def test_fails_to_clone_invalid_repo(self, mock_clone_from):
        g = Git()
        mock_clone_from.side_effect = GitCommandError("Repo not found")
        with pytest.raises(Exception):
            g.clone_repo("https://fake_repo", "c:\\fake_dir")

class TestCommit(unittest.TestCase):
    """
    Tests for git.commit
    """
    def setup(self):
        pass

    @mock.patch("os.path.exists")
    def test_fails_if_path_exists(self, mock_path_exists):
        g = Git()
        mock_path_exists.return_value = True
        with pytest.raises(Exception):
            g.commit("c:\\fake_dir", "Fake commit message")

    @mock.patch("os.path.exists")
    @mock.patch("git.Repo.init")
    def test_commits_successfully_with_message(self, mock_repo, mock_path_exists):
        commit_message = "Fake commit message"
        g = Git()
        mock_path_exists.return_value = True
        mock_repo = mock.Mock()
        g.commit("c:\\fake_path", commit_message)
        assert mock_repo.git.add.called_with(".")
        assert mock_repo.index.commit.called_with(commit_message)

    @mock.patch("os.path.exists")
    @mock.patch("git.Repo.init")
    def test_commit_raises_exception_on_failure(self, mock_repo, mock_path_exists):
        commit_message = "Fake commit message"
        g = Git()
        mock_path_exists.return_value = True
        mock_repo.side_effect = GitCommandError("Failure to launch!")
        with pytest.raises(Exception):
            g.commit("c:\\fake_path", commit_message)


class TestPull(unittest.TestCase):
    """
    Tests for git.pull
    """
    def setup(self):
        pass

    @mock.patch("os.path.exists")
    def test_fails_if_path_does_not_exist(self, mock_path_exists):
        g = Git()
        mock_path_exists.return_value = False
        with pytest.raises(Exception):
            g.pull("c:\\fake_dir", "origin", "main")

    @mock.patch("os.path.exists")
    @mock.patch("git.Repo.init")
    def test_pulls_successfully(self, mock_repo, mock_path_exists):
        branch = "main"
        g = Git()
        mock_path_exists.return_value = True
        mock_repo = mock.Mock()
        g.pull("c:\\fake_dir", "origin", branch)
        assert mock_repo.remotes.called_with(branch)

    @mock.patch("os.path.exists")
    @mock.patch("git.Repo.init")
    def test_pull_raises_exception_on_failure(self, mock_repo, mock_path_exists):
        g = Git()
        mock_path_exists.return_value = True
        mock_repo.side_effect = GitCommandError("Failure to launch!")
        with pytest.raises(Exception):
            g.pull("c:\\fake_dir", "origin", "main")

class TestPush(unittest.TestCase):
    """
    Tests for git.push
    """
    def setup(self):
        pass

    @mock.patch("os.path.exists")
    def test_fails_if_path_does_not_exist(self, mock_path_exists):
        g = Git()
        mock_path_exists.return_value = False
        with pytest.raises(Exception):
            g.push("c:\\fake_dir", "origin", "main")

    @mock.patch("os.path.exists")
    @mock.patch("git.Repo.init")
    def test_pushes_successfully(self, mock_repo, mock_path_exists):
        branch = "main"
        g = Git()
        mock_path_exists.return_value = True
        mock_repo = mock.Mock()
        g.push("c:\\fake_dir", "origin", branch)
        assert mock_repo.remotes.called_with(branch)

    @mock.patch("os.path.exists")
    @mock.patch("git.Repo.init")
    def test_push_raises_exception_on_failure(self, mock_repo, mock_path_exists):
        g = Git()
        mock_path_exists.return_value = True
        mock_repo.side_effect = GitCommandError("Failure to launch!")
        with pytest.raises(Exception):
            g.push("c:\\fake_dir", "origin", "main")

