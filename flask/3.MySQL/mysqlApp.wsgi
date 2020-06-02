#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/")

# Virtual env activation
#activate_this = '/path/to/env/bin/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))

from mysqlApp import app as application
application.secret_key = 'your secret key. If you share your website, do NOT share it with this key.'
