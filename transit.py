from conn.conn import ts,pro,engine,pd

sql = 'SELECT "date", "open", high, "close", low,volume, price_change, p_change,\
                ma5, ma10, ma20, v_ma5, v_ma10, v_ma20, turnover, code \
                FROM public.day_data \
                where code = %(code)s'

def train_data(code ):
    lc = pd.read_sql_query(sql,engine,params={'code':code})
    return lc
#lcxx = train_data('000977')
#print(lcxx)

def day_money(code,date):
    sqls = 'SELECT "index", "time", price, "change", volume, amount, "type", code, "date"\
        FROM public."202011" where code =%(code)s and date=%(date)s'
    d = pd.read_sql_query(sqls,engine,params={'code':code,'date':date})
    return d

def day_money_1(codedate):
    sqls = 'SELECT "index", "time", price, "change", volume, amount, "type", code, "date",code_day\
        FROM public."202011" where code_day=%(codedate)s'
    d = pd.read_sql_query(sqls,engine,params={'codedate':codedate})
    return d