import requests
import json

from superagi.helper.webpage_extractor import WebpageExtractor


class TrelloJobWrap:

    def __init__(self, trello_api_key, trello_token, application_list_id, cardName, dueDate):
        self.trello_endpoint="https://api.trello.com/1/"
        self.trello_api_key = trello_api_key
        self.trello_token = trello_token
        self.application_list_id = application_list_id
        self.cardName = cardName
        self.dueDate = dueDate

    def create_job_card(self):
        create_card_url=self.trello_endpoint+'cards'
        jsonObj={'key':self.trello_api_key,'token':self.trello_token,'idList':self.application_list_id,'name':self.cardName,'due':self.dueDate}
        new_card=requests.post(create_card_url,json=jsonObj)
        results=json.loads(new_card.text)

        return results
    



