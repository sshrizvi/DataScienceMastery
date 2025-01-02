# <picture> <source srcset="https://numpy.org/images/logo.svg" type="image/webp"> <img src="https://numpy.org/images/logo.svg" width="32" height="32"> </picture> NumPy for Data Science 

> [!TIP]  
> Link to Previous Article  
> 🡸 [Plotting Graphs Using NumPy](/Numpy/Articles/91_plotting_graphs_using_numpy.md)

## Numpy Tricks : Important Methods - Part One

NumPy, a core library in Python for numerical computing, provides various powerful functions to handle data manipulation and transformation. In this article, we’ll explore five essential NumPy functions—`np.sort()`, `np.argsort()`, `np.append()`, `np.concatenate()`, and `np.unique()`—and how they are used in data science workflows.

Each section includes:
1. A theoretical explanation.
2. A detailed example.
3. Deep explanation of the example.
4. Additional examples (if needed).
5. Applications in data science.

### 1. **`np.sort()`**

#### Theoretical Explanation  
The `np.sort()` function sorts the elements of an array in ascending order by default. Sorting can be performed along specific axes for multidimensional arrays. This function does **not modify** the original array but returns a sorted copy.

#### Syntax:  
```python
numpy.sort(a, axis=-1, kind='quicksort', order=None)
```

- **`a`**: The input array to be sorted.  
- **`axis`**: Axis along which to sort. Default is `-1` (last axis). Use `None` to flatten the array before sorting.  
- **`kind`**: Sorting algorithm to use. Options include:
  - `'quicksort'` (default): Fast but not stable.
  - `'mergesort'`: Stable and slower.
  - `'heapsort'`: Memory efficient.  
- **`order`**: Field names to sort for structured arrays.

#### Example:
```python
import numpy as np

arr = np.array([4, 2, 7, 1, 3])
sorted_arr = np.sort(arr)
print("Original Array:", arr)
print("Sorted Array:", sorted_arr)
```

#### Explanation:  
1. **Input**: The array `[4, 2, 7, 1, 3]` is unsorted.  
2. **`np.sort()`**: Returns a new array `[1, 2, 3, 4, 7]`, which is sorted in ascending order. The original array remains unchanged.

#### Applications in Data Science:  
- Organizing data for analysis.  
- Sorting feature values for statistical computations.  
- Preprocessing data for machine learning algorithms.

### 2. **`np.argsort()`**

#### Theoretical Explanation  
`np.argsort()` returns the indices that would sort the array. This is useful for reordering other arrays based on the sorting order of one array.

#### Syntax:  
```python
numpy.argsort(a, axis=-1, kind='quicksort', order=None)
```

- Parameters are the same as `np.sort()`.

#### Example:
```python
arr = np.array([4, 2, 7, 1, 3])
indices = np.argsort(arr)
sorted_arr = arr[indices]
print("Indices:", indices)
print("Sorted Array Using Indices:", sorted_arr)
```

#### Explanation:  
1. **`np.argsort()`**: Returns `[3, 1, 4, 0, 2]`, which are the indices that sort the array.  
2. **Indexing**: Using `arr[indices]` rearranges the original array into a sorted order.

#### Applications in Data Science:  
- Ranking data.  
- Sorting related datasets while maintaining relationships.  
- Efficient implementation of search algorithms.

### 3. **`np.append()`**

#### Theoretical Explanation  
The `np.append()` function adds elements to the end of an array and returns a new array. This function **does not modify** the original array.

#### Syntax:  
```python
numpy.append(arr, values, axis=None)
```

- **`arr`**: Input array.  
- **`values`**: Values to append. Must match the shape of the array along the specified axis.  
- **`axis`**: The axis along which to append. If `None`, both arrays are flattened.

#### Example:
```python
arr = np.array([1, 2, 3])
new_arr = np.append(arr, [4, 5])
print("Original Array:", arr)
print("Appended Array:", new_arr)
```

#### Explanation:  
1. **Input**: The array `[1, 2, 3]`.  
2. **`np.append()`**: Adds `[4, 5]` to the end, resulting in `[1, 2, 3, 4, 5]`.

#### Applications in Data Science:  
- Adding new data points.  
- Dynamically building datasets during data preprocessing.

### 4. **`np.concatenate()`**

#### Theoretical Explanation  
The `np.concatenate()` function combines two or more arrays along a specified axis. Unlike `np.append()`, it requires arrays to match dimensions along all but the concatenation axis.

#### Syntax:  
```python
numpy.concatenate((arr1, arr2, ...), axis=0)
```

- **`arr1, arr2, ...`**: Tuple of arrays to concatenate.  
- **`axis`**: Axis along which to join arrays. Default is `0`.

#### Example:
```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.concatenate((arr1, arr2))
print("Concatenated Array:", result)
```

#### Explanation:  
1. **Input**: Two arrays `[1, 2, 3]` and `[4, 5, 6]`.  
2. **`np.concatenate()`**: Joins them into `[1, 2, 3, 4, 5, 6]`.

#### Applications in Data Science:  
- Combining datasets.  
- Merging feature arrays.  
- Preparing training and test data for models.

### 5. **`np.unique()`**

#### Theoretical Explanation  
The `np.unique()` function finds and returns unique elements in an array. It can also return the counts or indices of unique values.

#### Syntax:  
```python
numpy.unique(arr, return_index=False, return_inverse=False, return_counts=False, axis=None)
```

- **`arr`**: Input array.  
- **`return_index`**: If `True`, returns indices of first occurrences.  
- **`return_inverse`**: If `True`, returns indices to reconstruct the array.  
- **`return_counts`**: If `True`, returns the count of each unique value.  
- **`axis`**: The axis along which to find unique values.

#### Example:
```python
arr = np.array([1, 2, 2, 3, 1, 4, 4])
unique_values, counts = np.unique(arr, return_counts=True)
print("Unique Values:", unique_values)
print("Counts:", counts)
```

#### Explanation:  
1. **Input**: The array `[1, 2, 2, 3, 1, 4, 4]`.  
2. **`np.unique()`**: Returns `[1, 2, 3, 4]` and counts `[2, 2, 1, 2]`.

#### Applications in Data Science:  
- Identifying distinct categories in categorical data.  
- Counting occurrences in datasets.  
- Feature engineering.

### Summary Table of Functions

| Function         | Purpose                                | Key Parameters                          | Returns                                  |
|-------------------|----------------------------------------|-----------------------------------------|------------------------------------------|
| **`np.sort()`**   | Sorts an array                        | `axis`, `kind`, `order`                | Sorted copy of the array                 |
| **`np.argsort()`**| Returns indices for sorting           | `axis`, `kind`, `order`                | Indices that sort the array              |
| **`np.append()`** | Adds elements to an array             | `values`, `axis`                       | New array with appended elements         |
| **`np.concatenate()`** | Combines arrays along an axis   | `axis`                                 | Concatenated array                       |
| **`np.unique()`** | Finds unique elements in an array     | `return_index`, `return_counts`, `axis`| Unique values and optional metadata      |

### Conclusion  

By mastering these essential NumPy functions, you can efficiently manipulate data for analysis, visualization, and machine learning workflows. They form the building blocks of many complex operations in data science, making them indispensable for beginners and experts alike.

<!-- > [!TIP]  
> Link to Next Article  
> 🡺 []() -->