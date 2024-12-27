# <picture> <source srcset="https://numpy.org/images/logo.svg" type="image/webp"> <img src="https://numpy.org/images/logo.svg" width="32" height="32"> </picture> NumPy for Data Science 

> [!TIP]  
> Link to Previous Article  
> 🡸 [Iterating Arrays and More](/Numpy/Articles/85_iterating_arrays_and_more.md)

## NumPy V/S Lists
- In this article, we are going to compare NumPy Arrays with Python Lists on the basis of various factors.

### Comparison on the basis of `Time`
- To be precise, NumPy Arrays take much lesser time to process than Python Lists.
- Let's understand it with the help of an example
  - **Code: Creating two `lists` and Adding them**
    ```python
    import time
    a = [i for i in range(10000000)]
    b = [i for i in range(10000000, 20000000)]
    c = []
    start_time = time.time()
    for i, j in zip(a, b):
        c.append(i + j)
    print(time.time() - start_time, 'seconds')
    ```
  - **Output**
    ```bash
    3.896937131881714 seconds
    ```
  - **Code: Creating two `ndarrays` and Adding them**
    ```python
    import numpy as np
    a = np.arange(10000000)
    b = np.arange(10000000, 20000000)
    start_time = time.time()
    c = a + b
    print(time.time() - start_time, 'seconds')
    ```
  - **Output**
    ```bash
    0.32480645179748535 seconds
    ```
- The above snippets of code and their output clearly shows that NumPy Arrays are much faster than Python Lists. Lets check the performance by simple mathematics.
  - **Code: Comparing Performance of `ndarray` and `list`**
    ```python
    antecedent = 3.90 # 3.896937131881714
    consequent = 0.32 # 0.32480645179748535
    rate = int(antecedent / consequent)
    print(f'ndarrays are {rate} times faster than lists :)')
    ```
  - **Output**
    ```bash
    ndarrays are 12 times faster than lists :)
    ```
- The above code snippet compares and shows that NumPy Arrays are 12 times faster than Python Lists. Ofcourse, the estimate is approx, but it clearly speaks of the better performance of `ndarrays` over `lists` in terms of time.

### Comparison on the basis of `Memory`
- NumPy Arrays are similar to, but better than Python Lists in terms of memory.
- By default, NumPy Arrays are not much better than Python Lists, because the default datatype of `ndarray` is `float64`, which is as efficient as `list`.
- `ndarray` outsmarts `list` by introducing the `dtype` parameter and flexibility of chosing data type of my own choice like `np.int32`, `np.int16`, `np.int8`, which ultimately reduces the size of `ndarray` by 2, 4, or 8 times, respectively.
- Let's understand the discussion with the help of an example.
  - **Code: Creating a `list`**
    ```python
    import sys
    a = [i for i in range(10000000)]
    print(sys.getsizeof(a), 'bytes')
    ```
  - **Output**
    ```bash
    89095160 bytes
    ```
  - **Code: Creating a `ndarray`**
    ```python
    import sys
    import numpy as np
    a = np.arange(10000000, dtype=np.int64)
    print(sys.getsizeof(a), 'bytes')
    ```
  - **Output**
    ```bash
    80000112 bytes
    ```
- In the above code snippet, it is pretty clear that there is not much difference between `ndarray` and `list`. But `ndarray` ace this criteria also by introducing other datatypes. Let's see it.
  - **Code: Creating a `ndarray`**
    ```python
    a = np.arange(10000000, dtype=np.int32)
    b = np.arange(10000000, dtype=np.int16)
    c = np.arange(10000000, dtype=np.int8)
    print(sys.getsizeof(a), 'bytes')
    print(sys.getsizeof(b), 'bytes')
    print(sys.getsizeof(c), 'bytes')
    ```
  - **Output**
    ```bash
    40000112 bytes 
    20000112 bytes
    10000112 bytes
    ```
- In the above code snippet, it is clear that datatypes like `np.int32` reduces the size of `ndarray` by ***2 times***, `np.int16` reduces the size of `ndarray` by ***4 times*** and `np.int8` reduces the size of `ndarray` by ***8 times***.

> [!CAUTION]
> We need to keep in mind that different datatypes have their capacity of representing numbers, hence we need to choose it wisely, else, we may loss our important information or values.
> - **Code: Creating a `ndarray`**
>   ```python
>   a = np.arange(10000000, dtype=np.int32)
>   b = np.arange(10000000, dtype=np.int16)
>   c = np.arange(10000000, dtype=np.int8)
>   print(a)
>   print(b)
>   print(c)
>   ```
> - **Output**
>   ```bash
>   [      0       1       2 ... 9999997 9999998 9999999] 
>   [     0      1      2 ... -27011 -27010 -27009]
>   [  0   1   2 ... 125 126 127]
>   ```
> - In the above code snippet, it is clear that, for each array `a`, `b`, `c`, we asked it to create an array with same values, but only array `a` gives us the desired value. Array `b` and `c` are not able to handle large values because of the datatypes provided, hence, accordingly changes the larger values in their range.

### Comparison on the basis of `Convenience`
- NumPy arrays are much convenient to use and handle than Python lists.
- The example shown in the comparison on the basis of time proves it.
- To add the elements of two lists we need to write a code from scratch, but in the case of NumPy arrays, it becomes much convenient by just  writing `a + b`.
- Also, `ndarrays` comes with a lot of methods loaded in NumPy module, that makes them much convenient than `lists`.


> [!TIP]  
> Link to Next Article  
> 🡺 [Advanced Indexing in NumPy Arrays](/Numpy/Articles/87_advanced_indexing.md)