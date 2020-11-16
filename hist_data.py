#from conn import conn.ts as ts
from  conn.conn import  engine,pd

import time
#time.localtime()
def hist_data():
    import tushare as ts
    code = ts.get_stock_basics()
    err = pd.DataFrame()
    for i in code.index:
        data = ts.get_hist_data(i)
        if data is not NOne:
            data['code'] = i
            data.to_sql("hist_data",engine,if_exists='append')
            print('success',i)
        else:
            print('error',i)
            err.to_sql('hist_err',engine,if_exists='append')
            continue


