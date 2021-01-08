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

    if boardResponse.ok:
        print("Successfully connected to board API " , boardResponse)
    else:
        print ('Could not connect to board API!')

    if labelResponse.ok:
        print("Successfully connected to label API" , labelResponse)
    else:
        print ('Could not connect to label API!')


    print('Below are a list of columns you can add a card too')

    boardResponse_data = boardResponse.json()
    for i in boardResponse_data:
        print('Name: ' + i['name'] + '\t' + 'ID : ' + i['id'])

    column = click.prompt(
        'Please enter the ID # corresponding with the column you want to add to')
    comments = click.prompt('Type in what comments you want to add')




