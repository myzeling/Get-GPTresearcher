# Deep Research Commander (Direct-Connect Ver.)

这是一个专为 OpenClaw 等 AI Agent 平台设计的 Skill 方案，用于稳定运行 `gpt-researcher`。

## 核心痛点解决
1.  **去 LiteLLM 化**：不再依赖不稳定的本地代理，直接通过 OpenAI 兼容接口连接 Kimi/DeepSeek。
2.  **防 Token 爆炸**：强制限制递归次数和并发数，防止 Deep Research 陷入死循环。
3.  **模型兼容性修复**：通过环境变量伪装，解决 gpt-researcher 对国产模型名不支持的问题。

## 快速开始
1.  安装依赖：`pip install -r requirements.txt`
2.  配置 `.env` (参考 example)
3.  运行：`python robust_researcher.py`

## 针对 Bot 的集成
请将 `system_skill.md` 中的内容添加到你的 Bot System Prompt 中。
