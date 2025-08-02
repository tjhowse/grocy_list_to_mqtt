FROM python:3.11

WORKDIR /grocy_list_to_mqtt

COPY requirements.txt main.py secrets_real.py grocy_api.py /grocy_list_to_mqtt/

RUN pip install -r requirements.txt --progress-bar off

CMD ["/grocy_list_to_mqtt/main.py"]
