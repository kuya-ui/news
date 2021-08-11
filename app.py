from flask import Flask, render_template
from newsapi import NewsApiClient




app = Flask(__name__)



@app.route('/')
def Index():
    newsapi =NewsApiClient(api_key="8120360ba9e342dbaccb75e01109ca34")
    topheadlines = newsapi.get__top__headlines(sources="https://www.bbc.com/news")


    articles =topheadlines['articles']

    desc = []
    news = []
    img = []


    for i in range(len(articles)):
        myarticles =articles[i]


        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])



    mylist = zip(news, desc, img)


    return render_template('index.html', context = mylist)




    # if__name__=="__main__":
    # app.run(debug=True)