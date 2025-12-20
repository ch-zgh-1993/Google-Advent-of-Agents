from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
import os
import asyncio
from google.genai import types
from dotenv import load_dotenv
from pathlib import Path

# 加载根目录的 .env 文件
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# 获取 env 文件中的 token   
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
APP_NAME="github_agent"
USER_ID="user1234"
SESSION_ID="12345"

root_agent = Agent(
    model="gemini-2.5-flash",
    name="test_github",
    instruction="你是一个 GitHub 助手。请使用提供的工具来查询仓库、Issue 或项目信息。- When using Firecrawl tools, check the tool schemas carefully for required parameters.",
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params={
                    "command": "npx",
                    "args": ["-y", "github-mcp"],
                    "env": {"GITHUB_TOKEN": GITHUB_TOKEN, "X-MCP-Toolsets": "all", "X-MCP-Readonly": "true"}
                }
            )
        )
    ]
)

# Session and Runner
async def setup_session_and_runner (): 
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
    runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)
    return session, runner


# Agent interaction

async def call_agent_async(query): 
    content = types.Content(role="user", parts=[types.Part(text=query)])
    session, runner = await setup_session_and_runner()
    events = runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

    async for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
            print("Agent Response: ", final_response)

if __name__ == "__main__":
    asyncio.run(call_agent_async("我有哪些项目可以访问"))