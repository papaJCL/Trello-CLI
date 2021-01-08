import click
import requests
import json

@click.command()

def cli():
    keys_file = open("keys.txt")
    lines = keys_file.readlines()
    key = lines[0].rstrip()
    token = lines[1].rstrip()
    board = lines[2].rstrip()

    print("Key is " , key)
    print("token is " , token)
    print("board is " , token)

    boardurl = "https://api.trello.com/1/boards/" + board + "/lists"
    labelurl = "https://api.trello.com/1/boards/" + board + "/labels"
    cardUrl = "https://api.trello.com/1/cards"

    query = {
        'key': key,
        'token': token
    }

    boardResponse = requests.request(
        "GET",
        boardurl,
        params=query
    )

    labelResponse = requests.request(
        "GET",
        labelurl,
        params=query
    )

    print(boardResponse)

    print(labelResponse)



