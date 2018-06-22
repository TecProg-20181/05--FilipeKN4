import diskspace
import unittest
import subprocess
import argparse
import os
import re

class TestDiskspace(unittest.TestCase):

    def test_subprocess_check_output(self):
        command = 'du -d 1 /home/filipe/Documentos'
        result = diskspace.subprocess_check_output(command)
        test = subprocess.check_output(command.strip().split(' '))
        self.assertEqual(result, test)

    def test_bytes_to_readable(self):
        blocks = 304
        result = diskspace.bytes_to_readable(blocks)
        test = '152.00Kb'
        self.assertEqual(result, test)

if __name__ == '__main__':
    unittest.main()
