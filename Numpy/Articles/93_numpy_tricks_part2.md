# <picture> <source srcset="https://numpy.org/images/logo.svg" type="image/webp"> <img src="https://numpy.org/images/logo.svg" width="32" height="32"> </picture> NumPy for Data Science 

> [!TIP]  
> Link to Previous Article  
> 🡸 [Numpy Tricks : Important Methods - Part One](/Numpy/Articles/92_numpy_tricks_part1.md)

## Numpy Tricks : Important Methods - Part Two

NumPy offers several advanced yet beginner-friendly functions that are essential for manipulating and analyzing data effectively. This article will cover the following topics in detail:  
- `np.expand_dims()`  
- `np.where()`  
- `np.argmax()` and `np.argmin()`  
- `np.cumsum()`  
- `np.cumprod()`  

Each section will include:
1. Theoretical explanation.  
2. Example with a deep explanation.  
3. Additional examples (if required).  
4. Applications in Data Science.

### 1. **`np.expand_dims()`**

#### Theoretical Explanation  
`np.expand_dims()` is used to add a new axis to an array, effectively increasing its dimensionality. It is useful for reshaping data for compatibility with other arrays or functions.  

#### Syntax:  
```python
numpy.expand_dims(a, axis)
```

- **`a`**: The input array.  
- **`axis`**: The index of the new axis in the expanded array. Negative values count from the end.

#### Example:
```python
import numpy as np

arr = np.array([1, 2, 3])
expanded_arr = np.expand_dims(arr, axis=0)
print("Original Shape:", arr.shape)
print("Expanded Shape:", expanded_arr.shape)
```

#### Explanation:  
1. **Input**: The array `[1, 2, 3]` has shape `(3,)`.  
2. **`np.expand_dims()`**: Adds a new axis at `axis=0`, changing the shape to `(1, 3)`. This makes it a 2D row vector.  

#### Applications in Data Science:  
- Preparing data for machine learning models requiring specific input shapes.  
- Adding batch dimensions to arrays.  

### 2. **`np.where()`**

#### Theoretical Explanation  
`np.where()` is a conditional selection function. It returns indices or values based on a condition.  

#### Syntax:  
```python
numpy.where(condition, [x, y])
```

- **`condition`**: A boolean expression to evaluate.  
- **`x`**: Values to choose if the condition is `True` (optional).  
- **`y`**: Values to choose if the condition is `False` (optional).  

#### Example:
```python
arr = np.array([1, 2, 3, 4, 5])
result = np.where(arr > 3, "High", "Low")
print("Result:", result)
```

#### Explanation:  
1. **Input**: The array `[1, 2, 3, 4, 5]`.  
2. **Condition**: `arr > 3` evaluates to `[False, False, False, True, True]`.  
3. **`np.where()`**: Replaces `True` values with `"High"` and `False` values with `"Low"`, resulting in `['Low', 'Low', 'Low', 'High', 'High']`.

#### Applications in Data Science:  
- Categorizing data based on thresholds.  
- Replacing missing or outlier values.  

### 3. **`np.argmax()` and `np.argmin()`**

#### Theoretical Explanation  
- `np.argmax()` returns the index of the maximum value in an array.  
- `np.argmin()` returns the index of the minimum value in an array.  

#### Syntax:  
```python
numpy.argmax(a, axis=None)
numpy.argmin(a, axis=None)
```

- **`a`**: Input array.  
- **`axis`**: Axis along which to find the maximum or minimum. Default is the flattened array.

#### Example:
```python
arr = np.array([10, 20, 5, 40, 15])
max_index = np.argmax(arr)
min_index = np.argmin(arr)
print("Max Index:", max_index, "Min Index:", min_index)
```

#### Explanation:  
1. **Input**: The array `[10, 20, 5, 40, 15]`.  
2. **`np.argmax()`**: Returns `3` (index of `40`).  
3. **`np.argmin()`**: Returns `2` (index of `5`).  

#### Applications in Data Science:  
- Finding best or worst-performing data points.  
- Locating peaks in datasets.  

### 4. **`np.cumsum()`**

#### Theoretical Explanation  
`np.cumsum()` computes the cumulative sum of elements in an array.  

#### Syntax:  
```python
numpy.cumsum(a, axis=None)
```

- **`a`**: Input array.  
- **`axis`**: Axis along which to calculate the cumulative sum. Default is the flattened array.

#### Example:
```python
arr = np.array([1, 2, 3, 4])
cumulative_sum = np.cumsum(arr)
print("Cumulative Sum:", cumulative_sum)
```

#### Explanation:  
1. **Input**: The array `[1, 2, 3, 4]`.  
2. **`np.cumsum()`**: Adds values sequentially: `[1, 3, 6, 10]`.

#### Applications in Data Science:  
- Calculating running totals.  
- Summing features over time.  

### 5. **`np.cumprod()`**

#### Theoretical Explanation  
`np.cumprod()` computes the cumulative product of elements in an array.  

#### Syntax:  
```python
numpy.cumprod(a, axis=None)
```

- **`a`**: Input array.  
- **`axis`**: Axis along which to calculate the cumulative product. Default is the flattened array.

#### Example:
```python
arr = np.array([1, 2, 3, 4])
cumulative_product = np.cumprod(arr)
print("Cumulative Product:", cumulative_product)
```

#### Explanation:  
1. **Input**: The array `[1, 2, 3, 4]`.  
2. **`np.cumprod()`**: Multiplies values sequentially: `[1, 2, 6, 24]`.

#### Applications in Data Science:  
- Computing compounded growth rates.  
- Analyzing sequential data.  

### Summary Table of Functions

| Function         | Purpose                                   | Key Parameters                     | Example Output                          |
|-------------------|-------------------------------------------|-------------------------------------|-----------------------------------------|
| **`np.expand_dims()`** | Adds a new axis to an array            | `axis`                             | `(3,) → (1, 3)`                         |
| **`np.where()`**   | Conditional selection                    | `condition`, `[x, y]`              | Replace values based on condition       |
| **`np.argmax()`**  | Index of maximum value                   | `axis`                             | Index of the largest value              |
| **`np.argmin()`**  | Index of minimum value                   | `axis`                             | Index of the smallest value             |
| **`np.cumsum()`**  | Cumulative sum of array elements         | `axis`                             | `[1, 2, 3] → [1, 3, 6]`                |
| **`np.cumprod()`** | Cumulative product of array elements     | `axis`                             | `[1, 2, 3] → [1, 2, 6]`                |


### Conclusion  

These advanced NumPy functions are essential for efficient data manipulation and analysis in Data Science. They simplify tasks like reshaping data, filtering values, and calculating cumulative statistics, enabling you to focus on deriving meaningful insights. By understanding their parameters and applications, you can confidently use them in your data science workflows.

it 
> Link to Next Article  
> 🡺 [Numpy Tricks : Important Methods - Part Three](/Numpy/Articles/94_numpy_tricks_part3.md)