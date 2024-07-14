import requests
import json
import streamlit as st
st.set_page_config(layout="wide")  # 와이드 화면 설정

st.title("웰빙 매니저")

def get_health_info(glucose, cholesterol, ldl, height, weight, sex, systolic_bp, diastolic_bp, heart_rate, hdl, bmi, alt, ast, uric_acid):
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'apiKey': '0cbef3b9254613826829f67cd3c171c296d08b4ef69ec27e089ba3a1925fca89',
        'project': 'PROMPTHON_PRJ_446'
    }
    
    body = {
        "hash": "2892794f90bfa27323e2c928b093c92f3469120cde02c41a98fbdcf3588e7929",
        "glucose": glucose,
        "cholesterol": cholesterol,
        "ldl": ldl,
        "height": height,
        "weight": weight,
        "sex": sex,
        "systolic_bp": systolic_bp,
        "diastolic_bp": diastolic_bp,
        "heart_rate": heart_rate,
        "hdl": hdl,
        "bmi": bmi,
        "alt": alt,
        "ast": ast,
        "uric_acid": uric_acid
    }
    
    response = requests.post(
        url="https://api-laas.wanted.co.kr/api/preset/chat/completions",
        headers=headers,
        data=json.dumps(body)
    )
    
    return response.json()

col1, col2, col3, col4 = st.columns(4)

with col1:
    glucose = st.number_input("혈당 수치", min_value=0, max_value=500, value=150, help="혈당 수치는 혈액 내 포도당의 농도를 나타냅니다.")
    ldl = st.number_input("LDL 수치", min_value=0, max_value=500, value=100, help="LDL 수치는 저밀도 지단백 콜레스테롤의 양을 나타냅니다.")
    height = st.number_input("키 (cm)", min_value=0, max_value=300, value=170, help="키를 입력하세요.")
    sex = st.selectbox("성별", ["남성", "여성"], help="성별을 선택하세요.")

with col2:
    systolic_bp = st.number_input("수축기 혈압 (mmHg)", min_value=0, max_value=300, value=120, help="수축기 혈압을 입력하세요.")
    heart_rate = st.number_input("심박수 (bpm)", min_value=0, max_value=200, value=70, help="심박수를 입력하세요.")
    bmi = st.number_input("체질량지수 (BMI)", min_value=0, max_value=100, value=22, help="체질량지수를 입력하세요.")
    ast = st.number_input("AST 수치", min_value=0, max_value=100, value=30, help="AST 수치를 입력하세요.")

with col3:
    cholesterol = st.number_input("콜레스테롤 수치", min_value=0, max_value=500, value=200, help="콜레스테롤 수치는 혈액 내 콜레스테롤의 양을 나타냅니다.")
    weight = st.number_input("몸무게 (kg)", min_value=0, max_value=300, value=70, help="몸무게를 입력하세요.")
    diastolic_bp = st.number_input("이완기 혈압 (mmHg)", min_value=0, max_value=200, value=80, help="이완기 혈압을 입력하세요.")
    hdl = st.number_input("HDL 수치", min_value=0, max_value=100, value=60, help="HDL 수치를 입력하세요.")

with col4:
    alt = st.number_input("ALT 수치", min_value=0, max_value=100, value=30, help="ALT 수치를 입력하세요.")
    uric_acid = st.number_input("요산 수치", min_value=0, max_value=10, value=5, help="요산 수치를 입력하세요.")

# 대화 기록을 화면에 표시
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "user",
        "content": f"내 건강검진 수치 : 키: {height} cm, 몸무게: {weight} kg, 성별: {sex}, 수축기 혈압: {systolic_bp} mmHg, 이완기 혈압: {diastolic_bp} mmHg, 심박수: {heart_rate} bpm, 혈당: {glucose} mg/dL, 콜레스테롤: {cholesterol} mg/dL, LDL: {ldl} mg/dL, HDL: {hdl} mg/dL, BMI: {bmi}, ALT: {alt} U/L, AST: {ast} U/L, 요산: {uric_acid} mg/dL"
    }
    )

# 사용자 입력 받기
with st.expander("건강 평가", expanded=True):
    if st.button("내 건강수치를 기반으로 내 건강을 평가해줘"):
        # 사용자 메시지 추가
        st.session_state.messages.append({"role": "user", "content": "내 건강수치를 기반으로 내 건강을 평가해줘"})
        with st.chat_message("user"):
            st.markdown("위에 내 건강수치를 기반으로 내 건강을 평가해줘")
        
        # 챗봇 응답 받기
        result = get_health_info(glucose, cholesterol, ldl, height, weight, sex, systolic_bp, diastolic_bp, heart_rate, hdl, bmi, alt, ast, uric_acid)
        response = result.get("choices", [{"message": {"content": "응답을 받을 수 없습니다."}}])[0]["message"]["content"]
        
        # 챗봇 메시지 추가
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

# # st.write(response)
st.write(st.session_state)