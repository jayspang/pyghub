"""
Exposes a command line interface for Github.py
"""
import json
from pyghub.github import Github

if __name__ == "__main__":
    gh = Github("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")
    parsed = json.loads(gh.get_repos())
    print(json.dumps(parsed, indent=4, sort_keys=True))
