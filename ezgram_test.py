# test.py


from EzGram import EzGram
import json
import os
from EzGram.tools import DateTimeEncoder

settings_file = "jacecall.json"
# Instantiate the EzGram object
ezgram = EzGram("jacecall", "1Wasatch!", "jacecall@deepturn.com", "Wigwam01!")
# ezgram = EzGram("larzrandana", "1Wasatch!", "jacecall@deepturn.com", "Wigwam01!")

# Log in to Instagram
client = ezgram.account.login()
login_info = ezgram.account.login_info()

# Check if the file exists
if not os.path.exists(settings_file):
    # with open(settings_file, 'w') as json_file:
    #     # Write the data to the file
    #     json.dump(resp, json_file)

    with open(settings_file, "w") as file:
        json.dump(login_info, file, cls=DateTimeEncoder)
        print(f"Created {settings_file}")


print("[ LOGIN RESPONSE ]", login_info)
ezgram.account.logout()
