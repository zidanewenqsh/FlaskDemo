#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""# API路由"""
from flask import jsonify
from app import app

@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())
