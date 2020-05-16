"""Create a regular expression that matches any word that 
starts with any character and is followed by two o's. 
Then use Python's re module to match boo and loo in the 
sentence The ghost that says boo haunts loo."""

import re

line = "The ghost that says boo haunts loo."

m = re.findall(".oo",line,
               re.IGNORECASE)

print(m)

#or

match = re.findall(".oo", "The ghost that says boo haunts the loo.")
print(match)