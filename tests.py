import unittest
from flask import Flask, url_for
from flask_testing import TestCase

class PremiumAirNotifierAppTests(TestCase):

    def create_app(self):
        from app import app
        app.config['TESTING'] = True
        return app


    def test_index_page_looks_like_it_should(self):
        response = self.client.get("/")
        self.assert200(response)
        self.assertTrue("All numbers" in response.data)
        self.assertTrue("Add Number" in response.data)


    def test_when_number_added_its_displayed_on_the_page(self):
        new_pax_data = {'number': '00447477999880'}
        response = self.client.post('/save_number', data=new_pax_data)
        self.assert_redirects(response, url_for('index'))

    def test_when_sms_sent_an_sms_gets_sent(self):
        response = self.client.get('/send_sms')
        self.assert_redirects(response, url_for('index'))
        

if __name__ == '__main__':
    unittest.main()