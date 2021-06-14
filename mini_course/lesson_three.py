# Load CSV using Pandas from URL
import pandas
import csv
import requests
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
print(data.shape)
# data = requests.Session().get(url)

# dataCSV = csv.reader(data.text, delimiter=' ', quotechar = "|")

# for row in dataCSV:
#     print(row)
