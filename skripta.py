import sqlite3


def add_data(file_name, table_name):
    con = sqlite3.connect("db.sqlite3")
    cursor = con.cursor()
    sql_file = open(file_name, 'r')
    lines = sql_file.readlines()

    for line in lines:
        print("Executing: ", line)
        cursor.execute(line)
    print("Added data to table")
    con.commit()

    cursor.execute("SELECT * FROM " + table_name)
    print("The table after adding data")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    con.close()


# morate paziti da id-evi ne budu isti ako hocete jos pozicija dodati
# zakomentarisete liniju ako hocete samo u jednu ili drugu tabelu dodati nove korisnike
#add_data("company_position.sql", "users_companyposition")
add_data("users.sql", "users_user")