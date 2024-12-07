from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
import json
import requests

# Création de l'application FastAPI
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Modèle de données pour l'email
class EmailContent(BaseModel):
    subject: str
    sender: str 
    body: str

def call_az_functions(text: EmailContent):
    try:
        email_from = text.sender
        email_subject = text.subject
        email_body = text.body
        
        data = {
            "from": f"{email_from}",
            "subject": f"{email_subject}",
            "body": f"{email_body}"
        }
        
        url = '' ## URL de l'api AZ Functions

        # Lancer la requete
        response = requests.post(url, json=data)

        # Anayse du code de réponse
        if response.status_code == 200:
            return response.text
        else:
            return f"Erreur dans la réponse du service externe : {response.status_code}"

    except Exception as e:
        print(f"Erreur dans l'analyse : {e}")
        return "Error"

# Route pour analyser l'email
@app.post("/api/analyze")
async def analyze_email(email: EmailContent):
    # Appeler l'API Cognitive pour prédire si l'email est du phishing
    result = call_az_functions(email)
    
    # Analyse de la réponse de l'API
    from_status = "Légitime" if result[1] == '0' else "Suspect"
    body_status = "Légitime" if result[4] == '0' else "Suspect"
    
    return {"from_status": from_status, "body_status": body_status, "email": email.dict()}

# Serveur l'index
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Lancer l'application FastAPI
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
