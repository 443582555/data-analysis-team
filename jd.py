import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from subprocess import check_output
print(check_output(["ls", "../data-analysis/jd"]).decode("utf8"))
# All csv files are within jd folder 

info = pd.read_csv("../data-analysis/jd/sku_info.csv")
# info 1000 rows x 5 columns id:0-999
attr = pd.read_csv("../data-analysis/jd/sku_attr.csv")
# attr  6776 rows x 3 columns
sales = pd.read_csv("../data-analysis/jd/sku_sales.csv")
# sales 2127485 rows x 7 columns
prom = pd.read_csv("../data-analysis/jd/sku_prom.csv")
# prom 862111 rows x 4 columns

#infoAttr=info.set_index('item_sku_id').join(attr.set_index('item_sku_id'))
#info_attr 6776 rows x 6 columns
#infoAttrSales=infoAttr.set_index('item_sku_id').join(sales.set_index('item_sku_id'))
#key error?

InfoAttrSales=sales.set_index('item_sku_id').join(info.set_index('item_sku_id')).join(attr.set_index('item_sku_id'))
# InfoAttrSales  #14041831 rows x 12 columns
# type(InfoAttrSales)   pandas.core.frame.DataFrame

# Create a new column called prom.promation where the value is 0
# if prom.item_sku_id == -999 and 1 if not
prom['promation'] = np.where(prom['item_sku_id']==-999, 0, 1)
# prom
prom = prom.rename(columns={'date': 'prom_date'})
# prom
