"""
Tests for the AWS CLI.

This mostly provides error case coverage.
We rely mostly on manual testing.
This is because automated tests for this would be very slow.
"""

import os
from pathlib import Path
from textwrap import dedent
from typing import List

import pytest
from click.testing import CliRunner

from cli import dcos_aws


class TestDcosAWS:
    """
    Tests for the top level `dcos-aws` command.
    """

    def test_version(self) -> None:
        """
        The CLI version is shown with ``dcos-aws --version``.
        """
        runner = CliRunner()
        result = runner.invoke(
            dcos_aws,
            ['--version'],
            catch_exceptions=False,
        )

        assert result.exit_code == 0
        expected = 'dcos-aws, version'
        assert expected in result.output


class TestDoctor:
    """
    Tests for the ``doctor`` subcommand.
    """

    def test_doctor(self) -> None:
        """
        No exception is raised by the ``doctor`` subcommand.
        """
        runner = CliRunner()
        result = runner.invoke(
            dcos_aws,
            ['doctor'],
            catch_exceptions=False,
        )
        assert result.exit_code == 0

_SUBCOMMANDS = [[item] for item in dcos_aws.commands.keys()]
_BASE_COMMAND = [[]]  # type: List[List[str]]
_COMMANDS = _BASE_COMMAND + _SUBCOMMANDS


class TestHelp:
    """
    Test help texts.
    """

    @pytest.mark.parametrize(
        'command',
        _COMMANDS,
        ids=[str(cmd) for cmd in _COMMANDS],
    )
    def test_help(self, command: List[str]) -> None:
        """
        Expected help text is shown for ``dcos-aws`` commands.

        This help text is defined in files.
        To update these files, run the command
        ``bash admin/update_cli_tests.sh``.
        """
        runner = CliRunner()
        arguments = command + ['--help']
        result = runner.invoke(dcos_aws, arguments, catch_exceptions=False)
        assert result.exit_code == 0
        help_output_filename = '-'.join(['dcos-aws'] + command) + '.txt'
        help_outputs_dir = Path(__file__).parent / 'help_outputs'
        expected_help_file = help_outputs_dir / help_output_filename
        try:
            expected_help = expected_help_file.read_text()
            assert result.output == expected_help
        except (AssertionError, FileNotFoundError):  # pragma: no cover
            if os.getenv('FIX_CLI_TESTS') == '1':
                help_outputs_dir.mkdir(exist_ok=True)
                expected_help_file.touch()
                expected_help_file.write_text(result.output)
            else:
                raise
