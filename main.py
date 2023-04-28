import csv
import re

def error_handling(line):
    error = ''
    print(line)
    valid_email = invalid_email(line[2])
    valid_phone = invalid_phone(line[3])
    if valid_phone is True:
        line[3] = line[3].replace('-', '.')
    valid_date = validate_date(line[4])
    if valid_date is True:
        list_date = line[4].split('/')
        line[4] = list_date[2]+'-'+list_date[0]+'-'+list_date[1]
    valid_time = validate_time(line[5])
    valid_id = invalid_id(line[0])
    valid_name = invalid_name(line[1])
    if valid_name is True:
        list_name = line[1].split(',')
        line[1] = list_name[1] + "," + list_name[0]
    if not valid_id:
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
    return [error, line]





def invalid_email(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def invalid_phone(phone):
    regex = re.compile(r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$')
    if re.fullmatch(regex, phone):
        return True
    else:
        return False


def invalid_id(num):
    if num.isdigit():
        return True
    else:
        return False


def invalid_name(name):
    names = name.split(',')
    if len(names) != 2 or not names[0].isalpha() or not names[1].isalpha():
        return False
    else:
        return True


def validate_date(date):
    pattern_str = re.compile(r'^\d{2}/\d{2}/\d{4}$')
    if re.fullmatch(pattern_str, date):
        return True
    else:
        return False

def validate_time(time):
    # Compile the ReGex
    p = re.compile("^([01]?[0-9]|2[0-3]):[0-5][0-9]$")

    # Pattern class contains matcher() method
    # to find matching between given time
    # and regular expression.
    m = re.search(p, time)

    # Return True if the time
    # matched the ReGex otherwise False
    if m is not None:
        return True
    else:
        return False


valid = []
invalid = []

with open('NotValidated.csv', newline='') as file:
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