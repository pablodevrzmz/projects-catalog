import pymongo
import os
import logging

from dotenv import load_dotenv
load_dotenv()

__con_str = "mongodb+srv://{0}:{1}@{2}/{3}?retryWrites=true&w=majority".format(
    os.getenv("MONGO_USER"),
    os.getenv("MONGO_PASS"),
    os.getenv("MONGO_SERVER"),
    os.getenv("MONGO_DB"),
)


try:
    __client = pymongo.MongoClient(__con_str)
    db = __client[os.getenv("MONGO_DB")]
except Exception as e:
    logging.info( str(e) )