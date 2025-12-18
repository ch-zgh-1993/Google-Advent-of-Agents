# 使用 YAML 构建 HelloWord

```cmd
<!-- 下载 adk， 并创建 agent -->
uvx --from google-adk adk create --type=config my_agent

<!-- 检查版本 -->
adk --version

<!-- 运行 agent -->
uvx --from google-adk adk web my_agent/
```

```yaml

```

## Agent Devlopment Kit

1. Agent Config 通过 Yaml 创建 ADK 工作流。代理可以包含函数、您可以使用 Agent Config 文件构建更复杂的代理， 工具、子代理等。
