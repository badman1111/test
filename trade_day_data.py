import  tushare as ts
from sqlalchemy import create_engine
import pandas as pd
import time
token = '43928d1e07fb05984041070a422bd77166393ae9c31ee3285b75acd0'
engine = create_engine('postgresql://stock:stock@127.0.0.1/stocks')
pro =ts.pro_api(token)
#获取所有2010年至2020年的数据
day = pro.trade_cal(exchange='SSE', is_open='1', 
                            start_date='20200801', 
                            end_date='20201114', 
                            fields='cal_date')
#
#
#循环过程中，为了保持数据提取的稳定性，可以先建立一个专门的函数，实现一个重试机制：
#
#
def get_daily(self, ts_code='', trade_date='', start_date='', end_date=''):
    for _ in range(3):
        try:
            if trade_date:
                df = self.pro.daily(ts_code=ts_code, trade_date=trade_date)
            else:
                df = self.pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
        except:
                time.sleep(1)
        else:
                return df

for date in day['cal_date']:
    df = get_daily(date)
    if df is not None:
        df.to_sql('day_value',engine,if_exists='append')
        print(date,'success')     
    
    else:
        print(date,'error')
        continue
