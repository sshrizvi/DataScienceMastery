# <picture> <source srcset="https://numpy.org/images/logo.svg" type="image/webp"> <img src="https://numpy.org/images/logo.svg" width="32" height="32"> </picture> NumPy for Data Science 

> [!TIP]  
> Link to Previous Article  
> 🡸 [Exploring More NumPy Functions](/Numpy/Articles/96_more_numpy_functions.md)

## Working with Random Functions in NumPy

Random number generation is a core feature of data science, enabling tasks like simulation, data augmentation, and sampling. NumPy provides a comprehensive suite of random-related functions to aid in these tasks. This guide covers:

- `np.random.random()`
- `np.random.seed()`
- `np.random.randint()`
- `np.random.shuffle()`
- `np.random.choice()`

Each section includes theoretical explanations, examples, deep insights, and applications in Data Science.

### 1. **`np.random.random()`**

#### Theoretical Explanation

`np.random.random()` generates random floating-point numbers in the range `[0.0, 1.0)`.

#### Syntax:

```python
numpy.random.random(size=None)
```

- **`size`**: (Optional) Specifies the shape of the output. If `None`, a single float is returned.

#### Example:

```python
import numpy as np

random_number = np.random.random()
print("Random Number:", random_number)

random_array = np.random.random(size=(2, 3))
print("Random Array:\n", random_array)
```

#### Explanation:
1. **Single Value**: The function generates one random float when no `size` is provided.
2. **Array**: With `size=(2, 3)`, it creates a 2x3 array of random values.

#### Applications in Data Science:
- Generating random features for simulations.
- Normalizing data.
- Testing algorithms with arbitrary inputs.

### 2. **`np.random.seed()`**

#### Theoretical Explanation

`np.random.seed()` sets the seed for the random number generator, ensuring reproducibility of random outputs.

#### Syntax:

```python
numpy.random.seed(seed)
```

- **`seed`**: Integer value to initialize the random number generator.

#### Example:

```python
np.random.seed(42)
random_number = np.random.random()
print("Random Number with Seed 42:", random_number)
```

#### Explanation:
1. **Reproducibility**: Using the same seed ensures the same sequence of random numbers every time.
2. **Consistency**: This is crucial for debugging and comparison.

#### Applications in Data Science:
- Ensuring reproducible experiments.
- Debugging models or simulations with controlled randomness.

### 3. **`np.random.randint()`**

#### Theoretical Explanation

`np.random.randint()` generates random integers within a specified range.

#### Syntax:

```python
numpy.random.randint(low, high=None, size=None, dtype=int)
```

- **`low`**: Inclusive lower bound.
- **`high`**: (Optional) Exclusive upper bound.
- **`size`**: Shape of the output.
- **`dtype`**: Data type of the output (default: `int`).

#### Example:

```python
random_int = np.random.randint(10, 20)
print("Random Integer:", random_int)

random_array = np.random.randint(1, 10, size=(3, 3))
print("Random Array:\n", random_array)
```

#### Explanation:
1. **Single Value**: Generates one random integer between 10 (inclusive) and 20 (exclusive).
2. **Array**: Produces a 3x3 matrix of random integers from 1 to 9.

#### Applications in Data Science:
- Randomly splitting datasets.
- Creating synthetic categorical data.
- Generating indices for sampling.

### 4. **`np.random.shuffle()`**

#### Theoretical Explanation

`np.random.shuffle()` randomly permutes the elements of an array in place.

#### Syntax:

```python
numpy.random.shuffle(x)
```

- **`x`**: Input array to be shuffled (modified in place).

#### Example:

```python
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print("Shuffled Array:", arr)
```

#### Explanation:
1. **In-Place Modification**: The original array is altered; no new array is returned.
2. **Randomness**: The order of elements is randomized.

#### Applications in Data Science:
- Randomizing the order of datasets.
- Preparing shuffled training data for machine learning models.

### 5. **`np.random.choice()`**

#### Theoretical Explanation

`np.random.choice()` selects random elements from an array, with or without replacement.

#### Syntax:

```python
numpy.random.choice(a, size=None, replace=True, p=None)
```

- **`a`**: Array or range to sample from.
- **`size`**: Number of samples to draw.
- **`replace`**: If `True`, elements can be selected multiple times.
- **`p`**: Probabilities associated with each element.

#### Example:

```python
arr = [10, 20, 30, 40]
choice = np.random.choice(arr, size=2, replace=False)
print("Random Choice:", choice)

weighted_choice = np.random.choice(arr, size=3, p=[0.1, 0.2, 0.3, 0.4])
print("Weighted Choice:", weighted_choice)
```

#### Explanation:
1. **Random Selection**: Draws 2 elements without replacement.
2. **Weighted Selection**: Probabilities `[0.1, 0.2, 0.3, 0.4]` influence the likelihood of selection.

#### Applications in Data Science:
- Sampling subsets of data.
- Implementing bootstrapping methods.
- Generating weighted random datasets.

### Conclusion

These random-related functions in NumPy are essential for various tasks in Data Science. From generating random numbers to sampling and shuffling, mastering these functions empowers beginners to handle randomness effectively, a key component of real-world data manipulation and modeling.


> [!TIP]  
> Link to Next Article  
> 🡺 [NumPy Meshgrid : A Useful Method](/Numpy/Articles/98_meshgrids.md)