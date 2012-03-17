#!/usr/bin/env python2.7
# vim: fileencoding=utf8

import os
base = os.path.dirname(os.path.abspath(__file__))
activate_this = os.path.join(base, 'env/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
os.chdir(base)

from hskatom import app
app.run(host='0.0.0.0', use_evalex=False)
