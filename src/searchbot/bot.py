from typing import Optional
from urllib.parse import quote_plus

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


# 获取页面body内容
def retrieve_content(item, verbose):
    url = item['url']
    title = item['title']
    try:
        if verbose:
            print(f"retrieving content from {title}")
        response = requests.get(url, headers=headers, timeout=5)
        response.encoding = 'utf-8'  # 设置编码
        response.raise_for_status()  # 检查请求是否成功
        soup = BeautifulSoup(response.text, 'html.parser')
        return f"{soup.get_text(strip=True)}\nOriginURL: {url}"  # 获取文本并去除空白字符
    except Exception as e:
        if verbose:
            print(f"failed to retrieve content from {title}: {e}")
        return ""


# 抓取页面列表
def retrieve_pages(links: list, verbose=False) -> str:
    with ThreadPoolExecutor(max_workers=len(links)) as executor:
        contents = list(executor.map(lambda item: retrieve_content(item, verbose=verbose), links))
    return "\n".join(contents)


class SearchBot:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def search(self, query: str) -> Optional[str]:
        links = self.retrieve_urls(query)
        if len(links) == 0:
            return None
        contents = retrieve_pages(links, verbose=self.verbose)
        if self.verbose:
            print(f"search completed, context length: {len(contents)} characters\nGenerating...")
        return contents

    def retrieve_urls(self, query: str) -> list:
        pass


class BingSearchBot(SearchBot):
    def retrieve_urls(self, query: str) -> list:
        encoded_query = quote_plus(query)
        url = f"https://www.bing.com/search?q={encoded_query}"
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        body = soup.get_text(strip=True)
        if "blocked" in body:
            raise Exception("Blocked by Bing")

        results = []
        for item in soup.select('.b_algo h2 a'):
            title = item.get_text(strip=True)
            link = item['href']
            results.append({'title': title, 'url': link})
        if len(results) == 0:
            return []
        if self.verbose:
            print(f"searched {len(results)} results")
        return results


class BaiduSearchBot(SearchBot):
    def retrieve_urls(self, query: str) -> list:
        encoded_query = quote_plus(query)
        url = f"https://www.baidu.com/s?wd={encoded_query}"
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        for item in soup.select('h3.c-title a'):
            title = item.get_text(strip=True)
            link = item['href']
            results.append({'title': title, 'url': link})
        if len(results) == 0:
            return []
        if self.verbose:
            print(f"searched {len(results)} results")
        return results


def make_bot(name: str, verbose=True) -> SearchBot:
    if name == "bing":
        return BingSearchBot(verbose=verbose)
    elif name == "baidu":
        return BaiduSearchBot(verbose=verbose)
    else:
        raise ValueError(f"Unsupported search engine: {name}")
