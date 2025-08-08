"""
analyze_wine.py
=================

This script performs a simple exploratory data analysis on the
red wine quality dataset from the UCI Machine Learning Repository.

It demonstrates basic Python skills appropriate for an
"Introduction to Python" course, including:

* Reading a CSV file with pandas
* Inspecting the data with `head()` and `describe()`
* Counting categorical values
* Plotting a bar chart using matplotlib
* Computing and displaying correlations

The script saves a bar chart of the quality distribution and
a correlation heatmap to PNG files in the current directory.

Author: (your name here)
Date: 2025-08-07
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    """Run the exploratory analysis on the wine quality dataset."""
    # Load the dataset. The dataset uses semicolon delimiters.
    # If the CSV file is present locally, load it; otherwise, download it
    # directly from the UCI Machine Learning Repository. This avoids the need
    # to store large data files in the repository while making the analysis
    # reproducible for anyone with an internet connection.
    local_path = "winequality-red.csv"
    url = (
        "https://archive.ics.uci.edu/ml/machine-learning-databases/"
        "wine-quality/winequality-red.csv"
    )

    if os.path.exists(local_path):
        df = pd.read_csv(local_path, sep=";")
    else:
        print("Local dataset file not found. Downloading from UCI repository...")
        df = pd.read_csv(url, sep=";")

    # Print the first five rows to understand the structure
    print("First five rows of the dataset:")
    print(df.head(), end="\n\n")

    # Display summary statistics for numeric columns
    print("Summary statistics:")
    print(df.describe(), end="\n\n")

    # Distribution of the quality scores
    quality_counts = df['quality'].value_counts().sort_index()
    print("Quality score distribution:")
    print(quality_counts, end="\n\n")

    # Plot the distribution as a bar chart
    plt.figure(figsize=(8, 5))
    quality_counts.plot(kind='bar', color='skyblue')
    plt.title('Distribution of Wine Quality Ratings')
    plt.xlabel('Quality Score')
    plt.ylabel('Number of Wines')
    plt.tight_layout()
    plt.savefig('quality_distribution.png')
    plt.close()

    # Compute correlation matrix
    corr_matrix = df.corr()
    # Correlation of each feature with the target variable 'quality'
    corr_quality = corr_matrix['quality'].drop('quality').sort_values(ascending=False)
    print("Correlation of physicochemical properties with wine quality:")
    print(corr_quality, end="\n\n")

    # Plot correlation heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, cmap='coolwarm', center=0, square=True,
                linewidths=.5, cbar_kws={'shrink': 0.8})
    plt.title('Correlation Matrix Heatmap')
    plt.tight_layout()
    plt.savefig('correlation_heatmap.png')
    plt.close()


if __name__ == '__main__':
    main()