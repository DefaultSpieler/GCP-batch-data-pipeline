import kagglehub
from kagglehub import KaggleDatasetAdapter
import requests
from google.cloud import storage
import functions_framework

@functions_framework.http
def upload(request):
    # Download latest version
    try:
        df = kagglehub.dataset_load(
            KaggleDatasetAdapter.PANDAS,
            "ayeshaseherr/delivery-logistics-dataset",
            "Delivery_Logistics.csv",
        )
    except Exception as e:
        return (f"Error occurred: {str(e)}", 500)

    df.to_csv("Delivery_Logistics.csv", index=False)

    storage_client = storage.Client()
    bucket_name = "csv_delivery_data"
    destination_blob_name = "Delivery_Logistics.csv"

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename("Delivery_Logistics.csv")

upload(None)