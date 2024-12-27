# <picture> <source srcset="https://numpy.org/images/logo.svg" type="image/webp"> <img src="https://numpy.org/images/logo.svg" width="32" height="32"> </picture> NumPy for Data Science 

> [!TIP]  
> Link to Previous Article  
> 🡸 [Numpy V/S Lists](/Numpy/Articles/86_numpy_vs_lists.md)

## Advanced Indexing in NumPy

In the world of NumPy, indexing is a powerful tool that allows you to manipulate and access data efficiently. Beyond basic slicing and indexing, NumPy provides advanced indexing techniques like fancy indexing and boolean indexing, which are indispensable in data manipulation and analysis. Let’s dive into these topics in detail.

### 1. Fancy Indexing

#### Theoretical Explanation

Fancy indexing refers to using *integer arrays* as indices to access specific elements from a NumPy array. Unlike basic slicing, which retrieves slices of data in a continuous range, fancy indexing allows you to *extract arbitrary elements* or reorder data flexibly.

#### Example of Fancy Indexing

```python
import numpy as np

# Create a NumPy array
data = np.array([10, 20, 30, 40, 50])

# Use an integer array as indices
indices = [1, 3, 4]
selected_elements = data[indices]
print(selected_elements)  # Output: [20 40 50]
```

#### Explanation of the Example

- The array `data` contains five elements.
- The `indices` list specifies which positions in the array to access: 1, 3, and 4.
- `data[indices]` fetches the elements at these positions, resulting in `[20, 40, 50]`.
- Fancy indexing is particularly useful when you need to extract or manipulate non-sequential data.

#### More Examples of Fancy Indexing

```python
# 2D Fancy Indexing
matrix = np.array([[1, 2], [3, 4], [5, 6]])
row_indices = [0, 2]
col_indices = [1, 0]
selected = matrix[row_indices, col_indices]
print(selected)  # Output: [2 5]
```

Here, `row_indices` and `col_indices` are combined to extract elements `(0, 1)` and `(2, 0)`.

#### Application in Data Science

Fancy indexing is widely applied in the data science workflow, particularly during the preprocessing and analysis stages. Let’s explore some practical applications:

1. **Feature Selection**: Fancy indexing can be employed to select specific features (columns) from a dataset based on their indices. For instance, if a dataset has columns representing various attributes, fancy indexing enables efficient extraction of the desired subset:

```python
import numpy as np

# Example dataset
dataset = np.array([[5.1, 3.5, 1.4, 0.2],
                    [4.9, 3.0, 1.4, 0.2],
                    [6.3, 3.3, 6.0, 2.5]])

# Selecting columns 0 and 2 (e.g., sepal length and petal length)
selected_columns = dataset[:, [0, 2]]
print(selected_columns)
# Output:
# [[5.1 1.4]
#  [4.9 1.4]
#  [6.3 6.0]]
```

This method is especially useful in feature engineering, where specific attributes are chosen for model training.

2. **Dataset Reshuffling**: During training, reshuffling the rows of a dataset is a common practice to improve model generalization. Fancy indexing makes this straightforward:

```python
# Original dataset
indices = np.array([2, 0, 1])  # Shuffle order
shuffled_dataset = dataset[indices]
print(shuffled_dataset)
# Output:
# [[6.3 3.3 6.0 2.5]
#  [5.1 3.5 1.4 0.2]
#  [4.9 3.0 1.4 0.2]]
```

By rearranging rows, the dataset is randomized, reducing the likelihood of overfitting.

3. **Cluster Analysis**: In clustering tasks, fancy indexing helps retrieve data points belonging to specific clusters identified by a clustering algorithm. For example:

```python
# Example cluster labels
cluster_labels = np.array([0, 1, 0, 2])  # Cluster assignment for each data point
cluster_0_indices = np.where(cluster_labels == 0)[0]
cluster_0_data = dataset[cluster_0_indices]
print(cluster_0_data)
# Output:
# [[5.1 3.5 1.4 0.2]
#  [6.3 3.3 6.0 2.5]]
```

Here, all data points belonging to cluster 0 are efficiently extracted for further analysis.

These applications highlight how fancy indexing enhances workflows by streamlining data selection and manipulation processes in real-world scenarios.

### 2. Boolean Indexing

#### Theoretical Explanation

Boolean indexing allows you to select elements from an array *based on conditions*. It uses a boolean mask—a boolean array of the same shape as the original array—to filter data.

#### Example of Boolean Indexing

```python
# Create a NumPy array
data = np.array([10, 20, 30, 40, 50])

# Apply a condition
greater_than_30 = data > 30
filtered_data = data[greater_than_30]
print(filtered_data)  # Output: [40 50]
```

#### Explanation of the Example

- The condition `data > 30` generates a boolean array: `[False, False, False, True, True]`.
- This boolean mask is applied to `data`, selecting elements where the mask is `True`.
- The result is `[40, 50]`—all elements greater than 30.

#### More Examples of Boolean Indexing

```python
# 2D Boolean Indexing
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mask = matrix % 2 == 0
filtered = matrix[mask]
print(filtered)  # Output: [2 4 6 8]
```

Here, all even numbers in the matrix are selected using the condition `matrix % 2 == 0`.

#### Application in Data Science

Boolean indexing plays a crucial role in:

- **Data cleaning**: Filtering out invalid or missing values.
- **Feature engineering**: Extracting data subsets that meet specific conditions.
- **Outlier detection**: Isolating data points that deviate significantly from the norm.

For example, consider a small dataset where we detect outliers:

```python
import numpy as np

# Sample dataset
data = np.array([10, 12, 15, 100, 18, 200, 22])

# Define an outlier as any value greater than 50
outlier_mask = data > 50
outliers = data[outlier_mask]
print("Outliers:", outliers)  # Output: [100 200]
```

Here, the condition `data > 50` creates a boolean mask, and the resulting array contains the outliers: `[100, 200]`. This approach is invaluable in preprocessing steps where outliers need to be identified and handled.

### Key Takeaways

1. Fancy indexing allows flexible access to specific elements or reordering data.
2. Boolean indexing filters data based on conditions, making it ideal for data preprocessing.
3. Both techniques simplify data manipulation, enhancing productivity in data science tasks.

These advanced indexing methods are foundational tools in data manipulation, enabling you to work efficiently with large datasets. With practice, you’ll unlock their full potential in your data science projects.


> [!TIP]  
> Link to Next Article  
> 🡺 [Broadcasting in NumPy](/Numpy/Articles/88_broadcasting.md)