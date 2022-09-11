from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from scrape.db2 import YtScrapeHitesh, YtScrapeKrishNaik, YtScrapeMySirji, YtScrapeTelusko
from scrape.db2 import commentsHitesh, commentsKrishNaik, commentsMySirji, commentsTelusko
from scrape import app
from scrape.csvcreate import csvWriter

current_youtuber = []

@app.route('/', methods=['GET', 'POST'])
def home_page():
    
    if request.method== 'POST':
        youtuber_name = str(request.form['ytnames'])
        current_youtuber.append(youtuber_name)

        if youtuber_name == "Telusko":
            data = [[u.id, u.video_url, u.thumbnail_urls,u.title,u.likes,u.no_of_comments,u.views,u.download_link] for u in YtScrapeTelusko.query.all()]                                   
        elif youtuber_name == "KrishNaik":
            data = [[u.id, u.video_url, u.thumbnail_urls,u.title,u.likes,u.no_of_comments,u.views,u.download_link] for u in YtScrapeKrishNaik.query.all()]                                 
        elif youtuber_name == "MySirji":
            data = [[u.id, u.video_url, u.thumbnail_urls,u.title,u.likes,u.no_of_comments,u.views,u.download_link] for u in YtScrapeMySirji.query.all()]                                   
        elif youtuber_name == "Hitesh":
            data = [[u.id, u.video_url, u.thumbnail_urls,u.title,u.likes,u.no_of_comments,u.views,u.download_link] for u in YtScrapeHitesh.query.all()]                                    
        
        csvWriter(data)
        
        
        return render_template('details.html',data=data)
    else:    
     return render_template('home.html')



@app.route('/details', methods=['GET'])
def details_page():
    return render_template('details.html')



@app.route('/comments', methods=['GET'])
def comments_page():
    if current_youtuber[0] == "Telusko":
        unique_titles =[each.title for each in YtScrapeTelusko.query.distinct(YtScrapeTelusko.title)]
        full = [[u.title, u.commentators, u.comments] for u in commentsTelusko.query.all()] #gives list of LIST of all the records
    if current_youtuber[0] == "KrishNaik":
        unique_titles =[each.title for each in YtScrapeKrishNaik.query.distinct(YtScrapeKrishNaik.title)]
        full = [[u.title, u.commentators, u.comments] for u in commentsKrishNaik.query.all()] #gives list of LIST of all the records
    if current_youtuber[0] == "MySirji":
        unique_titles =[each.title for each in YtScrapeMySirji.query.distinct(YtScrapeMySirji.title)]
        full = [[u.title, u.commentators, u.comments] for u in commentsMySirji.query.all()] #gives list of LIST of all the records
    if current_youtuber[0] == "Hitesh":
        unique_titles =[each.title for each in YtScrapeHitesh.query.distinct(YtScrapeHitesh.title)]
        full = [[u.title, u.commentators, u.comments] for u in commentsHitesh.query.all()] #gives list of LIST of all the records
    current_youtuber.pop()
    return render_template('comment.html',full=full, unique_titles=unique_titles)




@app.route('/downloads', methods = ["GET"])
def download_csv():
    return send_file("temp\\yt.csv",
                        mimetype='text/csv',
                        download_name = 'YTdetails.csv',
                        as_attachment=True )