import tushare as ts
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('postgresql://stock:stock@localhost/stocks')
token = '43928d1e07fb05984041070a422bd77166393ae9c31ee3285b75acd0'
pro =ts.pro_api(token)