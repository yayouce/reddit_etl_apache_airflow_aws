#pulling de l'image from apache
FROM apache/airflow:2.7.1-python3.9    
## copie le requirement txt qui vient avec et le charger dans /opt/airflow/
COPY requirements.txt /opt/airflow/
##on switch en root mode 
USER root 
## pour executer cette commande qui consiste à installer ces elements
RUN apt-get update && apt-get install -y gcc python3-dev

##après on switch en airflow user  afin 
USER airflow
## d'executer la commande suivante 
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt