#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/firstApp/")

# Virtual env activation
#activate_this_filepath = '/home/gautam/wwwappenv/bin/activate_this.py'
#with open(activate_this_filepath, "rb") as source_file:
#    code = compile(source_file.read(), activate_this_filepath, "exec")
#exec(code, globals(), locals())


from hello import app as application
application.secret_key = 'your secret key. If you share your website, do NOT share it with this key.'
