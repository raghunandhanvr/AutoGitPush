import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("PATH")
username = os.getenv("MYUNAME")
password = os.getenv("MYPWORD")

def autopush():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName))
    user = Github(username, password).get_user()
    repo = user.create_repo(folderName)
    print("Successfully {} has created".format(folderName))

if __name__ == "__main__":
    autopush()
