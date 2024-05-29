# Math module
import math

print(math.sqrt(16))
print(math.pow(2,5))
print(dir(math))
math.log10(100)

'''4.0
32.0
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']'''


import calendar
cal = calendar.month(2016,1)
print(cal)
print(calendar.isleap(2016))


# make my own module:

# method 1:
import function1

area1 = function1.area(6,7)
print(area1)

# # method 2:
# import function1 as f

# area1 = f.area(6,7)
# print(area1)


# If the function store in the another directory
# then write as if the function stored in srv1 file
# then write as ------> import srv1.function1 as f


# if the function store in unknown path, then write:
# import sys
# sys.path.append("C:\code")# "C:\code"- Is the system file directory.
