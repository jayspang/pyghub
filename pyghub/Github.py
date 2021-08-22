"""
Library for interfacing with the Github REST API
"""
import os
import requests

class Github:
    """
    Main class for interfacing with Github.com
    An API token is required, either as an arg or with the GH_TOKEN env var.
    """
    def __init__(self, api_token: str=None) -> None:
        assert api_token is not None or os.environ["GH_TOKEN"] is not None
        self.github_url = "https://api.github.com/"
        self.api_token = api_token or os.environ["GH_TOKEN"]
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": "token %s" % self.api_token
        }

    def get_events(self) -> str:
        """Hits github"s /events end point to retrieve events"""

        events_url = self.github_url + "events"
        req = requests.get(events_url, headers=self.headers)
        if req.status_code == 200:
            return req.content

        raise Exception("Failed to get events")

    def get_repos(self) -> str:
        """Hits github"s /user/repos end point to retrieve events"""

        repos_url = self.github_url + "user/repos"
        req = requests.get(repos_url, headers=self.headers)
        if req.status_code == 200:
            return req.content

        raise Exception("Failed to get repos")

    def get_repo(self, owner: str, repo_name: str) -> str:
        """Grabs the details of a specific github repo"""

        repos_url = self.github_url + "repos/{}/{}".format(owner, repo_name)
        req = requests.get(repos_url, headers=self.headers)
        if req.status_code == 200:
            ret = req.content
            return ret

        raise Exception("Failed to get repo information")
