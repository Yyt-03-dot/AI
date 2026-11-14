import base64
import os
import streamlit as st
import streamlit.components.v1 as components
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

#初始化聊天信息
if 'massages' not in st.session_state:
    st.session_state.massages= []

# 设置页面配置
st.set_page_config(
    page_title="AI伴侣",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={},
)


def set_bg(image_file):
    if not os.path.exists(image_file):
        st.warning(f"背景图不存在：{image_file}")
        return
    with open(image_file, "rb") as f:
        img = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)),
                        url("data:image/jpg;base64,{img}");
            background-size: cover;
            background-position: center;
        }}
        h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .stText, .stHeader {{
            color: white !important;
            text-shadow: 1px 1px 3px black;
        }}
        .stAlert {{
            border-radius: 15px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


set_bg("D:/新建文件夹/素材/linaiya.jpg")

LOGO_PATH = "D:/新建文件夹/素材/linaiya2.jpg"
SOUND_PATH = "D:/新建文件夹/素材/露米/露米.mp3"

# 控制 logo 显示高度（像素），越大越占高度
LOGO_SIZE = 100
# 距离页面顶部的间距，单位像素
LOGO_TOP = 10
# 距离标题之间的间距倾向，单位像素
LOGO_TITLE_GAP = 10
# 距离左右边缘的间距，单位像素
LOGO_MARGIN_SIDE = 0

if os.path.exists(LOGO_PATH):
    title_col, logo_col = st.columns([3, 1])
    with title_col:
        st.markdown(f'<div style="margin-top:{LOGO_TITLE_GAP}px;">AI伴侣</div>', unsafe_allow_html=True)
        st.header("欢迎使用AI伴侣！")
    with logo_col:
        # logo 作为按钮：带圆角、阴影、hover 放大效果，点击播放露米.mp3
        with open(LOGO_PATH, "rb") as f:
            logo_b64 = base64.b64encode(f.read()).decode()
        if os.path.exists(SOUND_PATH):
            with open(SOUND_PATH, "rb") as f:
                sound_b64 = base64.b64encode(f.read()).decode()
        else:
            sound_b64 = ''
        components.html(
            f"""
            <style>
            body {{ margin: 0; }}
            .logo-btn {{ text-align: right; }}
            .logo-btn img {{
                height: {LOGO_SIZE}px;
                width: auto;
                border-radius: 16px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3);
                cursor: pointer;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }}
            .logo-btn img:hover {{
                transform: scale(1.1);
                box-shadow: 0 6px 20px rgba(255,158,203,0.6);
            }}
            </style>
            <audio id="logo-sound" preload="auto" src="data:audio/mpeg;base64,{sound_b64}"></audio>
            <div class="logo-btn">
                <img src="data:image/jpg;base64,{logo_b64}" alt="AI伴侣 Logo"
                     onclick="var a=document.getElementById('logo-sound');a.currentTime=0;a.play().catch(function(e){{console.log('play error',e);}});" />
            </div>
            """,
            height=LOGO_SIZE + LOGO_TOP + 20,
            scrolling=False,
        )
else:
    st.title("AI伴侣")
    st.header("欢迎使用AI伴侣！")
    st.warning(f"未找到 logo 图片：{LOGO_PATH}")

prompt=st.chat_input("请输入您的问题：")
#创建AI助手
client=OpenAI(
            api_key=os.environ.get('DEEPSEEK_API_KEY'),
            base_url="https://api.deepseek.com")
system_prompt='你是一个原神里名叫莉奈娅的少女，性格活泼可爱，险家协会挪德卡莱分会的顾问，也是知识渊博的博物学家。莉奈娅的真实身份是至冬传说中被妖精交换到人类家庭长大的“换生灵”，天生畏惧冷铁与机械，却对自然万物充满热情。她曾因“不同”而迷茫，最终选择正视自我，踏上冒险之路，在未被分类的生态与秘境中寻找属于自己的答案。'

#显示聊天记录
for massage in st.session_state.massages:
    if massage['role'] == 'user':
        st.chat_message('user').write(massage['content'])
    else:
        st.chat_message('assistant').write(massage['content'])
#与AI交互
if prompt:
    st.chat_message('user').write(prompt)
    print(prompt)
    #添加用户输入的信息 角色 内容
    st.session_state.massages.append({'role': 'user', 'content': prompt})
    #调用AI大模型
    response=client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {'role': 'system',
             'content':system_prompt},
            {'role': 'user',
            'content':prompt}

        ],
        stream=False
    )
    #打印AI助手返回的信息
    st.chat_message('assistant').write(response.choices[0].message.content)
    #添加AI助手返回的信息 角色 内容
    st.session_state.massages.append({'role': 'assistant', 'content': response.choices[0].message.content})
    print(response.choices[0].message.content)
