from datetime import datetime
import  pandas as pd
date=datetime(2016,1,1)
dates = [datetime(2016,1,1),datetime(2016,1,2),datetime(2016,1,3)]
ts=pd.Series([1,2,3],index=dates)
print(ts[0])