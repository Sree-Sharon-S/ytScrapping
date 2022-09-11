from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from scrape import db

class YtScrapeTelusko(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    video_url  = db.Column(db.String(2083), default = 'unavailable')
    thumbnail_urls = db.Column(db.String(2083), default = 'unavailable')
    title = db.Column(db.String(500), default = 'unavailable')
    likes = db.Column(db.String(20), default = 'unavailable')
    no_of_comments = db.Column(db.Integer, default = 0)
    views = db.Column(db.Integer,default = 0)
    download_link = db.Column(db.String(2083), default = 'unavailable')

    def __repr__(self):
        return f"""YTScrape(
            '{self.id}', 
            '{self.video_url}', 
            '{self.thumbnail_urls}', 
            '{self.title}',
            '{self.likes}', 
            '{self.no_of_comments}', 
            '{self.views}', 
            '{self.download_link}'
            )"""

class commentsTelusko(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    title =db.Column(db.String(2083), default = 'unavailable')
    commentators =db.Column(db.String(2083), default = 'unavailable')
    comments = db.Column(db.String(10000), default = 'unavailable')

    def __repr__(self):
        return f"""comments(
            '{self.title}',
            '{self.commentators}',
            '{self.comments}'
        )"""


class YtScrapeKrishNaik(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    video_url  = db.Column(db.String(2083), default = 'unavailable')
    thumbnail_urls = db.Column(db.String(2083), default = 'unavailable')
    title = db.Column(db.String(500), default = 'unavailable')
    likes = db.Column(db.String(20), default = 'unavailable')
    no_of_comments = db.Column(db.Integer, default = 0)
    views = db.Column(db.Integer,default = 0)
    download_link = db.Column(db.String(2083), default = 'unavailable')

    def __repr__(self):
        return f"""YTScrape(
            '{self.id}', 
            '{self.video_url}', 
            '{self.thumbnail_urls}', 
            '{self.title}',
            '{self.likes}', 
            '{self.no_of_comments}', 
            '{self.views}', 
            '{self.download_link}'
            )"""

class commentsKrishNaik(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    title =db.Column(db.String(2083), default = 'unavailable')
    commentators =db.Column(db.String(2083), default = 'unavailable')
    comments = db.Column(db.String(10000), default = 'unavailable')

    def __repr__(self):
        return f"""comments(
            '{self.title}',
            '{self.commentators}',
            '{self.comments}'
        )"""


class YtScrapeMySirji(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    video_url  = db.Column(db.String(2083), default = 'unavailable')
    thumbnail_urls = db.Column(db.String(2083), default = 'unavailable')
    title = db.Column(db.String(500), default = 'unavailable')
    likes = db.Column(db.String(20), default = 'unavailable')
    no_of_comments = db.Column(db.Integer, default = 0)
    views = db.Column(db.Integer,default = 0)
    download_link = db.Column(db.String(2083), default = 'unavailable')

    def __repr__(self):
        return f"""YTScrape(
            '{self.id}', 
            '{self.video_url}', 
            '{self.thumbnail_urls}', 
            '{self.title}',
            '{self.likes}', 
            '{self.no_of_comments}', 
            '{self.views}', 
            '{self.download_link}'
            )"""

class commentsMySirji(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    title =db.Column(db.String(2083), default = 'unavailable')
    commentators =db.Column(db.String(2083), default = 'unavailable')
    comments = db.Column(db.String(10000), default = 'unavailable')

    def __repr__(self):
        return f"""comments(
            '{self.title}',
            '{self.commentators}',
            '{self.comments}'
        )"""


class YtScrapeHitesh(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    video_url  = db.Column(db.String(2083), default = 'unavailable')
    thumbnail_urls = db.Column(db.String(2083), default = 'unavailable')
    title = db.Column(db.String(500), default = 'unavailable')
    likes = db.Column(db.String(20), default = 'unavailable')
    no_of_comments = db.Column(db.Integer, default = 0)
    views = db.Column(db.Integer,default = 0)
    download_link = db.Column(db.String(2083), default = 'unavailable')

    def __repr__(self):
        return f"""YTScrape(
            '{self.id}', 
            '{self.video_url}', 
            '{self.thumbnail_urls}', 
            '{self.title}',
            '{self.likes}', 
            '{self.no_of_comments}', 
            '{self.views}', 
            '{self.download_link}'
            )"""

class commentsHitesh(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    title =db.Column(db.String(2083), default = 'unavailable')
    commentators =db.Column(db.String(2083), default = 'unavailable')
    comments = db.Column(db.String(10000), default = 'unavailable')

    def __repr__(self):
        return f"""comments(
            '{self.title}',
            '{self.commentators}',
            '{self.comments}'
        )"""