from typing import Optional

from langchain_core.runnables import Runnable, RunnableConfig
from langchain_core.runnables.utils import Input, Output

from . import bot as botmodule


class SearchBotRetriever(Runnable):
    def __init__(self, bot: botmodule.SearchBot):
        self.bot = bot

    def retrieve(self, query: str):
        return self.bot.search(query)

    def invoke(self, input: Input, config: Optional[RunnableConfig] = None) -> Output:
        return self.retrieve(input)
