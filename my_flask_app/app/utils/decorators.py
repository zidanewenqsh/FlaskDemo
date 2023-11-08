#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""# 工具函数和装饰器"""
from functools import wraps
from flask import request, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'authenticated' not in request.session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
