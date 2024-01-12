# Search Engine functionality

import requests
from collections import deque, defaultdict
from html.parser import HTMLParser


# Components
# SearchEngine: Main container for all the other components
# WebsiteMatcher: matches to_search against websites
# WebsiteFetcher: Gets the html for a given URL
# RefFetcher: Gets links from html
# ContentFetcher: Gets string content from html
# WebsiteUniverse: Structure holding websites and their relationships
# WebsiteDirectoryTree (WDT): Structure for holding a domain website and its webpages (children)
# WebsiteUniverseStorage: Storage were WebsiteUniverse will be persisted.


class SearchEngine:
    pass


class WebsiteMatcher:
    pass


class WebsiteFetcher:

    def __init__(self):
        pass

    def get_external_links(self, url):
        links = self.get_links(url)
        return []

    # TODO: How to improve the except being too broad?
    def get_content(self, url):
        content = ''
        try:
            res = requests.get(url)
            content = res.content
        except:
            pass
        return content

    def get_links(self, url):
        content = self.get_content(url)

        return []


class RefFetcher:
    pass


class ContentFetcher:
    pass


class WebsiteUniverse:
    SEED = 'https://es.wikipedia.org/'
    LIMIT = 100

    def __init__(self):
        self.websites = self.__load_web_universe()
        if not self.websites:
            self.websites = self.__generate_web_universe()

    def __generate_web_universe(self):
        websites = defaultdict(WebsiteDirectoryTree)
        queue = deque([self.SEED])
        # Getting the class method outside of loop makes it faster
        get_external_links = WebsiteFetcher.get_external_links
        while len(queue) > 0:
            website_url = queue.popleft()
            if website_url in websites:
                continue
            external_links = get_external_links(website_url)
            websites[website_url] = WebsiteDirectoryTree(website_url)
            queue.extend(external_links[:self.LIMIT])
        return websites

    # TODO: Implement the actual attempt to load from storage
    def __load_web_universe(self):
        return {}


# TODO: Implement the actual Tree data structure for a complete Website!
class WebsiteDirectoryTree:

    def __init__(self, url):
        self.url = url


class WebsiteUniverseStorage:
    pass


def search(to_search: str) -> list[str]:
    """
    Search a string content in the web and return a list of url matches.
    """
    return []
