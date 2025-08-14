#导入openai的聊天模型的方法
from langchain_openai import ChatOpenAI
#导入提示模版的方法
from langchain.prompts import ChatPromptTemplate
#导入输出解析器的方法
from langchain.output_parsers import  PydanticOutputParser
#导入提示模版包含的文本内容
from prompt_template_text import system_template_text,user_template_text
#导入输出解析器包含的格式要求
from output_parser_text import Xiaohongshu

#定义AI请求的函数
def generate_xiaohongshu(theme, api_key):
    # 创建聊天模型
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=api_key,
                       openai_api_base = "https://api.aigc369.com/v1")

    #创建提示模版
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", system_template_text),
            ("user", user_template_text)
        ]
    )

    #创建输出解析器
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)

    # 用链串起组件的输入输出,
    chain = prompt_template | model | output_parser

    #对提示模版填入对应的值,并获得解析后的模型回复
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })

    #返回函数的结果
    return result

#测试函数的输入输出是否正确
#print(generate_xiaohongshu("大模型","sk-0wtpjlf3lFomPHiHhZVTyXwa7DVBPW4EKsA3u2dBD1clxeqq"))