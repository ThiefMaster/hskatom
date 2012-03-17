# vim: ft=python

import os
base = os.path.dirname(os.path.abspath(__file__))
activate_this = os.path.join(base, 'env/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
os.chdir(base)

from hskatom import app as application
