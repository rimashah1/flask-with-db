import sqlite3 

# Connecting to sqlite
connect = sqlite3.connect('patients.db')
 
# db object
db = connect.cursor()

# delete table patient_table if it exists
db.execute("DROP TABLE IF EXISTS patient_table")
connect.commit() # commit means that the changes made are visible

# Create table 
table = """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL,
            age INTEGER NOT NULL,
            date_of_admit CHAR(25) NOT NULL,
            date_of_discharge CHAR(25) NOT NULL,
            insurance_name CHAR(25) NOT NULL
        ); """

db.execute(table)
connect.commit() # commit the changes again


## insert data into the table
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, age, date_of_admit, date_of_discharge, insurance_name) values('12345', 'MacKenn', 'Bross', '06/30/1999', 23, '11/16/2021', '11/17/2021', 'Cigna')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, age, date_of_admit, date_of_discharge, insurance_name) values('13578', 'Katie', 'McGrath', '01/03/1983', 39, '06/12/2021', '06/15/2021', 'Aetna')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, age, date_of_admit, date_of_discharge, insurance_name) values('98765', 'Karen', 'Chen', '03/21/1998', 24, '08/22/2021', '08/24/2021', 'Aetna')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, age, date_of_admit, date_of_discharge, insurance_name) values('65321', 'Lena', 'Luthor', '10/24/1990', 32, '11/25/2021', '11/26/2021', 'United')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, age, date_of_admit, date_of_discharge, insurance_name) values('73993', 'Erin', 'Kramer', '01/09/1982', 40, '05/04/2021', '05/07/2021', 'Blue_Cross_Blue_Shield')")


connect.commit()


# close the connection
connect.close()