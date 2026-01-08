# GCP Batch Data Pipeline

This project demonstrates the design and implementation of an end-to-end batch data pipeline on Google Cloud Platform (GCP).
The primary goal of this project is to gain hands-on experience with GCP data engineering services and understand how they integrate to build scalable and automated data pipelines.

## 🚀 Technologies & Services Used

Google Cloud Storage (GCS)

Cloud Functions

Cloud Scheduler

Dataflow (Apache Beam)

BigQuery

Dataproc (exploratory/learning)

Apache Airflow (orchestration – learning focus)

Python

KaggleHub

📊 Dataset

The pipeline uses a publicly available dataset from Kaggle:

Delivery Logistics Dataset
🔗 https://www.kaggle.com/datasets/ayeshaseherr/delivery-logistics-dataset

This dataset contains delivery-related records suitable for batch ingestion and analytical processing.

1️⃣ Data Ingestion (Cloud Functions + KaggleHub)

A Cloud Function is implemented to fetch the dataset using the KaggleHub library.

The raw CSV file is stored in a Google Cloud Storage (GCS) bucket.

The ingestion logic can be found in the fetch_kaggle_data.py file.

⚠️ Known Issue

The ingestion works correctly when executed via CLI.

When triggered via Cloud Functions, it fails while reading data from Kaggle.

This issue is currently under investigation (likely related to authentication, environment variables, or library compatibility in the Cloud Functions runtime).

2️⃣ Scheduling & Automation (Cloud Scheduler)

Cloud Scheduler is configured to trigger the Cloud Function at predefined intervals.

This enables automated batch ingestion without manual intervention.

3️⃣ Data Transformation (CSV → Parquet)

The raw CSV data from the ingestion bucket is:

Read

Cleaned (basic transformations)

Converted into Parquet format

The transformed data is stored in a separate GCS bucket optimized for analytics.

4️⃣ Data Loading & Analytics (Dataflow → BigQuery)

Dataflow (Apache Beam) is used to:

Read Parquet files from GCS

Load the processed data into BigQuery

This enables fast SQL-based analytics and downstream reporting.

🎯 Key Learning Outcomes

Building serverless ingestion pipelines using Cloud Functions

Scheduling batch jobs using Cloud Scheduler

Handling data format optimization (CSV → Parquet)

Implementing scalable ETL pipelines using Dataflow

Designing analytics-ready datasets in BigQuery

Understanding real-world cloud issues like environment-specific failures

🛠️ Project Status

✅ End-to-end pipeline implemented

⚠️ Cloud Function Kaggle ingestion issue under investigation

🚧 Future enhancements planned (see below)

🔮 Future Improvements

Fix Kaggle authentication issue in Cloud Functions

Add Airflow DAG for full orchestration

Implement data validation & schema checks

Add logging and monitoring using Cloud Logging
