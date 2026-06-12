# L1 Cyclical Encoding Documentation

## Prerequisites
* Python 3.8+
* NumPy 1.20.0+ (Only required for processing arrays)

## Setup & Installation

To use this library as a submodule in your project, clone it directly into your main directory:

```bash
git clone https://github.com/acdhemtos/l1-cyclic-encoding.git
```

Your project directory will look like this:
```
your_project/
│
├── main_script.py
└── l1-cyclic-encoding/
    └── l1_cyclic.py
```

## Importing the Function

Import the module directly from the cloned subdirectory:

```python
from l1_cyclic_encoding.l1_cyclic import l1_cyclic
```

## API Reference
```python
# Format 1: Implicit minimum of 0.0 (Triggers a warning)
x1, x2 = l1_cyclic(num, max_val)

# Format 2: Explicit range
x1, x2 = l1_cyclic(num, min_val, max_val)
```
### Parameters & Outputs
- `num` : `int`, `float` or `np.ndarray` to be encoded.
- `args` : Either `max_val` or `min_val, max_val`.
- **Returns** : A tuple of `(x1, x2)` coordinates on the L1 perimeter ($|x_1| + |x_2| = 1$).

## Usage Examples

### 1. Scalar Baseline
```python
x1, x2 = l1_cyclic(6, 24)
print(f"Coordinates: ({x1}, {x2})")
# Output: (0.0, 1.0)
```

### 2. Explicit Range
```python
x1, x2 = l1_cyclic(-90, -180, 180)
print(f"Coordinates: ({x1}, {x2})")
# Output: (0.0, -1.0)
```
### 3. Vectorized NumPy Column
```python
import numpy as np

hours = np.array([0, 6, 12, 18])
x1_arr, x2_arr = l1_cyclic(hours, 24)
```

## Error Handling
- **Incorrect Arguments** : Passing anything other than 2 or 3 positional parameters raises a `TypeError`.
- **Value Wrapping** : Inputs outside the defined min/max bounds automatically wrap around using native modulo operation logic.