# How to Run? Open Terminal> python3 libEg3.py
# Read the code comments and output on the terminal

# Objective: Know about standard built-in library

# Templating
from string import Template

message = Template('Hello World! my name is ${name}, and you can follow me at $github')

# Note: Raises a KeyError when a placeholder is not supplioed in a dictionary
data = message.substitute(name='Ashwin', github='github.com/hegdeashwin')

print('Template: ', data)

# Logging
import logging

# By default, info and debug messages are suppressed and the output is sent to standard error (STDERR)
logging.debug('[Debug]')
logging.info('[Info]')
logging.warning('[Warning]')
logging.error('[Error]')
logging.critical('[Critical Error]')

