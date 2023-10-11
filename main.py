from mylib.dbfunc import connectDB, createDB, insertDB, readDB, updateDB, deleteDB
import os
import click
@click.command()
@click.argument("db")
def main(db):

    if os.path.exists(db):
        os.remove(db)
    conn, cursor = connectDB(db)
    # C
    click.echo("Connection success")
    createDB(cursor)
    click.echo("Inserting data...")
    insertDB(cursor, 1, "Ethan", "Smith", 20, 1)
    insertDB(cursor, 2, "Emma", "Brown", 21, 2)
    insertDB(cursor, 3, "Lucas", "Davis", 18, 3)
    # R
    info = readDB(cursor)
    click.echo("Read current table:")
    click.echo(info)

    # U
    click.echo("\n")
    click.echo("Updata data1")
    updateDB(cursor, 1, "Ethan", "James", 23, 5)
    info = readDB(cursor)
    click.echo("Read current table:")
    click.echo(info)

    # D
    click.echo("\n")
    click.echo("Delete data2:")
    deleteDB(cursor, 2)
    info = readDB(cursor)
    click.echo("Read current table:")
    click.echo(info)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
