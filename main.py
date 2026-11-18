from dotenv import  load_dotenv
import os

from langchain_openai import ChatOpenAI

load_dotenv()

ZHIPUAI_API_KEY = os.getenv("ZHIPUAI_API_KEY")

llm = ChatOpenAI(
    model="glm-4.5-air",
    api_key=ZHIPUAI_API_KEY,
    temperature=0.7,
    base_url="https://open.bigmodel.cn/api/paas/v4"
)


print(llm.invoke("你好,自我介绍一下你自己").content)