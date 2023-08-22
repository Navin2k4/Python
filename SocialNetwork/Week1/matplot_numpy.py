import matplotlib.pyplot as plt
import numpy
x = [i for i in range(21)]
x=numpy.array(x) #changes the list of values into array for numpy
plt.plot(x,x**2,'r-',x,x**3,'g-',x,x**4,'b-') # for using this me must include numpy and change it as array
plt.title('Squares and the values', fontsize=20, color='blue')
plt.xlabel('Squares', fontsize=14, color='green')
plt.ylabel('Values', fontsize=14, color='green')
plt.grid(True)
plt.show()