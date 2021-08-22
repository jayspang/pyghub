"""
Exposes a command line interface for the Github module.
"""
import argparse
import json
from pyghub.github import Github

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--api-token', help='Github.com API token')
    args = parser.parse_args()

    gh = Github(args.api_token)
    parsed = json.loads(gh.get_repos())
    print(json.dumps(parsed, indent=4, sort_keys=True))
