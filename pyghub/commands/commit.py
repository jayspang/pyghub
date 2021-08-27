"""
CLI command for committing to a local.
"""
import argparse
from pyghub.providers.git import Git # pylint: disable=import-error


def execute_command(args: argparse.Namespace) -> int:
    """
    Executes the command described in this file.

    This particular command uses PyGithub to commit all changes
    to a local repo.

    Args:
        args (as in, the arguments from this command's subparser)

    Returns:
        return code (0 for success, 1 for failure)
    """
    g = Git()
    g.commit(args.repo_path, args.commit_message)
    return 0


def register_subparser(subparser) -> None:
    """
    Registers this command's parser with argparse

    Args:
        subparser object

    Returns:
        None
    """
    parser = subparser.add_parser(
        "commit", help="Commit to a repository."
    )

    parser.add_argument(
        "-r", "--repo-path", help="Path to local git repository."
    )

    parser.add_argument(
        "-m", "--commit-message", help="Commit message."
    )

    parser.set_defaults(func=execute_command)
