import jinja2
import pandas
import os
from os import path

dir_junkcalls = 'junkcalls'
fn_google_csv = 'Google.csv'

template = jinja2.Template(open('template-hkjunkcall.vcf').read())

df = pandas.read_csv(fn_google_csv)

if not path.exists(dir_junkcalls):
    os.mkdir(dir_junkcalls)

for (i, row) in df.iterrows():
    name = row['Name'].decode('utf-8')
    given_name = row['Given Name'].decode('utf-8')
    phone_str = row['Phone 1 - Value'].decode('utf-8')
    phones = [p.strip() for p in phone_str.split(':::')]
    #print(name, given_name, phones)
    for phone in phones:
        content = template.render(first_name=given_name, last_name=name, phone_number=phone)
        with open(path.join(dir_junkcalls, '%s.vcf' % phone), 'w') as fp:
        #with open(path.join(dir_junkcalls, '%s' % phone), 'w') as fp:
            #fp.write('%s\n%s\n%s' % (name, given_name, phone))
            fp.write(content.encode('utf-8'))

