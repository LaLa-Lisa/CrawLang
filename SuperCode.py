# config variables
import random
from typing import Optional, List
import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm
import validators

from threading import Thread

class LangMemory:
    mem = [dict()]
    current_index = 0

    @classmethod
    def set_variable(cls, name: str, value):
        cls.mem[cls.current_index][name] = value

    @classmethod
    def get_variable(cls, name: str):
        v = None
        local_index = cls.current_index
        while v is None:
            if len(cls.mem) <= local_index:
                raise ValueError(f'No such variable: {name}')
            v = cls.mem[local_index].get(name)
            local_index -= 1
        return v

    @classmethod
    def go_deeper(cls):
        cls.mem.append(dict())
        cls.current_index += 1

    @classmethod
    def go_upper(cls):
        cls.mem.pop()
        cls.current_index -= 1


class Pool_data:
    def __init__(self, base_url: str):
        self.base_url = "https://" + domain(base_url)
        self.domen_url = domain(base_url)
        self.visited_urls = []
        self.urls_to_visit = [base_url]

        # stats
        self.outer_urls = []
        self.domen_urls = []
        self.non_working_url = []

def is_document(url):
    doc_name = url.split('.')[-1]
    if doc_name.lower() in ['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png', 'djvu', 'bmp', 'raw',
                            'ppt', 'pptx', 'xsl', 'xlsx', 'gif', 'webp', 'zip', 'rar', 'gz',
                            '3gp', 'avi', 'mov', 'mp4', 'm4v', 'm4a', 'mp3', 'mkv', 'ogv', 'ogm',
                            'webm', 'wav', 'txt', 'rtf']:
        return True
    return False

def get_unique_domens(urls):
    s = set()
    for u in urls:
        if len(u) < 8:
            continue
        if u[:7] == 'http://':
            url = u[7:].split('/')[0]
        elif u[:8] == 'https://':
            url = u[8:].split('/')[0]
        elif u[:4] == 'www.':
            url = u.split('/')[0]
        else:
            continue

        if url[:4] == 'www.':
            url = url[4:]

        if '@' in url:
            continue
        s.add(url)
    return list(s)

def get_unique_documents(urls):
    s = set()
    for u in urls:
        if len(u) < 8:
            continue
        if u[:7] == 'http://':
            url = u[7:]
        elif u[:8] == 'https://':
            url = u[8:]
        elif u[:4] == 'www.':
            url = u
        else:
            continue

        if url[:4] == 'www.':
            url = url[4:]

        if '@' in url:
            continue

        if url.split('.')[-1] in ['pdf', 'doc', 'docx']:
            s.add(url)

    return list(s)

def domain(url: str):
    if '/' not in url:
        return url
    url = url.split('/')
    if url[0] == 'https:' or url[1] == 'http:':
        url = url[2]
    else:
        url = url[0]
    if url.startswith('www.'):
        url = url[4:]
    return url

def is_subdomain(url: str, base_url: str) -> bool:
    d1 = domain(base_url)
    d2 = domain(url)
    return (d1 in d2) and (d1 != d2)

def has_subdomain(url: str):
    try:
        html = Crawler.download_url(url)
        j = []
        for u in Crawler.get_linked_urls(url, html):
            if (u is None) or (not validators.url(u)):
                continue
            if is_subdomain(u, url):
                j.append(u)
        if not j:
            return False
        else:
            return random.choice(j)
    except Exception as e:
        return False

