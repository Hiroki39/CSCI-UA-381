#!/usr/bin/env python
# coding: utf-8


import datascience as ds
import numpy as np
import matplotlib.pyplot as plt

top = ds.Table.read_table('data/' + 'top_movies.csv')

movies_and_studios = top.select('Title', 'Studio')
studio_distribution = movies_and_studios.group('Studio')
studio_distribution.sort('count', descending=True).barh('Studio')
plt.savefig('studio_distribution_bar.png')
movies_and_years = top.select('Title', 'Year')
movies_and_years.group('Year').sort('count', descending=True).plot('Year')
plt.savefig('studio_distribution_plot.png')



