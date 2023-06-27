import scrapy
from Example_Book.items import ExampleBookItem

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/category/books/mystery_3"]
    cols=['title','price']
    
    def __init__(self):
        super().__init__()
        self.pg_cnt=0

    def parse(self, response):
        self.pg_cnt+=1

        res=response.css("article.product_pod")
                

        print("[Book Information]")
        for r in res:
            Example_Book=ExampleBookItem()
            btitle = r.css("h3 a::text").get()
            price = r.css("p.price_color::text").get()
            
            Example_Book['title']=btitle
            Example_Book['price']= price
            yield Example_Book
            
        print("[Page count] ",self.pg_cnt)
        next_pg=response.css("li.next a")
        print("Next page Output",next_pg)
        if next_pg:
            next_pg_url=f"{self.start_urls[0]}/{next_pg.attrib['href']}"
            yield scrapy.Request(url=next_pg_url)

        
