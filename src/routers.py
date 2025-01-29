from fastapi import Depends, APIRouter, HTTPException
from .calls import about_influencer_call
import json

router = APIRouter(prefix="/post",
                   tags=["post"])

@router.get("/")
def test():
    return{"message": "penis balls"}

@router.get("/ai/{name}")
def run_search(name:str):
    data = about_influencer_call(name)
    jdata = json.loads(data)
    return {"data": jdata}