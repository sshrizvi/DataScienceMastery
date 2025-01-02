# <picture> <source srcset="https://numpy.org/images/logo.svg" type="image/webp"> <img src="https://numpy.org/images/logo.svg" width="32" height="32"> </picture> NumPy for Data Science 

> [!TIP]  
> Link to Previous Article  
> 🡸 [Numpy Tricks : Important Methods - Part Two](/Numpy/Articles/93_numpy_tricks_part2.md)

## Numpy Tricks : Important Methods - Part Three

NumPy offers a variety of functions that simplify data analysis and manipulation tasks, making it indispensable for data science. This guide will focus on the following functions:
- `np.percentile()`
- `np.histogram()`
- `np.corrcoef()`
- `np.isin()`
- `np.flip()`
- `np.put()`
- `np.delete()`
- `np.clip()`

Each topic includes a theoretical explanation, an example, deep analysis of the example, additional examples (if necessary), and applications in the Data Science field.

### 1. **`np.percentile()`**

#### Theoretical Explanation
`np.percentile()` computes the nth percentile of an array—a value below which a certain percentage of data falls. Percentiles are widely used to summarize the distribution of data.

#### Syntax:
```python
numpy.percentile(a, q, axis=None, out=None, interpolation='linear')
```
- **`a`**: Input array.
- **`q`**: Percentile value(s) to compute (0-100).
- **`axis`**: Axis along which the percentiles are computed. Default is the flattened array.
- **`out`**: Alternative output array to store the result.
- **`interpolation`**: Method to calculate the percentile if the exact position is between data points (e.g., 'linear', 'nearest').

#### Example:
```python
import numpy as np

data = [10, 20, 30, 40, 50]
p50 = np.percentile(data, 50)
print("50th Percentile:", p50)
```

#### Explanation:
1. **Input**: The array `[10, 20, 30, 40, 50]`.
2. **50th Percentile**: The median value, which divides the data into two equal halves.
3. **Result**: `30` is returned as it’s the middle value.

#### Applications in Data Science:
- Identifying outliers by comparing data points to the 25th and 75th percentiles.
- Summarizing data distributions in exploratory data analysis (EDA).

### 2. **`np.histogram()`**

#### Theoretical Explanation
`np.histogram()` computes the frequency distribution of data by binning values into intervals. It’s commonly used for creating histograms.

#### Syntax:
```python
numpy.histogram(a, bins=10, range=None, density=False)
```
- **`a`**: Input array.
- **`bins`**: Number of bins or specific bin edges.
- **`range`**: Lower and upper range of bins.
- **`density`**: If `True`, normalizes the histogram.

#### Example:
```python
values = [1, 2, 1, 4, 3, 4, 2, 2]
bins, edges = np.histogram(values, bins=4)
print("Bins:", bins)
print("Edges:", edges)
```

#### Explanation:
1. **Input**: Data `[1, 2, 1, 4, 3, 4, 2, 2]` with `bins=4`.
2. **Bins**: Counts of values in each interval: `[2, 3, 1, 2]`.
3. **Edges**: The intervals: `[1.0, 1.75, 2.5, 3.25, 4.0]`.

#### Applications in Data Science:
- Visualizing data distributions in histograms.
- Grouping continuous data into discrete categories.

### 3. **`np.corrcoef()`**

#### Theoretical Explanation
`np.corrcoef()` calculates the Pearson correlation coefficient between two datasets, quantifying their linear relationship.

#### Syntax:
```python
numpy.corrcoef(x, y=None, rowvar=True, bias=<no value>, ddof=<no value>)
```
- **`x, y`**: Input datasets.
- **`rowvar`**: If `True`, rows represent variables; columns represent observations.

#### Example:
```python
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
correlation = np.corrcoef(x, y)
print("Correlation Matrix:", correlation)
```

#### Explanation:
1. **Input**: `x` and `y` have an inverse relationship.
2. **Output**: Correlation matrix shows `-1`, indicating a perfect negative correlation.

