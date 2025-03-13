#Average daily volume ticker 
average _volume =hep.groupby(‘Ticker’)[‘Volume’].mean()
print(“Average volume per ticker:\n”,average_volume)

#volume spikes detection 
volume_spikes=hep[hep[‘Volume’] > hep[‘Volume’].rolling(window=20).mean()*1.5]
print(“Volume spikes:\n”, volume_spikes[[‘Date’,’Ticker’,’Volume’]])
#Average price per sector
sector_avg_price = hep.groupby(‘Sector’)[‘Close Price’].mean() 
print(“Average Close Price per sector:\n”,sector_avg_price)
#visualizing the average price per sector 
plt.figure(figsize=(10,6))
sector_avg_price.plot(kind=‘bar’,color=‘skyblue’, edgecolor = ‘black’)
# Adding title and labels 
plt.title(“Average Close Price per Sector”)
plt.title(“Average Close Price per Sector”)
plt.xlabel(“Sector”)
plt.ylabel(“Average Close Price”)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#identify the sectors mean 
hep.groupby(‘Sector’)[‘PE Ratio’].mean()
#finance sector with a volume greater than 1000000 showing the ticker and capitalisation column 
hep[(hep[‘Sector’]==‘Finance’)|(hep[‘Volume’]>1000000)][[‘Ticker’,’Market Capitalisation’]]
#Tickers according to the mean of their volume , and , market capitalisation 
hep.groupby(‘Ticker’).agg({‘Volume’:’mean’,’Market Capitalisation’:’mean’})
#percentage difference between close and open price 
hep[‘percentage difference’]=((hep[‘Close Price’]-hep[‘Open Price’])/hep[‘Open Price’]) * 100
#correlation analysis 
correlation=hep[[‘Open Price’,’Close Price’,’High Price’,’Low Price’,’Volume’,’Market Capitalisation’,’PE Ratio’,‘Dividend Yield’,’EPS’]].corr()

#machine learning
hepnew=pd.get_dummies(hep,prefix=[‘Sector’],columns=[‘Sector’]) 
hepnew[[‘Sector_Finance’,’Sector_Technology’]]=hepnew[[‘Sector_Finance’,Sector_Technology’]].astype(int)
hepnew
now=hepnew[[‘Sector_Finance’,’PE Ratio’]]
now 
from sklearn.linear_model import LinearRegression
model=LinearRegression()
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LinearRegression()
X=now.drop(columns=[‘PE Ratio’])
X
y=now[‘PE Ratio’]
y
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
y_pred
new_data=[[1.5]]
predicted_value=model.predict(new_data)
print(f”predicted value for X={new_data[0] [0]}:{predicted_value[0]:2f}”)
