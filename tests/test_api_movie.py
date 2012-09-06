# -*- coding: utf-8 -*-

from uuid import uuid4
from framework import DoubanClientTestBase, main

class TestApiMovie(DoubanClientTestBase):
    def setUp(self):
        super(TestApiMovie, self).setUp()
        self.user_id = '40774605'
        self.movie_id = '1296357'
        self.review_id = '5565362'
        self.imdb = 'tt1345836'

    def test_get_movie(self):
        ret = self.client.movie.get(self.movie_id)

        self.assertTrue(isinstance(ret, dict))
        self.assertTrue(ret.has_key('author'))
        self.assertTrue(ret.has_key('title'))
        self.assertTrue(ret.has_key('summary'))

    def test_get_movie_by_imdb(self):
        ret= self.client.movie.imdb(self.imdb)

        self.assertTrue(isinstance(ret, dict))
        self.assertTrue(ret.has_key('author'))
        self.assertTrue(ret.has_key('title'))
        self.assertTrue(ret.has_key('summary'))

    def test_search_movie(self):
        ret = self.client.movie.search('蝙蝠侠')

        self.assertTrue(isinstance(ret, dict))
        self.assertTrue(isinstance(ret['movies'], list))
        self.assertTrue(ret.has_key('start'))
        self.assertTrue(ret.has_key('count'))
        self.assertTrue(ret.has_key('total'))

    # def test_movie_reviews(self):
    #     ret = self.client.movie.reviews(self.movie_id)

    #     self.assertTrue(isinstance(ret, dict))
    #     self.assertTrue(isinstance(ret['reviews'], list))
    #     self.assertTrue(ret.has_key('start'))
    #     self.assertTrue(ret.has_key('count'))
    #     self.assertTrue(ret.has_key('total'))

    def test_movie_tags(self):
        ret = self.client.movie.tags(self.movie_id)

        self.assertTrue(isinstance(ret, dict))
        self.assertTrue(isinstance(ret['tags'], list))
        self.assertTrue(ret.has_key('start'))
        self.assertTrue(ret.has_key('count'))
        self.assertTrue(ret.has_key('total'))

    def test_get_movie_tagged_list(self):
        ret = self.client.movie.tagged_list('40774605')

        self.assertTrue(isinstance(ret, dict))
        self.assertTrue(isinstance(ret['tags'], list))
        self.assertTrue(ret.has_key('start'))
        self.assertTrue(ret.has_key('count'))
        self.assertTrue(ret.has_key('total'))

    def test_new_update_delete_review(self):

        # new
        title = content = uuid4().hex
        content = content * 10
        ret = self.client.movie.review.new(self.movie_id, title, content)

        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(content, ret['content'])
        self.assertTrue(ret.has_key('author'))

        review_id = ret['id']

        # update
        content = content * 2
        ret = self.client.movie.review.update(review_id, title, content)
        self.assertEqual(content, ret['content'])

        # delete
        ret = self.client.movie.review.delete(review_id)
        self.assertEqual('OK', ret)


    # def test_get_movie_review(self):
    #     ret = self.client.movie.review.get(self.review_id)

    #     self.assertTrue(isinstance(ret, dict))
    #     self.assertEqual(ret['id'], self.review_id)
    #     self.assertTrue(ret.has_key('rating'))
    #     self.assertTrue(ret.has_key('author'))


if __name__ == '__main__':
    main()
