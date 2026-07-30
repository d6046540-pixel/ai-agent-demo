import os
from dotenv import load_dotenv

# 读取 .env 文件
load_dotenv()

# 获取 API Key
SILICONFLOW_API_KEY = os.getenv("SILICONFLOW_API_KEY")

# SiliconFlow 的 API 地址
BASE_URL = "https://api.siliconflow.cn/v1"