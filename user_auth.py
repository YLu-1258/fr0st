# Storing user credentials in a python dictionary
# These users will always be initialized with their given password and high score
from base_64 import encode, decode

user_data = {
    "frst_adm":{"pwd":"ZnIwJDdfRlRX","high_score":100},
    "frst_usr":{"pwd":"bGV0bWVpbg==","high_score":0},
    "alex":{"pwd":"QWV2dXMh","high_score":0}
    }

# VERY INSECURE, idk why I am doing this
def getCredentials():
    return user_data

# Return the password from a given user
def getPwd(usr):
    return decode(user_data[usr]["pwd"])

# Return the password from a given user
def getHighScore(usr):
    return user_data[usr]["high_score"]

# Get the user with the highest score in the current instance of the website
# returns a list
def getChampion():
    hi=0
    champ="placeholder"
    for k, v in user_data.items():
        if v["high_score"] > hi:
            hi = v["high_score"]
            champ = k
    return [champ, hi]

# Appends the user and assigns them a given password, use "password" if no arguments are given (default password)
# Automatically assign a high_score of 0
# If the user already exists, only update the password
def setUser(usr,pwd="password"):
    pwd_encoded = encode(pwd)
    if usr not in user_data.keys():
        user_data[usr] = {"pwd":pwd_encoded,"high_score":0}
    else:
        user_data[usr]["pwd"] = pwd_encoded
    return [usr,pwd,pwd_encoded]

# Sets a new high score, if the user beats their old record
def setScore(usr,score):
    user_data[usr]["high_score"] = score
    return [usr,score]

def verifyLogin(usr,pwd):
    if usr not in user_data.keys():
        return
    else:
        return True if pwd == decode(user_data[usr]["pwd"])  else False

champ = getChampion()[0]

if __name__ == "__main__":
    print("Initial List")
    print("\n-----------------------\n")
    print(getCredentials())
    print("\n-----------------------\n")
    print("Adding user Evan")
    setUser("evan")
    print("Adding user Haseeb")
    setUser("haseeb", "1234")
    print("Updating score for Alex with score of 109")
    setScore("alex", 109)
    print("Current champion is user {0}, with {1} points".format(getChampion()[0],getChampion()[1]))
    print("\n-----------------------\n")
    print("Final List")
    print(getCredentials())
    print("\n-----------------------\n")
    print("Attempting login on user \"alex\" with credentials \"password\" ")
    print(verifyLogin("alex","password"))
    print("Attempting login on user \"alex\" with credentials \"Aevus!\" ")
    print(verifyLogin("alex","Aevus!"))