"""
CLI command for getting repository information.
"""
import argparse
import json
from pyghub.github import Github # pylint: disable=import-error


def execute_command(args: argparse.Namespace) -> int:
    gh = Github(args.api_token)
    parsed = json.loads(gh.get_repo(args.owner, args.repo))
    print(json.dumps(parsed, indent=4, sort_keys=True))
    return 0


def register_subparser(subparser) -> None:
    parser = subparser.add_parser(
        "get_repo", help="Get repository information"
    )

    parser.add_argument(
        "-o", "--owner", help="Ower of the repository."
    )

    parser.add_argument(
        "-r", "--repo", help="Repository name."
    )

    parser.set_defaults(func=execute_command)
