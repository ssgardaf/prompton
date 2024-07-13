import streamlit as st
import requests

st.set_page_config(layout="wide")  # 페이지 레이아웃을 wide로 설정

# 네이버 클라우드 플랫폼 API 키 설정
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

def analyze_text(text):
    url = "https://naveropenapi.apigw.ntruss.com/nlp/v1/analyze"
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret,
        "Content-Type": "application/json"
    }
    data = {
        "content": text,
        "analysisCode": "morp"
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def main():
    st.title("건강 라이프스타일 추천")
    st.write("건강검진 데이터를 입력하고, 건강한 라이프스타일을 추천받으세요.")

    # 건강검진 데이터 입력
    age = st.number_input("나이", min_value=0, max_value=120, step=1)
    weight = st.number_input("체중 (kg)", min_value=0.0, max_value=200.0, step=0.1)
    height = st.number_input("키 (cm)", min_value=0.0, max_value=250.0, step=0.1)
    blood_pressure = st.number_input("혈압 (mmHg)", min_value=0, max_value=300, step=1)
    cholesterol = st.number_input("콜레스테롤 (mg/dL)", min_value=0, max_value=500, step=1)
    blood_sugar = st.number_input("혈당 (mg/dL)", min_value=0, max_value=500, step=1)

    if st.button("추천 받기"):
        # 간단한 추천 로직 (예시)
        recommendations = []
        if weight / ((height / 100) ** 2) > 25:
            recommendations.append("체중을 줄이기 위해 규칙적인 운동을 하세요.")
        if blood_pressure > 120:
            recommendations.append("혈압을 낮추기 위해 저염식을 하세요.")
        if cholesterol > 200:
            recommendations.append("콜레스테롤을 낮추기 위해 건강한 식단을 유지하세요.")
        if blood_sugar > 100:
            recommendations.append("혈당을 관리하기 위해 당 섭취를 줄이세요.")

        if recommendations:
            st.write("추천 라이프스타일:")
            for rec in recommendations:
                st.write(f"- {rec}")
        else:
            st.write("현재 건강 상태가 양호합니다. 계속해서 건강한 생활을 유지하세요!")

        # 텍스트 분석 예제
        text = " ".join(recommendations)
        analysis_result = analyze_text(text)
        st.write("텍스트 분석 결과:")
        st.json(analysis_result)

if __name__ == "__main__":
    main()