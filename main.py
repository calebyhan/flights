import airlabs
from decouple import config

api = airlabs.API(config("KEY"))

print(api.flight(flight_iata="AA6"))
