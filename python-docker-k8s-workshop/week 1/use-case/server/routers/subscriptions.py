from typing import List
from urllib import response
from fastapi import APIRouter
from models.subcription import Subscription
from services.mongo_subscription_service import SubscriptionService

router = APIRouter(
    prefix="/subscriptions",
    responses={404: {"description": "Not found"}},
)

__service = SubscriptionService()

@router.get("/", response_model = List[Subscription])
async def get_subscriptions():
    data = []
    db_subscriptions = __service.get_subscriptions()
    for d in db_subscriptions:
        sub = Subscription(
            id= str( d["_id"] ),
            exp_date=d["exp_date"],
            manifest=d["manifest"],
            status=d["status"]
        )
        data.append(sub)
    return data

@router.post("/")
async def post_subscriptions( sub: Subscription ):
    __service.post_subscription( sub )
    return { "status": "ok" }