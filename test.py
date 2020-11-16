import  tushare as ts
from sqlalchemy import create_engine
import pandas as pd
import time
token = '43928d1e07fb05984041070a422bd77166393ae9c31ee3285b75acd0'
engine = create_engine('postgresql://stock:stock@127.0.0.1/stocks')
pro =ts.pro_api(token)

day = pro.trade_cal(exchange='SSE', is_open='1', 
                            start_date='20200801', 
                            end_date='20201114', 
                            fields='cal_date')


for d in day.cal_date:
    t = pro.daily(trade_date=d)
    if t is not None:
        t.to_sql('day_value',engine,if_exists='append')
        print(d,'finished')
    else :
        print(d,'error')
        continue
