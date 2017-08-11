# encoding=utf-8
"""
coding for scraping html script and retrieving elements from it
"""
import requests
import bs4


def read_html(url):
    response = requests.get(url)
    return response.content


def read_html_withproxy(url):
    proxies = {
        "http": "http://localhost:1080",
        "https": "http://localhost:1080",
    }
    r = requests.get(url, proxies=proxies)
    return r.content


def retrieve_dom(html_str, dom_selector):
    soup = bs4.BeautifulSoup(html_str, "html.parser")
    return soup.select(dom_selector)


def get_baidulinks(url):
    print 'www.baidu.com ----------------'
    html_str = read_html(url)
    links = []
    for a in retrieve_dom(html_str, 'div#u1 a'):
        links.append(dict(name=a.get('name'), href=a.get('href'), text=a.get_text()))
    return links


def get_pyvideos(url):
    print 'pyvideo/scipy-2017 ----------------'
    html_str = read_html(url)
    article_selector = 'div.container div.content-list article'
    articles = retrieve_dom(html_str, article_selector)
    videos = []
    for a in articles:
        img = a.find('img')
        link = img.find_parent('a').get('href')
        title = a.find('section').find("h4").find('a').get('title')
        author = a.find('section').find('footer').find('address').find('a').get_text()
        date = a.find('section').find('footer').find('time').get('datetime')
        videos.append(dict(title=title, img=img.get('src'), author=author, link=link, date=date))
    return videos

def youtube_videos():
    html = read_html_withproxy('https://www.youtube.com/')
    print html
    print '------------------------------------'
    sections = []
    section_selector = 'div#feed-main-what_to_watch ol.item-section'
    topic_selector = "div.shelf-title-table div.shelf-title-row h2.shelf-title-cell span.branded-page-module-title-text"
    for topic in retrieve_dom(html, ("%s %s" % (section_selector, topic_selector))):
        print topic
    for s in sections:
        print s

if __name__ == "__main__":
    youtube_videos()

    '''
    links = get_baidulinks('https://www.baidu.com')
    for l in links:
        print l

    videos = get_pyvideos('http://pyvideo.org/events/scipy-2017.html')
    for v in videos:
        print v
    '''
