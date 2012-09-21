#!/home/v/vremen2com/vremena/env/bin/python
# -*- coding:utf-8 -*-
activate_this = '/home/v/vremen2com/vremena/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os
import sys

sys.path.insert( 0, '/home/v/vremen2com/vremena/env/lib/site-packages/django')
sys.path.insert( 0, '/home/v/vremen2com/vremena/project')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
