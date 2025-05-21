Solar Data Discovery
Overview
Solar Data Discovery is a data analysis project focused on exploring and cleaning solar irradiance and weather data from different countries (including Sierra Leone). The goal is to prepare clean and insightful datasets that will help optimize energy strategies for these regions.

This repository contains the code, notebooks, and methods used for data profiling, cleaning, and exploratory data analysis (EDA) of the Sierra Leone dataset.

Data Description
The dataset (sierraleone-bumbuna.csv) includes the following columns:

Timestamp (yyyy-mm-dd hh:mm): Date and time of each record.

GHI (W/m²): Global Horizontal Irradiance.

DNI (W/m²): Direct Normal Irradiance.

DHI (W/m²): Diffuse Horizontal Irradiance.

ModA (W/m²): Readings from module A.

ModB (W/m²): Readings from module B.

Tamb (°C): Ambient temperature.

RH (%): Relative humidity.

WS (m/s): Wind speed.

WSgust (m/s): Maximum wind gust speed.

WSstdev (m/s): Standard deviation of wind speed.

WD (°): Wind direction.

WDstdev: Standard deviation of wind direction.

BP (hPa): Barometric pressure.

Cleaning (1 or 0): Indicator of cleaning events.

Precipitation (mm/min): Precipitation rate.

TModA (°C): Temperature of module A.

TModB (°C): Temperature of module B.

Comments: Initially missing in the dataset.

Task 1: Git & Environment Setup
Set up a local Git environment, created a GitHub repository, and linked the local project to the remote repository. Used basic Git commands (add, commit, push) to manage the project.

Task 2: Profiling, Cleaning & EDA Plan
2.1 Data Profiling Summary
Loaded the datasets using pandas.

Inspected the initial rows and data types using .head() and .info().

Generated descriptive statistics using .describe(include='all') for all columns, giving insights into data distribution.

Conducted missing value analysis with .isnull().sum() and .isnull().mean(). Noted that the 'Comments' column was completely empty.

Checked for duplicate rows.

2.2 Planned Data Cleaning Steps
Handling Missing Values

Data Type Conversion

Outlier Management

Consistency Checks

2.3 Exploratory Data Analysis (EDA) Plan
The EDA will involve:

Univariate Analysis: Exploring individual features, using boxplots to visualize distributions.

Bivariate Analysis: Analyzing relationships between 'Cleaning' and other factors.

Multivariate Analysis: Examining relationships among multiple variables.

Time Series Analysis: Identifying trends and seasonality in key variables.

Next Steps
Future tasks include:

Completing data cleaning steps for all three countries.

Performing a comparative analysis across countries, as outlined in the EDA plan.

Documenting findings in the repository, possibly in a dedicated notebook (compare_countries.ipynb).

(Optional) Developing a visualization tool, like a Streamlit app, to present the insights.

Libraries Used
pandas

numpy

seaborn

matplotlib

scipy

License
This project is licensed under the MIT License — see the LICENSE file for details.
