#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Integration tests for Flask-Walrus."""

import flask
from flask_walrus import FlaskWalrus
import pytest


@pytest.fixture
def app():
    return flask.Flask(__name__)


def test_constructor(app):
    """Test that a constructor with app instance
    will initialize the connection."""
    walrus = FlaskWalrus(app)
    assert walrus._walrus_client is not None
    assert hasattr(walrus._walrus_client, 'connection_pool')


def test_init_app(app):

    walrus = FlaskWalrus()

    assert walrus._walrus_client is None
    walrus.init_app(app)
    assert walrus._walrus_client is not None
    assert hasattr(walrus._walrus_client, 'connection_pool')
    if hasattr(app, 'extensions'):
        assert 'walrus' in app.extensions
        assert app.extensions['walrus'] == walrus


def test_custom_prefix(app):
    app.config['RDB1_URL'] = 'redis://localhost:6379/5'
    app.config['RDB2_URL'] = 'redis://localhost:6379/23'

    walrus1 = FlaskWalrus(app, config_prefix='RDB1')
    walrus2 = FlaskWalrus(app, config_prefix='RDB2')

    assert walrus1.connection_pool.connection_kwargs['db'] == 5
    assert walrus2.connection_pool.connection_kwargs['db'] == 23
