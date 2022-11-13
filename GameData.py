import json     
def user_won(user_name): 
    user = "won"
    if user == "won":
        with open("text.json",'r') as f:
            sc_data = json.load(f)
            for i in range(len(sc_data)):
                if sc_data[i]["user"] == user_name:
                    sc_data[i]["score"] += 10
                    break
            else:
                score = 10
                score_data = {"user": user_name, "score":score}
                sc_data.append(score_data)
            with open("text.json","w") as sc:
                json.dump(sc_data,sc,indent=4)

def user_lose(user_name):
    user = "lose"
    if user == "lose":
        with open("text.json",'r') as f:
            sc_data = json.load(f)
            for i in range(len(sc_data)):
                if sc_data[i]["user"] == user_name:
                    sc_data[i]["score"] -= 10
                    break
            else:
                score = 0
                score_data = {"user": user_name, "score":score}
                sc_data.append(score_data)
            with open("text.json","w") as sc:
                json.dump(sc_data,sc,indent=4)    

def GameData_main():
    while 1:
        print("Enter 1 to call user_won")
        print("Enter 2 to call user_lose")
        print("Enter q to Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            user_won()
            print("Plus score already")
        elif choice == '2':
            user_lose()
            print("Minus score already")
        elif choice == 'q':
            break
        print("======================")