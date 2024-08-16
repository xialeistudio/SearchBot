# SearchBot

该项目是一个由 AI 驱动的信息检索助手，帮助用户根据提供的上下文回答问题。它支持多种搜索机器人和语言，提供灵活且准确的信息检索。

## 支持的机器人

- 百度
- 必应

## 支持的语言

- 中文
- 英文

## 示例用法
```bash
pip install searchbot
```

```python
from searchbot.rag import search

query = "法国的首都是哪里？"
bot_name = "bing"
lang = "chinese"
verbose = True

answer = search(query, bot_name=bot_name, lang=lang, verbose=verbose)
print(answer)
```

Verbose Output:
```text
searched 9 results
retrieving content from 法国(法兰西共和国) - 百度百科
retrieving content from 法国的首都是什么?_百度教育
retrieving content from 法国的首都是哪里-爱问教育
retrieving content from 法国的首都是( )A.伦敦B.巴黎C.罗马D.柏林 题目和参考答案...
retrieving content from 法国“文化首都”竟不是巴黎?这9座城市“杀”疯了!|勒芒|...
retrieving content from 落地法国第一站戴高乐机场|看完这篇不迷路,最全攻略拿走吧
retrieving content from 法国最佳求学城市大盘点!巴黎竟然不是第一名 - 知乎
retrieving content from 波城大学——一所开放的大学!
retrieving content from 图文解读法国地理和历史(法国最全地图收藏) - 知乎
search completed, context length: 55657 characters
Generating...
法国的首都是巴黎。
```