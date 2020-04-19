import numpy
import matplotlib.pyplot as plt

# Source data
x_data = [2000,
          2001,
          2002,
          2003,
          2004,
          2005,
          2006,
          2007,
          2008,
          2009,
          2010,
          2011,
          2012,
          2013,
          2014,
          2015,
          2016,
          2017,
          2018,
          2019,
          2020]
y_data = [107.754,
          112.700,
          110.608,
          111.538,
          124.977,
          126.985,
          125.469,
          140.119,
          148.507,
          128.978,
          133.586,
          145.819,
          147.449,
          149.176,
          156.573,
          147.479,
          140.674,
          139.677,
          137.005,
          140.743,
          146.396]
degree = 5

# Generate regression polynomial
polynomial_coefficients = numpy.polyfit(x_data, y_data, degree)

# Format polynomial
formatted_polynomial = numpy.poly1d(polynomial_coefficients)

# Generate data from first and last entry in array
interval = numpy.linspace(x_data[0], x_data[-1])

# Configure and display plots
fig, cx = plt.subplots()

# Plot initial dataset
cx.plot(x_data, y_data, '.k')

#Plot fitted polynomial over linspace interval
cx.plot(interval, formatted_polynomial(interval), '-g')

# Enable grid lines
cx.grid()

# Limit default maximum y value to largest polynomial result plus buffer
cx.set_ylim(0, formatted_polynomial(interval).max()*1.5)

plt.show()
plt.show()