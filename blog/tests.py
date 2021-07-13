from django.test import TestCase, Client
from bs4 import BeautifulSoup   #얘는 알아두기!
from .models import Post

# Create your tests here.

class TestView(TestCase):
    def setUp(self):
        self.client= Client()

    def test_post_list(self):
        # 포스트 목록 페이지
        response= self.client.get('/blog/')
        # 정상적으로 로드되는지 확인
        self.assertEqual(response.status_code, 200)
        # 타이틀 확인
        soup= BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'IRENE BLOG')
        '''
        navbar= soup.nav
        self.assertIn(first, second)
        '''