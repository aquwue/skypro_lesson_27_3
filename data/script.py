import pandas as pandas

data_ads = pandas.read_csv('ads.csv', sep=",").to_dict()

i = 0

while max(data_ads['Id'].keys()) > 1:

    print(data_ads['Id'][i])
    i += 1
