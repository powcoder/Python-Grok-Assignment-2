https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
import csv

VALID_SUBURBS = ["Richmond", "Southbank", "Fitzroy",
                  "Docklands", "St. Kilda", "Footscray",
                  "Hawthorn", "Parkville", "Toorak", "Brunswick",
                  "Kensington", "Flemington", "Frankston", "Dandenong",
                  "Caulfield", "Collingwood"]

MAX_SALARY = 200000

def read_data(filename):
    """
    Take a filename and output a dictionary of dictionaries of 
    the census data contained in that file.
    """
    data = {}
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ID = row["ID"]
            del row["ID"]
            data[ID] = dict(row) # for Python 3.6+ don't use OrderedDict
    return data