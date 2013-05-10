# -*- coding: utf-8 -*-

import unittest

from activity import Activity

class UtilityTest(unittest.TestCase):
    def test_key(self):
        'should return the correct key for the non-aggregate feed'
        a = Activity()
        self.assertEquals(a.feed_key('david'), 'activity_feed:david')

    def test_key_aggregate(self):
        'should return the correct key for an aggregate feed'
        a = Activity()
        self.assertEqual(a.feed_key('david', True), 'activity_feed:aggregate:david')

    def test_feederboard_for(self):
        'should create a leaderboard using an existing Redis connection'
        a = Activity()
        feederboard_david = a.feederboard_for('david')
        feederboard_person = a.feederboard_for('person')

        self.assertEqual(feederboard_david is None, False)
        self.assertEqual(feederboard_person is None, False)
