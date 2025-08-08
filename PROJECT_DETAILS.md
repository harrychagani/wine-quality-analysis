# Wine Quality Analysis Project Details

## Project Overview
This project analyzes the **Wine Quality (red wine)** dataset from the UCI Machine Learning Repository and showcases basic data analysis skills suitable for an **“Introduction to Python”** course.  The goal is to demonstrate how to load a dataset, explore it using the `pandas` library, visualize distributions with `matplotlib`, and compute correlations using `pandas` and `seaborn`.

The project contains a Python script called **`analyze_wine.py`** which performs the following tasks:

1. **Data Loading** – The script reads the `winequality-red.csv` dataset (semicolon‐separated) using `pandas`.  If the file isn’t already present, it downloads the dataset directly from the UCI repository so that the project remains reproducible without storing large datasets in the repository.

2. **Descriptive Statistics** – It prints the first five rows of the data (`head()`) and summary statistics (`describe()`) to provide an overview of the dataset’s structure and numeric ranges.

3. **Quality Distribution Plot** – Using `matplotlib`, it creates and saves a bar chart (`quality_distribution.png`) showing how many samples fall into each wine quality rating (scores range from 0 to 10).  This helps visualize the distribution of quality ratings.

4. **Correlation Analysis** – The script computes the Pearson correlation between each physicochemical property and the wine quality.  It prints these correlations to the console and saves a correlation heatmap (`correlation_heatmap.png`) using `seaborn`.  This helps identify which features are most strongly associated with quality.

## Dataset Information
- **Source** – UCI Machine Learning Repository – *Wine Quality Data Set*.
- **Samples** – 1,599 red wine samples from Portuguese **Vinho Verde** wines.
- **Features** – 11 physicochemical properties such as fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates and alcohol.
- **Target** – Quality score (sensory data) recorded by wine experts on a scale from 0 to 10.

## How to Run
1. Install the required Python packages:
   ```bash
   pip install pandas matplotlib seaborn requests
   ```
2. Run the script from the command line:
   ```bash
   python analyze_wine.py
   ```
   If `winequality-red.csv` is not present in the current directory, the script will download it automatically.  The script will generate two image files (`quality_distribution.png` and `correlation_heatmap.png`) in the working directory.

## Learning Outcomes
This project demonstrates basic skills often taught in an Introduction to Python course:
- Reading CSV files with `pandas` and inspecting data.
- Performing descriptive statistics and basic summarization.
- Plotting bar charts and heatmaps using `matplotlib` and `seaborn`.
- Computing correlations between numeric variables.
- Writing self‐contained, reproducible code that downloads data when needed.

## License
This project is provided for educational purposes and is published under the MIT license.
