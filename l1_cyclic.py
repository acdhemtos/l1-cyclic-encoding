import warnings
import numpy as np
from typing import Union, Tuple

def l1_cyclic(
	num: Union[int, float, np.ndarray], 
	*args: Union[int, float]
) -> Tuple[Union[float, np.ndarray], Union[float, np.ndarray]]:
	
	if len(args) == 1:
		min_val, max_val = 0.0, args[0]
		warnings.warn(
			f"Only 1 range argument provided. Assuming a range sequence from minimum = 0.0 to maximum = {max_val}.",
			UserWarning,
			stacklevel=2
		)
	elif len(args) == 2:
		min_val, max_val = args[0], args[1]
	else:
		raise TypeError(
			f"cyclic() takes either 2 or 3 positional arguments (num, max) or (num, min, max), "
			f"but {len(args) + 1} were given."
		)
		
	m = max_val - min_val
	num = num - min_val

	is_array = isinstance(num, (np.ndarray, list, tuple))
	if is_array:
		num = np.asarray(num, dtype=np.float64)
		
	num_wrapped = num % m
	mi = 0.25 * m
	f = (num_wrapped % mi) / mi
	q = (num_wrapped // mi).astype(int) if is_array else int(num_wrapped // mi)

	if is_array:
		conds = [q == 0, q == 1, q == 2, q == 3]
		x1 = np.select(conds, [1 - f, -f, -1 + f, f])
		x2 = np.select(conds, [f, 1 - f, -f, -1 + f])
	else:
		ans = [f, 1 - f, -f, -1 + f]
		x1 = ans[q]
		x2 = ans[(q + 1) % 4]

	return x1, x2