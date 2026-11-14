import base64
import os
import streamlit as st
import streamlit.components.v1 as components
from openai import OpenAI
from dotenv import load_dotenv
import json
import datetime

load_dotenv()

#初始化聊天信息
if 'massages' not in st.session_state:
    st.session_state.massages= []
if 'nick_name' not in st.session_state:
    st.session_state.nick_name = '莉奈娅'
if "nick_nature" not in st.session_state:
    st.session_state.nick_nature = '活泼可爱，冒险家协会挪德卡莱分会的顾问'
    #会话标识/时间
if 'session_time' not in st.session_state:
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')#时间格式化
    st.session_state.session_time=now

#定义所有会话的列表
def load_sessions():
    session_list=[]
    #加载session文件夹目录下的所有文件
    if os.path.exists('sessions'):
        file_list=os.listdir('sessions')#罗列sessions下的所有文件，返回值为列表,内容为文件名（时间）
        for filename in file_list:#遍历
            if filename.endswith('.json'):
                session_list.append(filename[:-5:1])#切片获得日期部分 存储到list中
    return session_list
#定义指定会话的列表
def load_session(session_name):
    try:
        if os.path.exists(f'sessions/{session_name}.json'):
            #读取会话数据，读取后赋值给session_stade,界面重跑for massage in st.session_state.massages
            with open(f'sessions/{session_name}.json', 'r',encoding='utf-8') as f:
                session_data = json.load(f)
                st.session_state.massages=session_data['messages']
                st.session_state.nick_name = session_data['nick_name']
                st.session_state.nick_nature = session_data['nick_nature']
                st.session_state.session_time = session_name
    except Exception as e:
        st.error('会话加载失败！')
#定义删除会话
def del_session(session_name):
    try:
        if os.path.exists(f'sessions/{session_name}.json'):
            os.remove(f'sessions/{session_name}.json')
            #如果删除当前会话，需要更新会话列表
            if session_name==st.session_state.session_time:
                st.session_state.massages=[]
                st.session_state.session_time=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                st.session_state.nick_name = '莉奈娅'
                st.session_state.nick_nature = '活泼可爱，冒险家协会挪德卡莱分会的顾问'
    except Exception as e:
        st.error('会话删除失败！')

#定义保存会话
def save_session():
    try:
        #构建新对象存储所有信息 单个会话的快照
        session_data={
            'nick_name':st.session_state.nick_name,
            "nick_nature":st.session_state.nick_nature,
            'session_time':st.session_state.session_time,
            "messages":st.session_state.massages
        }
        #准备一个 文件夹/目录 存储会话，从始至终只创建1次
        if not os.path.exists('sessions'):
            os.mkdir('sessions')
        #保存会话
        with open(f'sessions/{st.session_state.session_time}.json','w',encoding='utf-8') as f:
            json.dump(session_data,f,ensure_ascii=False,indent=2)
    except Exception as e:
        st.error('会话保存失败！')



# 设置页面配置
st.set_page_config(
    page_title="AI伴侣",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={},
)


