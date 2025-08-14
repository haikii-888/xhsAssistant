#导入basemodel类(创建数据模型，自动验证输入类型和约束),Field类(为模型字段添加额外约束[如范围、描述]和元数据)
#涉及版本兼容问题，这里导入不按照课程给的导入，改为以下方式导入
#from langchain_core.pydantic_v1 import BaseModel, Field
from pydantic import BaseModel, Field
#导入List类型,用于声明列表元素的具体类型
from typing import List

class Xiaohongshu(BaseModel):
    titles: List[str] = Field(description="小红书的5个标题", min_length=5, max_length=5)
    content: str = Field(description="小红书的正文内容")

# Pydantic v2配置示例
# model_config = {
#     "json_schema_extra": {
#         "example": {
#             "titles": [
#                 "惊艳！大模型的5个神奇应用",
#                 "大模型改变生活的5种方式",
#                 "不可不知的大模型实用技巧",
#                 "大模型入门指南：5个标题带你飞",
#                 "探索大模型：5个必看标题"
#             ],
#             "content": (
#                 "🔥最近大模型真的太火了！作为一个科技爱好者，我整理了5个超实用的大模型应用场景：\n\n"
#                 "1️⃣ 智能写作助手：自动生成高质量文案，解放双手\n"
#                 "2️⃣ 代码生成：描述需求即可生成可用代码\n"
#                 "3️⃣ 知识问答：复杂问题秒级解答\n"
#                 "4️⃣ 内容摘要：长文变精炼要点\n"
#                 "5️⃣ 语言翻译：多语种无缝切换\n\n"
#                 "💡使用技巧：\n"
#                 "- 尝试不同提示词会有意外惊喜\n"
#                 "- 结合具体场景使用效果更佳\n\n"
#                 "👇评论区分享你的大模型使用体验吧！"
#             )
#         }
#     }
# }