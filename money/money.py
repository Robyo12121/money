import click
from money import Transaction


@click.group()
def money():
    pass


@money.command()
@click.argument('date', required=True, type=str)  # , help="Date of expsense")
@click.argument('amount', required=True, type=float)  # , help="Expense amount")
@click.option('-c', '--category', type=str, help="classify expense type")
@click.option('--note', type=str, help="Attach a note to this expense")
def expense(date, amount, category, note):
    click.echo(f"DATE: {date} AMOUNT: {str(amount)} CATEGORY: {category} NOTE: {note}")
    tr = Transaction(date, amount, category=category, note=note)
    print(tr)


@money.command()
@click.argument('date', required=True, type=str)  # , help="Date of expsense")
@click.argument('amount', required=True, type=float)  # , help="Expense amount")
@click.option('-c', '--category', type=str, help="classify expense type")
@click.option('--note', type=str, help="Attach a note to this expense")
def income(date, amount, category, note):
    click.echo(f"DATE: {date} AMOUNT: {str(amount)} CATEGORY: {category} NOTE: {note}")
    tr = Transaction(date, amount, expense=False, category=category, note=note)
    print(tr)


@money.command()
def report():
    pass


if __name__ == '__main__':
    money()
