import unittest
from train import train_model
from joblib import load

class TestModel(unittest.TestCase):

    
    def test_train_model(self):
        train_model()
        clf = load("model.pkl")
        sample_data = [13.05, 2.05, 3.22, 25.0, 124, 2.63, 
                       2.68, 0.47, 1.92, 3.58, 1.13, 3.2, 830]
        prediction = clf.predict([sample_data])
        self.assertIn(prediction[0], [0, 1, 2])  # Since wine dataset has 3 classes


if __name__ == "__main__":
    unittest.main()
