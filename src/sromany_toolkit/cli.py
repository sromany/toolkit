import logging

import click
from loguru import logger

from sromany_toolkit.helpers.loadings import loading_bar


@click.command()
@click.option(
    "--name",
    help="The person to greet.",
)
def hello(name: str) -> None:
    """
    Say hello to <name> from command-line argument

    Args:
        name:

    Returns: Nothing

    Example:
    """
    click.echo(f"Hello {name}!")
    logger.log(logging.INFO, "✅ Hello executed.")


def something() -> None:
    res = click.confirm("Haaaaaa, something happened")
    logger.log(logging.INFO, res)


if __name__ == "__main__":
    loading_bar()
