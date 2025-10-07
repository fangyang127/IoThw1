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

1.  **Initial Planning**: The project began by translating the initial requirements from `hw1.md` into a structured English plan, `modified_plan.md`.
2.  **Core Application Development**: The main application was developed in `app.py` using Streamlit. This included creating the UI with interactive sliders for parameters, generating synthetic data, and performing linear regression with scikit-learn.
3.  **Visualization**: A plot was added to visualize the generated data, the regression line, and key model coefficients. A table for outliers was also included.
4.  **Dependency Management**: A `requirements.txt` file was created to list all necessary Python packages for easy installation and deployment.
5.  **First Version**: The initial version of the application and its supporting files were committed and pushed to GitHub.
6.  **Iteration and Refinement**: Based on user feedback, the application was refined. The main title was updated, and the plot was enhanced to visually distinguish the top 5 outliers, making the analysis more intuitive.
7.  **Documentation**: This `README.md` file was created to provide a comprehensive overview of the project, a link to the live demo, and a summary of the development process.
