# -*- coding: utf-8 -*-
# reference: https://github.com/izzyleung/ZhihuDailyPurify/wiki/%E7%9F%A5%E4%B9%8E%E6%97%A5%E6%8A%A5-API-%E5%88%86%E6%9E%90

from flask import Flask
import urllib2
from flask import jsonify
import json

app = Flask(__name__)


@app.route('/api/api/splash/')  # 启动界面图像获取
def splash():
    url = 'http://news-at.zhihu.com/api/4/start-image/1080*1776'
    response = urllib2.urlopen(url)
    return response.read()


@app.route('/api/latest/')  # 最新消息
def latest_ews():
    url = 'http://news-at.zhihu.com/api/4/news/latest'
    response = urllib2.urlopen(url)
    return jsonify(json.loads(response.read()))


@app.route('/api/latest/<id>/')  # 消息内容获取与离线下载
def latest_news(id):
    url = 'http://news-at.zhihu.com/api/4/news/' + id
    response = urllib2.urlopen(url)
    return jsonify(json.loads(response.read()))


@app.route('/api/before/<id>/')  # 过往消息
def before_news(id):
    url = 'http://news.at.zhihu.com/api/4/news/before/' + id
    response = urllib2.urlopen(url)
    return jsonify(json.loads(response.read()))


@app.route('/api/story-extra/<id>/')  # 新闻额外信息
def story_extra(id):
    url = 'http://news-at.zhihu.com/api/4/story-extra/' + id
    response = urllib2.urlopen(url)
    return jsonify(json.loads(response.read()))


@app.route('/api/long-comments/<id>/')  # 新闻长评论
def long_comments(id):
    url = 'http://news-at.zhihu.com/api/4/story/' + id + '/long-comments'
    response = urllib2.urlopen(url)
    return jsonify(json.loads(response.read()))


@app.route('/api/short-comments/<id>/')  # 新闻短评论
def short_comments(id):
    url = 'http://news-at.zhihu.com/api/4/story/' + id + '/short-comments'
    response = urllib2.urlopen(url)
    return jsonify(json.loads(response.read()))


@app.route('/api/themes/')  # 主题日报列表
def themes():
    url = 'http://news-at.zhihu.com/api/4/themes'
    response = urllib2.urlopen(url)
    return jsonify(json.loads(response.read()))


@app.route('/api/themes/<id>/')  #主题日报内容
def themes2(id):
    url = 'http://news-at.zhihu.com/api/4/themes/' + id
    response = urllib2.urlopen(url)
    return jsonify(json.loads(response.read()))


@app.route('/api/hot/')  # 热门消息
def hot():
    url = 'http://news-at.zhihu.com/api/3/news/hot'
    response = urllib2.urlopen(url)
    return jsonify(json.loads(response.read()))


@app.route('/api/recommenders/<id>/')  # 查看新闻的推荐者
def recommenders(id):
    url = 'http://news-at.zhihu.com/api/4/story/' + id + '/recommenders'
    response = urllib2.urlopen(url)
    return jsonify(json.loads(response.read()))


@app.route('/api/before/<section>/<timestamp>')  # 获取某个专栏之前的新闻
def before_section(section, timestamp):
    url = 'http://news-at.zhihu.com/api/4/section/' + section + '/before/' + timestamp
    response = urllib2.urlopen(url)
    return jsonify(json.loads(response.read()))


if __name__ == '__main__':
    app.run()
