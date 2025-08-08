# Wine Quality Analysis

This repository contains a simple project suitable for an **Introduction to Python** course.  
It demonstrates how to load and explore a dataset using Python's popular data analysis libraries.

## Dataset

The dataset used here is the **Wine Quality (red wine) dataset** from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/wine+quality).  
It contains 1,599 samples of Portuguese *Vinho Verde* red wines. Each sample is described by 11 physicochemical properties (e.g. acidity, pH, alcohol content) and a quality rating (score between 0 and 10).

The raw data file is **not included** in this repository to keep the repository size small.  
The analysis script will automatically download the dataset from the UCI repository if it is not present locally.  
More information about the dataset can be found on the UCI repository page linked above.

## What this project does

The `analyze_wine.py` script performs a straightforward exploratory analysis on the dataset:

1. **Loads the data** from the CSV file using pandas.
2. **Displays basic information**, such as the first few rows and summary statistics for each numeric column.
3. **Counts and plots** the distribution of wine quality scores.
4. **Calculates the correlation** between each physicochemical property and the quality rating, ranking them from strongest to weakest relationship.
5. **Produces two charts** saved as PNG files:
   - `quality_distribution.png` – a bar chart showing how many wines fall into each quality rating.
   - `correlation_heatmap.png` – a heatmap visualizing the full correlation matrix of all features.

These analyses illustrate foundational Python concepts: reading files, using dataframes, simple statistics, and plotting graphs.  
They can be extended with more advanced techniques (e.g. machine learning models) once you are comfortable with the basics.

## Requirements

To run the analysis, you'll need Python 3.x and the following packages:

```
pip install pandas matplotlib seaborn
```

`seaborn` is optional but recommended for the correlation heatmap. If it is not available, the script will still run but without the heatmap.

## How to run

1. Clone or download this repository.
2. In a terminal, navigate to the project directory and run:

```
python analyze_wine.py
```

The script will output text to the console and save two image files in the current directory.  
If `winequality-red.csv` is not found locally, the script will download it automatically from the UCI Machine Learning Repository.

## License

The original Wine Quality dataset is made available under a [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) license.  
This repository provides the dataset and analysis code for educational purposes. Feel free to use and adapt the code as you like.
