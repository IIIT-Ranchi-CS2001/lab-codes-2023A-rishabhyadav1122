import pandas as pd
import numpy as np
df = pd.read_csv("AQI_Data.csv")
print("Display the first five rows: ")
print(df.head())
print("Display the last six rows: ")
print(df.tail(6))
print("Summary Statistics  : ")
print(df.describe())


#Display the Mean values for AQI,PM2.5 and 
print("Mean AQI , PM2.5 and PM10 values for easy city")
# Numpy to calculate the mean AQI, PM2.5 and PM10 values for each city
print("\nMean AQI, PM2.5 and PM10 values for each city")
# Convert to NumPy arrays
cities = np.array(df['City'])
aqi = np.array(df['AQI'])
pm25 = np.array(df['PM2.5'])
pm10 = np.array(df['PM10'])
# Unique cities
unique_cities = np.unique(cities)
# Calculate mean values for each city
print("\nMean AQI, PM2.5, and PM10 values for each city")
for city in unique_cities:
    city_mask = cities == city  # Mask for the current city
    mean_aqi = np.mean(aqi[city_mask])
    mean_pm25 = np.mean(pm25[city_mask])
    mean_pm10 = np.mean(pm10[city_mask])
    print(f"{city}: AQI={mean_aqi:.2f}, PM2.5={mean_pm25:.2f}, PM10={mean_pm10:.2f}")

print("Filter and Display all rows where PM2.5 level exceeds 100 and their counts")
filtered_df = df[df['PM2.5'] > 100]

# Display filtered rows
print("Filtered Rows:")
print(filtered_df)

# Display count
count = filtered_df.shape[0]
print("\nCount of rows where PM2.5 > 100:", count)