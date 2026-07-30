from langchain_openai import ChatOpenAI
from config import SILICONFLOW_API_KEY, BASE_URL


llm = ChatOpenAI(
    api_key=SILICONFLOW_API_KEY,
    base_url=BASE_URL,
    model="Qwen/Qwen3-8B",
    temperature=0
)


response = llm.invoke("你好，请简单介绍一下你自己。")


print(response.content)
