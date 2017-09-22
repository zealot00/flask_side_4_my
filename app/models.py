#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author = 'zealot'

from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))
    real_name = db.Column(db.String(128))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    group_id = db.Column(db.Integer,db.ForeignKey('groups.id'))
    card_id = db.Column(db.String(16),unique=True)

    @property
    def password(self):
        raise AttributeError('password is not areadable attribute')



class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User',backref = 'role')

class Group(db.Model):
    __tablename__ = "groups"
    id = db.Column(db.Integer,primary_key=True)
    groupname = db.Column(db.String(64),unique=True,index=True)
    users = db.relationship('User',backref = 'group')

