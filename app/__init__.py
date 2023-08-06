from flask import Flask, request, render_template, send_from_directory, jsonify, redirect
from peewee import *
import os
import datetime
import re
from playhouse.shortcuts import model_to_dict

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
       user=os.getenv("MYSQL_USER"),
       password=os.getenv("MYSQL_PASSWORD"),
       host=os.getenv("MYSQL_HOST"),
       port=3306
)

print(mydb)

# Peewee saves us the trouble of creating tables manually; we just need a class and the table would be created
# ORM model
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])


@app.route('/')
def index():
    # Data to be displayed on the front end
    bio = "Hi, I'm Terrelle and I am web-developer based in Ohio, USA. My passion for coding through technology has led me to work on unique projects which solve in everyday life."
    school = "Kent State University"
    major = "Major - Computer Science (2020-Present)"
    return render_template('index.html', bio=bio, school=school, major = major)


@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")


@app.route('/places_visited')
def places_visited():
    return render_template('places_visited.html')


@app.route('/app/assets/<path:path>')
def send_static(path):
    return send_from_directory('assets', path)

# Endpoint to save and retrieve all our timeline posts
# POST route to add new timeline
@app.route('/api/timeline_post', methods=['POST'])
def postTimelinePost():
    name = request.form.get('name')
    email = request.form.get('email')
    content = request.form.get('content')

    

    if not name:
        return {'error': 'Invalid Name'}, 400
    if not email:
        return {'error': 'Invalid Email'}, 400
    if not content:
        return {'error': 'Invalid Content'}, 400
    
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return {'error': 'Invalid Email: Please provide a valid email address.'}, 400

    
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def getTimelinePost():
   
    timeline_posts = [
        model_to_dict(p)
        for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
    ]

    if not timeline_posts:
        return {'timeline_posts': len(timeline_posts)}

    return {'timeline_posts': timeline_posts}

""""
# Delete all at once
@app.route('/api/timeline_post', methods=['DELETE'])
def deleteTimelinePosts():
    try:    
        # Delete all timeline posts
        TimelinePost.delete().execute()

        return jsonify({'status': 'success', 'message': 'All timeline posts deleted successfully'})
    except DoesNotExist:
        return jsonify({'status': 'error', 'message': 'No timeline posts found'})   
"""

@app.route('/api/timeline_post/<int:post_id>', methods=['DELETE'])
def delete_timeline_post(post_id):
    try:
        timeline_post = TimelinePost.get_by_id(post_id)
        timeline_post.delete_instance()
        return {'message': 'Post deleted successfully'}
    except TimelinePost.DoesNotExist:
        return {'error': 'Post with that id not found'}




if __name__ == '__main__':
    app.run(debug=True)