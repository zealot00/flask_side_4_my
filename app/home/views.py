#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author = 'zealot'


from . import home


@home.route('/',methods = ['GET','POST'])
def home_index():
    return "aaa"
