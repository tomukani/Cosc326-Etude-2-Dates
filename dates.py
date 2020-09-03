import fileinput
import doctest
import sys

# List of months in their valid character combinations
# Used to compare if entered month is valid
month_list = {
    'jan', 'JAN', 'Jan',
    'feb', 'FEB', 'Feb',
    'mar', 'MAR', 'Mar',
    'apr', 'APR', 'Apr',
    'may', 'MAY', 'May',
    'jun', 'JUN', 'Jun',
    'jul', 'JUL', 'Jul',
    'aug', 'AUG', 'Aug',
    'sep', 'SEP', 'Sep',
    'oct', 'OCT', 'Oct',
    'nov', 'NOV', 'Nov',
    'dec', 'DEC', 'Dec'
    }

# Dictionary used to map month inputs to the month outputs
month_dict = {
    '1': 'Jan',
    '2': 'Feb',
    '3': 'Mar',
    '4': 'Apr',
    '5': 'May',
    '6': 'Jun',
    '7': 'Jul',
    '8': 'Aug',
    '9': 'Sep',
    '10': 'Oct',
    '11': 'Nov',
    '12': 'Dec',
    'jan': 'Jan',
    'feb': 'Feb',
    'mar': 'Mar',
    'apr': 'Apr',
    'may': 'May',
    'jun': 'Jun',
    'jul': 'Jul',
    'aug': 'Aug',
    'sep': 'Sep',
    'oct': 'Oct',
    'nov': 'Nov',
    'dec': 'Dec'
    
    }

#list of months with only 30 days
thirty_day_list = {
    'Apr', 'Jun', 'Sep', 'Nov' }

# list of months with 31 days
thirtyone_day_list = {
    'Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec'
    }
    

"""
Checks if a year passed as a paramter is a leap year or not
If the year is a leap year returns True
otherwise returns False
"""
def is_leap_year(year):
    if year % 4 == 0:
        if (year % 100 == 0) == False:
            return True
        elif year % 100 == 0 and year % 400 == 0:
            return True
        else:
            return False
    else:
        return False

"""
Checks whether an object is an integer or not
returns true is object is an integer
otherwise returns false
"""

def is_int(value):
    try:
        val = int(value)
        return True
    except ValueError:
        return False


