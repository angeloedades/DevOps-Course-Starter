import requests
import os
import pdb
from pprint import pprint

trello_api_base_url = "https://api.trello.com"
trello_api_key = os.getenv("TRELLO_KEY")
trello_api_token = os.getenv("TRELLO_TOKEN")

trello_request_parameters = {"key": trello_api_key, "token": trello_api_token}


def generic_request_handler(trello_request_url):
    generic_request = requests.get(trello_api_base_url + trello_request_url, params=trello_request_parameters)

    return generic_request


def get_board(trello_board_id):
    get_board_request = generic_request_handler(f"/1/boards/{trello_board_id}")

    return get_board_request.json()["id"]


def get_board_lists(trello_board_id):
    get_board_lists_requets = generic_request_handler(f"/1/boards/{trello_board_id}/lists")

    return get_board_lists_requets.json()


def get_board_cards(trello_board_id):
    get_board_cards_request = generic_request_handler(f"/1/boards/{trello_board_id}/cards")

    list_of_cards = [card for card in get_board_cards_request.json() if card["name"] != ""]

    pprint(list_of_cards[0])

    return list_of_cards
