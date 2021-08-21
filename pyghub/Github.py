"""
Library for interfacing with the Github REST API
"""
import requests

class Github:
    """
    Main class for interfacing with Github.com
    """
    def __init__(self, api_token):
        assert api_token is not None
        self.github_url = "https://api.github.com/"
        self.api_token = api_token
        self.headers = {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': 'token %s' % self.api_token
        }

    def get_events(self):
        """Hits github's /events end point to retrieve events"""
        events_url = self.github_url + "events"
        req = requests.get(events_url, headers=self.headers)
        if req.status_code == 200:
            return req.content

        raise Exception("Failed to get events")

    def get_repos(self):
        """Hits github's /user/repos end point to retrieve events"""
        repos_url = self.github_url + "user/repos"
        req = requests.get(repos_url, headers=self.headers)
        if req.status_code == 200:
            return req.content

        raise Exception("Failed to get events")
