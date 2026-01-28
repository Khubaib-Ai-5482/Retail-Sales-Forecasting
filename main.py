import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
import seaborn as sns

df = pd.read_csv("retail_sales_data.csv")
df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'])

daily_sales = df.groupby('Purchase_Date')['Total_Amount'].sum().reset_index()
daily_sales.rename(columns={'Purchase_Date':'Date', 'Total_Amount':'Sales'}, inplace=True)
daily_sales.to_csv("daily_sales.csv", index=False)
print(daily_sales.head())

sns.set_style("whitegrid")
plt.figure(figsize=(12,5))
plt.plot(daily_sales['Date'], daily_sales['Sales'], color='black', label='Actual Sales')
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.show()

prophet_df = daily_sales.rename(columns={'Date':'ds', 'Sales':'y'})

model = Prophet(interval_width=0.95)
model.fit(prophet_df)

future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)
forecast['Type'] = ['Past' if d <= daily_sales['Date'].max() else 'Future' for d in forecast['ds']]

plt.figure(figsize=(14,6))
plt.plot(prophet_df['ds'], prophet_df['y'], label='Actual Sales (Past)', color='black')
plt.plot(forecast['ds'], forecast['yhat'], label='Forecast (Next 90 Days)', color='orange')
plt.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='gray', alpha=0.3, label='Confidence Interval')
plt.axvline(x=daily_sales['Date'].max(), color='red', linestyle='--', label='Forecast Start')
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.show()

model.plot_components(forecast)
plt.show()

forecast[['ds','yhat','yhat_lower','yhat_upper','Type']].to_csv("forecast_output.csv", index=False)
print("Forecast saved as forecast_output.csv")