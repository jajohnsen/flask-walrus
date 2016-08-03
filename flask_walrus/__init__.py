"""Heavily based on this here Gist I found while doing some idle searching and
enjoying a cup 'o tea @
https://gist.github.com/SpotlightKid/7ffd841cc3f4c8bf90b9
Most of the structure and tests are based on the excellen FlaskRedis extension
@ https://github.com/underyx/flask-redis
"""
from __future__ import absolute_import, print_function, unicode_literals

from walrus import Database

__all__ = ('FlaskWalrus')
__version__ = '0.0.1'


class FlaskWalrus(object):
    """Flask extension class to support the walrus (redis) package in Flask."""

    def __init__(self, app=None, config_prefix='WALRUS', **kwargs):
        self._walrus_client = None
        self.provider_class = Database
        self.provider_kwargs = kwargs
        self.config_prefix = config_prefix

        if app is not None:
            self.init_app(app)

    def init_app(self, app, **kwargs):

        redis_url = app.config.get(
            '{0}_URL'.format(self.config_prefix), 'redis://localhost:6379/0'
        )
        self.provider_kwargs.update(kwargs)

        self._walrus_client = self.provider_class.from_url(
            redis_url, **self.provider_kwargs
        )

        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions[self.config_prefix.lower()] = self

    def __getattr__(self, name):
        return getattr(self._walrus_client, name)

    def __getitem__(self, name):
        return self._walrus_client[name]

    def __setitem__(self, name, value):
        self._walrus_client[name] = value

    def __delitem__(self, name):
        del self._walrus_client[name]
