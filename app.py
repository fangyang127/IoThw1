
import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# --- CRISP-DM: 1. Business Understanding ---
st.title("互動式簡單線性迴歸分析")
st.markdown("""
### **專案目標**
這個應用程式旨在模擬一個簡單的線性迴歸問題，並遵循 CRISP-DM 流程。
使用者可以動態調整以下參數，以觀察它們對模型結果的影響：
- **真實模型的斜率 (a)**
- **數據點的數量**
- **數據的雜訊程度**

透過互動式體驗，我們希望能更深入地理解線性迴歸的基本原理以及各項參數所扮演的角色。
""")

# --- CRISP-DM: 2. Data Understanding ---
st.sidebar.header("參數設定")
st.sidebar.markdown("請調整以下參數來生成數據：")

# Allow user to modify parameters
a_true = st.sidebar.slider("1. 選擇真實模型的斜率 (a)", 0.0, 10.0, 2.5, 0.1)
b_true = 5.0  # Let's keep b constant for simplicity
n_points = st.sidebar.slider("2. 選擇數據點數量", 10, 500, 100, 10)
noise_level = st.sidebar.slider("3. 選擇數據雜訊程度", 0.0, 10.0, 2.0, 0.5)

# --- CRISP-DM: 3. Data Preparation ---
st.header("CRISP-DM 步驟")
st.subheader("3. 數據準備")

# Generate synthetic data
np.random.seed(42)
X = np.random.rand(n_points) * 10
y_true = a_true * X + b_true
y_noisy = y_true + np.random.normal(0, noise_level, n_points)

df = pd.DataFrame({
    'X': X,
    'y_noisy': y_noisy,
    'y_true': y_true
})

st.markdown(f"""
我們基於您設定的參數生成了 **{n_points}** 個數據點。
- **真實關係**: `y = {a_true:.2f}x + {b_true:.2f}`
- **雜訊標準差**: `{noise_level}`
""")
st.dataframe(df.head())


# --- CRISP-DM: 4. Modeling ---
st.subheader("4. 模型建立")

# Reshape X for sklearn
X_reshaped = X.reshape(-1, 1)

# Create and fit the model
model = LinearRegression()
model.fit(X_reshaped, y_noisy)

# Get model predictions
y_pred = model.predict(X_reshaped)
df['y_pred'] = y_pred

# Get model parameters
a_pred = model.coef_[0]
b_pred = model.intercept_

st.markdown(f"""
我們使用 `scikit-learn` 的 `LinearRegression` 模型來擬合生成的數據。
- **模型找到的關係**: `y = {a_pred:.2f}x + {b_pred:.2f}`
""")


# --- CRISP-DM: 5. Evaluation ---
st.subheader("5. 模型評估")

# Calculate metrics
mse = mean_squared_error(y_noisy, y_pred)
r2 = r2_score(y_noisy, y_pred)

col1, col2 = st.columns(2)
col1.metric("均方誤差 (MSE)", f"{mse:.2f}")
col2.metric("R-squared (R²)", f"{r2:.2f}")

st.markdown("""
- **均方誤差 (MSE)**: 衡量模型預測值與實際值之間平均平方誤差。值越小，模型越準確。
- **R-squared (R²)**: 表示模型解釋的數據變異性比例。值越接近 1，表示模型對數據的解釋能力越強。
""")

# Visualization
st.subheader("數據與模型視覺化")
fig = px.scatter(df, x='X', y='y_noisy', labels={'y_noisy': '帶有雜訊的數據 (y_noisy)'},
                 title="數據點、真實關係與擬合模型")
fig.add_traces(px.line(df, x='X', y='y_true', color_discrete_sequence=['orange']).data)
fig.add_traces(px.line(df, x='X', y='y_pred', color_discrete_sequence=['green']).data)

# Update legend names
fig.data[0].name = '生成的數據點'
fig.data[1].name = f'真實關係 (y={a_true:.2f}x+{b_true:.2f})'
fig.data[2].name = f'模型擬合線 (y={a_pred:.2f}x+{b_pred:.2f})'

st.plotly_chart(fig, use_container_width=True)


# --- CRISP-DM: 6. Deployment ---
st.subheader("6. 部署")
st.success("""
這個 Streamlit 應用程式本身就是一個已部署的產品！

**如何在本機端運行:**
1.  確保您已安裝 Python。
2.  在您的終端機中，安裝必要的套件：
    ```bash
    pip install streamlit numpy pandas plotly scikit-learn
    ```
3.  執行以下命令來啟動應用程式：
    ```bash
    streamlit run app.py
    ```
""")
