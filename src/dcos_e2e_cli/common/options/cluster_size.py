"""
Options for choosing the cluster size.
"""

from typing import Callable

import click


def masters_option(command: Callable[..., None]) -> Callable[..., None]:
    """
    An option decorator for the number of masters.
    """
    return click.option(
        '--masters',
        type=click.INT,
        default=1,
        show_default=True,
        help='The number of master nodes.',
    )(command)


def agents_option(command: Callable[..., None]) -> Callable[..., None]:
    """
    An option decorator for the number of agents.
    """
    return click.option(
        '--agents',
        type=click.INT,
        default=1,
        show_default=True,
        help='The number of agent nodes.',
    )(command)


def public_agents_option(command: Callable[..., None]) -> Callable[..., None]:
    """
    An option decorator for the number of agents.
    """
    return click.option(
        '--public-agents',
        type=click.INT,
        default=1,
        show_default=True,
        help='The number of public agent nodes.',
    )(command)