class Crawler():
    def __init__(self, group: str, pool_data: Pool_data):
        assert group
        self.__group = group
        self.pool_data = pool_data

    @property
    def group(self):
        return self.__group

    @classmethod
    def download_url(cls, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
        return requests.get(url, headers=headers).text

    @classmethod
    def get_linked_urls(cls, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path

    def add_url_to_visit(self, url):
        if url not in self.pool_data.visited_urls and  url not in self.pool_data.urls_to_visit:
            self.pool_data.urls_to_visit.append(url)

    def crawl(self, url):
        if is_document(url):
            return
        html = self.download_url(url)
        for u in self.get_linked_urls(url, html):
            if (u is None) or (not validators.url(u)):
                self.pool_data.non_working_url.append(u)
                continue
            if self.pool_data.base_url in u:
                self.add_url_to_visit(u)
            else:
                if self.pool_data.domen_url in u:
                    self.pool_data.domen_urls.append(u)
                else:
                    self.pool_data.outer_urls.append(u)

    def run(self):
        t_start = time.time()
        # tqdm_ = tqdm()
        while self.pool_data.urls_to_visit:
            if time.time() - t_start > 66666*60 * 10:
                break
            # tqdm_.update(1)
            url = self.pool_data.urls_to_visit.pop(0)
            logging.info(f'Crawling: {url}')
            try:
                self.crawl(url)
            except Exception:
                logging.exception(f'Failed to crawl: {url}')
                self.pool_data.non_working_url.append(url)
            finally:
                self.pool_data.visited_urls.append(url)
                logging.info(f'Rest: {len(self.pool_data.urls_to_visit)}')


def print_all_stats():
    for group_name, pool in CRAWLERS.CRAWLERS.items():
        print('[================================' + group_name + '================================]')
        pool.print_stats()
        print('[================================' + '=' * len(group_name) + '================================]')


class CrawlerPool:
    def __init__(self, url: str, group: str, count: int):
        assert group
        assert url
        assert count > 0
        self.url = url
        self.group = group
        self.count = count
        self.pool_data = Pool_data(url)
        self.current_index = -1
        self.crawlers = []
        for i in range(self.count):
            new_crawler = Crawler(group, self.pool_data)
            self.crawlers.append(new_crawler)

    def run(self):
        ths = []
        for i in self.crawlers:
            th = Thread(target=i.run, daemon=True)
            ths.append(th)
            th.start()

        for i in ths:
            i.join()

    def print_stats(self):
        print("were visited", len(self.pool_data.visited_urls))
        print("not visited, but want to", len(self.pool_data.urls_to_visit))
        print("all inner domens urls: ", len(self.pool_data.domen_urls))
        print("all outer domens urls: ", len(self.pool_data.outer_urls))
        du = get_unique_domens(self.pool_data.domen_urls)
        print("unique inner domens urls: ", len(du), du)
        ou = get_unique_domens(self.pool_data.outer_urls)
        print("unique outer domens urls: ", len(ou), ou)

        ddu = get_unique_documents(self.pool_data.domen_urls)
        print("unique documents urls: ", len(ddu), ddu)

        print("total number of pages and all links",
              len(self.pool_data.visited_urls) + len(self.pool_data.urls_to_visit) + len(self.pool_data.domen_urls) + len(self.pool_data.outer_urls))
        print("number of internal pages", len(self.pool_data.visited_urls) + len(self.pool_data.urls_to_visit))
        print("number of internal subdomains (unique)", len(du))
        print("total number of links to external resources", len(self.pool_data.outer_urls))
        print("number of unique external resources", len(ou))
        print("number of unique links to doc/docx/pdf files", len(ddu))
        print("number of broken pages", len(self.pool_data.non_working_url), "unique",
              len(set(self.pool_data.non_working_url)))


class CRAWLERS:
    CRAWLERS: dict[str: CrawlerPool] = dict()

def get_pool_crawlers(group: str) -> Optional[CrawlerPool]:
    return CRAWLERS.CRAWLERS.get(group, None)

def get_group_crawlers(group: str) -> List[Crawler]:
    pool = get_pool_crawlers(group)
    if pool:
        return pool.crawlers
    return []

def get_list_groups() -> List[str]:
    return list(CRAWLERS.CRAWLERS.keys())



class SiteObject:
    def __init__(self, url: str, group: str, count: int):
        assert count > 0
        assert group
        assert url
        # check(url)

        if not get_pool_crawlers(group):
            CRAWLERS.CRAWLERS[group] = CrawlerPool(url, group, count)

        self.Pool: CrawlerPool = CRAWLERS.CRAWLERS[group]
        self.group = self.Pool.group
        self.count = self.Pool.count

        th1 = Thread(target=self.Pool.run, daemon=True)
        th1.start()


    def get_next_url(self) -> str:
        self.Pool.current_index += 1
        while (len(self.Pool.pool_data.visited_urls) <= self.Pool.current_index) and self.Pool.pool_data.urls_to_visit:
            pass
        if (len(self.Pool.pool_data.visited_urls) <= self.Pool.current_index):
            return "Done"
        return self.Pool.pool_data.visited_urls[self.Pool.current_index]




def _next(site_object: SiteObject) -> str:
    return site_object.get_next_url()


def site(url: str, group: str, count: int):
    b = SiteObject(url, group, count)
    time.sleep(5)
    return b


"""
base_url = "https://msu.ru";
start_url = site(base_url, group='Start_group', size=4);
for (i = 0; i < 100000; i = i + 1;) {
    url = next(start_url);
    if (is_subdomain(url, base_url)) {
        base_url_new = domain(url);
        start_url2 = site(base_url_new, group=base_url_new, size=3);
        for (j = 0; j < 100000; j = j + 1;) {
            url2 = next(start_url2);
        }
    }
}
"""

def main():
    base_url = "https://spbu.ru/universitet/uchebno-nauchnye-podrazdeleniya"
    start_url = site(base_url, group='Start_group', count=3)
    for i in range(3):
        url = _next(start_url)

        print('я посетил внешний сайтик', url)
        l = has_subdomain(url)
        if l:
            base_url_new = "https://" + domain(l)
            start_url2 = site(base_url_new, group=base_url_new, count=2)
            for j in range(50):
                url2 = _next(start_url2)

                print('я посетил внутренний сайтик', url2)

    print_all_stats()


if __name__ == '__main__':
    main()
