
from services.interface_subscription_service import ISubscriptionService
from db.mongo_provider import db as mongodb
from models.subcription import Subscription
import json

class SubscriptionService(ISubscriptionService):

    COLLECTION = "subscriptions"
    __db = mongodb[COLLECTION]

    def get_subscriptions(self):
        data = self.__db.find({})
        return data

    def post_subscription(self, subscription: Subscription):
        self.__db.insert_one(subscription.toJSON())