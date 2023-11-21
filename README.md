# VIDYO TECHNICAL TEST

This repository includes the following files: 


1. A script in Python located in scripts/setup.py to run on top of a stock Ubuntu Server 22.04 LTS Minimal that sets up a user account that only access to perform only the following administrative tasks: 

-restart services
-view, list, and stop network services
-view, list, and stop system services
-view, list, and stop logging services

Make sure you have the following installed:

- **Python 3:** If not installed, you can install Python 3 on Ubuntu using the following command:
  ```bash
  sudo apt update
  sudo apt install python3

- **pip:**. If not, install it by running:
  ```bash
  sudo apt install python3-pip

To run the script:
    ```python3 setup.py```


2. A bash script located in scripts/info_script.sh that can be run to extract the following information from an Ubuntu container and save it into a text file:
- A list of all of the currently installed OS packages**
- The status of all of the currently running Services**
- The hardware configuration – number of CPUs, model number, total/free RAM and Disk**

Steps to execute the script:
- Open a text editor on your Ubuntu 22.04 server
- Copy and paste the script into the text editor
- Save the file with a .sh extension (e.g., info_script.sh)
- Make the script executable using the command chmod +x info_script.sh
- Run the script with ./info_script.sh. It will generate a file named system_info.txt in the same directory containing the information you requested


3. A docker-compose file with the following services running: 
- nginx as an HTTPS reverse proxy, with a self-signed SSL/TLS certificate. The certificates were generated using openssl as you can see in the script setup-erts.sh inside nginx folder.
- A Web app that displays and creates tasks (React.js). Running in https://localhost
- A rest API for tasks with create and get all tasks (Flask). Running in https://localhost
- A database that stores the tasks (postgresql)


## Prerequisites

Ensure Docker and Docker Compose are installed on your system.

- [Docker Installation Guide](https://docs.docker.com/get-docker/)
- [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

## Docker Compose for Main Services

### Starting Containers and Applications

1. **Starting the Main Services:**
   Run the following command in the directory containing the first `docker-compose.yml` file:
   ```bash
   docker-compose up -d

This command initializes and starts containers for:
- REST API (Flask)
- PostgreSQL (Data Store)
- Web App (React.js)

2. **Start the Grafana and Prometheus Services:**
   Run the following command in the directory containing the first `docker-compose.yml` file:
   ```bash
   docker-compose -f docker-compose.yml -f docker-compose-monitoring.yml up

Access Grafana Dashboard:
Open a web browser and go to http://localhost:4000 to access the Grafana dashboard.

Access Prometheus:
Open a web browser and go to http://localhost:9090 to access Prometheus 



# Recommended KPIs

1. **Container CPU/Memory Usage:** Monitoring CPU load and memory usage of your containers can help detect bottlenecks and resource issues.

2. **API Latency:** Measuring your API's response time can indicate performance and responsiveness for users.

3. **Database Health:** Checking metrics like connection count, queued tasks, free space, etc., can be crucial to ensure the database is functioning properly.

4. **Successful vs. Failed Request Count:** Counting successful requests versus failed ones can provide insights into the stability and quality of your applications.

5. **Active User Count:** If your application has authentication, tracking the number of active users can be useful for understanding system load.

## File Structure
- `/scripts`: Contains Python and bash scripts for user account setup and initialization and system information.
- `/docker-compose`: Includes configuration files for setting up services, applications, and Grafana.


Feel free to reach out for any further assistance or inquiries.