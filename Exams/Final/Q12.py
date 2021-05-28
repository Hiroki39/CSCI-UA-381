import datascience as ds
import matplotlib.pyplot as plt

input_file = "https://data.cityofnewyork.us/api/views/7yay-m4ae/rows.csv"
input_table = ds.Table.read_table(input_file)
input_labels = input_table.labels

input_table2 = input_table.select('FISCAL YEAR', 'ALL FUNDS', 'CITY FUND').sort(
    'FISCAL YEAR').group('FISCAL YEAR', sum)
input_table2.plot('FISCAL YEAR', ['CITY FUND sum', 'ALL FUNDS sum'])

plt.savefig('financial_trend.png', bbox_inches='tight')
