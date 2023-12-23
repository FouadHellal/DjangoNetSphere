from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import json
import os
import random
import threading
import time
from .models import *
import telnetlib
'''---------------------------------'''

def generate_random_temperature():
    return round(random.uniform(5, 50), 2)
def generate_random_humidity():
    return round(random.uniform(0, 100), 1)
def generate_random_pressure():
    return round(random.uniform(0, 12000), 2)

# This lock (update_lock) will be used to synchronize access to the critical section of code, 
#ensuring that only one thread can execute it at a time.
update_lock = threading.Lock()

def update_temperature_periodically():
    while True:
        temperature_value = generate_random_temperature()
        humidity_value=generate_random_humidity()
        pressure_value=generate_random_pressure()

        # Acquire the lock
        with update_lock:
            # Update the JSON file with the new value
            json_file_path = os.path.join(os.path.dirname(__file__), 'data.json')

            with open(json_file_path, 'w') as json_file:
                
                json.dump(
                    {"timestamp": timezone.now().strftime("%Y-%m-%d %H:%M:%S"),
                 "temperature": temperature_value,
                 'humidity':humidity_value,
                 'preassure':pressure_value},
                  json_file
                  )

            # Save the temperature to the database
            save_to_database(temperature_value,humidity_value,pressure_value)


        time.sleep(5)

# Start the update loop in a thread when the application starts.
update_thread = threading.Thread(target=update_temperature_periodically)
update_thread.daemon = True  # Allow the thread to terminate when the application is stopped.
update_thread.start()


def get_from_json(file_path):
    # Lire les données depuis le fichier JSON
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    temperature = data.get("temperature", None)
    humidity = data.get("humidity", None)
    preassure = data.get("preassure", None)

    return temperature,humidity,preassure

def save_to_database(temperature_value,humidity_value,pressure_value):
    Temperature.objects.create(temperature=temperature_value, timestamp=timezone.now())
    Humidity.objects.create(humidity=humidity_value, timestamp=timezone.now())
    Preassure.objects.create(preassure=pressure_value, timestamp=timezone.now())



'''-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-CONDITIONS_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-'''


def execute_telnet_commands(host, username, password, commands):
    try:
        # Connect to the device
        tn = telnetlib.Telnet(host)

        # Read the login prompt
        tn.read_until(b"Username:")
        tn.write(username.encode('ascii') + b"\n")

        # Read the password prompt
        tn.read_until(b"Password:")
        tn.write(password.encode('ascii') + b"\n")

        # Wait for the prompt to make sure the login is successful
        tn.read_until(b">")

        # Execute commands
        for command in commands:
            tn.write(command.encode('ascii') + b"\n")
            time.sleep(1)  # Add a delay to allow the command to be processed

        # Close the connection
        tn.close()

        print("Commands executed successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Replace these values with your actual ones
host = "192.168.33.161"
username = "zac"
password = "zac"
commands = ["enable", "zac", "conf t", "logging console informational"]


# Fonction pour rétablir la vitesse normale du processeur
def retablir_vitesse_processeur():
    # Ajoutez ici la logique pour envoyer des commandes réseau pour rétablir la vitesse normale du processeur
    
    pass

#Pour laisser retablir vitesse processeur nkhellou 30s
action_duration = 0
action_duration_lock = threading.Lock()

def update_temperature_periodically():
    global action_duration

    while True:
        temperature_value = generate_random_temperature()

        with action_duration_lock:
            # Vérifier les conditions de température
            if temperature_value > 30 and action_duration == 0:
                execute_telnet_commands(host, username, password, commands)
                action_duration = 30
            elif temperature_value <= 30 and action_duration > 0:
                action_duration = 0
                retablir_vitesse_processeur()

            # Mettre à jour le fichier JSON avec la nouvelle valeur
            json_file_path = os.path.join(os.path.dirname(__file__), 'data.json')

            with open(json_file_path, 'w') as json_file:
                json.dump(
                    {"timestamp": timezone.now().strftime("%Y-%m-%d %H:%M:%S"),
                     "temperature": temperature_value},
                      json_file)

            # Enregistrez également la valeur dans la base de données si nécessaire
            save_to_database(temperature_value)

        time.sleep(5)

'''-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-'''

'''--------------------The return functions--------------------'''

def home_temp(request):
    # Chemin vers le fichier JSON
    json_file_path = os.path.join(os.path.dirname(__file__), 'data.json')

    # Utiliser la fonction pour obtenir la température
    temperature_value, humidity_value, pressure_value = get_from_json(json_file_path)
 
    # Enregistrez également la valeur dans la base de données si nécessaire
    save_to_database(temperature_value,humidity_value,pressure_value)

    # Récupérer toutes les températures de la base de données
    #all_temperatures = Temperature.objects.all()

    return render(request, 'events/home.html',
     {'temperature_value': temperature_value,
     'humidity_value':humidity_value,
     'preassure_value':pressure_value}
      )

def trigger_topology_commands(request):
    execute_telnet_commands(host, username, password, commands)
    return HttpResponse("Topology commands triggered successfully.")
    