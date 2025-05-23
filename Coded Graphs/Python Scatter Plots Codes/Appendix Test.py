import matplotlib.pyplot as plt
import numpy as np

# Your data

years = np.array(\[1930, 1947, 1953, 1954, 1954, 1955, 1959, 1959, 1964, 1965,
1970, 1972, 1984, 1991, 1991, 1998, 2001, 2002, 2004, 2008, 2012])
portamento = np.array(\[15, 5, 23, 24, 20, 15, 29, 21, 29, 26, 19, 4, 11, 7, 6, 13, 24, 16, 11, 9, 2])
clean\_shifts = np.array(\[14, 9, 8, 4, 4, 4, 14, 5, 7, 14, 13, 1, 1, 7, 6, 5, 10, 14, 7, 11, 6])

# Helper functions

def trendline(x, y):
coeffs = np.polyfit(x, y, 1)
poly = np.poly1d(coeffs)
return poly, poly(x)

def r\_squared(y, y\_pred):
ss\_res = np.sum((y - y\_pred) \*\* 2)
ss\_tot = np.sum((y - np.mean(y)) \*\* 2)
return 1 - ss\_res / ss\_tot

# Compute trendlines and R²

p\_port, yport\_pred = trendline(years, portamento)
p\_clean, yclean\_pred = trendline(years, clean\_shifts)

r2\_port = r\_squared(portamento, yport\_pred)
r2\_clean = r\_squared(clean\_shifts, yclean\_pred)

# Plotting

plt.figure(figsize=(12, 6))

# Sliding portamento in dark blue

plt.scatter(years, portamento,
color='darkblue',
label='Sliding Portamento',
marker='o')

# Clean shifts in red

plt.scatter(years, clean\_shifts,
color='red',
label='Clean Shifts',
marker='s')

# Trendlines in matching colors

plt.plot(years, yport\_pred,
linestyle='--',
color='darkblue',
label=f'Portamento Trendline (\$R^2\$ = {r2\_port:.2f})')
plt.plot(years, yclean\_pred,
linestyle='--',
color='red',
label=f'Clean Shifts Trendline (\$R^2\$ = {r2\_clean:.2f})')

plt.title('Trends in Sliding Portamento vs. Clean Shifts (1930–2012)')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(range(1930, 2020, 10))
plt.legend()
plt.grid(True)
plt.show()

