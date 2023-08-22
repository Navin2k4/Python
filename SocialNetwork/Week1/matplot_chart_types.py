from wordcloud import WordCloud
import squarify
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Line chart
"""
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Chart')
plt.show()
"""

#Bar chart
"""
categories = ['A', 'B', 'C', 'D']
values = [10, 25, 15, 30]
plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Simple Bar Chart')
plt.show()
"""

#Scatter Plot
"""
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.scatter(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Scatter Plot')
plt.show()
"""

#Pie chart
"""
categories = ['A', 'B', 'C', 'D']
values = [30, 20, 25, 15]
plt.pie(values, labels=categories, autopct='%1.1f%%')
plt.title('Simple Pie Chart')
plt.show()
"""

#Histogram
"""
data = [5, 10, 15, 20, 25, 25, 30, 35, 40, 45, 50]
plt.hist(data, bins=5)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Simple Histogram')
plt.show()
"""

#Box plot
"""
data = [10, 15, 20, 25, 25, 30, 35, 40, 45, 50]
plt.boxplot(data)
plt.title('Simple Box Plot')
plt.show()
"""

#Area chart
"""
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
plt.stackplot(x, y1, y2, labels=['Series 1', 'Series 2'])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Area Chart')
plt.legend()
plt.show()
"""

#Barh chart
"""
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [10, 25, 15, 30]
plt.barh(categories, values)
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Simple Horizontal Bar Chart')
plt.show()
"""

# Plotting the stacked bar chart4
"""
categories = ['A', 'B', 'C', 'D']
values1 = [10, 25, 15, 30]
values2 = [5, 15, 10, 20]
plt.bar(categories, values1, label='Series 1')
plt.bar(categories, values2, bottom=values1, label='Series 2')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Stacked Bar Chart')
plt.legend()
plt.show()
"""
# Plotting the step chart
"""
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 6, 3]
plt.step(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Step Chart')
plt.show()
"""

# Plotting the violin plot
"""
data = [10, 15, 20, 25, 30, 35, 40, 45, 50]
plt.violinplot(data)
plt.title('Violin Plot')
plt.show()
"""

# Plotting the 3D scatter plot
"""
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
z = [5, 3, 2, 7, 4]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
plt.title('3D Scatter Plot')
plt.show()
"""

# Plotting the polar plot
"""
theta = np.linspace(0, 2*np.pi, 8, endpoint=False)
values = [2, 4, 1, 6, 3, 5, 2, 7]
plt.polar(theta, values)
plt.title('Polar Plot')
plt.show()
"""

# Plotting the heatmap
"""
data = np.random.rand(5, 5)
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Heatmap')
plt.show()
"""

# Plotting with error bars
"""
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 6, 3]
y_err = [0.5, 0.2, 0.8, 0.3, 0.4]
plt.errorbar(x, y, yerr=y_err, fmt='o', capsize=5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Error Bars')
plt.show()
"""

# Plotting the contour plot
"""
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)
plt.contour(X, Y, Z, levels=20)
plt.colorbar()
plt.title('Contour Plot')
plt.show()
"""

# Plotting the hexbin plot
"""
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.hexbin(x, y, gridsize=20, cmap='Blues')
plt.colorbar()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Hexbin Plot')
plt.show()
"""

# Plotting the 3D surface plot
"""
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.title('3D Surface Plot')
plt.show()
"""

# Plotting the streamplot
"""
x, y = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))
u = -y
v = x
plt.streamplot(x, y, u, v)
plt.title('Streamplot')
plt.show()
"""

# Plotting the funnel plot
"""
observed = [10, 8, 5, 4, 3]
expected = [20, 10, 6, 3, 2]
categories = ['Category 1', 'Category 2',
              'Category 3', 'Category 4', 'Category 5']
plt.scatter(expected, categories, color='red', label='Expected', marker='o')
plt.scatter(observed, categories, color='blue', label='Observed', marker='x')
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Funnel Plot')
plt.legend()
plt.show()
"""

# Plotting the radar chart
"""
categories = ['A', 'B', 'C', 'D', 'E']
values = [4, 3, 2, 5, 4]
categories += categories[:1]
values += values[:1]
angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
values = np.array(values)
plt.polar(angles, values, marker='o')
plt.fill(angles, values, alpha=0.25)
plt.xticks(angles[:-1], categories[:-1])
plt.title('Radar Chart')
plt.show()
"""
# Plotting the treemap
"""
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
squarify.plot(sizes=sizes, label=labels, alpha=0.8)
plt.title('Treemap')
plt.axis('off')
plt.show()
"""

# Plotting the word cloud
"""
text = "Python is an amazing programming language that makes data analysis and visualization easy and fun."
# Generating the word cloud
wordcloud = WordCloud(width=800, height=400,
                      background_color='white').generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('on')
plt.show()
"""