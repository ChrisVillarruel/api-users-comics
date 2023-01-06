import json
import pika

from config.db import client as db
from constans import USERNAME_AMQP, PASSWORD_AMQP

cloud_url_rabbitmq = f"amqps://{USERNAME_AMQP}:{PASSWORD_AMQP}@kebnekaise.lmq.cloudamqp.com/qcwoiucd"
params = pika.URLParameters(cloud_url_rabbitmq)
conection = pika.BlockingConnection(params)

channel = conection.channel()
channel.queue_declare(queue="api_users_comics")


def callback(ch, method, properties, body):
    if properties.content_type == "user_login":
        my_db = db["comics"]
        my_collection = my_db["user_comics"]
        data: dict = json.loads(body.decode())

        if my_collection.find_one({"id": data.get("id")}):
            query = {"id": data.get("id")}
            newvalues = {"$set": {'token': data.get("token")}}
            my_collection.update_one(query, newvalues)
        else:
            my_collection.insert_one(json.loads(body.decode()))


channel.basic_consume(queue="api_users_comics", on_message_callback=callback)
print("Started consuming")
channel.start_consuming()
channel.close()
