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
    createDB(cursor)
    insertDB(cursor, 1, "Ethan", "Smith", 20, 1)
    insertDB(cursor, 2, "Emma", "Brown", 21, 2)
    insertDB(cursor, 3, "Lucas", "Davis", 18, 3)
    # R
    info = readDB(cursor)

    click.echo(info)

    # U
    updateDB(cursor, 1, "Ethan", "James", 23, 5)
    info = readDB(cursor)
    click.echo(info)

    # D
    deleteDB(cursor, 2)
    info = readDB(cursor)
    click.echo(info)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
