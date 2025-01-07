# <picture> <source srcset="https://numpy.org/images/logo.svg" type="image/webp"> <img src="https://numpy.org/images/logo.svg" width="32" height="32"> </picture> NumPy for Data Science 

> [!TIP]  
> Link to Previous Article  
> 🡸 [Working with Random Functions in NumPy](/Numpy/Articles/97_working_with_numpy.md)

## NumPy Meshgrid : A Useful Method

Matrix operations are a useful tool for data analysts when modifying structured data. For example, if you already have a table of prices for a set of products by region and need to convert all prices to a single currency, matrix multiplication will likely be the fastest way to get the prices adjusted.

NumPy, Python’s prominent scientific computing package, offers a convenient way to implement matrix operations through the np.meshgrid method. In this article, you’ll learn how to use meshgrid, and why you might want to create grids from NumPy arrays. You’ll also visualize data using meshgrid, and explore practical applications of matrix math.

### What is NumPy Meshgrid?
Meshgrid is a method from Python’s NumPy library, which Python programmers frequently use for scientific computing. Meshgrid is a combination of the words ”mesh” and “grid,” which both refer to a network-like structure. Building such structures is the meshgrid method’s primary purpose.

NumPy arrays are the preferred data structure for large volumes of data in NumPy because of their performance and memory-efficiency. Meshgrid turns one-dimensional NumPy arrays into grids called matrices. If we pass two NumPy arrays into meshgrid, we get two matrices back. Below we use meshgrid to create two grids from two arrays: 

```python
import numpy as np
array_a = [1,2,3,4]
array_b = [10,20,30,40]
 
XX,YY = np.meshgrid(array_a, array_b)
 
XX
>>> array([
      [1, 2, 3, 4, 5],
      [1, 2, 3, 4, 5],
      [1, 2, 3, 4, 5],
      [1, 2, 3, 4, 5],
      [1, 2, 3, 4, 5]])
 
YY
>>> array([
      [10, 10, 10, 10, 10],
      [20, 20, 20, 20, 20],
      [30, 30, 30, 30, 30],
      [40, 40, 40, 40, 40],
      [50, 50, 50, 50, 50]])
```

The grids, or matrices, that meshgrid generates are suitable for matrix math and plotting, among other things. In the following sections, we’ll talk about what makes meshgrid useful.

### Meshgrid Uses

1. Meshgrid turns NumPy arrays into coordinate matrices, or grids of values. Using the matplotlib library, a widely used Python library for creating plots and charts, we can visually represent the two matrices from our example above. The resulting plot contains a grid of values:
    ```python
    import matplotlib.pyplot as plt
    
    plt.plot(XX, YY, marker=".", color='k', linestyle='none')
    
    plt.xticks(array_a)
    plt.yticks(array_b)
    
    plt.show()
    ```
    **Output**  
    ![Alt text](/Numpy/Resources/Images/d83ec82f-0846-4927-917a-b7d30a9120c9.png)
2. If you’ve ever dabbled in *machine learning*, you’ve probably seen meshgrid in action. Meshgrid is often used to visualize the loss function of a machine learning model and how the margin for error of the results the model predicts decreases as the model learns and updates its parameters.

### Plotting Two-dimensional Functions

To plot a function we’ll need some additional code compared to the plotting we did with a static matrix in the previous section. First, we’ll define a sine function:
```python
def sin(x, y):
    return np.sin(x) + np.sin(y)
```
We’ll apply our function over the two arrays that we defined previously and store the result into a variable ZZ:
```python
XX, YY = np.meshgrid(array_a, array_b)
ZZ = sin(XX, YY) 
```
We’ll then plot the results:
```python
fig = plt.figure(figsize=(9, 6))
# Build the plot
plt.imshow(Z, origin="lower")
 
# Display a color scale (values denoted by colors)
plt.colorbar()
 
# Limit the number of values on the axes to 4
plt.locator_params(axis='y', nbins=4)
plt.locator_params(axis='x', nbins=4)

# Display the plot
plt.show()
```
**Output**  
![Alt text](/Numpy/Resources/Images/a280dac4-22c2-467a-aece-4583751d82d8.png)

Unfortunately, the resulting visualization does not contain enough detail for us to understand the behavior of our sine function, since our 4×4 grid was too small to visualize the function’s entire range of values. Let’s give it another attempt on a larger grid. We’ll use NumPy’s linspace method to create two grids consisting of 100 linearly spaced values between –10 and 10.
```python
XX, YY = np.meshgrid(np.linspace(-10,10,100), np.linspace(-10,10,100))
Z = sin(XX, YY) 
```
The new plot looks like this:  
**Output**  
![Alt text](/Numpy/Resources/Images/379d05ec-af0b-4b7a-8fb7-2656ed0242ee.png)

> [!NOTE]
> The new grid looks more detailed. Sampling the function on a larger grid allowed us to visualize the sine function’s characteristic periodicity. Increasing the number of values would make the visualization even smoother, whereas decreasing it would make it more coarse.

You can plot any function as long as you can apply it to the coordinates of the elements in a matrix. Here’s another example of a two-dimensional function:

```python
ZZ = XX ** 2 + (YY - XX) * 2
```
**Output**  
![Alt text](/Numpy/Resources/Images/c69a19b7-0c34-4ca2-ba3d-fd391a75064b.png)

### Plotting Three-Dimensional Functions
To plot a three-dimensional function, we’ll need an additional import:
```python
from mpl_toolkits.mplot3d import Axes3D
```

We’ll create our matrices:
```python
XX, YY = np.meshgrid(np.linspace(-30,30,15), np.linspace(-30,30,15))
Z = XX ** 2 + (YY - XX) * 2
```

Next, we’ll visualize them:
```python
fig = plt.figure(figsize=(10, 14))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(XX,YY,Z)
plt.show()
```
**Output**  
![Alt text](/Numpy/Resources/Images/10274ba3-345c-4384-8c37-d6ed8c85a90a.png)  
Voila! We’ve created a three-dimensional surface plot of a function.


> **ATTRIBUTION**  
> The content of this article is a contribution of Udacity. Check the link in case for detailed article.  
> [Udacity](https://www.udacity.com/blog/2021/10/numpy-np-meshgrid-tutorial-for-beginners.html#:~:text=Meshgrid%20is%20often%20used%20to,meshgrid%20to%20plot%20a%20function.)

> [!TIP]  
> Link to Next Article  
> 🡺 [Image Processing Using NumPy](/Numpy/Articles/99_image_processing.md)