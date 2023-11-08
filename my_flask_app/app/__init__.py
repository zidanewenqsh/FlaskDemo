#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""# 应用初始化"""
from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app.main import views
from app.auth import views

