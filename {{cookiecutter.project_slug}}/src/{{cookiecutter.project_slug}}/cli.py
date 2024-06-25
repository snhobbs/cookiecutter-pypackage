"""Console script for {{cookiecutter.project_slug}}."""
import {{cookiecutter.project_slug}}

import click
import sys
import logging

_log = logging.getLogger("{{cookiecutter.project_slug}}")


@click.command()
@click.version_option()
def main():
    """Console script for {{cookiecutter.project_slug}}."""
    return




if __name__ == "__main__":
    logging.basicConfig()
    sys.exit(main())
