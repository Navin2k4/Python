import numpy
import matplotlib.pyplot as plt
import random
x=[random.randint(1,100) for i in range(20)]
y=[random.randint(1,100) for i in range(20)]
plt.axis([0,100,0,100])
#plt.scatter(x,y)  # Scatter Plot
#plt.bar(x,y)      # Bar Chart
#plt.grid()
plt.show()