import streamlit as st
import joblib
import numpy as np

# Load model
try:
    model = joblib.load('best_rf_modelmodel.pkl')
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Custom Theme: Earth Tones
st.markdown(
    """
    <style>
    body {
        background-color: #faf3e0; /* Cream background */
        font-family: 'Verdana', sans-serif;
        color: #4a4a4a; /* Dark gray text */
    }
    h1, h2, h3 {
        text-align: center;
        font-family: 'Georgia', serif;
        color: #2c5f2d; /* Earthy green */
    }
    .stButton>button {
        background-color: #a2d5c6; /* Light green */
        border: none;
        color: #ffffff;
        border-radius: 10px;
        font-size: 16px;
        padding: 10px 15px;
    }
    .stButton>button:hover {
        background-color: #76b29d; /* Darker green */
        color: white;
    }
    .stSidebar {
        background-color: #f6f1d1; /* Pale yellow sidebar */
        border-right: 2px solid #d9d9d9; /* Subtle sidebar divider */
        padding: 15px;
    }
    .footer {
        background-color: #2c5f2d; /* Earthy green */
        color: #ffffff;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        border-radius: 5px;
        margin-top: 20px;
    }
    .footer a {
        color: #a2d5c6;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.title("🌟 Future Water Use Estimator by Hannah and Samuel 🌟")
st.subheader("💦 Empowering smarter water management 💦")

# Split layout for inputs
st.markdown("---")
st.markdown("### **Input Features**")

col1, col2 = st.columns(2)
with col1:
    wat_bas_r = st.number_input("🌱 Basic Rural Water Access (%)", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
    wat_bas_u = st.number_input("🏠 Basic Urban Water Access (%)", min_value=0.0, max_value=100.0, value=70.0, step=0.1)
    wat_lim_n = st.number_input("🚿 Limited National Water Access (%)", min_value=0.0, max_value=100.0, value=5.0, step=0.1)

with col2:
    wat_unimp_n = st.number_input("🪠 Unimproved National Water Access (%)", min_value=0.0, max_value=100.0, value=10.0, step=0.1)
    wat_unimp_r = st.number_input("🌾 Unimproved Rural Water Access (%)", min_value=0.0, max_value=100.0, value=20.0, step=0.1)

# Prepare input for prediction
input_data = np.array([[wat_bas_r, wat_unimp_n, wat_bas_u, wat_lim_n, wat_unimp_r]])

# Prediction
st.markdown("---")
if st.button("🔮 Predict Future Water Use"):
    try:
        prediction = model.predict(input_data)
        st.success(f"🌟 🌟 Predicted Future Water Use: {prediction[0]:.2f} units")
        st.markdown(
            f"""
            ### What Does This Mean?
            The **Future Water Use** refers to the estimated amount of water resources (in specific units) 
            that will be required by the population in the future, based on the provided access metrics.

            #### Explanation:
            - **Predicted Value:** {prediction[0]:.2f} units represent the expected water demand or usage. 
            This value helps identify water needs for basic rural and urban water access, limited access, and unimproved access across national and rural areas. 
            - For example, if the predicted value is 68.03 units, it indicates that approximately 68 units of water resources will be needed to meet population demands, considering the current access metrics you have entered.

            #### Why Is This Important?
            Understanding future water use is crucial for:
            - **Planning:** Helps policymakers allocate resources for sustainable water management.
            - **Sustainability:** Supports identifying areas needing immediate intervention.
            - **Research:** Provides data for future projections and water infrastructure development.
            """)
        if prediction[0] > 100:
            st.warning("⚠️ The predicted value is quite high, indicating potential water scarcity.")
        elif prediction[0] < 30:
            st.info("💧 The predicted water use is low, suggesting efficient water management.")

    except Exception as e:
        st.error(f"Error during prediction: {e}")

# Footer
st.markdown(
    """
    <div class="footer">
        <p><strong>About This App</strong></p>
        <p>This app predicts the estimated future water usage based on provided water access metrics, helping communities 
        and policymakers plan for sustainable water management.</p>
        <p>Learn more about global water management initiatives on <a href="https://www.unwater.org" target="_blank">UN Water</a>.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
