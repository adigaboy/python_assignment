from database import mydatabase

def main():
    dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='mydb.sqlite')
    # Create Tables
    #dbms.create_db_tables()

    #dbms.insert_single_data()
    #dbms.print_all_data(mydatabase.USERS)
    #dbms.sample_delete() # delete data
    #dbms.insert(3, (2,5,1), 10) # insert data
    dbms.updateResult(3, 15)
    print(dbms.getResult(3)) # simple query
    #dbms.sample_update() # update data

main()