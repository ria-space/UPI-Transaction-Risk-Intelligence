# UPI Transaction Risk Intelligence

An end-to-end data analytics and fraud risk intelligence project built using **Python, SQL, MySQL, Power BI, and DAX**.

The project analyzes UPI transaction data to identify fraud patterns, understand transaction risk drivers, and present actionable insights through an interactive Power BI dashboard.

---

## Project Overview

UPI transactions generate large volumes of financial data, making it important to identify unusual transaction patterns and potential fraud.

This project follows an end-to-end analytics workflow:

**Raw Data → Data Cleaning → Feature Engineering → SQL Analysis → Risk Scoring → Power BI Dashboard → Business Insights**

The objective is to analyze transaction behavior and create a practical risk intelligence system rather than simply performing descriptive analysis.

---

## Key Project Statistics

| Metric                 |                 Value |
| ---------------------- | --------------------: |
| Total Transactions     |               250,000 |
| Fraud Transactions     |                   480 |
| Fraud Rate             |                0.192% |
| High-Risk Transactions |               ~11,000 |
| Data Period            | January–December 2024 |

The dataset contains a highly imbalanced fraud class, making fraud-rate analysis and risk-based segmentation particularly important.

---

## Technology Stack

* **Python** — Data cleaning, preprocessing, feature engineering and analysis
* **Pandas & NumPy** — Data manipulation and numerical analysis
* **SQL** — Risk analysis and transaction-level investigation
* **MySQL** — Database storage and querying
* **Power BI** — Interactive dashboard and visualization
* **DAX** — Measures, KPIs and risk calculations
* **Jupyter Notebook** — Exploratory data analysis
* **Git & GitHub** — Version control and project documentation

---

## Project Structure

```text
UPI_Transaction_Risk_Intelligence/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── 01_data_understanding.ipynb
│
├── reports/
│   └── UPI_Transaction_Risk_Intelligence.pbix
│
├── sql/
│   └── 01_risk_analysis
│
├── src/
│   └── load_to_mysql.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

> **Note:** The transaction CSV files are intentionally excluded from this GitHub repository because of their size. They are kept locally and are covered by `.gitignore`.

---

## Dataset

The project uses a synthetic UPI transaction dataset containing approximately **250,000 transactions** across 2024.

The dataset includes transaction and behavioral attributes such as:

* Transaction ID
* Timestamp
* Transaction type
* Merchant category
* Transaction amount
* Transaction status
* Sender age group
* Receiver age group
* Sender state
* Sender bank
* Receiver bank
* Device type
* Network type
* Fraud flag

The dataset contains **480 fraud transactions**, representing approximately **0.192%** of all transactions.

---

## Data Preparation

The data preparation workflow included:

1. Loading the raw transaction data using Python.
2. Checking dataset dimensions and column information.
3. Converting timestamp fields into appropriate datetime format.
4. Checking for missing values.
5. Checking categorical values for inconsistencies.
6. Validating transaction statuses and categories.
7. Performing exploratory data analysis.
8. Creating additional features for risk analysis.
9. Generating transaction risk scores and risk tiers.

---

## Risk Analysis

The project investigates fraud and transaction risk across multiple dimensions, including:

* Transaction type
* Merchant category
* Device type
* Network type
* Sender state
* Transaction status
* Transaction amount
* Time of transaction
* Risk tier

Because fraud represents a very small proportion of total transactions, the analysis focuses on both **fraud patterns** and broader **risk indicators**.

---

## SQL Analysis

MySQL is used to perform structured transaction analysis and investigate risk patterns.

The SQL analysis includes:

* Transaction volume analysis
* Fraud transaction analysis
* Fraud-rate calculations
* Category-level comparisons
* Risk segmentation
* Transaction investigation queries

The SQL scripts are available in the `sql/` directory.

---

## Power BI Dashboard

The project includes an interactive Power BI dashboard consisting of three main pages.

### 1. Executive Risk Overview

Provides a high-level view of:

* Total transactions
* Fraud transactions
* Fraud rate
* High-risk transactions
* Overall transaction risk

### 2. Risk Drivers

Analyzes factors associated with transaction risk, including:

* Transaction type
* Merchant category
* Device type
* Network type
* Sender state
* Risk tier

### 3. Transaction Investigation

Provides a more detailed transaction-level view for investigating individual transactions and their associated risk characteristics.

**Power BI File**

The complete Power BI dashboard is available here:

UPI_Transaction_Risk_Intelligence.pbix

---

## Key Findings

Some observations from the analysis include:

* The dataset contains a highly imbalanced fraud class, with fraud accounting for approximately **0.192%** of transactions.
* Most transactions are successful, while failed transactions form a smaller proportion of the dataset.
* Fraud patterns vary across transaction types and merchant categories.
* Risk segmentation helps identify a much broader set of potentially risky transactions than confirmed fraud cases alone.
* Transaction-level analysis can be used to investigate individual risk indicators.

---

## Risk Scoring

A risk-scoring approach was developed to categorize transactions into different risk levels.

Example risk tiers:

* **Low Risk**
* **Medium Risk**
* **High Risk**

The risk tier is intended as an analytical risk indicator and should not automatically be interpreted as confirmed fraud.

---

## Python Workflow

The Python workflow includes:

```text
Raw Dataset
     ↓
Data Understanding
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
Risk Scoring
     ↓
Processed Dataset
```

The main exploratory notebook is available in:

```text
notebooks/01_data_understanding.ipynb
```

---

## MySQL Workflow

The Python loader connects the processed transaction data to MySQL.

The database workflow is:

```text
Processed Data
      ↓
Python MySQL Loader
      ↓
MySQL Database
      ↓
SQL Risk Analysis
```

Database credentials are stored locally using environment variables and are **not included in this repository**.

---

## Reproducibility

### 1. Clone the repository

```bash
git clone https://github.com/ria-space/UPI-Transaction-Risk-Intelligence.git
cd UPI-Transaction-Risk-Intelligence
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a local `.env` file containing:

```text
MYSQL_HOST=localhost
MYSQL_USER=YOUR_MYSQL_USERNAME
MYSQL_PASSWORD=YOUR_MYSQL_PASSWORD
MYSQL_DATABASE=upi_risk_intelligence
```

Do not upload the `.env` file to GitHub.

---

## Repository Data Policy

The following files are intentionally excluded from GitHub:

* Raw transaction CSV files
* Processed transaction CSV files
* `.env`
* Python virtual environment

This keeps the repository lightweight and prevents credentials from being exposed.

---

## Project Objective

The main objective of this project is to demonstrate an end-to-end **data analytics and fraud risk intelligence workflow** using real-world-style transaction data.

It combines:

**Python + SQL + MySQL + Power BI + DAX**

to transform raw transaction data into analytical insights and an interactive risk dashboard.

---

## Author

**Data Science Student**

GitHub: [@ria-space](https://github.com/ria-space)
