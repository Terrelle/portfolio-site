import unittest
import os
from app import app

os.environ['TESTING'] = 'true'
class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Portfolio Site</title>" in html
        # Test sub sections
        assert '<section class="page-section text-white mb-0" id="education">' in html
        assert '<section class="page-section portfolio" id="projects">' in html
        assert '<section class="page-section text-white mb-0" id="work">' in html    
   
    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert json["timeline_posts"] == 0
    
    def test_timeline_get_post(self):
        # POST
        response_post = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "jdoe@example.com", "content": "Hello, world!"})
        assert response_post.status_code == 200
        assert response_post.is_json
        # GET
        response_get = self.client.get('/api/timeline_post')
        assert response_get.status_code == 200
        assert response_get.is_json
        json_response = response_get.get_json()
        posts = json_response['timeline_posts']
        self.assertEqual(posts[0]['name'], 'John Doe')
        self.assertEqual(posts[0]['email'], 'jdoe@example.com')
        self.assertEqual(posts[0]['content'], 'Hello, world!')
        


    def test_timeline_page(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        # Check the form 
        assert '<form id="timeline-post-form" action="/api/timeline_post" method="post" enctype="multipart/form-data">' in html
        assert '<input class="form-control" type="text" id="name" name="name" placeholder="Your Name">' in html
        assert '<input class="form-control" type="text" id="email" name="email" placeholder="Your Email">' in html


    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={"email": "jooe@ex.com", "content": "Hii, I\'m John Doe"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid Name" in html

        # POST content empty container
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "jdoe@ex.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid Content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "joee-ex-com", "content": "Hi, I\'m John Doe"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid Email" in html

    




