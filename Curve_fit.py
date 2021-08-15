from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pprint
import datetime
import matplotlib.pyplot as plt
import numpy as np
from numpy import arange
import pandas as pd
from scipy import stats
from scipy.optimize import curve_fit

df1 = pd.read_csv ('Resources/HistoricalEsportData.csv')
df1 = df1[df1['Earnings'] > 0.0]
df1['Date']= pd.to_datetime(df1['Date'])
df1['Date'] = df1['Date'].dt.strftime('%Y')

df1[['Date']] = df1[['Date']].astype(float)
df1[['Tournaments']] = df1[['Tournaments']].astype(float)

df2 = pd.DataFrame()
df2["Year"]=pd.unique(df1['Date'])
df2["Total"]=list((df1.groupby(["Date"])["Earnings"].sum()))
df2["Tournaments"]=list((df1.groupby(["Date"])["Tournaments"].sum()))
#Avgearnings is total earnings per tournament
df2["Avgearnings"]= df2["Total"]/df2["Tournaments"]

x = df2.Year.values.reshape(-1, 1)
y = df2.Total.values.reshape(-1, 1)

y1 = df2.Tournaments.values.reshape(-1, 1)

y2 = df2.Avgearnings.values.reshape(-1, 1)

        #Year vs Total Earnings

model = LinearRegression()
model.fit(x, y)
x_min = np.array([[x.min()]])
x_max = np.array([[x.max()]])
y_min = model.predict(x_min)
y_max = model.predict(x_max)
predicted = model.predict(x)
r2 = round(r2_score(y, predicted),2)
Trend=f"R-squared (R2 ): {r2}"

fig = plt.figure(figsize=(10,5))
fig.suptitle('Year vs Total Earnings')
plt.xlabel('Year')
plt.ylabel('Earnings in USD (by Hundred million)')
plt.scatter(x, y, c='blue')
plt.plot([x_min[0], x_max[0]], [y_min[0], y_max[0]], c='red',label=str(Trend))
plt.legend()
plt.savefig('Images/Historic Trends/Linear Year vs Total Earnings.png')
plt.show()

        #Year vs Tournaments
model1 = LinearRegression()
model1.fit(x, y1)
x_min = np.array([[x.min()]])
x_max = np.array([[x.max()]])
y_min1 = model1.predict(x_min)
y_max1 = model1.predict(x_max)
predicted = model1.predict(x)
r2 = round(r2_score(y1, predicted),2)
Trend=f"R-squared (R2 ): {r2}"

fig = plt.figure(figsize=(10,5))
fig.suptitle('Year vs Tournaments')
plt.xlabel('Year')
plt.ylabel('Tournaments')
plt.scatter(x, y1, c='blue')
plt.plot([x_min[0], x_max[0]], [y_min1[0], y_max1[0]], c='red',label=str(Trend))
plt.legend()
plt.savefig('Images/Historic Trends/Linear Year vs Total Tournaments.png')
plt.show()

        #Year vs Earning per Tournament
model2 = LinearRegression()
model2.fit(x, y2)
x_min = np.array([[x.min()]])
x_max = np.array([[x.max()]])
y_min2 = model2.predict(x_min)
y_max2 = model2.predict(x_max)
predicted = model2.predict(x)
r2 = round(r2_score(y2, predicted),2)
Trend=f"R-squared (R2 ): {r2}"

fig = plt.figure(figsize=(10,5))
fig.suptitle('Year vs Earning per Tournament')
plt.xlabel('Year')
plt.ylabel('Earnings in USD')
plt.scatter(x, y2, c='blue')
plt.plot([x_min[0], x_max[0]], [y_min2[0], y_max2[0]], c='red',label=str(Trend))
plt.legend()
plt.savefig('Images/Historic Trends/Linear Year vs Earning per Tournament.png')
plt.show()


# Second polynomial regression for Year vs Total Earnings
def objective(x, a, b, c):
	return a * x + b * x**2 + c
 

x, y = df2['Year'], df2['Total']

popt, _ = curve_fit(objective, x, y)

a, b, c = popt
print('y = %.1f * x + %.1f * x^2 + %.1f' % (a, b, c))

x_line = arange(min(x), max(x), 1)

y_line = objective(x_line, a, b, c)

residuals = y- objective(x, *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y-np.mean(y))**2)
r_squared =round(1 - (ss_res / ss_tot),2)
Trend=f"R-squared: {r_squared}"

fig = plt.figure(figsize=(10,5))
plt.scatter(x, y)
fig.suptitle('Year vs Total Earnings')
plt.xlabel('Year')
plt.ylabel('Earnings in USD')

plt.plot(x_line, y_line, '--', color='red',label=str(Trend))
plt.legend()
plt.savefig('Images/Historic Trends/polynomial Year vs Total Earnings.png')
plt.show()

# Second polynomial regression for Year vs Tournaments
def objective(x, a, b, c):
	return a * x + b * x**2 + c
 
x, y = df2['Year'], df2['Tournaments']

popt, _ = curve_fit(objective, x, y)

a, b, c = popt
print('y = %.1f * x + %.1f * x^2 + %.1f' % (a, b, c))

x_line = arange(min(x), max(x), 1)
y_line = objective(x_line, a, b, c)

residuals = y- objective(x, *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y-np.mean(y))**2)
r_squared =round(1 - (ss_res / ss_tot),2)
Trend=f"R-squared: {r_squared}"

fig = plt.figure(figsize=(10,5))
plt.scatter(x, y)
fig.suptitle('Year vs Tournaments')
plt.xlabel('Year')
plt.ylabel('Tournaments')

plt.plot(x_line, y_line, '--', color='red',label=str(Trend))
plt.legend()
plt.savefig('Images/Historic Trends/polynomial Year vs Tournament.png')
plt.show()

# Second polynomial regression for Year vs Earnings per Tournaments
def objective(x, a, b, c):
	return a * x + b * x**2 + c
 
x, y = df2['Year'], df2['Avgearnings']

popt, _ = curve_fit(objective, x, y)

a, b, c = popt
print('y = %.1f * x + %.1f * x^2 + %.1f' % (a, b, c))

x_line = arange(min(x), max(x), 1)
y_line = objective(x_line, a, b, c)

residuals = y- objective(x, *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y-np.mean(y))**2)
r_squared =round(1 - (ss_res / ss_tot),2)
Trend=f"R-squared: {r_squared}"

fig = plt.figure(figsize=(10,5))
plt.scatter(x, y)
fig.suptitle('Year vs Earnings per Tournaments')
plt.xlabel('Year')
plt.ylabel('Earnings in USD')

plt.plot(x_line, y_line, '--', color='red',label=str(Trend))
plt.legend()
plt.savefig('Images/Historic Trends/polynomial Year vs Earning per Tournament.png')
plt.show()