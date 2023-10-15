#!/usr/bin/python3
import unittest
import sys
from console import HBNBCommand
from io import StringIO


class TestHBNBCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cmd = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        del cls.cmd

    def setUp(self):
        self.output = StringIO()
        self.old_stdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = self.old_stdout
        self.output.close()

    def test_do_create(self):
        result = self.cmd.onecmd("create")
        self.assertEqual(self.output.getvalue().strip(),
                         "** class name missing **")

    def test_do_show(self):
        result = self.cmd.onecmd("show")
        self.assertEqual(self.output.getvalue().strip(),
                         "** class name missing **")

    def test_do_destroy(self):
        result = self.cmd.onecmd("destroy")
        self.assertEqual(self.output.getvalue().strip(),
                         "**class name missing **")

    def test_do_all(self):
        result = self.cmd.onecmd("all NonExistentClass")
        self.assertEqual(self.output.getvalue().strip(),
                         "** class doesn't exist **")

    def test_do_update(self):
        self.cmd.onecmd("create BaseModel")
        instance_id = self.output.getvalue().strip()
        result = self.cmd.onecmd(f"update BaseModel
                                 {instance_id} name John")
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
