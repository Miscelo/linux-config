i#!/usr/bin/env python3

# A simple script to create a valid username.


def checkusername(username):
        assert type(username) == str, "ERROR: Username must be letters or numbers."
        #assert len(username) >=2, "ERROR: Username must be have at least 1 character."


def createuser():
    while(True):
        try:
            username = input("Username: ")
            checkusername(username)
            break
        except Exception as e:
            print("{}: Please choose another username!".format(e))
    print("Your username is {}!".format(username))

if __name__ == "__main__":
    createuser()

