#Importing necessary Libraries
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

trends = TrendReq()
"""
Requesting trends to start with Food analysis
that means anyone have a search history related
to food there data will be retrieve
"""
trends.build_payload(kw_list=["Food"])
#Seggretaing and sorting the data based on country
data = trends.interest_by_region()
data = data.sort_values(by="Food", ascending = False)
data = data.head(10)

#Plotting the graph
data.reset_index().plot(x="geoName", y="Food",figsize=(20,15),kind="bar")
plt.style.use('fivethirtyeight')
plt.show()

data = TrendReq(hl='en-US', tz=360)
data.build_payload(kw_list=['Food'])
data = data.interest_over_time()
fig,ax = plt.subplots(figsize=(20,15))
data['Food'].plot()
plt.style.use('fivethirtyeight')
plt.title("Total Google Searches for Foods", fontweight='bold')
plt.xlabel("Year")
plt.ylabel("Total Count")
plt.show()