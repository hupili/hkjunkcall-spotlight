import pandas
import os
from os import path

dir_junkcalls = 'junkcalls'
fn_google_csv = 'Google.csv'

df = pandas.read_csv(fn_google_csv)

if not path.exists(dir_junkcalls):
    os.mkdir(dir_junkcalls)

for (i, row) in df.iterrows():
    name = row['Name']
    given_name = row['Given Name']
    phone_str = row['Phone 1 - Value']
    phones = [p.strip() for p in phone_str.split(':::')]
    #print(name, given_name, phones)
    for phone in phones:
        with open(path.join(dir_junkcalls, '%s.txt' % phone), 'w') as fp:
        #with open(path.join(dir_junkcalls, '%s' % phone), 'w') as fp:
            fp.write('%s\n%s\n%s' % (name, given_name, phone))

