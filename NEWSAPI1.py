from newsapi import NewsApiClient
import os


results = []
results1 = []
results2 = []
results3 = []
results4 = []
results5 = []
results6 = []
results7 = []
results8 = []
results9 = []

alt_message = ""     


x1=[]
x2=[]
x3=[]
x4=[]
x5=[]
x6=[]
x7=[]
x8=[]
x9=[]
x10=[]
my_secret = "991a2264e9284a9f92013f63450f97b9"
def get_tech_news():
    global all_articles,x1
    

    print("TODAY'S TOP TECH NEWS ARE AS FOLLOWS : \n")

    api = NewsApiClient(api_key= my_secret)

    tech_news = api.get_top_headlines(category="technology",page_size=10)
    all_articles = tech_news["articles"]
    for ar in all_articles:
        results.append(ar["publishedAt"][11:16]+"  :  **"+ar["title"] + "**  :  " + "[LINK](" + ar["url"] + ")")

    if len(x1)!=0:
      x1=[]
      for i in range(len(results)):
          x1.append(str(str(i+1)+ ") "+ results[i]))
    else:
      for i in range(len(results)):
          x1.append(str(str(i+1)+ ") "+ results[i]))


def get_business_news():
    global x2

    print("TODAY'S TOP BUSINESS NEWS ARE AS FOLLOWS : \n")

    api = NewsApiClient(api_key=my_secret)

    tech_news = api.get_top_headlines(category="business",page_size=10)
    all_articles = tech_news["articles"]
    for ar in all_articles:
        results1.append(ar["publishedAt"][11:16]+"  :  **"+ar["title"] + "**  :  " + "[LINK](" + ar["url"] + ")")



    if len(x2)!=0:
      x2=[]
      for i in range(len(results1)):
          x2.append(str(str(i+1)+ ") "+ results1[i]))
    else:
      for i in range(len(results1)):
          x2.append(str(str(i+1)+ ") "+ results1[i]))



def get_entertainment_news():
    global x3
    print("TODAY'S TOP ENTERTAINMENT NEWS ARE AS FOLLOWS : \n")

    api = NewsApiClient(api_key=my_secret)

    tech_news = api.get_top_headlines(category="entertainment",page_size=10)
    all_articles = tech_news["articles"]
    for ar in all_articles:
        results2.append(ar["publishedAt"][11:16]+"  :  **"+ar["title"] + "**  :  " + "[LINK](" + ar["url"] + ")")



    if len(x3)!=0:
      x3=[]
      for i in range(len(results2)):
          x3.append(str(str(i+1)+ ") "+ results2[i]))
    else:
      for i in range(len(results2)):
          x3.append(str(str(i+1)+ ") "+ results2[i]))



def get_general_news():
    global x4
    print("TODAY'S TOP GENERAL NEWS ARE AS FOLLOWS : \n")

    api = NewsApiClient(api_key=my_secret)

    tech_news = api.get_top_headlines(category="general",page_size=10)
    all_articles = tech_news["articles"]
    for ar in all_articles:
        results3.append(ar["publishedAt"][11:16]+"  :  **"+ar["title"] + "**  :  " + "[LINK](" + ar["url"] + ")")



    if len(x4)!=0:
      x4=[]
      for i in range(len(results3)):
          x4.append(str(str(i+1)+ ") "+ results3[i]))
    else:
      for i in range(len(results3)):
          x4.append(str(str(i+1)+ ") "+ results3[i]))


def get_health_news():
    global x5
    print("TODAY'S TOP HEALTH NEWS ARE AS FOLLOWS : \n")

    api = NewsApiClient(api_key=my_secret)

    tech_news = api.get_top_headlines(category="health",page_size=10)
    all_articles = tech_news["articles"]
    for ar in all_articles:
        results4.append(ar["publishedAt"][11:16]+"  :  **"+ar["title"] + "**  :  " + "[LINK](" + ar["url"] + ")")



    if len(x5)!=0:
      x5=[]
      for i in range(len(results4)):
          x5.append(str(str(i+1)+ ") "+ results4[i]))
    else:
      for i in range(len(results4)):
          x5.append(str(str(i+1)+ ") "+ results4[i]))



