from pydantic import BaseModel
from typing import Optional
import json
import copy

class Subscription(BaseModel):
    id: Optional[str] = None
    exp_date: str
    manifest: str
    status: str

    def toJSON(self):
        local = copy.copy(self.__dict__)
        local.pop( "id" )
        return local

