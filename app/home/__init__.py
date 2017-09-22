#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author = 'zealot'

from flask import Blueprint

home = Blueprint('home',__name__)


from . import views