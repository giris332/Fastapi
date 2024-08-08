import streamlit as st
import httpx

FASTAPI_URL = "http://127.0.0.1:8000"

st.title("Student Management System")

menu = ["Home", "View Student", "Add Student", "Update Student", "Delete Student"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Home")
    r = httpx.get(f"{FASTAPI_URL}/")
    st.write(r.json())

elif choice == "View Student":
    st.subheader("View Student")
    student_id = st.number_input("Student ID", min_value=1, step=1)
    if st.button("Get Student"):
        r = httpx.get(f"{FASTAPI_URL}/get-student/{student_id}")
        st.write(r.json())

elif choice == "Add Student":
    st.subheader("Add Student")
    student_id = st.number_input("Student ID", min_value=1, step=1)
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, step=1)
    year = st.text_input("Year")

    if st.button("Add Student"):
        student_data = {"name": name, "age": age, "year": year}
        r = httpx.post(f"{FASTAPI_URL}/create-student/{student_id}", json=student_data)
        st.write(r.json())

elif choice == "Update Student":
    st.subheader("Update Student")
    student_id = st.number_input("Student ID", min_value=1, step=1)
    name = st.text_input("Name (optional)")
    age = st.number_input("Age (optional)", min_value=1, step=1)
    year = st.text_input("Year (optional)")

    if st.button("Update Student"):
        student_data = {}
        if name:
            student_data["name"] = name
        if age:
            student_data["age"] = age
        if year:
            student_data["year"] = year
        r = httpx.put(f"{FASTAPI_URL}/update-student/{student_id}", json=student_data)
        st.write(r.json())

elif choice == "Delete Student":
    st.subheader("Delete Student")
    student_id = st.number_input("Student ID", min_value=1, step=1)

    if st.button("Delete Student"):
        r = httpx.delete(f"{FASTAPI_URL}/delete-student/{student_id}")
        st.write(r.json())
