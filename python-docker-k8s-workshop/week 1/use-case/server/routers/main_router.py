from fastapi import APIRouter
import routers.subscriptions as subscriptions
import routers.liveness as liveness

router = APIRouter()
router.include_router(subscriptions.router)
router.include_router(liveness.router)