# Importer moduler
import shutil
from datetime import datetime
import filecmp
import os
import csv
import rows as rows
import glob


def ReadDir(dir1):
    # read file names from a dir into a list
    # compare the file names and keep the files that are with the same name
    filelist1 = []
    for filename in glob.glob(os.path.join(dir1, '*.txt')):
        filelist1.append(filename)
    return filelist1


def GetFileName(filedir):
    return filedir.split('\\')[-1]


def CmpFile(file1, file2):
    # Compare two files, if file1 is not identical with file2,
    # return False; otherwise return True
    # Also print out the filename and change starting line
    f1 = open(file1).readlines()
    f2 = open(file2).readlines()
    filename = GetFileName(file1)
    IsIdentical = True
    for linenum in range(len(f1)):
        if f1[linenum] != f2[linenum]:
            print('change in file "{0}" starts from line {1}'.format(filename, linenum))
            IsIdentical = False
            break
    return IsIdentical


def CmpDir(dir1, dir2):
    # Compare txt files in two directories dir1 and dir2
    # with the same file name, to see if they are identical
    [list1, list2] = map(ReadDir, [dir1, dir2])
    list1.sort()
    list2.sort()
    for filedir1 in list1:
        filename = GetFileName(filedir1)
        filedir2 = dir2 + filename
        if filedir2 in list2:
            is_same_file = CmpFile(filedir1, filedir2)
            if is_same_file:
                pass
            else:
                pass


def write_in_csv(rows):
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


# Importer datoen lige nu. Det bliver brugt til navngivning af backupmappe.
dato = datetime.now().strftime("_%Y_%m_%d-%I:%M:%S_%p")

# Spørg om user input til hvilke stier som skal tages backup fra og hvor backuppen skal hen.
choice = input("Please choose a Backup Method (Full/Incremental/Differential): ")

# Forgreninger - Vil du lave Full Backup / Incremental Backup / Differential Backup
if choice == "Full":
    # inform user
    print("And you have chosen Full Backup.")

    # ask user for input
    src = input("src-path for backup: ")
    dst = input("dst-path for backup: ")

    # inform user
    print("You have chosen to backup from", src, "=>", dst, "at time:", dato)

    # Kopierer hele mappen og laver en ny mappe med navn givet af bruger+timestamp.
    filez = shutil.copytree(src, dst + str(dato))

    # Check whether the specified path exists or not
    path = dst + str(dato)
    isExist = os.path.exists(path)
    print(isExist)

    # write in csv file
    write_in_csv(rows)

elif choice == "Incremental":
    # create result variable
    result = filecmp.cmp(src, dst)

    # inform user
    print("And you have chosen Incremental Backup.")

    # ask user for input for variables
    src = input("src-path for backup: ")
    dst = input("dst-path for backup: ")

    # inform user
    print("Is", src, "equal to", dst, "?".format(src, dst, result))
    print("You have chosen to backup from", src, "=>", dst, "at time:", dato)

    # copy folders/files from src => dst with timestamp
    filez = shutil.copytree(src, dst + str(dato))

    # Check whether path exists or not
    path = dst + str(dato)
    isExist = os.path.exists(path)
    print(isExist)

    # write in csv file
    write_in_csv(rows)

elif choice == "Differential":
    # inform user
    print("And you have chosen Differential Backup.")

    # ask user for input to get src and dst
    src = input("src-path for backup: ")
    dst = input("dst-path for backup: ")

    # inform user
    print("You have chosen to backup from", src, "=>", dst, "at time:", dato)

    CmpDir(src, dst)

    # copy files from one place to another, specified by user
    # filez = shutil.copytree(src, dst + str(dato))

    # Check whether the specified path exists or not
    path = dst + str(dato)
    isExist = os.path.exists(path)
    print(isExist)

    # write in csv file
    write_in_csv(rows)
else:
    # If user inputs wrong form of Backup, inform of mistake and make them try again.
    print("Userinput is not correct. Try again (Full, Incremental, Differential)")
