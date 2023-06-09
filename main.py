import csv
import re


def error_handling(line):  # error handling
    error = ''
    valid_email = invalid_email(line[2])  # error handling for email
    valid_phone = invalid_phone(line[3])  # error handling for phone
    if valid_phone is True:
        line[3] = line[3].replace('-', '.')  # replacing the period with the dash
    valid_date = validate_date(line[4])  # error handling for the date
    if valid_date is True:
        list_date = line[4].split('/')  # separates date with dash
        line[4] = list_date[2] + '-' + list_date[0] + '-' + list_date[1]
    valid_time = validate_time(line[5])  # error handling for time
    valid_id = invalid_id(line[0])  # error handling for ID
    valid_name = invalid_name(line[1]) # error handling for name
    if valid_name is True:
        list_name = line[1].split(',') # validates both last and first name
        line[1] = list_name[1] + "," + list_name[0]
    if not valid_id:  # error codes
        error += 'I'
    if not valid_name:
        error += 'N'
    if not valid_email:
        error += 'E'
    if not valid_phone:
        error += 'P'
    if not valid_date:
        error += 'D'
    if not valid_time:
        error += 'T'
    return [error, line]  # returns the error


def invalid_email(email):  # validating email
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    if re.fullmatch(regex, email):
        print("This email is valid") # states email is valid
        return True
    else:
        print("This email is invalid") # states email is invalid
        return False


def invalid_phone(phone):   # validates the phone number
    regex = re.compile(r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$')
    if re.fullmatch(regex, phone): # if it matches the format it's valid
        print("This phone number is valid")
        return True
    else:
        print("This phone number is invalid") # returns false if it doesn't match the format
        return False


def invalid_id(num): # validates ID
    if num.isdigit(): # makes sure it's a number
        print("This id is valid")
        return True
    else:
        print("This id is invalid")
        return False


def invalid_name(name):
    names = name.split(',') # splits the name so it validates first and last
    if len(names) != 2 or not names[0].isalpha() or not names[1].isalpha():
        print("This name is invalid") # if false returns invalid
        return False
    else:
        print("This name is valid")  # if true returns valid
        return True


def validate_date(date): # validates date
    pattern_str = re.compile(r'^\d{2}/\d{2}/\d{4}$')  # format for the date
    if re.fullmatch(pattern_str, date):  # if date matches format return true
        print("This date is valid")
        return True
    else:
        print("This date is invalid") # if date doesn't match format return false
        return False


def validate_time(time):
    # regex format for time
    p = re.compile("^([01]?[0-9]|2[0-3]):[0-5][0-9]$")

    # Pattern class contains matcher() method
    # to find matching between given time
    # and regular expression.
    m = re.search(p, time)

    # Return True if the time
    # matched the ReGex otherwise False
    if m is not None:
        print("This time is valid")
        return True
    else:
        print("This time is invalid")
        return False


valid = []
invalid = []

with open('NotValidated.csv', newline='') as file: # opening multiple CSV files at at a time
    # reading the CSV file
    csvFile = csv.reader(file, delimiter='|')

    # displaying the contents of the CSV file
    for lines in csvFile:
        result = error_handling(lines)
        if result[0] != '':
            invalid.append(result[1])
        else:
            valid.append(result[1])

with open('validated.csv', 'w') as valid_file, \
        open('invalid.csv', 'w') as invalid_file:
    for line in valid:
        valid_file.write(','.join(line))
    for line in invalid:
        invalid_file.write(','.join(line))
