# flake8: noqa
from gevent import monkey
monkey.patch_all(thread=False)
import default_settings
from web import blueprint
