import pandas as pd
import matplotlib.pyplot as plt

mymoviedata=pd.read_table("http://bit.ly/movieusers",sep="|",header=None)

# add headings to the column- sr.no,age,Gender,profession,Views
mymoviedata.columns=['sr.no','age','Gender','profession','Views']

#display only column gender
mymoviedata['Gender']

#add col6 concatenate values of age and gender and seperate them by :
mymoviedata['col6']=mymoviedata['age'].astype(str)+':'+mymoviedata['Gender']
mymoviedata.head()

mymoviedata['Views'] = pd.to_numeric(mymoviedata['Views'], errors='coerce').convert_dtypes()
mymoviedata['age'] = pd.to_numeric(mymoviedata['age'], errors='coerce').convert_dtypes() 

mymoviedata.info()

# retrieve values of age and views display bar graph
mymoviedata.plot(x="Views", y=["age"], kind="bar",figsize=(9,8))
plt.show()

# retrieve values of profession and views display bar graph
mymoviedata.plot(x="profession", y=["Views"], kind="bar",figsize=(9,8))
plt.show()




