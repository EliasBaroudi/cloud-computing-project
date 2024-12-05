import requests
import joblib
from io import BytesIO
import azure.functions as func
from azure.functions import FunctionApp

app = FunctionApp()

@app.function_name(name="MyFunction")
@app.route(route="example", methods=["POST"]) 
def example_function(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Récupérer les données JSON depuis le corps de la requête
        body = req.get_json()

        ## Pour récuperer des modèles présents sur Azure Functions ##

        # Reseigner le chemin des blobs 
        # model_path = 'https://.blob.core.windows.net/model-blob/model.pkl'
        # modelf_path = 'https://.blob.core.windows.net/modelf-blob/modelf.pkl'
        # vectorizer_path = 'https://.blob.core.windows.net/vectorizer-blob/vectorizer.pkl'
        # vectorizerf_path = 'https://.blob.core.windows.net/vectorizerf-blob/vectorizerf.pkl'

        # Télécharger les modèles depuis Blob Storage
        # response_model = requests.get(model_path)
        # response_modelf = requests.get(modelf_path)
        # response_vectorizer = requests.get(vectorizer_path)
        # response_vectorizerf = requests.get(vectorizerf_path)

        # Charger les modèles et les vectorizers
        # model = joblib.load(BytesIO(response_model.content))
        # modelf = joblib.load(BytesIO(response_modelf.content))
        # vectorizer = joblib.load(BytesIO(response_vectorizer.content))
        # vectorizerf = joblib.load(BytesIO(response_vectorizerf.content))

        ## Récuperer les modèles présents localement ##

        model = joblib.load('../ia/model.pkl')
        modelf = joblib.load('../ia/modelf.pkl')
        vectorizer = joblib.load('../ia/vectorizer.pkl')
        vectorizerf = joblib.load('../ia/vectorizerf.pkl')

        req_from = body.get('from')  
        req_body = body.get('body')  

        new_email_body = [body.get('body')]  
        new_email_from = [body.get('from')]
        new_emailf_transformed = vectorizerf.transform(new_email_from)
        new_email_transformed = vectorizer.transform(new_email_body) 

        # Prédire avec le modèle
        res = model.predict(new_email_transformed)
        resf = modelf.predict(new_emailf_transformed)

        # Retourner une réponse avec les données traitées
        return func.HttpResponse(f"{resf}{res}", status_code=200)

    except ValueError:
        # Si le corps n'est pas un JSON valide, on renvoie une erreur
        return func.HttpResponse(
            "Invalid JSON format", status_code=400
        )
    except Exception as e:
        return func.HttpResponse(f"An error occurred: {str(e)}", status_code=500)
