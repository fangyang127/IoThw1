# Development Log (`devLog.md`)

This document details the prompts and development process for creating the Interactive Linear Regression Visualizer.

---

### 1. Initial Request & Planning

*   **Prompt:** Read the initial requirements from `hw1.md`, add new specifications for the UI and parameter ranges, and create a consolidated project plan in English.
*   **Process:**
    1.  Read the content of `hw1.md` which outlined the base requirement for a linear regression web app using CRISP-DM.
    2.  Incorporated user's new requirements: specific UI elements (sliders for 3 parameters), output sections (plot, coefficients, outliers), and defined ranges for the parameters.
    3.  Translated and combined these points into a clear project plan.
    4.  Saved the final plan as `modified_plan.md`.

---

### 2. Core Application Development

*   **Prompt:** Read `modified_plan.md`, write the Python application, and upload it to GitHub.
*   **Process:**
    1.  Chose the Streamlit framework for its simplicity in creating interactive data apps.
    2.  Wrote the application code in `app.py`, including:
        *   UI sliders for "Number of data points", "Coefficient 'a'", and "Noise Variance".
        *   Data generation logic using NumPy.
        *   Linear regression modeling using scikit-learn.
        *   Plotting with Matplotlib to display data, the regression line.
        *   Outlier calculation based on residuals.
        *   Displaying model coefficients and the top 5 outliers.
    3.  Created a `requirements.txt` file to list dependencies (`streamlit`, `numpy`, `pandas`, `scikit-learn`, `matplotlib`).
    4.  Staged (`git add`) and committed (`git commit`) the new files (`app.py`, `modified_plan.md`, `requirements.txt`).
    5.  Pushed the commit to the remote GitHub repository.

---

### 3. Iteration and Refinement

*   **Prompt:** Change the application title to "HW1: Interactive Linear Regression Visualizer", visually highlight the top 5 outliers on the plot, and improve the plot's title.
*   **Process:**
    1.  Modified `app.py` to update the `st.title`.
    2.  Enhanced the Matplotlib plotting function to include a second `scatter` call specifically for the outliers, using a distinct color and size to make them stand out.
    3.  Updated the plot title to be more descriptive.
    4.  Committed and pushed the updated `app.py` to GitHub.

---

### 4. Project Documentation (README)

*   **Prompt:** Create a `README.md` file with an introduction, a link to the deployed demo site, a project summary, and a development log.
*   **Process:**
    1.  Drafted an introduction and project summary based on the application's functionality.
    2.  Included the provided URL for the demo site.
    3.  Used `git log` to generate an initial commit history for the development log section.
    4.  Created the `README.md` file, committed it, and pushed it to GitHub. This initially caused a push conflict because the remote repository had changes (a `.devcontainer` file) that were not present locally.
    5.  Resolved the conflict by running `git pull` to merge the remote changes, then successfully pushed the new `README.md`.

---

### 5. Final Documentation Refinement

*   **Prompt:** Update the "Development Log" in `README.md` to be a narrative description of the process instead of a raw git log.
*   **Process:**
    1.  Rewrote the "Development Log" section to be a step-by-step summary of the project's lifecycle.
    2.  Replaced the old git log list with this new narrative content in `README.md`.
    3.  Committed and pushed the final documentation update to GitHub.

---
