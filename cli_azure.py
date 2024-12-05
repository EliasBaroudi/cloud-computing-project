from azureml.core import Model
from azureml.core import Workspace
from azureml.core.webservice import AciWebservice, Webservice
from azureml.core import Environment
from azureml.core.model import InferenceConfig


ws = Workspace.from_config('config.json')
model = Model(ws, name='phishing-model')

env = Environment.from_conda_specification(name="phishing-env", file_path="./environement.yml")
inference_config = InferenceConfig(entry_script="score.py", environment=env)

deployment_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)
service = Model.deploy(
    workspace=ws, name="phishing-endpoint", 
    models=[model], 
    inference_config=inference_config, 
    deployment_config=deployment_config
)

service.wait_for_deployment(show_output=True)

print(f"Service state: {service.state}")
print(f"Scoring URI: {service.scoring_uri}")

service_name = "phishing-endpoint"
service = Webservice(workspace=ws, name=service_name)
logs = service.get_logs()
print(logs)