def newSQLfile():
    print("Generate New SQL databse sequence placeholder")

def OpenSettingsWindow():
    print("Open the Settings Window (lock the main one)")
    
import pickle

savedata = {
    "0": {
        "password": "",
        "keybind": "Tab",
        "counter": 2,
        "rollover": True,
        "theme": "vista"
    },
    "1": {
        "name": "Google",
        "login": "michal",
        "password": "bak"
    },
    "2": {
        "name": "FaceBook",
        "login": "michal2",
        "password": "bak2"
    }
}

with open('filename.pickle', 'wb') as handle:
    pickle.dump(savedata, handle)

with open('filename.pickle', 'rb') as handle:
    b = pickle.load(handle)



print(b)
print("Finished")


exit()