import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Review Intelligence Engine",
    layout="wide"
)

# ---------------------------
# Load Products
# ---------------------------
@st.cache_data
def get_products():
    res = requests.get(f"{BACKEND_URL}/products")
    return res.json()["products"]

products = get_products()

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("AI Review Intelligence Engine")
page = st.sidebar.radio(
    "Navigation",
    ["Ask Product Question", "Compare Products"]
)

# ---------------------------
# Header
# ---------------------------
st.markdown(
    "<h1 style='text-align:center;'>AI Review Intelligence Engine</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>Ask questions powered by real Amazon reviews</p>",
    unsafe_allow_html=True
)

# ---------------------------
# ASK TAB
# ---------------------------
if page == "Ask Product Question":

    col1, col2 = st.columns(2)

    with col1:
        selected_product = st.selectbox(
            "Select a product",
            products
        )

    with col2:
        question = st.text_input(
            "Enter your question",
            placeholder="e.g. Is this product reliable?"
        )

    if st.button("Ask AI"):
        if question.strip() == "":
            st.warning("Please enter a question.")
        else:
            with st.spinner("Analyzing reviews..."):
                final_query = f"{question} about {selected_product}"
                res = requests.post(
                    f"{BACKEND_URL}/ask",
                    json={"question": final_query}
                )
                answer = res.json()["answer"]

                st.markdown("### Answer")
                st.success(answer)

# ---------------------------
# COMPARE TAB
# ---------------------------
if page == "Compare Products":

    col1, col2 = st.columns(2)

    with col1:
        product_a = st.selectbox("Product A", products)

    with col2:
        product_b = st.selectbox("Product B", products)

    if st.button("Compare"):
        with st.spinner("Comparing products..."):
            compare_query = f"""
Compare these two products based on reviews:

Product A: {product_a}
Product B: {product_b}

Give strengths, weaknesses, and final verdict.
"""
            res = requests.post(
                f"{BACKEND_URL}/ask",
                json={"question": compare_query}
            )

            st.markdown("### Comparison Result")
            st.success(res.json()["answer"])
