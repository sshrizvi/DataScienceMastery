# <picture> <source srcset="https://numpy.org/images/logo.svg" type="image/webp"> <img src="https://numpy.org/images/logo.svg" width="32" height="32"> </picture> NumPy for Data Science 

> [!TIP]  
> Link to Previous Article  
> 🡸 [Numpy Tricks : Set Functions](/Numpy/Articles/95_%20numpy_tricks_set_functions.md)

## Exploring More NumPy Functions

NumPy is a powerful library for numerical computing in Python. This article introduces six useful NumPy functions and explains their theoretical concepts, practical examples, and applications in data science.

### 1. **`np.swapaxes()`**

#### Theoretical Explanation
`np.swapaxes()` exchanges two axes of a NumPy array. This is useful for reshaping or reorienting multidimensional data.

#### Syntax:
```python
numpy.swapaxes(a, axis1, axis2)
```
- **`a`**: Input array.
- **`axis1`**: First axis to swap.
- **`axis2`**: Second axis to swap.

#### Example:
```python
import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])
swapped = np.swapaxes(array, 0, 1)
print("Original Array:", array)
print("Swapped Axes Array:", swapped)
```

#### Explanation:
1. **Input**: A 2D array `[[1, 2, 3], [4, 5, 6]]`.
2. **Operation**: Swaps axis 0 (rows) with axis 1 (columns).
3. **Output**: `[[1, 4], [2, 5], [3, 6]]`.

#### Applications in Data Science:
- Reorienting images in image processing.
- Preparing data for machine learning models that require specific dimensional structures.

### 2. **`np.uniform()`**

#### Theoretical Explanation
`np.uniform()` generates random samples from a uniform distribution over a specified range.

#### Syntax:
```python
numpy.uniform(low=0.0, high=1.0, size=None)
```
- **`low`**: Lower boundary of the range.
- **`high`**: Upper boundary of the range.
- **`size`**: Number of random samples to generate.

#### Example:
```python
random_numbers = np.uniform(low=0, high=10, size=5)
print("Random Numbers:", random_numbers)
```

#### Explanation:
1. **Input**: Range `[0, 10]` and size `5`.
2. **Output**: A 1D array with 5 random numbers uniformly distributed between 0 and 10.

#### Applications in Data Science:
- Initializing weights in neural networks.
- Simulating random scenarios for Monte Carlo analysis.

### 3. **`np.count_nonzero()`**

#### Theoretical Explanation
`np.count_nonzero()` counts the number of non-zero elements in an array.

#### Syntax:
```python
numpy.count_nonzero(a, axis=None)
```
- **`a`**: Input array.
- **`axis`**: Axis along which to count non-zero elements. If `None`, counts all non-zero elements.

#### Example:
```python
array = np.array([[0, 1, 2], [3, 0, 4]])
count = np.count_nonzero(array)
print("Number of Non-Zero Elements:", count)
```

#### Explanation:
1. **Input**: A 2D array `[[0, 1, 2], [3, 0, 4]]`.
2. **Output**: Counts non-zero elements and returns `4`.

#### Applications in Data Science:
- Data quality checks by identifying missing or zero-filled entries.
- Summarizing sparse data matrices.

### 4. **`np.tile()`**

#### Theoretical Explanation
`np.tile()` repeats an array along specified dimensions, creating a tiled version of the input.

#### Syntax:
```python
numpy.tile(a, reps)
```
- **`a`**: Input array.
- **`reps`**: Number of repetitions for each axis.

#### Example:
```python
array = np.array([1, 2, 3])
tiled = np.tile(array, 2)
print("Tiled Array:", tiled)
```

#### Explanation:
1. **Input**: Array `[1, 2, 3]` and repetitions `2`.
2. **Output**: `[1, 2, 3, 1, 2, 3]`.

#### Applications in Data Science:
- Data augmentation by repeating values.
- Creating patterns for visualization or testing.

### 5. **`np.repeat()`**

#### Theoretical Explanation
`np.repeat()` repeats elements of an array along a specified axis.

#### Syntax:
```python
numpy.repeat(a, repeats, axis=None)
```
- **`a`**: Input array.
- **`repeats`**: Number of repetitions for each element.
- **`axis`**: Axis along which to repeat values.

#### Example:
```python
array = np.array([1, 2, 3])
repeated = np.repeat(array, 3)
print("Repeated Array:", repeated)
```

#### Explanation:
1. **Input**: Array `[1, 2, 3]` and repetitions `3`.
2. **Output**: `[1, 1, 1, 2, 2, 2, 3, 3, 3]`.

#### Applications in Data Science:
- Data preprocessing to match the size of arrays.
- Creating synthetic data.

### 6. **`np.allclose()`**

#### Theoretical Explanation
`np.allclose()` checks whether two arrays are element-wise equal within a tolerance.

#### Syntax:
```python
numpy.allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False)
```
- **`a, b`**: Input arrays.
- **`rtol`**: Relative tolerance parameter.
- **`atol`**: Absolute tolerance parameter.
- **`equal_nan`**: If `True`, NaN values in the same positions are considered equal.

#### Example:
```python
arr1 = np.array([1.0, 2.0, 3.0])
arr2 = np.array([1.00001, 2.00001, 3.00001])
close = np.allclose(arr1, arr2)
print("Are Arrays Close:", close)
```

#### Explanation:
1. **Input**: Two arrays with minor differences.
2. **Output**: Returns `True` if differences are within tolerance.

#### Applications in Data Science:
- Validating numerical computations.
- Comparing floating-point results.

### Conclusion
These additional NumPy functions offer diverse capabilities for data manipulation, validation, and analysis. Mastering these tools will empower beginners to tackle more complex data science challenges effectively.

> [!TIP]  
> Link to Next Article  
> 🡺 [Working with Random Functions in NumPy](/Numpy/Articles/97_working_with_numpy.md)