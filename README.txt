### To run the application locally ###
function_app.py:
    Do not modify the comments and load the models locally (make sure the model paths are correct).
    Install the required dependencies.
    Run the API using Azure Core Tools.

main.py:
    url: '' : Enter the Azure Functions API URL.
    Install the required dependencies.
    Run the web application with uvicorn on port 8000.

### To deploy on Azure ###
sdk.py:
    Enter the credentials and update the path for the Azure Storage account.
    Deploy the models in blobs on Azure.

function_app.py:
    Uncomment and use the models deployed on Azure. Be sure to update the paths (URLs) to the blob storage.
    Deploy the function to Azure Functions.

main.py:
    url: '' : Enter the Azure Functions API URL (on Azure).
    Create a ZIP file containing: main.py, /static, /templates, requirements.txt.
    Deploy the ZIP to Azure Web App.

static/js/main.js:
    Change the URL at line 12: replace the local URL with the URL of the deployed web application.