#### Applications in Data Science:
- Identifying relationships between features.
- Feature selection for machine learning models.

### 4. **`np.isin()`**

#### Theoretical Explanation
`np.isin()` checks if elements of an array are present in another array and returns a boolean array.

#### Syntax:
```python
numpy.isin(element, test_elements, assume_unique=False, invert=False)
```
- **`element`**: Array to test.
- **`test_elements`**: Values to check against.

#### Example:
```python
arr = [1, 2, 3, 4, 5]
check = [2, 5]
result = np.isin(arr, check)
print("Result:", result)
```

#### Explanation:
1. **Input**: Checks if `[2, 5]` are in `[1, 2, 3, 4, 5]`.
2. **Result**: `[False, True, False, False, True]`.

#### Applications in Data Science:
- Filtering data based on membership conditions.
- Checking category memberships.

### 5. **`np.flip()`**

#### Theoretical Explanation
`np.flip()` reverses the order of elements along a specified axis.

#### Syntax:
```python
numpy.flip(a, axis=None)
```
- **`a`**: Input array.
- **`axis`**: Axis to flip. Default is all axes.

#### Example:
```python
arr = np.array([1, 2, 3, 4])
flipped = np.flip(arr)
print("Flipped Array:", flipped)
```

#### Explanation:
1. **Input**: Array `[1, 2, 3, 4]`.
2. **Output**: Reversed array `[4, 3, 2, 1]`.

#### Applications in Data Science:
- Reversing time-series data.
- Creating mirrored datasets for augmentation.

### 6. **`np.put()`**

#### Theoretical Explanation
`np.put()` replaces specific elements in an array at specified indices with new values.

#### Syntax:
```python
numpy.put(a, ind, v, mode='raise')
```
- **`a`**: Array to modify.
- **`ind`**: Indices of elements to replace.
- **`v`**: Values to assign.

#### Example:
```python
arr = np.array([1, 2, 3, 4])
np.put(arr, [0, 3], [9, 8])
print("Modified Array:", arr)
```

#### Explanation:
1. **Input**: Replaces indices `[0, 3]` with values `[9, 8]`.
2. **Output**: `[9, 2, 3, 8]`.

#### Applications in Data Science:
- Replacing outliers or missing values.

### 7. **`np.delete()`**

#### Theoretical Explanation
`np.delete()` removes elements along a specified axis.

#### Syntax:
```python
numpy.delete(arr, obj, axis=None)
```
- **`arr`**: Input array.
- **`obj`**: Indices of elements to remove.
- **`axis`**: Axis to perform deletion.

#### Example:
```python
arr = np.array([1, 2, 3, 4])
modified = np.delete(arr, 2)
print("Modified Array:", modified)
```

#### Explanation:
1. **Input**: Removes element at index `2`.
2. **Output**: `[1, 2, 4]`.

#### Applications in Data Science:
- Removing irrelevant or noisy data.

### 8. **`np.clip()`**

#### Theoretical Explanation
`np.clip()` limits the values in an array to a specified range.

#### Syntax:
```python
numpy.clip(a, a_min, a_max, out=None)
```
- **`a`**: Input array.
- **`a_min`**: Minimum value.
- **`a_max`**: Maximum value.

#### Example:
```python
arr = np.array([1, 5, 10, 15])
clipped = np.clip(arr, 3, 12)
print("Clipped Array:", clipped)
```

#### Explanation:
1. **Input**: Limits values to range `[3, 12]`.
2. **Output**: `[3, 5, 10, 12]`.

#### Applications in Data Science:
- Handling outliers.
- Ensuring data stays within realistic bounds.

### Conclusion

These advanced NumPy functions are essential for data manipulation and analysis in Data Science. By mastering them, beginners can handle real-world datasets more effectively, making them a cornerstone of exploratory and preprocessing stages in the data science workflow.

> [!TIP]  
> Link to Next Article  
> 🡺 [umpy Tricks : Set Functions](/Numpy/Articles/95_%20numpy_tricks_set_functions.md)