import requests,json
class SyncService:

    def __init__(self):
        pass

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


        data_user_to_create = {"user_id": user_id, "nameLast": nameLast, "nameFirst": nameFirst, "email": email,
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

        r_game = requests.post(url='/Game', data=data_game_to_create,
                      headers={})
        r_user = requests.post(url='/users', data=data_user_to_create,
                               headers={})
        r_address = requests.post(url='/addresses', data=data_address_to_create,
                               headers={})
        r_forum = requests.post(url='/forums', data=data_forum_to_create,
                               headers={})

        return
