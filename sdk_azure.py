from azure.storage.blob import BlobServiceClient

credential = '' ## Mettre à jours les credential avec la clé d'accès
blob_service_client = BlobServiceClient(account_url="https://.blob.core.windows.net", credential=credential) ## Mettre à jour avec l'url du conteneur


# Connexion au Blob Storage
container_name = "model-blob"
blob_name = "model.pkl"

blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
with open("model.pkl", "rb") as model_file:  
    blob_client.upload_blob(model_file)

container_name = "vectorizer-blob"
blob_name = "vectorizer.pkl"

blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
with open("vectorizer.pkl", "rb") as model_file:  
        blob_client.upload_blob(model_file)

container_name = "modelf-blob"
blob_name = "modelf.pkl"

blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
with open("modelf.pkl", "rb") as model_file:  
    blob_client.upload_blob(model_file)

container_name = "vectorizerf-blob"
blob_name = "vectorizerf.pkl"

blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
with open("vectorizerf.pkl", "rb") as model_file:  
        blob_client.upload_blob(model_file)


