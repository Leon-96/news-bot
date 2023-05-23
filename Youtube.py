from pyyoutube import Api


urlist = []
def url_getter(query):
    
    
    api = Api(api_key="AIzaSyCeO13_iowNSoY-wJJhLb4W6I4zL8_PZxw  ")
    r = api.search_by_keywords(q=query, search_type=["video"], count=5,    limit=5)
    resultdict = (r.items[0].to_dict())
    VideoID = (resultdict["id"]["videoId"])

    urlist.append("https://www.youtube.com/watch?v="+VideoID)



