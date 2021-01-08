import click
import requests
import json

def read_file(file):
    keys_file = open(file)
    
    lines = keys_file.readlines()
    key = lines[0].rstrip()
    token = lines[1].rstrip()
    board = lines[2].rstrip()

    return key, token, board

def getURLs(boardID):

    boardUrl = "https://api.trello.com/1/boards/" + boardID + "/lists"
    labelUrl = "https://api.trello.com/1/boards/" + boardID + "/labels"
    cardUrl = "https://api.trello.com/1/cards"

    return boardUrl, labelUrl, cardUrl

def basicQuery(key, token):
    query = {
        'key': key,
        'token': token
    }
    return query

def getRequest(URL, query):
    boardResponse = requests.request(
        "GET",
        URL,
        params=query
    )
    return boardResponse

def checkRequest(request, typeofRequest):
    if request.ok:
        print("Successfully connected to " + typeofRequest + " API " )
    else:
        print ('Could not connect to API!')

def postQuery(key, token, column, comments, idLabelsArray):
    postQuery = {
        'key': key,
        'token': token,
        'idList': column,
        'name': comments,
        'idLabels': idLabelsArray
    }
    return postQuery

def postResponse(cardURL, listQuery):
    postRequest = requests.request(
        "POST",
        cardURL,
        params=listQuery
    )
    return postRequest
    

@click.command()
def main():

    key, token, board = read_file("keys.txt")

    boardURL, labelURL, cardURL = getURLs(board)

    query = basicQuery(key, token)

    boardResponse = getRequest(boardURL, query)

    labelResponse = getRequest(labelURL, query)

    checkRequest(boardResponse, "board")

    checkRequest(labelResponse, "label")

    print('Below are a list of columns you can add a card too')

    boardResponse_data = boardResponse.json()
    for i in boardResponse_data:
        print('Name: ' + i['name'] + '\t' + 'ID : ' + i['id'])

    column = click.prompt(
        'Please enter the ID # corresponding with the column you want to add to')
    comments = click.prompt('Type in what comments you want to add')

    print('Below are a list that show what labels you can add')

    labelResponse_data = labelResponse.json()
    for i in labelResponse_data:
        print('Name: ' + i['name'] + '\t\t\t' + 'ID : ' + i['id'] + '\t\t')

    labels = click.prompt(
        'Please enter the ID #s corresponding with the label you want added seperated by commas')
  
    idLabelsArray = []
    x = labels.split(',')
    for i in range(len(x)):  
        idLabelsArray.append([x[i].replace(' ','')])

    listQuery = postQuery(key, token, column, comments, idLabelsArray)

    addingCardPost = postResponse(cardURL, listQuery)

    checkRequest(addingCardPost , "adding to card")

# ---------------------------------------------------------------
@click.group()
def cli():
    pass

main()
