# Importing matplotlib package for plotting, csv package for handling csv files and numpy for calculation
import matplotlib.pyplot as plt
import csv
import numpy as np


def addNewRecord():  # Function to add a new record
    while True:  # Get a valid Student Name
        sname = input('\nEnter Student Name: ')  # Student Name
        if sname.strip().isalpha():  # Check for proper input
            sname = sname.strip()
            break
        else:
            print('Enter a valid name !')  # Notify user for invalid input

    while True:  # Get a valid Student Number
        snumber = input('\nEnter Student Number: ')
        if snumber.isdecimal():  # Check for proper input
            snumber = snumber.strip()
            break
        else:
            print('Enter a valid student number !')  # Notify user for invalid input

    while True:  # Get a valid Course Code
        scourse = input('\nEnter Course Code: ')
        if len(scourse.strip()) > 0:  # Check for proper input
            break
        else:
            print('Enter a valid course code !')  # Notify user for invalid input

    while True:  # Get a valid Grade
        try:
            sgrade = int(input('\nEnter Student Grade: ').strip())
            if not 0 <= sgrade <= 100:
                raise Exception
            else:
                break
        except:  # catch exception for improper input
            print('Enter a valid grade !')  # Notify user for invalid input

    recordlist.append({'name': sname.title(), 'number': snumber, 'grade': sgrade, 'course': scourse.upper()})  # Add record to list


def saveRecord():  # Function to save records in a file
    fieldnames = ['name', 'number', 'course', 'grade']  # Fieldname for the csv file header
    fname = input('\nEnter the file name to save Student Records: ')  # Get filename from user

    with open(fname + '.csv', 'w') as f:  # Open file to write data
        csvwriter = csv.DictWriter(f, fieldnames=fieldnames)  # Create csv writer object to write data in a csv file
        csvwriter.writeheader()  # Write header to the file
        for row in recordlist:
            csvwriter.writerow(row)  # Write the records from the recordlist in rows


def loadRecord():  # Function to load records from a file
    try:
        fname = input('\nEnter filename to load(without extension): ')  # Get filename from user
        with open(fname + '.csv', 'r') as f:
            recordlist.clear()  # Clear the list of student record before fetching the new records from the file
            for line in csv.DictReader(f):  # .csv dictionary reader to read data line by line
                if list(line.keys()) == ['name', 'number', 'course', 'grade']:  # Check for proper key values
                    recordlist.append({'name': line['name'], 'number': line['number'], 'course': line['course'],
                                       'grade': int(line['grade'])})  # Append data to list if keys exist
                else:
                    print('File is corrupted !')  # Notify user for corrupt file when records are not proper
                    recordlist.clear()
                    return

        print('Records Loaded Successfully')  # Notify user records loaded successfully
    except FileNotFoundError:
        print('The filename entered could\'nt be found !')  # Notify user file not found
    except:
        print('File is corrupted !')  # Notify user for corrupt file when records are not proper


def deleteRecord():  # Function to delete all records
    recordlist.clear()  # Delete all the student records from the list


def maxavgScore():  # Function to calculate max and avg score of class
    maxscore = max(recordlist, key=lambda x: x['grade'])  # Get student record with max score
    print('Student {} has max score of {}'.format(maxscore['name'], maxscore['grade']))
    avgscore = np.mean([i['grade'] for i in recordlist])  # Get average grade of whole class
    print('The average score of the class is', avgscore)


def sortRecords():  # Function to sort records as per user's choice
    print('\nSorting Options:\n1) By Student Name\n2) By Student Number\n3) By Course Code\n4) By Grades\n5) Go Back')
    user_choice = input('\nEnter Choice:')  # Take input from user

    if user_choice == '1':  # User wants to sort records by Student Name
        recordlist.sort(key=lambda i: i['name'])  # Sort by name
        displayRecords()  # Display after sorting

    elif user_choice == '2':  # User wants to sort records by Student Number
        recordlist.sort(key=lambda i: int(i['number']))  # Sort by number
        displayRecords()  # Display after sorting

    elif user_choice == '3':  # User wants to sort records by Course Code
        recordlist.sort(key=lambda i: i['course'])  # Sort by course
        displayRecords()  # Display after sorting

    elif user_choice == '4':  # User wants to sort records by Grades
        recordlist.sort(key=lambda i: i['grade'], reverse=True)  # Sort by grades
        displayRecords()  # Display after sorting

    elif user_choice == '5':  # User doesn't wants to sort and wants to go back to main menu
        return

    else:  # Invalid choice
        print('Please enter a valid choice !')  # Notify user invalid choice


