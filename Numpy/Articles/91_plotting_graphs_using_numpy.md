# <picture> <source srcset="https://numpy.org/images/logo.svg" type="image/webp"> <img src="https://numpy.org/images/logo.svg" width="32" height="32"> </picture> NumPy for Data Science 

> [!TIP]  
> Link to Previous Article  
> 🡸 [Handling Null Values in NumPy](/Numpy/Articles/90_working_with_null_values.md)

## Plotting Graphs Using NumPy

Graphical visualization is a key part of understanding mathematical functions and data in data science. NumPy, combined with Python's plotting libraries like Matplotlib, provides a seamless way to plot graphs of various mathematical functions. In this article, we'll explore how NumPy facilitates plotting graphs and walk through examples of common mathematical functions such as $ y = x $, $ y = x^2 $, $ y = \sin(x) $, and $ y = x \log(x) $.

### Why Use NumPy for Plotting Graphs?

#### Theoretical Explanation
NumPy simplifies the creation of numerical data points that are often needed to plot mathematical functions. By leveraging its efficient array operations, you can generate a range of values, compute function outputs, and then visualize them using a plotting library like Matplotlib.

#### Benefits of Using NumPy:
1. **Efficiency**: Quickly generates a large set of values for plotting.
2. **Flexibility**: Supports a variety of mathematical operations on arrays.
3. **Integration**: Works seamlessly with Matplotlib for creating graphs.

### Getting Started with NumPy and Matplotlib

Before plotting graphs, ensure you have the required libraries installed:

```bash
pip install numpy matplotlib
```

Here’s a quick setup for plotting:

```python
import numpy as np
import matplotlib.pyplot as plt
```

### Example 1: Plotting $ y = x $

#### Theoretical Explanation
The function $ y = x $ represents a straight line with a slope of 1 passing through the origin.

#### Implementation

```python
# Generate data
x = np.linspace(-10, 10, 100)  # 100 points between -10 and 10
y = x  # y = x

# Plot the graph
plt.plot(x, y, label='y = x', color='blue')
plt.title('Graph of y = x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
```

#### Output:
You’ll see a straight line passing through the origin.
![Alt text](/Numpy/Resources/Images/f591b70f-d3cd-43e7-85a9-e4d5480f2774.png)

#### Explanation:
- **`np.linspace(-10, 10, 100)`** generates 100 equally spaced points between -10 and 10.
- **`plt.plot(x, y)`** plots the $ x $ and $ y $ values.

### Example 2: Plotting $ y = x^2 $

#### Theoretical Explanation
The function $ y = x^2 $ represents a parabola opening upwards, symmetric about the y-axis.

#### Implementation

```python
# Generate data
x = np.linspace(-10, 10, 100)
y = x ** 2  # y = x^2

# Plot the graph
plt.plot(x, y, label='y = x^2', color='green')
plt.title('Graph of y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
```

#### Output:
![Alt text](/Numpy/Resources/Images/ad1943cf-8609-4591-b7d4-acf77bbfbcb1.png)


#### Explanation:
- Each value in `x` is squared to compute `y`.
- The graph shows the parabola shape, visually demonstrating the relationship between $ x $ and $ y $.

### Example 3: Plotting $ y = \sin(x) $

#### Theoretical Explanation
The sine function oscillates between -1 and 1, with a period of $ 2\pi $.

#### Implementation

```python
# Generate data
x = np.linspace(-2 * np.pi, 2 * np.pi, 200)  # Cover two periods
y = np.sin(x)  # y = sin(x)

# Plot the graph
plt.plot(x, y, label='y = sin(x)', color='red')
plt.title('Graph of y = sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
```
#### Output:
![Alt text](/Numpy/Resources/Images/624e8b9c-9191-4438-9a9e-33600c9178bd.png)

#### Explanation:
- `np.sin(x)` computes the sine of each element in `x`.
- The resulting graph illustrates the oscillatory nature of the sine function.

### Example 4: Plotting $ y = x \log(x) $

#### Theoretical Explanation
The function $ y = x \log(x) $ is undefined for $ x \leq 0 $. It grows logarithmically for $ x > 0 $.

#### Implementation

```python
# Generate data
x = np.linspace(0.1, 10, 100)  # Avoid x = 0 to prevent log(0)
y = x * np.log(x)  # y = x * log(x)

# Plot the graph
plt.plot(x, y, label='y = x*log(x)', color='purple')
plt.title('Graph of y = x*log(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
```

#### Output:
![Alt text](/Numpy/Resources/Images/66330d5b-9bfc-4380-a9bd-5f912fd05f99.png)


#### Explanation:
- The function computes the product of $ x $ and its natural logarithm (`np.log(x)`).
- The graph highlights the logarithmic growth, demonstrating how $ y $ increases with $ x $.

### Combined Visualization

To visualize all the functions in one graph:

```python
x = np.linspace(-10, 10, 100)
x_positive = np.linspace(0.1, 10, 100)

plt.plot(x, x, label='y = x', color='blue')
plt.plot(x, x**2, label='y = x^2', color='green')
plt.plot(x, np.sin(x), label='y = sin(x)', color='red')
plt.plot(x_positive, x_positive * np.log(x_positive), label='y = x*log(x)', color='purple')

plt.title('Combined Graphs')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
```

#### Output:
![Alt text](/Numpy/Resources/Images/c4b25e70-44e9-470a-a1a2-d3f4e8f5695f.png)

### Applications in Data Science

1. **Exploratory Data Analysis (EDA)**:
   - Visualizing relationships between variables.
   - Understanding data distributions using mathematical functions.
   
2. **Signal Processing**:
   - Using functions like $ y = \sin(x) $ to analyze waveforms.

3. **Optimization Problems**:
   - Graphing loss functions to understand optimization dynamics.

4. **Feature Engineering**:
   - Applying transformations (e.g., logarithmic scaling) and visualizing their effects.

5. **Model Training**:
   - Plotting cost functions to monitor model performance.

### Conclusion

NumPy makes it simple to generate data for plotting mathematical functions, while Matplotlib visualizes these functions effectively. By understanding how to plot graphs like $ y = x $, $ y = x^2 $, $ y = \sin(x) $, and $ y = x \log(x) $, you gain insights into their behavior and practical applications in data science workflows.


> [!IMPORTANT]  
> If you have studied Article 86-91, I would suggest you to perform some task so that you can check on your learning. Here is the link : [Task 14](/Numpy/Tasks/task_14.ipynb)


<!-- > [!TIP]  
> Link to Next Article  
> 🡺 []() -->