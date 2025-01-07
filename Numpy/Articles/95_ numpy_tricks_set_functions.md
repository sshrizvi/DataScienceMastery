# <picture> <source srcset="https://numpy.org/images/logo.svg" type="image/webp"> <img src="https://numpy.org/images/logo.svg" width="32" height="32"> </picture> NumPy for Data Science 

> [!TIP]  
> Link to Previous Article  
> 🡸 [Numpy Tricks : Important Methods - Part Three](/Numpy/Articles/94_numpy_tricks_part3.md)

## Numpy Tricks : Set Functions

NumPy provides robust set functions that enable operations like union, intersection, and set differences. These are particularly useful for handling array-based data and understanding relationships between datasets. This guide will cover the following functions:

- `np.union1d()`
- `np.intersect1d()`
- `np.setdiff1d()`
- `np.setxor1d()`
- `np.in1d()`

Each topic includes a theoretical explanation, an example, deep analysis of the example, additional examples (if necessary), and applications in the Data Science field.

### 1. **`np.union1d()`**

#### Theoretical Explanation

`np.union1d()` returns the union of two arrays, i.e., all unique elements present in either array, sorted.

#### Syntax:

```python
numpy.union1d(ar1, ar2)
```

- **`ar1`**: First input array.
- **`ar2`**: Second input array.

#### Example:

```python
import numpy as np

arr1 = [1, 2, 3]
arr2 = [3, 4, 5]
union = np.union1d(arr1, arr2)
print("Union:", union)
```

#### Explanation:

1. **Input**: Arrays `[1, 2, 3]` and `[3, 4, 5]`.
2. **Process**: Combines both arrays and removes duplicates.
3. **Output**: `[1, 2, 3, 4, 5]`.

#### Applications in Data Science:

- Combining unique values from multiple datasets.
- Aggregating features across different sources.

### 2. **`np.intersect1d()`**

#### Theoretical Explanation

`np.intersect1d()` computes the intersection of two arrays, i.e., elements that are common to both arrays.

#### Syntax:

```python
numpy.intersect1d(ar1, ar2, assume_unique=False, return_indices=False)
```

- **`ar1`**: First input array.
- **`ar2`**: Second input array.
- **`assume_unique`**: If `True`, assumes arrays are unique (default: `False`).
- **`return_indices`**: If `True`, returns the indices of the common elements.

#### Example:

```python
arr1 = [1, 2, 3]
arr2 = [3, 4, 5]
intersection = np.intersect1d(arr1, arr2)
print("Intersection:", intersection)
```

#### Explanation:

1. **Input**: Arrays `[1, 2, 3]` and `[3, 4, 5]`.
2. **Process**: Finds common element(s).
3. **Output**: `[3]`.

#### Applications in Data Science:

- Identifying shared attributes between datasets.
- Filtering overlapping data points.

### 3. **`np.setdiff1d()`**

#### Theoretical Explanation

`np.setdiff1d()` computes the set difference, returning elements in the first array that are not in the second.

#### Syntax:

```python
numpy.setdiff1d(ar1, ar2, assume_unique=False)
```

- **`ar1`**: Input array.
- **`ar2`**: Values to remove from `ar1`.
- **`assume_unique`**: If `True`, assumes arrays are unique (default: `False`).

#### Example:

```python
arr1 = [1, 2, 3]
arr2 = [3, 4, 5]
difference = np.setdiff1d(arr1, arr2)
print("Difference:", difference)
```

#### Explanation:

1. **Input**: Arrays `[1, 2, 3]` and `[3, 4, 5]`.
2. **Process**: Removes elements of `arr2` from `arr1`.
3. **Output**: `[1, 2]`.

#### Applications in Data Science:

- Finding unique entries in a dataset.
- Filtering irrelevant data.

### 4. **`np.setxor1d()`**

#### Theoretical Explanation

`np.setxor1d()` computes the symmetric difference, returning elements present in either array but not in both.

#### Syntax:

```python
numpy.setxor1d(ar1, ar2, assume_unique=False)
```

- **`ar1`**: First input array.
- **`ar2`**: Second input array.
- **`assume_unique`**: If `True`, assumes arrays are unique (default: `False`).

#### Example:

```python
arr1 = [1, 2, 3]
arr2 = [3, 4, 5]
xor = np.setxor1d(arr1, arr2)
print("Symmetric Difference:", xor)
```

#### Explanation:

1. **Input**: Arrays `[1, 2, 3]` and `[3, 4, 5]`.
2. **Process**: Finds elements unique to each array.
3. **Output**: `[1, 2, 4, 5]`.

#### Applications in Data Science:

- Comparing datasets to find exclusive values.
- Analyzing differences in feature sets.

### 5. **`np.in1d()`**

#### Theoretical Explanation

`np.in1d()` tests whether elements of one array are present in another and returns a boolean array.

#### Syntax:

```python
numpy.in1d(element, test_elements, assume_unique=False, invert=False)
```

- **`element`**: Input array to test.
- **`test_elements`**: Values to check against.
- **`assume_unique`**: If `True`, assumes both arrays are unique (default: `False`).
- **`invert`**: If `True`, returns elements not in `test_elements`.

#### Example:

```python
arr = [1, 2, 3, 4, 5]
test = [3, 5]
result = np.in1d(arr, test)
print("In1D Result:", result)
```

#### Explanation:

1. **Input**: Array `[1, 2, 3, 4, 5]` and test elements `[3, 5]`.
2. **Process**: Checks membership.
3. **Output**: `[False, False, True, False, True]`.

#### Applications in Data Science:

- Filtering rows based on membership.
- Checking categorical data values.

### Conclusion

Set functions in NumPy are essential for understanding and manipulating relationships between datasets. They simplify tasks such as combining, comparing, and filtering data, making them indispensable for data science workflows.

> [!IMPORTANT]  
> If you have studied Article 92-95, I would suggest you to perform some task so that you can check on your learning. Here is the link : [Task 15](/Numpy/Tasks/task_15.ipynb)

> [!TIP]  
> Link to Next Article  
> 🡺 [Exploring More NumPy Functions](/Numpy/Articles/96_more_numpy_functions.md)