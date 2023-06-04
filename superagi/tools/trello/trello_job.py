from typing import Type, List
from pydantic import BaseModel, Field

from superagi.helper.trello_job import TrelloJobWrap
from superagi.tools.base_tool import BaseTool
from superagi.config.config import get_config



class TrelloJobSchema(BaseModel):
    query: str = Field(
        ...,
        description="The job card details.",
    )


class TrelloJobTool(BaseTool):
    name = "TrelloJob"
    description = (
        "A tool to create Card in Trello Board with deadline"
    )
    args_schema: Type[TrelloJobSchema] = TrelloJobSchema

    def _execute(self, query: str) -> tuple:

        trello_api_key=get_config('trello_api_key')
        trello_token=get_config('trello_token')
        application_list_id=get_config('application_list_id')
        cardName=get_config('cardName')
        dueDate=get_config('dueDate')

        print('test',cardName)

        trello_job_create = TrelloJobWrap(trello_api_key, trello_token, application_list_id, cardName, dueDate)
        result = trello_job_create.create_job_card()

        return result