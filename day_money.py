from transit import train_data,day_money
from conn.conn import ts,pro,engine,pd
#codes = ts.get_stock_basics( )

#test = day_money('003018','2020-11-06')
#print(test)

def cha_jia(code,date):
    d =pd.DataFrame()
    s = day_money(code,date)
    print(s)
    d['date'] = date
    d['code'] = code
    d['buy']  = s[s['type']=='买盘']['amount'].sum()
    d['sell'] = s[s['type']=='卖盘']['amount'].sum()
    d['other'] = s[s['type']=='中性盘']['amount'].sum()
    return d

fuck = cha_jia('003018','2020-11-06')
print(fuck)