#!/usr/bin/env python
"""
Test models
"""
import unittest
import os,sys
from datetime import date, datetime
sys.path.append(os.path.join(os.path.dirname(__file__), '..', "solution"))

from model import model_load, model_predict, model_train, nearest

MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', 'models')
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'cs-train')

class ModelTest(unittest.TestCase):
    """
    Tests
    """
        
    def test_01_train(self):
        """
        Test train routine
        """
        ## train the model
        model_train(prefix='ut', data_dir=DATA_DIR, test=False, countries=['united_kingdom'])
        SAVED_MODEL = os.path.join(MODEL_DIR, "ut-united_kingdom-0_1.joblib")
        self.assertTrue(os.path.exists(SAVED_MODEL))

    def test_02_load(self):
        """
        Test train routine
        """
                        
        ## train the model
        _, models = model_load(prefix='ut', data_dir=DATA_DIR, countries=['united_kingdom'])
        model = list(models.values())[0]
        self.assertTrue('predict' in dir(model))
        self.assertTrue('fit' in dir(model))

    def test_03_nearest(self):
        """
        Test nearest date
        """
        dates = ['2019-01-01', '2019-02-01', '2019-05-01','2018-12-01']
        nearest_date = nearest(dates, date.fromisoformat('2019-02-02'))
        print("nearest date is {}".format(nearest_date))
        self.assertTrue(nearest_date == '2019-02-01') 
        
    def test_04_predict(self):
        """
        Test input list 
        """

        country='united_kingdom'
        year='2018'
        month='01'
        day='05'
        result = model_predict(country,year,month,day, prefix='ut')
        ## List validated

        y_pred = result['y_pred']
        self.assertTrue(y_pred[0] is not None)
          
### Run the tests
if __name__ == '__main__':
    unittest.main()
