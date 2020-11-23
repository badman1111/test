from transit import train_data,day_money,day_money_1
from conn.conn import ts,pro,engine,pd
#codes = ts.get_stock_basics( )

#test = day_money('003018','2020-11-06')
#print(test)
d =pd.DataFrame()

def cha_jia(code,date,codedate):
    d =[]
    s = day_money_1(codedate)
#    print(s)
    d['date'] = date
    d['code'] = code
    d['buy']  = s[s['type']=='买盘']['amount'].sum()
    d['sell'] = s[s['type']=='卖盘']['amount'].sum()
    d['other'] = s[s['type']=='中性盘']['amount'].sum()
    return d
    print(d)

fuck = cha_jia('003018','2020-11-06','0030182020-11-06')
print(fuck)