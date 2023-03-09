In Python, modules are a way to organize and reuse code. A module is simply a file containing Python definitions and statements. To use the definitions in a module, you need to import it into your code.

Here are the different ways you can import modules in Python:

import module_name: This statement imports the entire module into your code, and you can access the definitions using the module_name.definition_name syntax.

import module_name as alias: This statement imports the module and gives it an alias, so you can refer to it by the alias instead of the full name.

from module_name import definition_name: This statement imports a specific definition from the module into your code, so you can refer to it directly without using the module_name. prefix.

from module_name import *: This statement imports all the definitions from the module into your code, so you can refer to them directly without using the module_name. prefix. However, this is generally not recommended, as it can lead to name clashes and make it harder to read and understand your code.

Here's an example of importing the math module and using some of its definitions:

import math

print(math.pi)              # prints the value of pi
print(math.sqrt(4))         # prints the square root of 4
You can also use the as keyword to give the module an alias:

import math as m

print(m.pi)                 # prints the value of pi using the alias
print(m.sqrt(4))            # prints the square root of 4 using the alias
Finally, here's an example of importing a specific definition from a module:

from math import pi

print(pi)                   # prints the value of pi directly
Overall, understanding how to import modules in Python is an important part of writing reusable and maintainable code.
