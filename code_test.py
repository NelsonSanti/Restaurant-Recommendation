import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from main_project.main_code import restart, restart_another_category
#You can tests manually or
#Run tests with pytest with PYTHONPATH=. pytest -s (this depends on the path of the file) 



def connect():
    print("Initializing tests...")

def disconnect():
    print("Tests finished.")

class TestsMainCode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connect()
 
    def test_restart(self):
        restart()
        self.assertEqual(restart(), None)
    
    
    def test_restart_another_category(self):
        restart_another_category()
        self.assertEqual(restart_another_category(), None)
    
    @classmethod
    def tearDownClass(cls):
        disconnect()

if __name__ == '__main__':
    unittest.main()