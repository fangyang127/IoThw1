import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# --- CRISP-DM Documentation ---
# This app follows the CRISP-DM model.
# 1. Business Understanding: The goal is to create an interactive web app for visualizing simple linear regression. Users can understand the effect of changing parameters like the number of data points, the underlying relationship (coefficient 'a'), and the amount of noise.
# 2. Data Understanding: The data is synthetically generated. It consists of a single independent variable 'x' and a dependent variable 'y'. The relationship is defined by y = ax + b + noise.
# 3. Data Preparation: Data is generated and formatted into a Pandas DataFrame, ready for modeling. 'x' is reshaped for scikit-learn.
# 4. Modeling: A simple linear regression model from scikit-learn is trained on the generated data to find the best-fit line.
# 5. Evaluation: The model's learned coefficients are displayed. Outliers are identified by calculating the residual (the difference between the actual and predicted 'y' values).
# 6. Deployment: The application is deployed as a Streamlit web app.

st.set_page_config(layout="wide")

st.title("HW1: Interactive Linear Regression Visualizer")

st.markdown("""
This application demonstrates a simple linear regression model.
- **CRISP-DM Stages**: The process from understanding the business need to deploying this app follows the CRISP-DM framework.
- **Data Generation**: We create synthetic data based on the equation `y = ax + b + noise`.
- **Modeling**: A linear regression model is trained to find the line of best fit.
- **Evaluation**: We inspect the model's coefficients and identify outliers.
""")

# --- Sidebar for Adjustable Parameters ---
st.sidebar.header("Adjustable Parameters")

num_points = st.sidebar.slider(
    "Number of data points",
    min_value=100,
    max_value=1000,
    value=300,
    step=50,
    help="Number of data points to generate."
)

a_coeff = st.sidebar.slider(
    "Coefficient 'a' (y = ax + b + noise)",
    min_value=-10.0,
    max_value=10.0,
    value=2.5,
    step=0.5,
    help="Controls the slope of the underlying linear relationship."
)

noise_var = st.sidebar.slider(
    "Noise Variance (var)",
    min_value=0.0,
    max_value=100.0,
    value=10.0,
    step=5.0,
    help="Controls the amount of random noise added to the data."
)

# --- Data Generation (Data Preparation) ---
np.random.seed(42)
b_coeff_true = 5.0  # Constant 'b'
x = np.linspace(0, 10, num_points)
noise = np.random.normal(0, np.sqrt(noise_var), num_points)
y = a_coeff * x + b_coeff_true + noise

df = pd.DataFrame({'x': x, 'y': y})

# --- Modeling ---
X = df[['x']]
y_true = df['y']

model = LinearRegression()
model.fit(X, y_true)
y_pred = model.predict(X)

# --- Evaluation ---
a_pred = model.coef_[0]
b_pred = model.intercept_

df['y_pred'] = y_pred
df['residual'] = abs(df['y'] - df['y_pred'])
outliers = df.sort_values(by='residual', ascending=False).head(5)


# --- Display Results ---
col1, col2 = st.columns(2)

with col1:
    st.header("Generated Data and Linear Regression")
    fig, ax = plt.subplots(figsize=(10, 6))
    # Plot all data points
    ax.scatter(df['x'], df['y'], alpha=0.6, label='Generated Data')
    # Plot the regression line
    ax.plot(df['x'], y_pred, color='red', linewidth=2, label='Regression Line')
    # Highlight the outliers
    ax.scatter(outliers['x'], outliers['y'], color='orange', s=60, edgecolor='k', zorder=5, label='Top 5 Outliers')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Linear Regression Fit and Outliers")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

with col2:
    st.header("Model Coefficients")
    st.metric(label="Learned Coefficient 'a'", value=f"{a_pred:.4f}", delta=f"{a_pred - a_coeff:.4f} from true 'a'")
    st.metric(label="Learned Intercept 'b'", value=f"{b_pred:.4f}", delta=f"{b_pred - b_coeff_true:.4f} from true 'b'")

    st.header("Top 5 Outliers")
    st.dataframe(outliers[['x', 'y', 'y_pred', 'residual']].style.format("{:.2f}"))

st.info("To run this app locally, save the code as `app.py` and run `streamlit run app.py` in your terminal.")