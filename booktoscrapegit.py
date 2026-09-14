import requests
from bs4 import BeautifulSoup

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Wed, 08 Feb 2023 21:02:32 GMT',
    'if-none-match': 'W/"63e40de8-c85e"',
    'priority': 'u=0, i',
    'referer': 'https://www.bing.com/',
    'sec-ch-ua': '"Microsoft Edge";v="153", "Not_A Brand";v="8", "Chromium";v="153"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0',
}

pages=[]
x="https://books.toscrape.com/catalogue/category/books_1/page-"
for i in range(1,51):
    pages.append(x+str(i)+".html")
list1=[]
list2=[]
for i in pages:
    response=requests.get(i,headers=headers)
    # print(response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())

    articles=soup.find_all('article', class_='product_pod')

# print("Total Books:", len(articles))
    for article in articles:
        a_tag=article.find("h3").find("a")
        book_name=a_tag.get("title")
        list1.append(book_name)
        b_tag=article.find("div",class_="product_price").find("p")
        book_price=b_tag.text.strip()
        list2.append(book_price)
print(len(list1))
print(len(list2))