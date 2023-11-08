#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""# 认证相关视图函数"""
from flask import render_template, redirect, url_for, flash
from app import app
from app.auth.forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # 这里添加验证用户逻辑
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
# app/views.py


@app.route('/register', methods=['GET', 'POST'])
def register():
    # 注册逻辑
    return render_template('register.html')
