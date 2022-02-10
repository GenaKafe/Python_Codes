print()
print("Welcome to Your Restaurant!")
print()
print("MENU")
print("""
Press 1 for entering the "FOOD" section.
Press 2 for entering the "DRINKS" section. 
Press 0 to return to the main menu. 
""") # main or previous menu? 

# 0. Phase: Annehmen # 1. Phase: User inputs

user = {"id": 1 , "first_name": "Thomas", "last_name": "Meier"}
print(user, type(user))

test_dic = {1 : "A", 2: "B"}
print(test_dic)

food = {
    "Pizza" : [["Margarita", 5] , ["Tuna fish", 6] , ["Salami", 7] ],
    "Auflauf" : ["Casserole", 1,5] , ["Pasta", 2] ,
    "Salat" : ["Regular", 2] , 
} 

drinks = {
    "Cold" : [["Water", 1]] , ["Cola", 2] , ["Fanta" , 3]],
    "Hot" : [["Tea", 1] , ["Coffee", 2]] ,     
}

# Desserts - they could be added to the dictionary easily in the future 

# TODO : exit point to return to the main menu
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




customer_choice = [] # it might have many orders
while True: 
    customer_choice = int(input("Select a number: "))
    if customer_choice == "1":
        print("FOOD")  # to substitute with dictionary FOOD
    elif customer_choice == "2":
        print("DRINKS") # to substitute with dictionary DRINKS
    elif customer_choice == "0":
        break
    else: 
        print("Sorry, wrong entry. Please try again.")




# 2. Phase: Calculations for the bill

# 3. Phase: Print the total 