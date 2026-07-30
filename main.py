from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from config import SILICONFLOW_API_KEY, BASE_URL

llm = ChatOpenAI(
    api_key=SILICONFLOW_API_KEY,
    base_url=BASE_URL,
    model="Qwen/Qwen3-8B",
    temperature=0
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一位专业的Python导师，请用简洁、易懂的方式回答问题。"),
        ("human", "{question}")
    ]
)

chain = prompt | llm

response = chain.invoke(
    {
        "question": "什么是LangChain？"
    }
)

print(response.content)