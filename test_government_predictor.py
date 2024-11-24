import unittest

from government_predictor import GovernmentPredictor


class GovernmentPredictorTest(unittest.TestCase):
    def setUp(self):
        self.testee = GovernmentPredictor()

    def test_proper_construction(self):
        self.assertEqual(len(self.testee.key_definitions), 13)
        self.assertEqual(len(self.testee.boolean_keys), 13)
    
    def test_make_prediction_returns_True_when_keys_all_True(self):
        self.testee.boolean_keys = [True for _ in range(13)]
        self.assertTrue(self.testee.make_prediction())
    
    def test_make_prediction_returns_False_when_keys_all_False(self):
        self.testee.boolean_keys = [False for _ in range(13)]
        self.assertFalse(self.testee.make_prediction())

    def test_make_prediction_returns_True_when_6_keys_True(self):
        self.testee.boolean_keys = [True if i < 6 else False for i in range(13)]
        self.assertTrue(self.testee.make_prediction())

    def test_make_prediction_returns_False_when_5_keys_True(self):
        self.testee.boolean_keys = [True if i < 5 else False for i in range(13)]
        self.assertFalse(self.testee.make_prediction())

    def test_get_predicted_result_returns_correctly_when_keys_False(self):
        """
        When boolean keys are all false, a string stating that there will be a change in government should be returned. The boolean keys are False by default
        """
        self.assertEqual(
            self.testee.get_predicted_result(),
            "\n\nThere will be a change of government")
        
    def test_get_predicted_result_returns_correctly_when_keys_True(self):
        """
        When boolean keys are all True, a string stating that the incumbent governmentremains should be printed
        """
        self.testee.boolean_keys = [True for _ in range(13)]
        self.assertEqual(
            self.testee.get_predicted_result(),
            '\n\nThe incumbent government remains in power')


if __name__ == "__main__":
    unittest.main()