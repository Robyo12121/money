import click
import transaction

@click.group()
def money():
    pass

@money.command()
@click.option('date')
def expense():
    pass

@money.command()
def income():
    pass

@money.command()
def report():
    pass


if __name__ == '__main__':
    money()
