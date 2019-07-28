from tinymongo import TinyMongoClient
from tinymongo.serializers import DateTimeSerializer
from tinydb_serialization import SerializationMiddleware


class CustomClient(TinyMongoClient):
    @property
    def _storage(self):
        serialization = SerializationMiddleware()
        serialization.register_serializer(DateTimeSerializer(), "TinyDate")
        return serialization


conn = CustomClient()

db = conn.monitor
collection = db.log
