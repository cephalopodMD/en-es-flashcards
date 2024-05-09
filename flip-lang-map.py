# utility to get english to spanish word mappings from 'es2en.csv' and write them to 'en2es.csv'

import csv

en2es = {}
with open('es2en.csv', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        es = row[0]
        ens = row[1:]
        for en in ens:
            en2es[en] = en2es.get(en, [])
            en2es[en].append(es)

with open('en2es.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for en in sorted(en2es):
        writer.writerow([en, *en2es[en]])
        pass