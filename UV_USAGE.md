# UV 环境使用指南

## 激活虚拟环境

在项目根目录下运行：

```bash
source .venv/bin/activate
```

或者使用 UV 内置命令：

```bash
uv run <command>
```

## 安装依赖

### 添加新依赖包

```bash
# 添加生产依赖
uv add <package-name>

# 添加开发依赖
uv add --dev <package-name>
```

### 安装所有依赖

```bash
uv sync
```

### 安装指定包（临时）

```bash
uv pip install <package-name>
```

## 常用命令

### 运行 Python 脚本

```bash
# 在虚拟环境中运行
uv run python script.py

# 或者先激活环境
source .venv/bin/activate
python script.py
```

### 更新依赖

```bash
uv lock --upgrade
uv sync
```

### 查看已安装的包

```bash
uv pip list
```

### 卸载包

```bash
uv remove <package-name>
```

## 项目信息

- **Python 版本**: 3.11.13
- **虚拟环境位置**: `.venv/`
- **配置文件**: `pyproject.toml`

## 注意事项

1. `.venv` 目录已被添加到 `.gitignore`，不会提交到版本控制
2. 依赖信息保存在 `pyproject.toml` 和 `uv.lock` 文件中
3. 推荐使用 `uv add` 而不是 `pip install` 来管理依赖
