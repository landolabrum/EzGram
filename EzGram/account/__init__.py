import email
import imaplib
import re
import random

from instagrapi.mixins.challenge import ChallengeChoice

CHALLENGE_EMAIL = "larzrandana@deepturn.com"
CHALLENGE_PASSWORD = "eteyytvwymbsdyxb"


class Account(object):
    def __init__(self, ezgram):
        self.ezgram = ezgram
        self.api = ezgram.api
        self.api.challenge_code_handler = self.challenge_code_handler
        self.api.change_password_handler = self.change_password_handler

    def get_code_from_email(self, username):
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(CHALLENGE_EMAIL, CHALLENGE_PASSWORD)
        mail.select("inbox")
        result, data = mail.search(None, "(UNSEEN)")
        assert result == "OK", "Error1 during get_code_from_email: %s" % result
        ids = data.pop().split()
        for num in reversed(ids):
            mail.store(num, "+FLAGS", "\\Seen")  # mark as read
            result, data = mail.fetch(num, "(RFC822)")
            assert result == "OK", "Error2 during get_code_from_email: %s" % result
            msg = email.message_from_string(data[0][1].decode())
            payloads = msg.get_payload()
            if not isinstance(payloads, list):
                payloads = [msg]
            code = None
            for payload in payloads:
                body = payload.get_payload(decode=True).decode()
                if "<div" not in body:
                    continue
                match = re.search(
                    ">([^>]*?({u})[^<]*?)<".format(u=username), body)
                if not match:
                    continue
                print("Match from email:", match.group(1))
                match = re.search(r">(\d{6})<", body)
                if not match:
                    print('Skip this email, "code" not found')
                    continue
                code = match.group(1)
                if code:
                    return code
        return False

    def get_code_from_sms(self, username):
        while True:
            code = input(f"Enter code (6 digits) for {username}: ").strip()
            if code and code.isdigit():
                return code
        return None

    def challenge_code_handler(self, username, choice):
        if choice == ChallengeChoice.SMS:
            return self.get_code_from_sms(username)
        elif choice == ChallengeChoice.EMAIL:
            return self.get_code_from_email(username)
        return False

    def change_password_handler(self, username):
        # Simple way to generate a random string
        chars = list("abcdefghijklmnopqrstuvwxyz1234567890!&£@#")
        password = "".join(random.sample(chars, 10))
        return password

    def login(self, enable_2fa=False):
        # print(
        #     f"Username: {self.ezgram.username}, Password: {self.ezgram.password}")
        self.api.login(self.ezgram.username, self.ezgram.password)
        return {
            "inbox": self.api.news_inbox_v1(),
            "account":  self.api.account_info().__dict__
        }

    def login_info(self):
        login_info = self.api.login_info()
        return login_info

    def edit_profile(self, **kwargs):
        profile_info = self.api.account_edit(**kwargs)
        return profile_info

    def change_password(self, old_password, new_password):
        self.api.change_password(old_password, new_password)

    def two_factor(self, enable=False, identifier=None, method='email'):
        if enable:
            if identifier is None:
                identifier = self.api.username

            self.api.request_challenge_code(method, identifier=identifier)
            code = input("Enter the verification code: ")
            self.api.verify_request_challenge_code(code, identifier=identifier)

        else:
            self.api.disable_two_factor()

    def logout(self):
        self.api.logout()
        self.api = None

    def news_inbox_v1(self, mark_as_seen=False):
        inbox = self.api.news_inbox_v1(mark_as_seen=mark_as_seen)
        return inbox

    def account_info(self):
        # print("[ ACOUNT OMFP ]", vars(vars(self)['ezgram']), vars(vars(self)['api']))
        return self.api.account_info(self.ezgram.authenticated_user_id)
