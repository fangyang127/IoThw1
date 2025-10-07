# HW1: Interactive Linear Regression Visualizer

## Introduction

This project is an interactive web application for visualizing and understanding simple linear regression. Users can dynamically adjust parameters such as the number of data points, the slope of the line, and the level of noise to see how they affect the regression model in real-time.

The application is built using Python and the Streamlit library, following the CRISP-DM methodology for data projects.

## Demo Site

The application is deployed and accessible at the following URL:

[**https://iothw1-fang.streamlit.app/**](https://iothw1-fang.streamlit.app/)

## Project Summary

This tool allows you to:
*   **Adjust Parameters**: Modify the number of data points, the coefficient 'a' (slope), and the noise variance.
*   **Visualize Data**: See a scatter plot of the generated data, the calculated regression line, and the top 5 outliers.
*   **Analyze Coefficients**: Review the learned model coefficients ('a' and 'b') and compare them to the true values.
*   **Identify Outliers**: View a table of the top 5 data points with the largest residuals.

The entire process, from data generation to model evaluation, is designed to provide a clear and intuitive understanding of linear regression.

## Development Log

- 60e444f refactor: Update title and enhance plot (2025-10-07)
- 4c5a868 feat: Create linear regression Streamlit app (2025-10-07)
- 4da27e7 Add requirements.txt for Streamlit Cloud (2025-10-07)
- 0edad06 Add homework instructions (hw1.md) (2025-10-07)
- 25be876 Initial commit: Add linear regression Streamlit app (2025-10-07)
