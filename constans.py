from decouple import config

# MongoDb Atlas access database
USERNAME = config("USERNAME_DB")
PASSWORD = config("PASSWORD")
DATABASE = config("DATABASE")

# URL CloudAMQP Access
USERNAME_AMQP = config("USERNAME_AMQP")
PASSWORD_AMQP = config("PASSWORD_AMQP")
