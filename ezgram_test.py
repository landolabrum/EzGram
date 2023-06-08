# test.py


from EzGram import EzGram
import json
import os
from EzGram.tools import DateTimeEncoder

settings_file = "jacecall2.json"
# Instantiate the EzGram object
ezgram = EzGram("jacecall", "1Wasatch!", "jacecall@deepturn.com", "Wigwam01!")
# ezgram = EzGram("larzrandana", "1Wasatch!", "jacecall@deepturn.com", "Wigwam01!")

# Log in to Instagram
client = ezgram.account.login()
resp = ezgram.account.login_response()

# Check if the file exists
if not os.path.exists(settings_file):
    # with open(settings_file, 'w') as json_file:
    #     # Write the data to the file
    #     json.dump(resp, json_file)

    with open(settings_file, "w") as file:
        json.dump(resp, file, cls=DateTimeEncoder)
        print(f"Created {settings_file}")


print("[ LOGIN RESPONSE ]", resp)
ezgram.account.logout()
