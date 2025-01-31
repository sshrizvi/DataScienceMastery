# <picture> <source srcset="https://numpy.org/images/logo.svg" type="image/webp"> <img src="https://numpy.org/images/logo.svg" width="32" height="32"> </picture> NumPy for Data Science 

> [!TIP]  
> Link to Previous Article  
> 🡸 [Image Processing Using NumPy](/Numpy/Articles/99_image_processing.md)

# Structured Arrays and Saving/Loading NumPy Objects

In data science, working with complex datasets and efficiently saving/loading them is a common task. NumPy provides robust tools like structured arrays for handling heterogeneous data and functions for persisting data. This guide will provide a beginner-friendly explanation of these concepts, examples, and their applications in data science.

## 1. Structured Arrays

### **Theoretical Explanation**
Structured arrays in NumPy allow you to work with heterogeneous data (i.e., data of different types) in a single array. This is particularly useful when you need to manage datasets with fields like names, ages, and scores, each having a different datatype.

Structured arrays use a `dtype` parameter to define a structure for each element in the array. The `dtype` specifies the field names and their associated types.

### **Syntax**
```python
numpy.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
```

- **`object`**: The input data (e.g., a list of tuples or dictionaries).
- **`dtype`**: Specifies the data type of each field.
- **`copy`**: If `True`, a new copy of the data is made.

### **Example**
```python
import numpy as np

# Creating a structured array
data = np.array([("Alice", 25, 85.5), ("Bob", 30, 90.0)],
                dtype=[("Name", "U10"), ("Age", "i4"), ("Score", "f4")])
print(data)
```

### **Explanation**
1. **Input**: A list of tuples with fields: name (string), age (integer), and score (float).
2. **`dtype`**: Defines the structure: `"U10"` for a string of up to 10 characters, `"i4"` for a 4-byte integer, and `"f4"` for a 4-byte float.
3. **Output**:
   ```
   [('Alice', 25, 85.5) ('Bob', 30, 90.0)]
   ```
   Each tuple corresponds to one row in the dataset.

### **More Examples**
#### Accessing Specific Fields:
```python
print(data["Name"])  # Output: ['Alice' 'Bob']
print(data["Score"] > 85)  # Output: [ True  True ]
```

#### Adding a New Entry:
```python
new_entry = np.array([("Charlie", 35, 78.0)], dtype=data.dtype)
data = np.append(data, new_entry)
print(data)
```

### **Applications in Data Science**
- Managing tabular datasets with different types (e.g., numerical and categorical data).
- Preprocessing structured data for machine learning models.
- Organizing datasets during exploratory data analysis (EDA).

## 2. Saving and Loading NumPy Objects

### **Theoretical Explanation**
NumPy provides simple and efficient methods to save and load data. This is essential when working with large datasets or models that need to be reused across sessions.

NumPy supports two key formats:
1. **Binary Format (`.npy`)**: Saves a single array in binary format.
2. **Compressed Archive (`.npz`)**: Saves multiple arrays in a compressed format.

### **Saving Objects**
#### **Syntax for `save`**
```python
numpy.save(file, arr, allow_pickle=True, fix_imports=True)
```
- **`file`**: File path or name (e.g., `"data.npy"`).
- **`arr`**: Array to save.
- **`allow_pickle`**: If `True`, saves objects using Python’s pickle module.

#### Example:
```python
array = np.array([1, 2, 3, 4, 5])
np.save("my_array.npy", array)
print("Array saved!")
```

#### **Explanation**
1. **Input**: An array `[1, 2, 3, 4, 5]`.
2. **Output**: File `my_array.npy` is created in the current directory.

### **Loading Objects**
#### **Syntax for `load`**
```python
numpy.load(file, mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII')
```
- **`file`**: File path or name.
- **`mmap_mode`**: Memory-mapping mode for efficient loading of large files.

#### Example:
```python
loaded_array = np.load("my_array.npy")
print("Loaded Array:", loaded_array)
```

#### **Explanation**
1. **Input**: File `my_array.npy`.
2. **Output**:
   ```
   Loaded Array: [1 2 3 4 5]
   ```
   Restores the saved array.

### **Saving Multiple Objects**
#### Example:
```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
np.savez("my_data.npz", array1=x, array2=y)
```

### **Loading Multiple Objects**
```python
data = np.load("my_data.npz")
print(data["array1"])  # Output: [1 2 3]
print(data["array2"])  # Output: [4 5 6]
```

### **Applications in Data Science**
- Saving preprocessed datasets for future analysis.
- Storing trained model parameters or intermediate results.
- Efficiently managing large datasets in compressed formats.

### Conclusion
Structured arrays simplify the management of heterogeneous data, while saving/loading functions make workflows efficient and reproducible. Together, these tools are indispensable for handling and persisting data in data science projects. Mastering them is a crucial step for any beginner in the field.

> [!IMPORTANT] QUESTIONS    
> I would suggest you to solve 100 questions on NumPy for experience and learning purpose.  
> I am going to attach a Jupyter Notebook Link here which contains 100 questions on NumPy that are officially listed in NumPy website.  
> Here is the link : [100 Numpy Questions]()



> [!TIP]  
> Link to Next Article  
> 🡺 [Pandas Introduction](../../Pandas/Articles/101_pandas_introduction.md)