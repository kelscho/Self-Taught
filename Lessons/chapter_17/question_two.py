""" Come up with a regular expression that matches all the
digits in the string 497,501,870. California 209,213,650"""
# echo Arizona: 479, 501, 870. California: 209, 213, 650. | grep [[:digit:]]
import re

line= """497,501,870.
 California 209,213,650"""

m = re.findall("\d",
               line,
               re.IGNORECASE)

print(m)