# file structure:
# package
#   common
#       validators
#           __init__.py
#           boolean.py
#           date.py

# In __init__.py
from .boolean import *
from .date import *

# With the __init__ set up 
# main.py:
import common.validators as validators

validators.is_boolean('true')

# in date.py
__all__ = ['fn_name'] # this will export only that fn_name described
# or having a "_" in front of a name makes functions private
# then in __init__.py of the parent folder
__all__ = (boolean.__all__ + date.__all__)

# common parent folder will have an empty __init__.py

# in main.py
import common.validators as validators
# can now do this because validators __init__.py has been set up to pull .boolean and with __all__
# as well as having __init__ in validators