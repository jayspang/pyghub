"""
A library for interfacing with the Github REST API.

    Typical usage examples:
    gh = Github("api_token")
    repo = gh.get_repo("owner", "repo")
"""
import os
import requests

class Github:
    """
    Main class for interfacing with Github.com

    Args:
        api_token: Can be either an arg or the GH_TOKEN env var.
    """
    def __init__(self, api_token: str=None) -> None:
        """Inits Gihub"""
        assert api_token is not None or os.environ["GH_TOKEN"] is not None
        self.github_url = "https://api.github.com/"
        self.api_token = api_token or os.environ["GH_TOKEN"]
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": "token %s" % self.api_token
        }

    def get_repos(self) -> str:
        """
        Gets a list of repos available to the current user.

        Args:
            None

        Returns:
            List of repos (JSON)

        Raises:
            Exception - Failed to retrieve requested information
        """

        repos_url = self.github_url + "user/repos"
        req = requests.get(repos_url, headers=self.headers)
        if req.status_code == 200:
            return req.content

        raise Exception("Failed to get repos")

    def get_repo(self, owner: str, repo_name: str) -> str:
        """
        Grabs the details of a specific github repo.

        A repository URL looks like this: https://github.com/owner/repo

        Args:
            owner: The owner name
            repo: The repository name

        Returns:
            Dict of repository information (JSON)

        Raises:
            Exception - Failed to retrieve requested information
        """

        repos_url = self.github_url + "repos/{}/{}".format(owner, repo_name)
        req = requests.get(repos_url, headers=self.headers)
        if req.status_code == 200:
            ret = req.content
            return ret

        raise Exception("Failed to get repo information")
