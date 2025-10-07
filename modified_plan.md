## Project Goal: Simple Linear Regression Analysis Web App

Create a Python-based web application to demonstrate a simple linear regression model. The entire process should follow the CRISP-DM methodology, and the final output should be a deployed web application using either Streamlit or Flask.

### Core Requirements:

1.  **CRISP-DM Framework**: The development process must be structured and documented according to the Cross-Industry Standard Process for Data Mining (CRISP-DM) stages. This documentation should explain the steps taken, not just present the final code and results.

2.  **Interactive Web Interface**: The application must provide an interactive user interface with the following features:
    *   **Adjustable Parameters**:
        *   **Number of data points**: A slider or input to select a value between 100 and 1000.
        *   **Coefficient 'a' (for y = ax + b + noise)**: A slider or input to select a value between -10 and 10.
        *   **Noise Variance (var)**: A slider or input to control the amount of random noise added to the data.
    *   **Visualizations and Outputs**:
        *   A plot showing the **Generated Data and the resulting Linear Regression line**.
        *   A display of the calculated **Model Coefficients** (the learned 'a' and 'b' values).
        *   A list of the **Top 5 Outliers** from the generated data.

3.  **Technology Stack**:
    *   **Backend**: Python
    *   **Web Framework**: Streamlit or Flask
    *   **Deployment**: The final application should be deployed and accessible.
