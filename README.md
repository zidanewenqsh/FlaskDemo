# FlaskDemo
My flask demo project

# My Flask App

这是一个使用 Flask 框架构建的 Web 应用示例项目。

## 特性

- 用户认证（注册、登录、登出）
- 数据库集成
- RESTful API
- 前端使用 Bootstrap 框架

## 快速开始

以下指南将帮助您在本地环境上运行项目。

### 先决条件

确保您已经安装了 Python 和 pip。此项目使用 Python 3。

### 安装

克隆仓库到本地：

```bash
git clone https://github.com/zidanewenqsh/FlaskDemo.git
cd FlaskDemo/my_flask_app
```

建立并激活虚拟环境：

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# 或者在 Unix 或 MacOS 上
source venv/bin/activate
```

安装依赖：

```bash
pip install -r requirements.txt
```

### 配置

复制 `.env.example` 文件为 `.env` 并填写必要的环境变量。

```bash
cp .env.example .env
```

### 数据库迁移

初始化数据库并创建必要的表：

```bash
flask db init
flask db migrate
flask db upgrade
```

### 运行

运行开发服务器：

```bash
flask run
```

或者使用 `run.py`：

```bash
python run.py
```

打开浏览器并访问 `http://127.0.0.1:5000/`。

## 测试

运行测试：

```bash
pytest
```

## 部署

关于如何部署到生产环境的说明。

## 贡献

如果您想为项目贡献代码，请阅读 `CONTRIBUTING.md`。

## 许可证

此项目使用 MIT 许可证 - 详见 [LICENSE.md](LICENSE) 文件了解详情。
