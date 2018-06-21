from diskspace import *
import unittest

class TestDiskspace(unittest.TestCase):

    def test_subprocess_check_output(self):
        command = 'du -d 1 /home/filipe/Documentos'
        command = command.strip().split(' ')
        result = ['du', '-d', '1', '/home/filipe/Documentos']
        self.assertEqual(command, result)