def get_science_news():
    global x6

    print("TODAY'S TOP SCIENCE NEWS ARE AS FOLLOWS : \n")

    api = NewsApiClient(api_key=my_secret)

    tech_news = api.get_top_headlines(category="science",page_size=10)
    all_articles = tech_news["articles"]
    for ar in all_articles:
        results5.append(ar["publishedAt"][11:16]+"  :  **"+ar["title"] + "**  :  " + "[LINK](" + ar["url"] + ")")


    if len(x6)!=0:
      x6=[]
      for i in range(len(results5)):
          x6.append(str(str(i+1)+ ") "+ results5[i]))
    else:
      for i in range(len(results5)):
          x6.append(str(str(i+1)+ ") "+ results5[i]))


def get_sports_news():
    global x7

    print("TODAY'S TOP SPORTS NEWS ARE AS FOLLOWS : \n")

    api = NewsApiClient(api_key=my_secret)

    tech_news = api.get_top_headlines(category="sports",page_size=10)
    all_articles = tech_news["articles"]
    for ar in all_articles:
        results6.append(ar["publishedAt"][11:16]+"  :  **"+ar["title"] + "**  :  " + "[LINK](" + ar["url"] + ")")



    if len(x7)!=0:
      x7=[]
      for i in range(len(results6)):
          x7.append(str(str(i+1)+ ") "+ results6[i]))
    else:
      for i in range(len(results6)):
          x7.append(str(str(i+1)+ ") "+ results6[i]))

def get_regional_news(count):
    
    results7 = []

    print("TODAY'S TOP REGIONAL NEWS ARE AS FOLLOWS : \n")

    api = NewsApiClient(api_key=my_secret)

    tech_news = api.get_top_headlines(country=count,page_size=10)
    all_articles = tech_news["articles"]
    
    for ar in all_articles:
        results7.append(ar["publishedAt"][11:16]+"  :  **"+ar["title"] + "**  :  " + "<" + ar["url"] + ">")
        

    x8.clear()
    for i in range(len(results7)):
          x8.append(str(str(i+1)+ ") "+ results7[i]))


    if len(x8)<3:    
 
      tech_news = api.get_everything(country=count, page_size=10)
      all_articles = tech_news["articles"]

      for ar in all_articles:

        results7.append(ar["publishedAt"][11:16]+"  :  **"+ar["title"] + "**  :  " + "<" + ar["url"] + ">")

      x8.clear()
    
      for i in range(len(results7)):
          x8.append(str(str(i+1)+ ") "+ results7[i]))
    


def get_queried_news(query):

  

    results8 = []

    print(f"TODAY'S TOP **{query}** NEWS ARE AS FOLLOWS : \n")

    api = NewsApiClient(api_key=my_secret)

    tech_news = api.get_top_headlines(q=query, page_size=10)
    all_articles = tech_news["articles"]


      
    for ar in all_articles:

        results8.append(ar["publishedAt"][11:16]+"  :  **"+ar["title"] + "**  :  " + "<" + ar["url"] + ">")

    x9.clear()
    
    for i in range(len(results8)):
          x9.append(str(str(i+1)+ ") "+ results8[i]))

    if len(x9)<3:    
 
      tech_news = api.get_everything(q=query, page_size=(10-len(x9)))
      all_articles = tech_news["articles"]

      for ar in all_articles:

        results8.append(ar["publishedAt"][11:16]+"  :  **"+ar["title"] + "**  :  " +  ar["url"] )

      x9.clear()
    
      for i in range(len(results8)):
          x9.append(str(str(i+1)+ ") "+ results8[i]))
    

def sourceslist():

  

    results9 = []

    print("The available sources are ")

    api = NewsApiClient(api_key=my_secret)

    sources_list = api.get_sources()
    all_sources = sources_list["sources"]


      
    for ar in all_sources:

        results9.append("**"+ar["name"]+"**  :  **"+ar["language"]+ "**  :   **"+ar["country"]  + "**  :  " + "<" + ar["url"] + ">")

    x10.clear()
    
    for i in range(len(results9)):
          x10.append(str(str(i+1)+ ") "+ results9[i]))

    

