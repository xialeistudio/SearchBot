import sys

sys.path.append('..')

from rag import search

result = search("What's the weather in Beijing today?", bot_name='baidu', lang='english', verbose=True)
print(result)
