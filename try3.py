import os
from llama_index.llms.dashscope import DashScope, DashScopeGenerationModels
from llama_index.core.base.llms.types import MessageRole, ChatMessage

# 确保API密钥是一个有效字符串，直接传递API密钥
api_key = "sk-b94504df255e47d69196d08d2cd0e448"  

# 初始化 DashScope 对象，传入模型名称和API密钥
dashscope_llm = DashScope(
    model_name=DashScopeGenerationModels.QWEN_MAX, 
    api_key=api_key
)

# 初始化消息列表，包含系统消息
messages = [
    ChatMessage(role=MessageRole.SYSTEM, content="You are a helpful assistant."),
]

# 进行多轮对话，模拟用户与助手的连续问答
while True:
    # 等待用户输入新的问题
    user_input = input("\nUser: ")  # 用户输入新问题
    
    # 判断用户是否希望结束对话
    if user_input.lower() in ["再见", "结束", "停止"]:
        print("Assistant: 谢谢咨询，再见！")
        break  # 用户希望结束对话
    
    # 将用户的输入添加到消息列表中
    messages.append(ChatMessage(role=MessageRole.USER, content=user_input))

    # 处理流式输出（如果需要）
    # 流式多轮对话：使用 stream_chat 进行流式输出
    responses = dashscope_llm.stream_chat(messages)
    print("Streaming chat responses:")
    for response in responses:
        print(response.delta, end="")

    # 添加助手的回复到消息列表中，供下一轮对话使用
    messages.append(ChatMessage(role=MessageRole.ASSISTANT, content=response.delta))
