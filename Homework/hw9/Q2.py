import datascience as ds
import numpy as np
import matplotlib.pyplot as plt

fec = ds.Table.read_table('fec.csv').select('contbr_nm', 'contbr_occupation',
                                            'contb_receipt_amt').where('contb_receipt_amt', ds.are.above(200))
grouped_fec = fec.group(['contbr_nm', 'contbr_occupation'], sum).where(
    'contb_receipt_amt sum', ds.are.above(10000)).sort("contb_receipt_amt sum", descending=True)

for occupation in np.unique(grouped_fec['contbr_occupation']):
    grouped_fec.where('contbr_occupation', occupation).select('contbr_nm', 'contb_receipt_amt sum').relabel(ds.make_array('contbr_nm', 'contb_receipt_amt sum'), ds.make_array('Contributor Name', 'Total Amount')).sort(
        'Total Amount', descending=True).barh('Contributor Name')
    plt.savefig(occupation + '.png', bbox_inches='tight')
