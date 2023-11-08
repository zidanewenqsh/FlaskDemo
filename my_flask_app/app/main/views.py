#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""# 主视图函数"""
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')
