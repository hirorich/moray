import unittest
from unittest.mock import patch, MagicMock

import moray
from moray.exception import ConfigurationError, SupportError

@patch('moray._runner', MagicMock())
class MorayTest(unittest.TestCase):
    pass
