FROM python:3.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code

# Puerto para el servicio del backend
EXPOSE 80

# Puerto para la escucha del servicio de mensajeria
# EXPOSE 81

# Servicio backend API
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80", "--reload"]

# Servicio de mensajeria que siempre debe de estar a la escucha
# Debe tener su propio contenedo levantado
# CMD [ "python", "-u", "consumer.py" ]
