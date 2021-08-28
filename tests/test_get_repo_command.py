"""
Unit tests for commands/get_repo.py
"""
import argparse
import mock
import json
import os
import pytest
import unittest

import pyghub.commands.get_repo

class TestGetRepoCommand(unittest.TestCase):
    """
    Tests for pyghub.commands.get_repo command
    """
    def setup(self):
        pass

    def test_register_subparser(self):
        subparser = mock.Mock()
        subparser.add_parser.return_value = subparser

        pyghub.commands.get_repo.register_subparser(subparser)

        subparser.add_parser.assert_called_once_with("get_repo", help=mock.ANY)
        subparser.add_argument.assert_any_call("-o", "--owner", help=mock.ANY)
        subparser.add_argument.assert_any_call("-r", "--repo", help=mock.ANY)

        subparser.set_defaults.assert_called_once_with(func=pyghub.commands.get_repo.execute_command)

    @mock.patch("requests.get")
    def test_execute_command_with_valid_input_succeeds(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = json.dumps({"foo":"bar"})

        input_args = argparse.Namespace()
        input_args.api_token = "fake_token"
        input_args.owner = "JohnDoe"
        input_args.repo = "myRepo"

        result = pyghub.commands.get_repo.execute_command(input_args)
        self.assertEqual(result, 0)

    @mock.patch("requests.get")
    def test_execute_command_raises_when_repo_not_found(self, mock_get):
        mock_get.return_value.status_code = 404

        input_args = argparse.Namespace()
        input_args.api_token = "fake_token"
        input_args.owner = "JohnDoe"
        input_args.repo = "myRepo"

        with pytest.raises(Exception):
            pyghub.commands.get_repo.execute_command(input_args)
