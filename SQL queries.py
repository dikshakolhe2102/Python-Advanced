"""DDL = Data Defination language = it includes command related to structure of table,data base
SYNTAX
1. create = create database dname
    create table tname
    (
    columnname datatype(size),
    colname2 datatype(size)
    )
2. use = use databasename 

3. desc = desc tablename

4. drop/delete a table = drop table tname

"""

"""DML = Data manipulation language 
COMMANDS
1. insert:
    1.insert into tablename
        values(1,'abc');
    2.insert into tablename
        (name)values('pqr');
    3.insert into tablename values
        (2,'abc'),(3,'pqr');
2. select:
    1.select * from tablename
    2.select colname from tablename
    3.select *from tablename
        where colname = value
3.update:
    1.update tablename 
        set colname = value
    2.update tablename
        set colname = value
        where colname = value
4.Delete:
    1.delete from tablename;
    2.delete from tablename where
        colname = value;
"""


