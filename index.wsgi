
import os,sys,sae
root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages'))


import duoshuo

from web_app import wsgi
application=sae.create_wsgi_app(wsgi.application)
