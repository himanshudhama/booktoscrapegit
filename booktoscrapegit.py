import requests
from bs4 import BeautifulSoup
pages=[]
x="https://books.toscrape.com/catalogue/category/books_1/page-"
for i in range(1,51):
    pages.append(x+str(i)+".html")
list1=[]
list2=[]
for i in pages:
    response=requests.get(i)
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