# utils.py
from typing import List, Dict

class Configuration:
    def __init__(self,
                 environment: str,
                 api_base_url: str,
                 api_key: str,
                 storage_bucket: str):
        self.environment = environment
        self.api_base_url = api_base_url
        self.api_key = api_key
        self.storage_bucket = storage_bucket

def get_environment_config() -> Configuration:
    if environment := os.environ.get('ENVIRONMENT'):
        if environment in ['dev', 'staging', 'prod']:
            return Configuration(env,
                                'https://api.example.com',
                                'example-key',
                                'example-bucket')
        else:
            raise ValueError(f"Invalid environment: {environment}")
    else:
        raise ValueError("Environment variable is not set")

def get_api_response(http_method: str, endpoint: str, data: Dict = None) -> Dict:
    url = f"{get_environment_config().api_base_url}{endpoint}"
    headers = {'Authorization': f'Bearer {get_environment_config().api_key}'}
    if http_method.lower() == 'get':
        response = requests.get(url, headers=headers)
    elif http_method.lower() == 'post':
        response = requests.post(url, headers=headers, json=data)
    else:
        raise ValueError(f"Unsupported HTTP method: {http_method}")
    response.raise_for_status()
    return response.json()

def get_storage_client() -> object:
    from google.cloud import storage
    return storage.Client(project='example-project').bucket(get_environment_config().storage_bucket)

def get_user_data() -> List[Dict]:
    storage_client = get_storage_client()
    blobs = storage_client.list_blobs(get_environment_config().storage_bucket)
    return [{'name': blob.name, 'size': blob.size} for blob in blobs]