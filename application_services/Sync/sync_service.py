import requests
import json
from flask import Response, request

class SyncService:

    def __init__(self):
        pass

    @classmethod
    def postForum(self, data, game_id=None):
        user_id = data['user_id']
        f_id = data['f_id']
        title = data['title']
        content = data['content']
        # Game_id = data['Game_id']
        if game_id:
            Game_id = game_id
        else:
            Game_id = None
        data_forum_to_create = {"f_id": f_id, "title": title, "content": content, "userID": user_id, "gameID": Game_id}
        url_forum = "http://3.140.248.102:5000/forums"
        r_forum = requests.post(url=url_forum, data=data_forum_to_create)
        if r_forum.status_code == 201:
            return Response(json.dumps({"location": request.path}, default=str, indent=4), status=201,
                               content_type="application/json")
        else:
            return Response(json.dumps({"error":r_forum.status_code}, default=str, indent=4), status=r_forum.status_code,
                               content_type="application/json")

    @classmethod
    def postGame(self,data):
        url_game = "http://6156game-env.eba-xtamzhzp.us-east-2.elasticbeanstalk.com/Game"
        Game_name = data['Game_name']
        DEVELOPER = data['DEVELOPER']
        Type_all = data["G_Type"]

        data_game_to_create = {
            "Game_name": Game_name,
            "G_Type": Type_all,
            "DEVELOPER": DEVELOPER
        }
        r_game = requests.post(url=url_game, data=data_game_to_create)
        if r_game.status_code == 201:
            game_id = int(r_game.text.split(" ")[-1][:-1])
            rsp = Response(json.dumps({"location": request.path}, default=str, indent=4), status=201,
                               content_type="application/json")
            return rsp, game_id
        else:
            return Response(json.dumps({"error":r_forum.status_code}, default=str, indent=4), status=r_forum.status_code,
                               content_type="application/json"), None

    def postall(self, data):
        # TODO
        user_id = data['user_id']
        nameLast = data['nameLast']
        nameFirst = data['nameFirst']
        email = data['email']
        addr_id = data['addr_id']
        streetNo = data['streetNo']
        streetName1 = data['streetName1']
        streetName2 = data['streetName2']
        city = data['city']
        region = data['region']
        countryCode = data['countryCode']
        postalCode = data['postalCode']
        f_id = data['f_id']
        title = data['title']
        content = data['content']
        Game_id = data['Game_id']
        Game_name = data['Game_name']
        Type1 = data['Type1']
        Type2 = data['Type2']
        Type3 = data['Type3']
        Type4 = data['Type4']
        Type5 = data['Type5']
        DEVELOPER = data['DEVELOPER']


        data_user_to_create = {"id": user_id, "nameLast": nameLast, "nameFirst": nameFirst, "email": email,
                       "addressID": addr_id}
        data_address_to_create = {"id": id, "streetNo": streetNo, "streetName1": streetName1, "streetName2": streetName2,
                       "city": city, "region": region, "countryCode": countryCode, "postalCode": postalCode}
        data_forum_to_create = {"f_id":f_id, "title":title, "content": content, "userID": user_id, "gameID": Game_id}
        data_game_to_create = {
            "Game_id": Game_id,
            "Game_name": Game_name,
            "Type1": Type1,
            "Type2": Type2,
            "Type3": Type3,
            "Type4": Type4,
            "Type5": Type5,
            "DEVELOPER": DEVELOPER
        }
        data_game_to_create = json.dumps(data_game_to_create)
        data_user_to_create = json.dumps(data_user_to_create)
        data_forum_to_create = json.dumps(data_forum_to_create)
        data_address_to_create = json.dumps(data_address_to_create)

        url_game = "http://6156game-env.eba-xtamzhzp.us-east-2.elasticbeanstalk.com/Game"
        r_game = requests.post(url=url_game, data=data_game_to_create)

        url_user = "http://52.15.243.33:5000/users"
        r_user = requests.post(url=url_user, data=data_user_to_create)

        url_address = "http://52.15.243.33:5000/addresses"
        r_address = requests.post(url=url_address, data=data_address_to_create)

        url_forum = "http://3.140.248.102:5000/forums"
        r_forum = requests.post(url=url_forum, data=data_forum_to_create)

        return
