from conn.conn import ts,pro,engine,pd

code  = pro.query('stock_basic')  
#print(code)

code.to_sql('stock_basic',engine)