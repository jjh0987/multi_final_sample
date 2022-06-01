# Streamlit으로 웹서비스 구현하기
import streamlit as st
from PIL import Image
import execute
import time
from datetime import datetime

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

st.sidebar.subheader(':sparkles: Team Another Sense :sunglasses:')
# 사이드바1 - 회사 선택 (최상위 선택지)
comp = st.sidebar.selectbox('🏢 회사를 선택해주세요. ',
                 ('NAVER', '카카오')) # comp = 기업이름

if comp == '카카오':
    codenum = '035720'
else:
    codenum = '035420'

# codenum = execute.get_company_code(comp) # codenum = 기업코드


# 사이드바2 - 카테고리 선택
option = st.sidebar.selectbox(
    '열람할 페이지를 선택해주세요.',
    ('메인 홈 Main Home', '기업정보 Company Information', '개미 동향 Ants MIND','기사 News','예측 Prediction')
)