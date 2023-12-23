# DjangoNetSphere

## Overview

DjangoNetSphere is a sophisticated smart home automation system that leverages the power of Django, a robust web framework, to seamlessly integrate network automation. This project includes a feature-rich temperature dashboard that monitors real-time environmental conditions and triggers network commands based on temperature thresholds.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [File Structure](#file-structure)
- [Temperature Dashboard Flow](#temperature-dashboard-flow)
- [Network Topology](#network-topology)
- [License](#license)
- [Contributors](#contributors)

## Features

- **Temperature Dashboard:** View real-time temperature, humidity, and pressure data through a simple HTML web interface.

- **Network Integration:** Dynamically trigger network commands using Telnet based on temperature conditions.

## Getting Started

### Prerequisites

- Python (3.6 or higher)
- Django
- Telnetlib3

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/DjangoNetSphere.git
   cd DjangoNetSphere

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate

3. Install dependencies:

    ```bash
    Copy code
    pip install -r requirements.txt

4. Set up Django database:

    ```bash
    Copy code
    python manage.py migrate

5. Run the Django development server:

    ```bash
    Copy code
    python manage.py runserver

6. Access the web interface at http://localhost:8000.

# Configuration

1. **Django Settings:**
   - Configure Django settings in `settings.py`, including database settings.

2. **Telnet Configurations:**
   - Adjust Telnet configurations in `views.py`.
   - Update the `execute_telnet_commands` function with your specific commands and network details(Such as the host ip address, username, password..etc).

# Files and Directories

- **data.json:**
  - Stores real-time environmental data.
  
- **events/views.py:**
  - Contains view functions, including Telnet commands and data retrieval logic.

- **events/urls.py:**
  - Defines URL patterns for the application.

- **events/templates/events/home.html:**
  - HTML template for the home page.

- **requirements.txt:**
  - Lists project dependencies.

## Temperature Dashboard Flow

### Data Generation:

- Random temperature, humidity, and pressure values are generated periodically.

### Backend:

- The generated data is stored in `data.json` and saved to the database using Django models (`Temperature`, `Humidity`, `Pressure`).

### Frontend:

- The web interface (`home.html`) retrieves real-time data from the database and displays it to the user.
- Temperature values above a threshold trigger network commands.

# Telnet Commands

- **execute_telnet_commands:**
  - Function in `views.py` responsible for establishing a Telnet connection and executing commands on a network device.

  ```python
  
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

# More Informations

This project includes a sample network topology created using EVE-NG, a network emulation platform. The topology is designed for testing connectivity and showcasing the integration of Django with network automation.

## Topology Diagram
<img width="251" alt="topology_diagram" src="https://github.com/FouadHellal/DjangoNetSphere/assets/113594352/a78f54c9-97dc-4148-ad15-5cd9897c7480">

## Purpose

The topology has been configured to simulate a small network environment. It includes a MultiLayer Cisco Switch to demonstrate the interaction between the Django web application and network devices. The primary goal is to test connectivity and verify the functionality of network commands triggered by the temperature conditions in the Django application.


Feel free to explore and modify the topology for your specific testing needs.
# License

This project is licensed under the MIT License.

# Contributors

- Fouad HELLAL
