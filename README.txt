### Instructions to Run the Application Locally ###

function_app.py:
    	Do not modify the comments and load the models locally (make sure the model paths are correct).
    
Commands in terminal:	

	cd azfunctions/

	## Install requirements ##
	pip install --break-system-packages -r requirements.txt

	## Ensure that npm and func are installed if they haven't been already ##
	apt install nodejs npm
	npm install func 

	## Install Azure Core Tools ##
	sudo npm install -g azure-functions-core-tools@4 --unsafe-perm true

	## Start the API ## If any issues arise with the requirements when launching the app, please install them manually.
	func start
	azurite


main.py :
	url: '' : Enter the Azure Functions API URL.

Commands in terminal :
	
	## Navigate to the project's root directory ##
	cd ../ 	

	## Ensure that Uvicorn is installed if it hasn't been already ##
	pip install uvicorn

	## Install requirements ##        
	pip install -r requirements.txt

	## Run the web application with uvicorn on port 8000 ## If any issues arise with the requirements when launching the app, please install them manually.
	uvicorn main:app --reload




### Deployment Instructions for Azure ###

sdk.py:
	Enter the credentials and update the path for the Azure Storage account.
	Deploy the models in blobs on Azure.

function_app.py:
	Uncomment and use the models deployed on Azure. Be sure to update the paths (URLs) to the blob storage.
	Deploy the function to Azure Functions.

static/js/main.js:
	Change the URL at line 12: replace the local URL with the URL of the deployed web application.

main.py:
	url: '' : Enter the Azure Functions API URL provided upon deployment.
	Create a ZIP file containing: main.py, /static, /templates, requirements.txt.
	Deploy the ZIP to Azure Web App.