"""
Method that takes a date as a parameter
Checks that the inputed is in a valid format and is a real date
returns an error if date is not valid, with reasoning
if date is valid returns the date in format 01 Jan 2006
"""
def format_date(date):
    """
    >>> format_date("03 JUN 3004")
    '03 JUN 3004 - INVALID: Year out of range.'
    >>> format_date("02 Apr 1996")
    '02 Apr 1996'
    >>> format_date("4-6-92")
    '04 Jun 1992'
    >>> format_date("04/06/1992")
    '04 Jun 1992'
    >>> format_date("3 AUG 97")
    '03 Aug 1997'
    >>> format_date("12-Sep-1955")
    '12 Sep 1955'
    >>> format_date("13-04-13")
    '13 Apr 2013'
    >>> format_date("13-04/12")
    '13-04/12 - INVALID: More than one seperator type used.'
    >>> format_date("15021984")
    '15021984 - INVALID: No seperator used.'
    >>> format_date("13-02-92-1996")
    '13-02-92-1996 - INVALID: Too many sections.'
    >>> format_date("133/Mar/1996")
    '133/Mar/1996 - INVALID: Not a valid day.'
    >>> format_date("02/MARCH/2003")
    '02/MARCH/2003 - INVALID: Not a valid month.'
    >>> format_date("29/FEB/2020")
    '29 Feb 2020'
    >>> format_date("29/02/2019")
    '29/02/2019 - INVALID: Year is not a leap year.'
    >>> format_date("31/sep/2019")
    '31/sep/2019 - INVALID: Day out of range.'
    >>> format_date("12/03/198")
    '12/03/198 - INVALID: Not a valid year.'
    >>> format_date("03-14-2000")
    '03-14-2000 - INVALID: Month out of range.'
    >>> format_date("03-0-2000")
    '03-0-2000 - INVALID: Month out of range.'
    >>> format_date("04-02-1653")
    '04-02-1653 - INVALID: Year out of range.'
    >>> format_date("05-12-3000")
    '05-12-3000 - INVALID: Year out of range.'
    """
    
    # Check that the date contains numbers
    if any(char.isdigit() for char in date) == False:
        return date + " - INVALID: Date must contain numbers."
    # Checks that a seperator was used
    if ("/" in date or " " in date or "-" in date) == False:
        return date + " - INVALID: No seperator used."
    # checks that only one type of seperator was used
    if ("/" in date and " " in date) or ("/" in date and "-" in date) or (" " in date and "-" in date):
        return date + " - INVALID: More than one seperator type used."
    
    #Determines the type of seperator used
    if "/" in date:
        seperator = "/"
    
    if " " in date:
        seperator = " "
    
    if "-" in date:
        seperator = "-"
    
    #splits date into its day, month and year determined by seperator
    split_date = date.split(seperator)
    split_date[-1] = split_date[-1].strip() # removes the newline character at the end of the year
    
    # checks format is given in day then month then year and no other sections are given
    if(len(split_date) > 3):
        return date + " - INVALID: Too many sections."
    
    #put the day, month and year into seperate variables to test their validity individually
    day = split_date[0]
    month = split_date[1]
    year = split_date[2]
    
    #Check that inputed day/month/year have a valid lenth
    if(len(day) > 2 or len(day) < 1):
        return date + " - INVALID: Not a valid day."
    
    if(len(month) > 3 or len(month) < 1):
        return date + " - INVALID: Not a valid month."
    
    if(len(year) > 4 or len(year) < 1 or len(year) == 3):
        return date + " - INVALID: Not a valid year."
    
    #Check that the day is valid
    
    #Check that day is a number
    if is_int(day) == False:
        return date + " - INVALID: Not a valid day."
    
    #if day is enterd a 0d, grabs just the meaningful part of the day
    if len(day) > 1 and day[0] == "0":
        day = day[1]
        
    #Check that day is a valid calendar day
    if int(day) < 1 or int(day) > 31:
        return date + " - INVALID: Day out of range."
    
    
    # Check that month is valid
    # if date was input with less than 3 characters, confirm these characters are numbers
    # otheriws the input is invalid
    if len(month) < 3:
        if is_int(month) == False:
            return date + " - INVALID: Not a valid month."
    
    # If month input as text,check that a valid month was entered
    if len(month) == 3:
        if month not in month_list:
            return date + " - INVALID: Not a valid month."
        
    # if month entered as 0m, grabs meaningful part of month
    if len(month) > 1 and month[0] == "0":
        month = month[1]
        
    # Check that month is a valid calendar date    
    if len(month) < 3: #makes sure month isn't in string form when converting to int
        if int(month) < 1 or int(month) > 12:
            return date + " - INVALID: Month out of range."


    #Check that year is valid
    if is_int(year) == False:
        return date + " - INVALID: Not a valid year."
    
    #Check that year is between 1753 and 3000
    if len(year) == 4:
        if int(year) < 1754 or int(year) > 2999:
            return date + " - INVALID: Year out of range."
  
    #Convert day to output format
    if len(day) == 1:
        day = "0" + day
    
    
    #Convert month to output format
    if len(month) == 3:
        month = month_dict[month.lower()]
    else:
        month = month_dict[month]
    
    #Convert year to output format
    if len(year) == 2:
        
        if int(year) < 50:
            year = "20" + year
        else:
            year = "19" + year
            
    #Check that if month is feb has less than 30 days
    if int(day) > 29 and month == "Feb":
        return date + " - INVALID: Day out of range."
    
    #Check leap year validity
    if day == "29" and month == "Feb":
        if is_leap_year(int(year)) == False:
            return date + " - INVALID: Year is not a leap year."
    
    #Check day isnt 31 in a month with30 days
    if day == "31" and month not in thirtyone_day_list:
        return date + " - INVALID: Day out of range."
   
    # return converted date as string
    return day + " " + month + " " + year



#Main method
if __name__ == '__main__':
    if (len(sys.argv) > 1 and sys.argv[1] == '-t'):
        doctest.testmod()
    else:
        for line in fileinput.input():
            print(format_date(line))