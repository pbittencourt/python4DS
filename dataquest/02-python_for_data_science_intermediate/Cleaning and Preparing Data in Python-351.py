## 1. Introducing Data Cleaning ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`

num_rows = len(moma)

## 2. Reading our MoMA Data Set ##

# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('children.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
children = list(read_file)

# remove the first row of the data, which
# contains the column names
children = children[1:]

# Write your code here

# 0A. closes file opened before this section
opened_file.close()

# 0B. we've already imported reader module, so let's jump it!

# 1. opens a csv file
opened_file = open('artworks.csv')

# 2. read file and parses data
read_file = reader(opened_file)

# 3. create a list from read_file contents
moma = list(read_file)

# 4. slices content of moma list, removing header
moma = moma[1:]

## 3. Replacing Substrings with the replace Method ##

age1 = "I am thirty-one years old"
age2 = age1.replace('thirty-one', 'thirty-two')

## 4. Cleaning the Nationality and Gender Columns ##

# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again

for item in moma:
    nationality = item[2]
    nationality = nationality.replace('(', '')
    nationality = nationality.replace(')', '')
    item[2] = nationality
    
    gender = item[5]
    gender = gender.replace('(', '')
    gender = gender.replace(')', '')
    item[5] = gender


## 5. String Capitalization ##

for row in moma:
    
    # fetch gender value
    gender = row[5]
    
    # capitalize (and strip!) gender value
    gender = gender.strip().title()
    
    # check in gender is empty
    if gender == '':
        gender = 'Gender Unknown/Other'
        
    # assign back this value to the dataset
    row[5] = gender
        
    # fetch nationality value 
    nationality = row[2]
    
    # capitalize (and strip!) nationality value 
    nationality = nationality.strip().title()
    
    # check if nationality is empty
    if nationality == '':
        nationality = 'Nationality Unknown'
        
    # assign back this value to the dataset
    row[2] = nationality


## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

for row in moma:
    begindate = row[3]
    enddate = row[4]
    row[3] = clean_and_convert(begindate)
    row[4] = clean_and_convert(enddate)

## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

def strip_characters(string):
    bad_chars = ["(",")","c","C",".","s","'", " "]
    for char in bad_chars:
        string = string.replace(char, "")
    return string
    
stripped_test_data = []
for item in test_data:
    item = strip_characters(item)
    stripped_test_data.append(item)
    
print(stripped_test_data)

## 8. Parsing Numbers from Complex Strings, Part Two ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

def process_date(string):
    if '-' in string:
        date = string.split('-')
        date_one = int(date[0])
        date_two = int(date[1])
        date = round((date_one + date_two)/2)
    else:
        date = int(string)

    return date

processed_test_data = []
for date in stripped_test_data:
    processed_test_data.append(process_date(date))

for row in moma:
    date = row[6]
    date = strip_characters(date)
    date = process_date(date)
    row[6] = date