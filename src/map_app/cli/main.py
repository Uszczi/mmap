import click

from map_app.cli.load_data import load_data as _load_data


@click.group()
def cli():
    pass


@cli.command()
def load_data():
    _load_data()


if __name__ == "__main__":
    cli()
