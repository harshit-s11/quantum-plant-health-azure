from azure.storage.blob import BlobServiceClient

connection_string = "YOUR_CONNECTION_STRING"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_client = blob_service_client.get_container_client("models")

with open("plant_health_model_fast.pkl", "rb") as data:
    container_client.upload_blob(name="plant_health_model_fast.pkl", data=data)
