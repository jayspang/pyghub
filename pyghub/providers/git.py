"""
A library for interfacing with git.

    Typical usage examples:
    g = git()
    repo = g.clone("https://github.com/owner/repo")
"""
import os
from git import Repo, GitCommandError

class Git:
    """
    Main class for interfacing with Git
    """
    def __init__(self, api_token: str=None) -> None:
        """Inits Git"""
        pass


    def clone_repo(self, repo_url: str, path: str) -> None:
        """
        Clones the specified git repository.

        A repository URL looks like this: https://github.com/owner/repo

        Args:
            repo_url: The repository URL, either https or ssh
            path: The local path to clone into

        Returns:
            None

        Raises:
            Exception - Failed to clone
        """
        if os.path.exists(path):
            raise Exception("Destination path already exists. Cannot clone repository. ({})".format(path))

        return Repo.clone_from(repo_url, path)

    def commit(self, repo_path: str, commit_message) -> None:
        """
        Commits all changes to a local repository with the provided message.

        Args:
            repo_path: Local path to the repository to commit to.
            commit_message: Commit message.

        Returns:
            None

        Raises:
            Exception - Failed to commit
        """
        if not os.path.exists(repo_path):
            raise Exception("Unable to find a git repository at the specified path. ({})".format(repo_path))

        repo = Repo.init(repo_path)
        repo.git.add(".")
        repo.index.commit(commit_message)

        return 0

    def pull(self, repo_path: str, remote: str = "origin", branch: str = None) -> None:
        """
        Pulls all changes from a remote repository. Remote and Branch can
        be specified, otherwise defaults to the equiv of 'git pull'.

        Args:
            repo_path: Local path to the repository to commit to.
            remote (optional): remote repostitory
            branch: branch name

        Returns:
            None

        Raises:
            Exception - Failed to pull
        """
        if not os.path.exists(repo_path):
            raise Exception("Unable to find a git repository at the specified path. ({})".format(repo_path))

        try:
            repo = Repo.init(repo_path)
            if branch:
                repo.remotes[remote].pull(branch)
            else:
                repo.remotes[remote].pull()
        except GitCommandError as e:
            raise Exception("Failed to pull: {}".format(e))
        return 0
