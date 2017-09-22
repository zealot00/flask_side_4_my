#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author = 'zealot'

from flask import jsonify
from . import api


@api.route('/demo',methods = ['GET','POST']) #蓝图
def api_demo():
    key = 'hello'
    value = 'world'
    return jsonify({'key':key,'value':value})