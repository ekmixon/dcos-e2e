"""
Click arguments which are common across CLI tools.
"""

from typing import Callable

import click
import click_pathlib


def dcos_checkout_dir_argument(command: Callable[..., None],
                               ) -> Callable[..., None]:
    """
    Decorate a function to allow choosing a DC/OS checkout directory.
    """
    return click.argument(
        'dcos_checkout_dir',
        type=click_pathlib.Path(exists=True),
        envvar='DCOS_CHECKOUT_DIR',
        default='.',
    )(command)


def node_args_argument(command: Callable[..., None]) -> Callable[..., None]:
    """
    Decorate a function to allow choosing arguments to run on a node.
    """
    return click.argument(
        'node_args',
        type=str,
        nargs=-1,
        required=True,
    )(command)


def installer_path_argument(command: Callable[..., None],
                            ) -> Callable[..., None]:
    """
    Argument to choose a DC/OS installer URL.
    """
    return click.argument(
        'installer',
        type=click_pathlib.Path(
            exists=True,
            dir_okay=False,
            file_okay=True,
            resolve_path=True,
        ),
    )(command)


def installer_url_argument(command: Callable[..., None],
                           ) -> Callable[..., None]:
    """
    Argument to choose a DC/OS installer URL.
    """
    return click.argument(
        'installer_url',
        type=str,
    )(command)
