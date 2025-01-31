from fastapi import Depends, APIRouter, HTTPException
from .calls import about_influencer_call, influencer_leaderboard, get_claims
import json

router = APIRouter(prefix="/post",
                   tags=["post"])

@router.get("/")
def test():
    return{"message": "hello world"}

@router.get("/ai/{name}")
def run_search(name:str):
    data = about_influencer_call(name)
    claims = get_claims(name)
    jclaims = json.loads(claims)
    jdata = json.loads(data)
    return {"data": jdata, "claims": jclaims}

@router.get("/LB")
def get_leaderboard():
    data = influencer_leaderboard()
    jdata = json.loads(data)
    return {"data": jdata}

