
import matplotlib.pyplot as plt

import pandas as pd 

data=[["ball",35435,24234,32432,456546,324],
      ["dice",35435,24234,32432,456546,324],
      ["stressball",57345,5757,2457,978976,63453],
      ["toy",353543,34345,6546,2423,56765],
      ["GIjo",353543,34345,6546,2423,56765]

     ]

df=pd.DataFrame(data,columns=["product","2010","2011","2012","2013","2014"])
print(df)

df["totalsale"]=df['2010']+df['2011']+df['2012']+df['2013']+df['2014']

df.set_index('product',inplace=True)

df.plot(x="totalsale", y=["2010","2011","2012","2013","2014"], kind="bar",figsize=(9,8))
plt.show()

plot = df.plot.pie(y='totalsale', figsize=(5, 5))

plot = df.plot.pie(y='2010', figsize=(5, 5))

plot = df.plot.pie(y='2011', figsize=(5, 5))

plot = df.plot.pie(y='2012', figsize=(5, 5))

plot = df.plot.pie(y='2013', figsize=(5, 5))

plot = df.plot.pie(y='2014', figsize=(5, 5))

