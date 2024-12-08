import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Generate sample time series data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Value': np.cumsum(np.random.normal(0, 1, 100))  # Cumulative sum of random values
}
time_series = pd.DataFrame(data)
time_series.set_index('Date', inplace=True)

# Train ARIMA model
model = ARIMA(time_series, order=(2, 1, 2))  # Order: (p, d, q)
model_fit = model.fit()

# Forecast future values
forecast_steps = 20
forecast = model_fit.get_forecast(steps=forecast_steps)
forecast_index = pd.date_range(start=time_series.index[-1] + pd.Timedelta(days=1), periods=forecast_steps, freq='D')
forecast_series = pd.Series(forecast.predicted_mean, index=forecast_index)
conf_int = forecast.conf_int()

# Plot original data and forecast
plt.figure(figsize=(12, 6))
plt.plot(time_series, label='Original Data', color='blue')
plt.plot(forecast_series, label='Forecast', color='orange')
plt.fill_between(forecast_index, conf_int.iloc[:, 0], conf_int.iloc[:, 1], color='orange', alpha=0.3, label='95% Confidence Interval')
plt.legend(loc='upper left')
plt.title('ARIMA Model Forecast')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid()
plt.show()