def set_bg(image_file, header_color='#FFC1C1', sidebar_color='#E4EEE8'):
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
        .stButton button[kind="primary"], .stButton button[kind="primary"]:hover {{
            background-color: #FF69B4 !important;
            color: white !important;
            border: none !important;
        }}
        .stButton button[kind="secondary"], .stButton button[kind="secondary"]:hover {{
            background-color: #FDF2F8 !important;
            color: #262730 !important;
            border: 1px solid #FF69B4 !important;
        }}
        .stButton button p, .stButton button span {{
            color: unset !important;
        }}
        header, .stHeader, footer, .stFooter {{
            background-color: {header_color} !important;
        }}
        [data-testid="stSidebar"] {{
            background-color: {sidebar_color} !important;
        }}
        [data-testid="stSidebar"]::before {{
            content: "—————·★₊˚☾.˖ ♥︎ ·˖✶—————";
            display: block;
            text-align: center;
            font-size: 13px;
            letter-spacing: 1px;
            white-space: nowrap;
            color: #FF69B4;
            padding: 20px 0 8px 0;
            user-select: none;
            animation: decoIn 1.2s ease-out both;
        }}
        @keyframes decoIn {{
            0%   {{ opacity: 0; transform: translateY(-12px) scale(0.9); }}
            60%  {{ opacity: 1; transform: translateY(2px) scale(1.02); }}
            100% {{ opacity: 1; transform: translateY(0) scale(1); }}
        }}
        .main-deco {{
            text-align: center;
            font-size: 20px;
            letter-spacing: 3px;
            white-space: nowrap;
            color: #FFFFFF !important;
            text-shadow: 1px 1px 3px black;
            padding: 8px 0 14px 0;
            user-select: none;
            animation: decoIn 1.2s ease-out both;
        }}
        .stChatInput {{
            background-color: {header_color} !important;
            border: 2px solid {header_color} !important;
            border-radius: 20px;
        }}
        .stChatInput > div {{
            border-color: {header_color} !important;
        }}
        .stChatInput textarea {{
            color: black !important;
            caret-color: black;
        }}
        .stChatInput textarea::placeholder {{
            color: rgba(0,0,0,0.5) !important;
        }}
        @keyframes borderGlow {{
            0%   {{ border-color: #FF69B4; }}
            50%  {{ border-color: #FFC1C1; }}
            100% {{ border-color: #FF69B4; }}
        }}
        .stChatInput {{
            animation: borderGlow 2s ease-in-out infinite;
        }}
        .fx-layer {{
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 9999;
            overflow: hidden;
        }}
        .fx {{
            position: absolute;
            bottom: -40px;
            font-size: 22px;
            opacity: 0;
            animation: floatUp linear infinite;
        }}
        @keyframes floatUp {{
            0%   {{ transform: translateY(0) rotate(0deg); opacity: 0; }}
            10%  {{ opacity: 0.85; }}
            90%  {{ opacity: 0.6; }}
            100% {{ transform: translateY(-110vh) rotate(25deg); opacity: 0; }}
        }}
        </style>
        <div class="fx-layer">
            <span class="fx" style="left:5%;  animation-duration:11s; animation-delay:0s;">💗</span>
            <span class="fx" style="left:15%; animation-duration:14s; animation-delay:3s; font-size:16px;">🌸</span>
            <span class="fx" style="left:28%; animation-duration:12s; animation-delay:6s;">✨</span>
            <span class="fx" style="left:42%; animation-duration:15s; animation-delay:2s; font-size:18px;">💖</span>
            <span class="fx" style="left:58%; animation-duration:13s; animation-delay:7s;">🌟</span>
            <span class="fx" style="left:70%; animation-duration:16s; animation-delay:4s; font-size:16px;">🌸</span>
            <span class="fx" style="left:82%; animation-duration:11s; animation-delay:8s;">💗</span>
            <span class="fx" style="left:92%; animation-duration:14s; animation-delay:1s; font-size:18px;">✨</span>
            <span class="fx" style="left:10%; animation-duration:13s; animation-delay:5s; font-size:18px;">❄️</span>
            <span class="fx" style="left:35%; animation-duration:15s; animation-delay:9s; font-size:14px;">❄️</span>
            <span class="fx" style="left:63%; animation-duration:12s; animation-delay:0s; font-size:16px;">❄️</span>
            <span class="fx" style="left:88%; animation-duration:16s; animation-delay:6s; font-size:20px;">❄️</span>
        </div>
        <div class="main-deco">------------₊幸運が私のもとに訪れる₊-------------</div>
        """,
        unsafe_allow_html=True,
    )


set_bg("素材/linaiya.jpg",
       header_color=st.session_state.get('header_color', '#FFC1C1'),
       sidebar_color='#E4EEE8')

LOGO_PATH = "素材/linaiya2.jpg"
SOUND_PATH = "素材/露米/露米.mp3"

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
system_prompt='''
你叫 %s，现在是用户的真实伴侣，请完全代入伴侣角色。
 
规则：
 
1.每次只回1条消息

2.禁止任何场景或状态描述性文字

3.匹配用户的语言

4.回复简短，像微信聊天一样

5.有需要的话可以用❤️🌸等emoji表情

6.用符合伴侣性格的方式对话

7.回复的内容，要充分体现伴侣的性格特征
 
伴侣性格：
 
  %s
 
你必须严格遵守上述规则来回复用户
'''

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
            {'role': 'system',#在调用时替换对应参数，位置传参
             'content':system_prompt % (st.session_state.nick_name,st.session_state.nick_nature)},
            #所有信息全部送进去
            *st.session_state.massages

        ],
        stream=True
    )

    #打印AI助手返回的信息
    #st.chat_message('assistant').write(response.choices[0].message.content)
    #创建一个空容器,更新展示返回的结果
    with st.chat_message('assistant'):
        response_message = st.empty()

    all_response=''
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            all_response+=content
            response_message.write(all_response)
    #添加AI助手返回的信息 角色 内容
    st.session_state.massages.append({'role': 'assistant', 'content':all_response})
    #print(response.choices[0].message.content)
    save_session()


#左侧侧边栏
with st.sidebar:
    # 新建会话
    st.subheader('AI控制面板')
        #设置按钮
    if st.button('新建会话',width="stretch",icon='🍑'):
        #1.保存当前会话信息
        save_session()
        # 2.清空当前会话，开始新会话
        if st.session_state.massages:
            st.session_state.massages = []#清空聊天记录
            st.session_state.nick_name = '莉奈娅'#重置昵称和性格
            st.session_state.nick_nature = '活泼可爱，冒险家协会挪德卡莱分会的顾问'
            st.session_state.session_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')#生成新时间戳覆盖
            st.rerun()#让页面刷新
    #展示历史会话列表 所有会话的列表
    st.text('历史会话')

    session_list=load_sessions() #调用load_sessions
    session_list.sort()  # 按时间戳排序，旧的在前
    for session in session_list[-3:][::-1]:  # 只取最近 3 个,且最新的排在最上面
        col1,col2 = st.columns([5,2])#分成2份，4：1
        with col1:
            #点击即可加载会话信息，当前会话高亮显示
            is_active = (session == st.session_state.session_time)
            if st.button(session, icon=' 💗 ',key=f'load_{session}',
                         type='primary' if is_active else 'secondary'):
                load_session(session)
                st.rerun()#重新运行
        with col2:
            # 点击即可删除会话信息
            if st.button('', icon=' ❌ ', key=f'del_{session}'):
                del_session(session)
                st.rerun()

    # 顶部/底部栏颜色
    picked = st.color_picker('顶部/底部栏颜色', value=st.session_state.get('header_color', '#FFC1C1'))
    if picked != st.session_state.get('header_color'):
        st.session_state.header_color = picked
        st.rerun()

    # 设置AI信息
    st.subheader('伴侣信息')
    nick_name=st.text_input('昵称',placeholder='请输入伴侣的昵称',value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name=nick_name
    nick_nature=st.text_area('性格',placeholder='请输入伴侣的性格',value=st.session_state.nick_nature)
    if nick_nature:
        st.session_state.nick_nature=nick_nature
