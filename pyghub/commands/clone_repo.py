"""
CLI command for Cloning a remote repository.
"""
import argparse
from pyghub.providers.git import Git # pylint: disable=import-error


def execute_command(args: argparse.Namespace) -> int:
    """
    Executes the command described in this file.

    This particular command uses PyGithub to clone a remote repo.

    Args:
        args (as in, the arguments from this command's subparser)

    Returns:
        return code (0 for success, 1 for failure)
    """
    g = Git()
    g.clone_repo(args.repo_url, args.path)
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
        "clone_repo", help="Get repository information"
    )

    parser.add_argument(
        "-r", "--repo-url", help="Remote repository URL (either https or SSH)."
    )

    parser.add_argument(
        "-p", "--path", help="Local path to clone the repository into."
    )

    parser.set_defaults(func=execute_command)
