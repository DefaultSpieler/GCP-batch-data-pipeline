# GCP-batch-data-pipeline
This pipeline is implemented to get hands on experience on some of the GCP concepts like Dataproc, Dataflow, Cloud Function, Cloud Scheduler and Airflow.
For this, I have used a dataset from Kaggle. For the ingestion part, I have implemented a cloud function which will use KaggleHub library dataset and put it into GCS Bucket. For this, you can refer fetch_kaggle_data,py file. 
The issue with this is - the code is able to dump the csv data from Kaggle into GCS bucket when executed through CLI. When triggered through cloud function it is giving error while reading data from Kaggle. This is under investigation.
Through a cloud scheduler, the cloud function will be triggered which will read the CSV data and put it into a GCS bucket. From this bucket - the data will read and converted into Parquet data format and put the data into another GCS bucket. 
Using Dataflow, the parquet data will be put into BigQuery for further querying. 
Kaggle Dataset Link - https://www.kaggle.com/datasets/ayeshaseherr/delivery-logistics-dataset?resource=download


