# Define the string
from operator import or_
from re import S
import string
from tokenize import String


string = "Peter piper pickedP P P P P  a p p p p p ickle of pickles not peppers"
# Define the search string
search = 'P'
search2 = 'p'
# Store the count value
count = string.count(search)
count2 = string.count(search2)
# Print the formatted output
print("%r appears %d times" % (string, (count + count2)))