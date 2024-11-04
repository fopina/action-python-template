import json
import os
import unittest


class TestIntegration(unittest.TestCase):
    def test_sumit(self):
        """
        Assert integration run for:
            ...
            id: sumit
            with:
                number-one: 2
                number-two: 1
        """
        data = json.loads(os.getenv('STEPS_CONTEXT'))
        self.assertEqual(data['sumit']['outputs']['sum'], '3')
