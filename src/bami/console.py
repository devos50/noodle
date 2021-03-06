# src/project_name/console.py
import textwrap

import click

from . import __version__


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="Language of Wikipedia page",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language: str) -> None:
    """Output extract from a random page with a language

    Args:
        language: Wikipedia page language, default 'en'.
    """
    click.secho("Title", fg="green")
    click.echo(textwrap.fill("Extract"))
