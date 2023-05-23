import json
import sys
import os
import time
# Add the parent directory to the Python module search path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from EzGram import EzGram




def main():
    # Create an instance of EzGram
    ezgram = EzGram(username="larzrandana", password="1Wasatch!")

    # Log in to the account
    account = ezgram.account.login()
    print("[ ACCOUNT ]", json.dumps(account))
    time.sleep(3)
    # # Perform actions with EzGram
    # # Example: Sending direct messages
    # ezgram.direct_messages.send(
    #     user_id="123456789",
    #     message="Hello, this is a test message!"
    # )

    # Log out of the account
    ezgram.account.logout()

if __name__ == "__main__":
    main()