def displayRecords():  # Function to display all student records

    ndata = [{'name': 'Student Name', 'number': 'Student Number', 'grade': 'Student Grade',
              'course': 'Course Code'}]  # Another list to get max length of respective strings for formatting table
    ndata.extend(recordlist)
    maxname = len(max(ndata, key=lambda x: len(x['name']))['name'])  # Get max length of student name
    maxnumber = len(max(ndata, key=lambda x: len(x['number']))['number'])  # Get max length of student number
    maxgrade = len(max(ndata, key=lambda x: len(str(x['grade'])))['grade'])  # Get max length of grade
    maxcourse = len(max(ndata, key=lambda x: len(x['course']))['course'])  # Get max length of course code

    # Printing title and header of table in formatted manner
    print('=' * (maxname + maxnumber + maxgrade + maxcourse + 13))
    print('| ' + 'Student Name'.center(maxname, ' ') + ' | ' + 'Student Number'.center(maxnumber, ' ') + ' | ' +
          'Course Code'.center(maxcourse, ' ') + ' | ' + 'Student Grade'.center(maxgrade, ' ') + ' |')
    print('|' + '=' * (maxname + maxnumber + maxgrade + maxcourse + 11) + '|')

    # Printing all the records in formatted manner
    for i in recordlist:
        print('| ' + i['name'].ljust(maxname) + ' | ' + i['number'].ljust(maxnumber) + ' | ' +
              i['course'].ljust(maxcourse) + ' | ' + str(i['grade']).ljust(maxgrade) + ' |')
        print('|' + '_' * (maxname + maxnumber + maxgrade + maxcourse + 11) + '|')


def showChart(data):  # Function to show graph of sorted student record
    plt.style.use('seaborn')  # Use a style from matplotlib
    plt.bar([i['name'] for i in data], [i['grade'] for i in data])  # Plot Bar chart
    plt.title('Visualizing Student Grades')  # Give title to BarChart
    plt.xlabel('Student Name')  # Give label to X-axis
    plt.ylabel('Grade')  # Give label to Y-axis
    plt.show()  # Enable plot


recordlist = []  # List to store temporary student records in form of dictionaries


# Main driver code which will keep executing until user exits
while True:
    # Menu shows different options available to the user in the program
    print('1) Enter New Student Record\n2) Display Student Records\n3) Save Records to a File\n4) Load Records '
          'from a File\n5) Sort Student Records\n6) Visualize data in 2D\n7) Clear Student Records\n8) Exit\n')
    user_input = input('Enter Your Choice: ')  # Get user input

    if user_input == '1':  # User wants to add a New Student Record
        addNewRecord()
        print('New Student Record Added !')  # Notify user student record added

    elif user_input == '2':  # User wants to see all student records
        if len(recordlist) != 0:  # Check for available records
            displayRecords()
            maxavgScore()
        else:
            print('\nNo Records Available to Display at the Moment !')  # Notify user about empty records

    elif user_input == '3':  # User wants to save records to a file
        if len(recordlist) != 0:  # Check for available records 
            saveRecord()  # Save records in a file
            print('Records saved Successfully !')  # Notify user records saved successfully
        else:
            print('\nNo Records Available to be Saved !')  # Notify user about empty records

    elif user_input == '4':  # User wants to load records from a File
        loadRecord()  # Load data from a file

    elif user_input == '5':  # User wants to sort student records
        sortRecords()  # Sort records

    elif user_input == '6':  # User wants to visualize records in 2D
        showChart(recordlist)

    elif user_input == '7':  # User wants to delete student records
        deleteRecord()
        print('All student records are cleared !')  # Notify user records cleared

    elif user_input == '8':  # User wants to exit
        exit(0)  # Terminate program successfully

    else:  # User has entered invalid choice
        print('\nPlease enter a Valid Choice !')  # Notify user about invalid choice

    print('\n')  # Add some space for next menu
