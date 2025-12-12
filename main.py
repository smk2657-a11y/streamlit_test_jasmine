def main():
    print("Hello from streamlit-test-jasmine!")


if __name__ == "__main__":
    main()


import streamlit as st
import numpy as np
import random
import pandas as pd
import seaborn as sns
import matplotlib .pyplot as plt
import plotly.express as px

# 기본 텍스트 출력
st.title("Hello Streamlit!!")
st.header("헤더")
st.write("st.write() 기본 텍스트 출력")

# 사용자 입력 받기
name = st.text_input("이름을 입력하세요:")
print(f"안녕하세요, {name}님")
st.write(f"안녕하세요, {name}님")

# 숫자 입력 받기
age = st.number_input("나이를 입력하세요", 
min_value=0, max_value=120)
print(f"나이: {age}")
st.write(f"나이: {age}")

# 사이드바 메뉴
menus = ["A", "B", "C"]
options = st.sidebar.selectbox("메뉴 선택", menus)
print("선택한 메뉴:", options)
st.write("선택한 메뉴:", options)
         
# 버튼 클릭 이벤트
if st. button("버튼 클릭"):
st.sucess("버튼이 눌렸습니다")

# 데이터 프레임 표시
tips = sns.load_dataset("tips")
print(tips)
st.dataframe(tips)
st.write(tips) # 비추천

# matplotlib 그래프 출력
# 객체 지향으로 출력
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [10, 20, 30])
# fig.show()
st.pyplot(fig)

# 이미지 출력
img url = https://ichef.bbci.co.uk/ace/ws/800/cpsprodpb/c82c/live/d2c695c0-8408-11f0-84c8-99de564f0440.jpg
st.image(imgurl)

# Progress Bar
import time
progress = st.progress(0)
for i in range(100):
    progress.progress(i+1)
    time.sleep(0.01)

# with st.spinner("처리 중..."):
#   time.sleep(3)
#st.sucess("완료!")

#Layout
col1, col2 = st.columns(2)
#col1.write("완쪽 컬럼")
#col2.write("오른쪽 컬럼")

# 사용자 입력 영역
with col1:
    st.subheader("설정 메뉴")
    min_val = st.number_input("최솟값", value=1)
    max_val = st.number_input("최댓값", value=100)

    count = st.slider("생성할 난수 개수", 1, 10, 50)
    st.write(count)

    run_btn = st.button("난수 생성 및 시각화")
    st.write(min_val, max_val, count, run_btn)

# 결과 출력 영역
with col2:
    if run_btn:
        st.subheader("결과 시각화")

        # 난수 생성
        numbers = [random.randint(min_val, max_val) for _ in range(count)]
        df = pd.DataFrame({"index": list(range(1, count+1)), "value": numbers})
        st.dataframe(random_df)
        st.write("생성된 난수:", numbers)
        #시각화 코드
        fig = px.bar(df, x="index", y="value",
                     title="난수 Bar Chart",
                     text="value")

        fig.update_traces(textposition="outside")
        fig.update_layout(yaxis_range=[0, max(numbers) + 5])

        st.plotly_chart(fig, use_container_width=True)

# Tabs 구성
tab1, tab2 = st.tabs(["탭1", "탭2"])
with tab1:
    st.write("탭 1 코드실행")

with tab2:
    st.write("탭ㅈ 코드 실행")
