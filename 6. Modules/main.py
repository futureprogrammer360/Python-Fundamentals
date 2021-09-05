"""main.py"""

# Import statement
import module

# Accessing module members
print(module.x)
module.my_function(2)
print(module.C.a)

# Modifying module members
module.x += 2
print(module.x)

# Import from module
from module import x, my_function

print(x)
my_function(2)
print(module.x)

# Import everything
from module import *
print(C.a)

# Aliasing modules
import module as m
print(m.x)
print(module.x)

# dir()
import module
print(dir(module))
