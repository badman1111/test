from conn.conn import pro,engine,get_code
from transit import days
df = get_code()
ts_code = df.ts_code

for i in ts_code:
    data = days(i)
    
