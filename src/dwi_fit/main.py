import click

from dwi_fit.ui import app


@click.command()
@click.option('--gui/--no-gui', default=False)
def main(gui):
    if gui:
        app.exec()
    else:
        click.echo('Hello World!')


if __name__ == '__main__':
   main() 
