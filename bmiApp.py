import streamlit as st
st.markdown("# :red[🏋️แอพลิเคชันค่าคำนวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูงน้ำหนักและส่วนสูงของคุุณ เพื่อเช็กสุขภพเบื้องต้น")

weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):")
height_cm = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):")

if st.button ("ค่าคำนวณค่า BMI🎯"):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2 )
    st.write("---")
    st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")

if bmi < 18.5:
    st.warning("⚠️ คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
elif 18.5 <= bmi < 23.0:
    st.success("🎉 คุณมีน้ำหนักอยู่ในเกณฑ์ปกติ (สุขภาพดี)")
elif  23.0 <= bmi < 25.0:
    st.info("💡 คุณเริ่มมีน้ำหนักเกินเกฑ์ (ท้วม)")
else :
    st.error("🚨 คุรอยู่ในเกณฑ์อ้วน ควรระวังเรื่องสุขภาพและออกกำลังกาย")

st.divider()
st.write("นางสาวบารณีย์ อวนวัง เลขที่ 35 ม.4/6")
