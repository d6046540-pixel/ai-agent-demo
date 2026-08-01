from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from config import SILICONFLOW_API_KEY, BASE_URL


class Person(BaseModel):
    name: str
    age: int
    skills: list[str]

from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """计算数学表达式，例如：25*8"""
    return str(eval(expression))


llm = ChatOpenAI(
    api_key=SILICONFLOW_API_KEY,
    base_url=BASE_URL,
    model="Qwen/Qwen3-8B",
    temperature=0,
    timeout=15
)
llm_with_tools = llm.bind_tools([calculator])

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
# 第一次调用模型
response = llm_with_tools.invoke(
    "请帮我计算25*8"
)


# 查看模型有没有调用工具
print(response.tool_calls)


# 获取模型请求调用的工具
tool_call = response.tool_calls[0]

# 获取参数
args = tool_call["args"]

# 执行工具
tool_result = calculator.invoke(args)

print("工具执行结果：")
print(tool_result)


from langchain_core.messages import ToolMessage


tool_message = ToolMessage(
    content=tool_result,
    tool_call_id=tool_call["id"]
)


final_response = llm_with_tools.invoke(
    [
        "请帮我计算25*8",
        response,
        tool_message
    ]
)


print(final_response.content)