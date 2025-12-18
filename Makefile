.PHONY: help install sync update clean activate

help:
	@echo "可用命令:"
	@echo "  make install    - 安装所有依赖"
	@echo "  make sync       - 同步依赖（安装 pyproject.toml 中的所有依赖）"
	@echo "  make update     - 更新所有依赖到最新版本"
	@echo "  make clean      - 清理虚拟环境和缓存"
	@echo "  make activate   - 显示激活虚拟环境的命令"

install:
	uv sync

sync:
	uv sync

update:
	uv lock --upgrade
	uv sync

clean:
	rm -rf .venv
	rm -rf __pycache__
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

activate:
	@echo "运行以下命令激活虚拟环境:"
	@echo "source .venv/bin/activate"
