import pymongo
import os
import logging
import traceback


DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_SERVER = os.getenv("DB_SERVER")
DB_NAME = os.getenv("DB_NAME")
STATE = os.getenv("STATE")

if __name__ == "__main__":

    try:

        conn_str = "mongodb://{0}:{1}@{2}:27017/{3}".format(
            DB_USER,
            DB_PASS,
            DB_SERVER,
            ""
        )
        
        client = pymongo.MongoClient(conn_str)
        db = client[DB_NAME]

        users = db["users"]

        print("#"*15)
        print("STATE", STATE)
        print("#"*15)

        if STATE == "INSERT":
            users.insert_one({
                "name": "Jose",
                "apellidos": "Ramirez"
            })
            print("Usuario insertado con exito!")
        elif STATE == "READ":
            for u in users.find({}):
                print(u)


    except Exception as e:
        print(str(e))
        print(traceback.format_exc())