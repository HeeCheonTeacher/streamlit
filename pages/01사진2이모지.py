import streamlit as st
from PIL import Image
import numpy as np
import emoji

# 이모지 변환 함수
def image_to_emoji(img, emoji_char='😀', scale=10):
    img = img.convert('L')  # 이미지를 흑백으로 변환
    img = img.resize((img.width // scale, img.height // scale))
    img_array = np.array(img)
    
    # 픽셀 값을 기반으로 이모지 문자열 생성
    emoji_str = ""
    for row in img_array:
        for pixel in row:
            if pixel > 128:  # 밝기에 따라 이모지 결정
                emoji_str += emoji_char
            else:
                emoji_str += ' '
        emoji_str += '\n'
    return emoji_str

# Streamlit 앱 설정
st.title("사진을 이모지로 변환하기")

# 이모지 선택
emoji_char = st.text_input("사용할 이모지를 입력하세요:", value='😀')

# 이미지 업로드
uploaded_file = st.file_uploader("이미지를 업로드하세요:", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="업로드된 이미지", use_column_width=True)
    
    # 이모지 변환 및 출력
    st.subheader("이모지 변환 결과")
    emoji_art = image_to_emoji(img, emoji_char)
    st.text(emoji_art)
