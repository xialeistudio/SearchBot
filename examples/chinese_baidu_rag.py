import sys
sys.path.append('..')

from src import search

result = search("北京今天是什么天气?", bot_name='baidu', lang='chinese', verbose=True)
print(result)
