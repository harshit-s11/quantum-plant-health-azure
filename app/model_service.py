import os
import pickle
import tempfile
from azure.storage.blob import BlobServiceClient
from vqc_fast import FastPlantHealthClassifier

class AzureModelService:

    def __init__(self):
        self.connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        self.container_name = "models"
        self.model_name = "plant_health_model_fast.pkl"
        self.classifier = FastPlantHealthClassifier(n_qubits=4)

    def download_model_from_blob(self):
        blob_service_client = BlobServiceClient.from_connection_string(
            self.connection_string
        )

        container_client = blob_service_client.get_container_client(self.container_name)

        blob_client = container_client.get_blob_client(self.model_name)

        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(blob_client.download_blob().readall())
        temp_file.close()

        return temp_file.name

    def load_model(self):
        model_path = self.download_model_from_blob()
        self.classifier.load_model(model_path)

    def predict(self, image_path):
        return self.classifier.predict(image_path)
