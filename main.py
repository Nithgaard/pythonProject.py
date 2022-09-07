# Importer moduler
import shutil
from datetime import datetime
import filecmp
import os
import sys
import csv

# function to write in csv file
def write_in_csv(rows):

    # Opening the CSV file in read and
    # write mode using the open() module
    with open(r'/Users/AK42VU/backup.csv', 'r+', newline='') as file:

        # creating the csv writer
        file_write = csv.writer(file)

        # Iterating over all the data in the rows
        # variable
        for val in rows:

            # writing the data in csv file
            file_write.writerow(val)

#Importer datoen lige nu. Det bliver brugt til navngivning af backupmappe.
dato = datetime.now().strftime("_%Y_%m_%d-%I:%M:%S_%p")

#Spørg om user input til hvilke stier som skal tages backup fra og hvor backuppen skal hen.
choice = input("Please choose a Backup Method (Full/Incremental/Differential): ")

# src = /Users/AK42VU/Screenshots/
# dst = /Users/AK42VU/test

# Informerer brugeren om src og dst mapper og giver et timestamp for copieringen.
#print("You have chosen to backup from", src, "to", dst, "at time:", dato)

#Forgreninger - Vil du lave Full Backup / Incremental Backup / Differential Backup
if choice == "Full":
    print("And you have chosen Full Backup.")
    src = input("src-path for backup: ")
    dst = input("dst-path for backup: ")
    print("You have chosen to backup from", src, "=>", dst, "at time:", dato)
    #Kopierer hele mappen og laver en ny mappe med navn givet af bruger+timestamp.
    filez = shutil.copytree(src, dst + str(dato))
    # Check whether the specified
    # path exists or not
    path = dst + str(dato)
    isExist = os.path.exists(path)
    print(isExist)

    # list to store the values of the rows
    rows = []
    # while loop to take
    # inputs from the user
    run = ''
    while run != 'no':

        # lists to store the user data
        val = []

        # Taking inputs from the user
        val1 = input("Enter Backup Type:- ")
        val2 = input("Enter Username of who did Backup:- ")
        val3 = input("Enter name of folder that was done Backup of:- ")

        # Appending the inputs in a list
        val.append(dato)
        val.append(val1)
        val.append(val2)
        val.append(val3)

        # Taking input to add one more row
        # If user enters 'no' then the will loop will break
        run = input("Do you want to add one more row? Type Yes or No:- ")
        run = run.lower()

        # Adding the stored data in rows list
        rows.append(val)
        # Calling function to write in csv file
        write_in_csv(rows)

elif choice == "Incremental":
    result = filecmp.cmp(src, dst)
    print("And you have chosen Incremental Backup.")
    src = input("src-path for backup: ")
    dst = input("dst-path for backup: ")
    result = filecmp.cmp(src, dst)
    print("Is", src, "equal to", dst, "?".format(src, dst, result))
    print("You have chosen to backup from", src, "=>", dst, "at time:", dato)
    filez = shutil.copytree(src, dst + str(dato))
    # Check whether the specified
    # path exists or not
    path = dst + str(dato)
    isExist = os.path.exists(path)
    print(isExist)
    # list to store the values of the rows
    rows = []
    # while loop to take
    # inputs from the user
    run = ''
    while run != 'no':

        # lists to store the user data
        val = []

        # Taking inputs from the user
        val1 = input("Enter Backup Type:- ")
        val2 = input("Enter Username of who did Backup:- ")
        val3 = input("Enter name of folder that was done Backup of:- ")

        # Appending the inputs in a list
        val.append(dato)
        val.append(val1)
        val.append(val2)
        val.append(val3)

        # Taking input to add one more row
        # If user enters 'no' then the will loop will break
        run = input("Do you want to add one more row? Type Yes or No:- ")
        run = run.lower()

        # Adding the stored data in rows list
        rows.append(val)
        # Calling function to write in csv file
        write_in_csv(rows)

elif choice == "Differential":
    print("And you have chosen Differential Backup.")
    src = input("src-path for backup: ")
    dst = input("dst-path for backup: ")

    print("You have chosen to backup from", src, "=>", dst, "at time:", dato)
    filez = shutil.copytree(src, dst + str(dato))

    # Check whether the specified
    # path exists or not
    path = dst + str(dato)
    isExist = os.path.exists(path)
    print(isExist)

    # list to store the values of the rows
    rows = []
    # while loop to take
    # inputs from the user
    run = ''
    while run != 'no':

        # lists to store the user data
        val = []

        # Taking inputs from the user
        val1 = input("Enter Backup Type:- ")
        val2 = input("Enter Username of who did Backup:- ")
        val3 = input("Enter name of folder that was done Backup of:- ")

        # Appending the inputs in a list
        val.append(dato)
        val.append(val1)
        val.append(val2)
        val.append(val3)

        # Taking input to add one more row
        # If user enters 'no' then the will loop will break
        run = input("Do you want to add one more row? Type Yes or No:- ")
        run = run.lower()

        # Adding the stored data in rows list
        rows.append(val)
        # Calling function to write in csv file
        write_in_csv(rows)
else:
    print("Userinput is not correct. Try again (Full, Incremental, Differential)")
