import asyncio
import requests
import json


# `Game_id`,
# `Game_name`,
# `Type1`,
# `Type2`,
# `Type3`,
# `Type4`,
# `Type5`,
# `DEVELOPER`
async def post_game(data):
    game_keys = ['Game_id', 'Game_name', 'Type1', 'Type2', 'Type3', 'Type4', 'Type5', 'DEVELOPER']
    req_dict = dict()
    for k in data:
        if k in game_keys:
            req_dict[k] = data[k]
    url = "http://6156game-env.eba-xtamzhzp.us-east-2.elasticbeanstalk.com/Game"
    r = requests.post(url, files=req_dict)
    return r.status_code == 201


# id
# nameLast
# nameFirst
# email
# addressID
async def post_user(data):
    req_dict = dict()
    req_dict['nameLast'] = data['nameLast']
    req_dict['nameFirst'] = data['nameFirst']
    req_dict['email'] = data['email']
    req_dict['id'] = data['user_id']
    req_dict['addressID'] = data['addr_id']

    url = "http://52.15.243.33:5000/users"
    r = requests.post(url, files=req_dict)
    return r.status_code == 201


# id
# streetNo
# streetName1
# streetName2
# city
# region
# countryCode
# postalCode
async def post_addr(data):
    addr_keys = ['streetNo', 'streetName1', 'streetName2', 'city', 'region', 'countryCode', 'postalCode']
    req_dict = dict()
    req_dict['id'] = data['addr_id']
    for k in data:
        if k in addr_keys:
            req_dict[k] = data[k]
    url = "http://52.15.243.33:5000/addresses"
    r = requests.post(url, files=req_dict)
    return r.status_code == 201


# f_id
# title
# content
# userID
# gameID

async def post_forum(data):
    req_dict = dict()
    req_dict['f_id'] = data['f_id']
    req_dict['title'] = data['title']
    req_dict['content'] = data['content']
    req_dict['userID'] = data['user_id']
    req_dict['gameID'] = data['Game_id']

    url = "http://3.140.248.102:5000/forums"
    r = requests.post(url, files=req_dict)
    return r.status_code == 201


class AsyncService:

    def __init__(self):
        pass

    @classmethod
    async def postall(cls, data):
        # await asyncio.gather(post_user(data), post_addr(data), post_game(data), post_forum(data))
        await asyncio.gather(post_user(data), post_addr(data), post_forum(data))
