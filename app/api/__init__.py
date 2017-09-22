#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author = 'zealot'

from flask import Blueprint

api = Blueprint('api',__name__)


from . import views