```python
import os
import asyncio
import sys
from gpt_researcher import GPTResearcher

# ==========================================
#  Deep Research Commander - Execution Script
# ==========================================

def setup_environment():
    """
    配置环境变量，强制使用 OpenAI 协议连接目标模型
    """
    # 建议从系统环境变量读取，或者在此处填入默认值用于测试
    os.environ["LLM_PROVIDER"] = "openai"
    os.environ["RETRIEVER"] = "duckduckgo"
    
    # 默认超时设置 (国产模型通常较慢)
    if "OPENAI_TIMEOUT" not in os.environ:
        os.environ["OPENAI_TIMEOUT"] = "120"

    # 检查必要配置
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY is missing.")
        sys.exit(1)
        
    print(f"🔧 Configured to connect to: {os.getenv('OPENAI_BASE_URL', 'Default OpenAI')}")

async def run_task(query):
    setup_environment()
    
    print(f"🐢 Starting Low-Concurrency Research: {query}")
    
    researcher = GPTResearcher(
        query=query, 
        report_type="research_report",
        verbose=True
    )
    
    # --- 强制参数修正 ---
    # 这些设置是为了在不稳定网络下获得最大成功率
    researcher.cfg.max_iterations = 2           # 迭代轮数
    researcher.cfg.max_subtopics = 3            # 子话题广度
    researcher.cfg.max_search_results_per_query = 3 # 减少单次请求量
    
    await researcher.conduct_research()
    report = await researcher.write_report()
    return report

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python robust_researcher.py 'Your research question'")
        sys.exit(1)
        
    user_query = sys.argv[1]
    
    try:
        report = asyncio.run(run_task(user_query))
        print("\n=== REPORT OUTPUT ===\n")
        print(report)
        # 可选：保存到文件
        with open("report.md", "w", encoding="utf-8") as f:
            f.write(report)
        print("\n✅ Report saved to report.md")
    except Exception as e:
        print(f"\n❌ Execution Failed: {e}")
