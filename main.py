from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from config import SILICONFLOW_API_KEY, BASE_URL


class Person(BaseModel):
    name: str
    age: int
    skills: list[str]
llm = ChatOpenAI(
    api_key=SILICONFLOW_API_KEY,
    base_url=BASE_URL,
    model="Qwen/Qwen3-8B",
    temperature=0,
    timeout=15
)

parser = PydanticOutputParser(
    pydantic_object=Person
)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            你是一位信息提取助手。

            请根据用户信息提取人物资料。

            {format_instructions}
            """
        ),
        ("human", "{question}")
    ]
)



chain = prompt | llm | parser


print("开始调用模型")

response = chain.invoke(
    {
        "question": "张三，21岁，会Python、SQL和LangChain。",
        "format_instructions": parser.get_format_instructions()
    }
)

print("模型调用完成")
print(response)
print(type(response))