user_data = {
    "id":1, 
    "first_name" : "Thomas", 
    "last_name" : "Meier", 
    "cars" : ["Audi", "VW", "Tesla"], 
    "kids1" : ["Lena", "Jana", "Julia"],
    "kids2" : [ ["Lena", 8] , ["Jana", 10] , ["Julia", 12] ], 
    "kids3" : [
                {
                    "first_name": "Lena", 
                    "age" : 8, 
                    "friends": ["Sara", "Gena"]
                }, 
                {
                    "first_name": "Jana",
                    "age" :  10, 
                    "friends" : ["Richelle", "Dirk"]
                }, 
                {
                    "first_name" : "Julia",
                    "age" : 12
                },
              ],
}



print(user_data["first_name"]) # Thomas
print(user_data["kids1"]) # ['Lena', 'Jana', 'Julia'] List
print(user_data["kids2"][1][1]) # 10
print(user_data["kids3"][0]["friends"]) # ["Sara", "Gena"]
print(user_data["kids3"][1]["friends"][1]) # "Dirk"
print(user_data["kids3"][2]["age"]) # 12
print(user_data["kids3"][1]["friends"][0]) # Richelle