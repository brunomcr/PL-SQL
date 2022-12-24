import os
import cx_Oracle
from dotenv import load_dotenv


"""
Take environment variables from .env.
"""
load_dotenv()


"""
Connect to Database
"""
# DSN
dsn = cx_Oracle.makedsn(host=os.getenv('host'), port=os.getenv('port'), sid=os.getenv('sid'))
# CONNECTION
connection = cx_Oracle.connect(user=os.getenv('user'), password=os.getenv('password'), dsn=dsn)

print("Successfully connected to Oracle Database")

cursor = connection.cursor()

# Create a table

cursor.execute(
    """
    begin
        execute immediate 'drop table todoitem';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;
    """
)

cursor.execute(
    """
    create table todoitem (
        id number generated always as identity,
        description varchar2(4000),
        creation_ts timestamp with time zone default current_timestamp,
        done number(1,0),
        primary key (id))
    """
)

# Insert some data

rows = [("Task 1", 0), ("Task 2", 0), ("Task 3", 1), ("Task 4", 0), ("Task 5", 1)]

cursor.executemany("insert into todoitem (description, done) values(:1, :2)", rows)
print(cursor.rowcount, "Rows Inserted")

connection.commit()

# Now query the rows back
for row in cursor.execute("select description, done from todoitem"):
    if row[1]:
        print(row[0], "is done")
    else:
        print(row[0], "is NOT done")