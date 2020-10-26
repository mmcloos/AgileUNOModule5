"""
Maggie Cloos
Agile UNO Module 5
Strings and Lists
"""

# import system.exit
from sys import exit

# import requests library
import requests

# create site_data dictionary
site_data = {}

# with sites.csv, read as infile
with open("sites.csv", "r") as infile:
    # data variable reads the contents of sites.csv
    data = infile.read()
    # sites variable is a list of sites.csv contents split by commas
    sites = data.split(",")

# for each site in sites list
for site in sites:
    # get site from site_data dictionary
    site_data[data] = requests.get(site)

# for key and value in site_data dictionary list
for key, value in site_data.items():
    # return site and response code
    print(f"\n{key} : {value}")


# 1
#################################
"""
Print out each URL extension with string slicing
"""
print(sites[16:19])
print(sites[-28:-25])
print(sites[-3:0])

# 2
###################################
"""
Print out sites ending in .com
"""
for site in sites:
    if ".com" in site:
        print(site)

# 3
##################################
"""
Convert all sites names to upper case and print each
"""
sites.upper()
print(sites)

# 4
#################################
"""
Using list of sites, add a new site
Use input method to get name of new site from user
Reverse order of the list and print
"""
# add input as new element in sites list
sites.append(input(f"Please enter new site name."))

# reverses list in place and then prints
print(sites.reverse())

#5
#################################
"""
print out 'server' of the response of the URL request of the items in the list
"""

# I am totally lost with this one
r = requests.get(
    print(r.url)

# 6
#################################
"""
exit the program using sys module exit function imported at beginning
"""
    
exit()
