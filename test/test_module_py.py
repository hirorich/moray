import unittest
from unittest.mock import patch, MagicMock

from moray._module import py

def sample1(a, b):
    return a + b

def sample2(a, b):
    return a - b

class PyTest(unittest.TestCase):
    
    def init(self):
        py.register(sample1)
        py.register(sample2)
    
    def test_register_1(self):
        try:
            module1 = sample1.__module__
            func_name1 = sample1.__name__
            module2 = sample2.__module__
            func_name2 = sample2.__name__
            
            self.init()
            
            self.assertEqual(py._expose_module[module1][func_name1], sample1)
            self.assertEqual(py._expose_module[module2][func_name2], sample2)
        except Exception as e:
            self.fail()
    
    def test_call_1(self):
        try:
            self.init()
        except Exception as e:
            self.fail()
        
        try:
            module1 = sample1.__module__
            func_name1 = sample1.__name__
            module2 = sample2.__module__
            func_name2 = sample2.__name__
            
            self.assertEqual(py.call(module1, func_name1, (8, 5)), sample1(8, 5))
            self.assertEqual(py.call(module2, func_name2, (8, 5)), sample2(8, 5))
            
            self.assertNotEqual(py.call(module1, func_name1, (5, 8)), sample1(9, 6))
            self.assertNotEqual(py.call(module2, func_name2, (5, 8)), sample2(9, 6))
        except Exception as e:
            self.fail()
    
    def test_call_2(self):
        try:
            self.init()
        except Exception as e:
            self.fail()
        
        try:
            module1 = "test_{0}".format(sample1.__module__)
            func_name1 = sample1.__name__
            
            py.call(module1, func_name1, (8, 5))
        except Exception as e:
            return
        
        self.fail()
    
    def test_call_3(self):
        try:
            self.init()
        except Exception as e:
            self.fail()
        
        try:
            module1 = sample1.__module__
            func_name1 = "test_{0}".format(sample1.__name__)
            
            py.call(module1, func_name1, (8, 5))
        except Exception as e:
            return
        
        self.fail()
    
    def test_call_4(self):
        try:
            self.init()
        except Exception as e:
            self.fail()
        
        try:
            module1 = sample1.__module__
            func_name1 = sample1.__name__
            
            py.call(module1, func_name1, (8, 5, 7))
        except Exception as e:
            return
        
        self.fail()
