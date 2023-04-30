import os
from dotenv import load_dotenv

# carrega as variáveis de ambiente do arquivo .env
load_dotenv()
# obtém o valor das variáveis de ambiente usando os.getenv()

#Broker
BROKER_HOST = os.getenv("BROKER_HOST")
BROKER_PORT = int(os.getenv("BROKER_PORT"))

#Credentials
MQTT_USERNAME = os.getenv("MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")

# Numero de requests

NUM_REQUESTS = os.getenv("NUM_REQUESTS")


