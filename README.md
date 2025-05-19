# Solar-Data-Discovery
Solar data discovery is a data analysis initiative focused on cleaning and exploring solar irradiance and weather data from three West African countries — Benin, Sierra Leone, and Togo. The objective is to prepare high-quality datasets that support energy optimization strategies in each region.

This repository contains the code, notebooks, and processes used for data profiling, cleaning, and exploratory data analysis (EDA).

📁 Repository Structure
The EDA notebooks are maintained in separate branches and have not yet been merged into the main branch. Each branch corresponds to one of the countries:

benin-eda

sierraleone-eda

togo-eda

📊 Data Description
The dataset includes files for each country:

benin-malanville.csv

sierraleone-bumbuna.csv

togo-dapaong_qc.csv

Each dataset contains the following columns:

Column Name	Description
Timestamp	Date and time of each observation (yyyy-mm-dd hh:mm)
GHI	Global Horizontal Irradiance (W/m²)
DNI	Direct Normal Irradiance (W/m²)
DHI	Diffuse Horizontal Irradiance (W/m²)
ModA, ModB	Sensor measurements from modules A and B (W/m²)
Tamb	Ambient Temperature (°C)
RH	Relative Humidity (%)
WS, WSgust, WSstdev	Wind Speed, Max Gust Speed, and Wind Speed Std Dev (m/s)
WD, WDstdev	Wind Direction and its Standard Deviation (°)
BP	Barometric Pressure (hPa)
Cleaning	Indicates a cleaning event (1 or 0)
Precipitation	Precipitation rate (mm/min)
TModA, TModB	Temperature of Modules A and B (°C)
Comments	Column was found to be entirely missing

✅ Task 1: Git & Environment Setup
Initialized a local Git environment.

Created and linked a remote GitHub repository.

Used standard Git commands (add, commit, push) to manage version control.

📌 Task 2: Data Profiling, Cleaning & EDA Plan
2.1 Data Profiling Summary
Datasets loaded using pandas.

Initial exploration using .head() and .info() to inspect structure and data types.

Descriptive statistics generated using .describe(include='all').

Missing value analysis using .isnull().sum() and .isnull().mean() — notably, the Comments column is fully missing.

(Optional) Checked for duplicate rows.

2.2 Planned Data Cleaning Steps
Handle missing values appropriately.

Convert data types as needed.

Identify and manage outliers.

Ensure consistency across variables and time ranges.

2.3 Exploratory Data Analysis (EDA) Plan
Univariate Analysis: Explore distributions (e.g., boxplots for Precipitation, Cleaning).

Bivariate Analysis: Examine relationships between variables such as cleaning events vs. weather factors.

Multivariate Analysis: Understand combined effects and interactions.

Time Series Analysis: Investigate seasonal and temporal trends in key metrics.

📈 Next Steps
Complete data cleaning for all three datasets.

Perform a cross-country comparative analysis (compare_countries.ipynb planned).

Document insights and visualizations in each EDA branch.

(Optional) Build a Streamlit app to showcase key findings.

Prepare for subsequent stages of the challenge.

🛠️ Libraries Used
pandas

numpy

seaborn

matplotlib

scipy

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
