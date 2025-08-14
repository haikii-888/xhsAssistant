# 导入前端框架streamlit
import streamlit as st

# 导入AI请求函数
from airequest import generate_xiaohongshu

# 网页标题
st.title("爆款小红书AI写作助手")

# 插入侧边栏
with st.sidebar:
    openai_api_key = st.text_input('请输入OpenAI API密钥：', type='password')
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")

# 编写正文
theme = st.text_input("💡 请输入主题")
submit = st.button("开始写作")

#插入分隔符
st.divider()

# 判断输入是否完整
if submit and not openai_api_key:
    st.info("请输入你的OpenAI API密钥")
    st.stop()
if submit and not theme:
    st.info("请输入主题")
    st.stop()

# 获取api回复并展示在页面
if submit:
    # 插入加载中的提示
    with st.spinner("AI正在思考中，请稍等..."):
        result = generate_xiaohongshu(theme, openai_api_key)
        # 插入布局并分成2列,参数值代表列宽
        column1, column2 = st.columns([1,1])
        with column1:
            st.markdown("##### 小红书标题1")
            st.write(result.titles[0])
            st.markdown("##### 小红书标题2")
            st.write(result.titles[1])
            st.markdown("##### 小红书标题3")
            st.write(result.titles[2])
            st.markdown("##### 小红书标题4")
            st.write(result.titles[3])
            st.markdown("##### 小红书标题5")
            st.write(result.titles[4])
        with column2:
            st.markdown("##### 小红书正文")
            st.write(result.content)