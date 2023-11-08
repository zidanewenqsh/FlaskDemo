import os
import sys

# 定义要创建的目录和文件结构
project_structure = {
    'my_flask_app/': {
        'app/': {
            'templates/': {
                'base.html': '',
                'index.html': '',
                'login.html': '',
                'register.html': '',
            },
            'static/': {
                'css/': {},
                'js/': {},
                'images/': {},
            },
            'main/': {
                '__init__.py': '# 主模块初始化',
                'views.py': '# 主视图函数',
            },
            'auth/': {
                '__init__.py': '# 认证模块初始化',
                'forms.py': '# 表单定义',
                'views.py': '# 认证相关视图函数',
                'email.py': '# 认证相关邮件处理',
            },
            'api/': {
                '__init__.py': '# API模块初始化',
                'routes.py': '# API路由',
            },
            'models/': {
                '__init__.py': '# 数据模型初始化',
                'user.py': '# 用户模型',
            },
            'utils/': {
                'decorators.py': '# 工具函数和装饰器',
            },
            'tests/': {
                '__init__.py': '# 测试模块初始化',
                'test_basic.py': '# 基础测试',
                'test_user_model.py': '# 用户模型测试',
            },
            '__init__.py': '# 应用初始化',
            'config.py': '# 配置文件',
        },
        'migrations/': {
            'versions/': {},
        },
        'requirements.txt': '# 项目依赖',
        '.env': '# 环境变量配置',
        'config.py': '# 主配置文件',
        'manage.py': '# 管理脚本',
        'run.py': '# 运行脚本',
    },
}
pythonprefix = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# 创建目录和文件的函数
def create_project_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        try:
            if isinstance(content, dict):
                # 创建目录
                os.makedirs(path, exist_ok=True)
                # 递归创建子目录和文件
                create_project_structure(path, content)
            else:
                # # 创建文件并写入注释
                # with open(path, 'w', encoding='utf-8') as f:
                #     if (path.endswith(".py")):
                #         f.write(pythonprefix)
                #         f.write('"""' + content + '"""\n')
                #     # f.write(content)
                pass
        except PermissionError as e:
            print(f"权限错误: {e}")
            sys.exit(1)

# 在当前目录下创建项目结构
create_project_structure('.', project_structure)

print("Flask 项目结构已创建完成！")
