
import requests
from google.colab import userdata

class AIConnectorFactory:
    def __init__(self):
        self.gemini_key = userdata.get('GEMINI_API_KEY')
        self.nasa_key = userdata.get('NASA_API_KEY')

    def call_gemini(self, prompt):
        return f"Gemini Response to: {prompt[:50]}..."

    def call_nasa_data(self, endpoint, params={}):
        params['api_key'] = self.nasa_key
        url = f"https://api.nasa.gov/{endpoint}"
        return requests.get(url, params=params).json()
