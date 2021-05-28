#!/usr/bin/env python
# coding: utf-8

import datascience as ds
import numpy as np
import matplotlib.pyplot as plt

nyc_class_size_file = "https://data.cityofnewyork.us/api/views/82rt-zc4y/rows.csv"
nyc_table = ds.Table.read_table(nyc_class_size_file)
nyc_labels = nyc_table.labels
CSD,BORO,GRADE = nyc_labels[0:3]
SEATS = nyc_labels[7]
AVE = nyc_labels[-1]
nyc_table = nyc_table.relabeled(GRADE,'GRADE').relabeled(SEATS,'SEATS')
nyc_table = nyc_table.relabeled(AVE,'CLASS SIZE')
nyc_table1 = nyc_table.select('GRADE','SEATS','CLASS SIZE')
nyc_table2 = nyc_table.select(BORO,'SEATS','CLASS SIZE')

def average(sequence):
    result = sum(sequence)/len(sequence)
    return(round(result,2))

nyc_table1.group('GRADE',average).barh('GRADE')
plt.savefig('grade.png')
nyc_table2.group('BORO',average).barh('BORO')
plt.savefig('boro.png')




