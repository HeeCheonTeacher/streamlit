import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# 데이터 불러오기 및 전처리 함수
def load_data():
    file_path = 'age2411.csv'
    df = pd.read_csv(file_path)
    df = df[['행정구역'] + [col for col in df.columns if '계_' in col and '총인구수' not in col]]
    return df

def plot_population(data, region):
    filtered_data = data[data['행정구역'].str.contains(region)]
    if filtered_data.empty:
        st.error("입력한 지역을 찾을 수 없습니다. 다시 확인해주세요.")
        return

    # 연령대별 인구 데이터 추출
    population = filtered_data.iloc[0, 1:].values
    ages = [i for i in range(len(population))]

    # 그래프 그리기
    plt.figure(figsize=(10, 6))
    plt.bar(ages, population)
    plt.title(f'{region} 지역의 인구 구조')
    plt.xlabel('연령대 (0세 ~ 100세 이상)')
    plt.ylabel('인구수')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)

# Streamlit UI 설정
st.title('우리 지역 인구 구조 알아보기')

# 데이터 불러오기
data = load_data()

# 사용자 입력: 지역 이름 입력
region_input = st.text_input("원하는 지역을 입력하세요 (예: 서울특별시, 종로구)")

if region_input:
    plot_population(data, region_input)

st.write("**데이터 출처**: 제공된 CSV 파일 기반")
