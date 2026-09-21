import pandas as pd
import streamlit as st

# ตั้งค่าหน้าเพจทำให้อยู่ตรงกลางและเปลี่ยนชื่อแท็บ
st.set_page_config(page_title="Student Scores", layout="centered") #ทดลองเปลี่ยนเป็น centered - > wide

st.header(":green[Input Student Score]")
st.divider() # เส้นกั้นตกแต่ง

# -----------------------------
# Create DataFrame in Session State
# -----------------------------
if "std_df" not in st.session_state:
    st.session_state.std_df = pd.DataFrame({
        "Name": [],
        "M_Score": [],
        "F_Score": [],
        "Total_Score": []
    })

# -----------------------------
# Input (ใช้ st.form เพื่อให้เคลียร์ค่าอัตโนมัติ)
# -----------------------------
with st.form("score_form", clear_on_submit=True):
    st.subheader(" Student Details")
    
    # เพิ่ม Placeholder ให้ดูสวยงาม
    name = st.text_input("Enter Your Name", placeholder="e.g., Wanthanee Prachuabsupakij")
    
    # ใช้ st.columns แบ่งช่องกรอกคะแนนซ้าย-ขวา ให้อยู่บรรทัดเดียวกัน
    col1, col2 = st.columns(2)
    with col1:
        m_score = st.number_input(
            "Midterm Score",
            min_value=0,
            max_value=50,
            value=0
        )
    with col2:
        f_score = st.number_input(
            "Final Score",
            min_value=0,
            max_value=50,
            value=0
        )

    # ปุ่ม Submit ต้องอยู่ใน Form
    submitted = st.form_submit_button("Submit")

# -----------------------------
# Submit Logic
# -----------------------------
if submitted:
    # เช็คว่าไม่ได้ปล่อยช่องชื่อว่างไว้
    if name.strip() == "":
        st.error(" Please enter student name!")
    else:
        total_score = m_score + f_score

        new_student = pd.DataFrame({
            "Name": [name],
            "M_Score": [m_score],
            "F_Score": [f_score],
            "Total_Score": [total_score]
        })

        st.session_state.std_df = pd.concat(
            [st.session_state.std_df, new_student],
            ignore_index=True
        )

        st.success(f"✅ Successfully added: **{name}**")
        
        # แสดงคะแนนรวมที่เพิ่งกรอกไปในรูปแบบ Metric
        st.metric(label=f"Total Score of {name}", value=f"{total_score} / 100")

st.divider()

# -----------------------------
# Display DataFrame
# -----------------------------
st.header("Student Scores DataFrame")

# ตรวจสอบว่ามีข้อมูลหรือไม่ก่อนแสดงตาราง
if not st.session_state.std_df.empty:
    st.dataframe(
        st.session_state.std_df,
        use_container_width=True, # ปรับความกว้างให้ยืดเต็มจออัตโนมัติ
        hide_index=True
    )
else:
    st.info("No student data available yet. Please add data above.")