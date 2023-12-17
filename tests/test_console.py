#!/usr/bin/env python3
""" unittests for console.py, all features """
import unittest
import subprocess


class TestConsole_CreateErrors(unittest.TestCase):
    """Test stderr in console Create cmd"""

    def test_empty(self):
        """empty line + ENTER shouldn’t execute anything"""
        cmd = 'echo "" | ./console.py'
        output = "(hbnb) (hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)

    def test_nonValid_Input(self):
        """Unknown Input"""
        cmd = 'echo "ll" | ./console.py'
        output = "(hbnb) *** Unknown syntax: ll\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)

    def test_createEmpty(self):
        """class name is missing"""
        cmd = 'echo "create" | ./console.py'
        output = "(hbnb) ** class name missing **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)

    def test_createNonValid(self):
        """class name doesn’t exist"""
        cmd = 'echo "create MyModel" | ./console.py'
        output = "(hbnb) ** class doesn't exist **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)


class TestConsole_showErrors(unittest.TestCase):
    """Test stderr in console Create cmd"""

    def test_showNonValid(self):
        """class name doesn’t exist"""

        cmd = 'echo "show MyModel" | ./console.py'
        output = "(hbnb) ** class doesn't exist **\n(hbnb) "
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)

    def test_showEmpty(self):
        """the class name is missing"""
        cmd = 'echo "show " | ./console.py'
        output = "(hbnb) ** class name missing **\n(hbnb) "
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)

    def test_showIdEmpty(self):
        """the id is missing,"""
        cmd = 'echo "show BaseModel" | ./console.py'
        output = "(hbnb) ** instance id missing **\n(hbnb) "
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)

    def test_showNonValidId(self):
        """the instance of the class name doesn’t exist for the id"""
        cmd = 'echo "show BaseModel 12121211" | ./console.py'
        output = "(hbnb) ** no instance found **\n(hbnb) "
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)

    def test_showNonValid(self):
        """class name doesn’t exist"""

        cmd = 'echo "show MyModel" | ./console.py'
        output = "(hbnb) ** class doesn't exist **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)

    def test_showEmpty(self):
        """the class name is missing"""
        cmd = 'echo "show " | ./console.py'
        output = "(hbnb) ** class name missing **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)

    def test_showIdEmpty(self):
        """the id is missing,"""
        cmd = 'echo "show BaseModel" | ./console.py'
        output = "(hbnb) ** instance id missing **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)

    def test_showNonValidId(self):
        """the instance of the class name doesn’t exist for the id"""
        cmd = 'echo "show BaseModel 12121211" | ./console.py'
        output = "(hbnb) ** no instance found **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)


class TestConsole_DestroyErrors(unittest.TestCase):
    """Test stderr in console destroy cmd"""

    def test_DestroyIdEmpty(self):
        """the id is missing,"""
        cmd = 'echo "destroy BaseModel" | ./console.py'
        output = "(hbnb) ** instance id missing **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)

    def test_destroyNonValidId(self):
        """the instance of the class name doesn’t exist for the id"""
        cmd = 'echo "destroy BaseModel 12121211" | ./console.py'
        output = "(hbnb) ** no instance found **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)

    def test_DestroyEmpty(self):
        """the class name is missing"""
        cmd = 'echo "destroy " | ./console.py'
        output = "(hbnb) ** class name missing **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)

    def test_showNonValid(self):
        """class name doesn’t exist"""
        cmd = 'echo "destroy MyModel" | ./console.py'
        output = "(hbnb) ** class doesn't exist **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)


class TestConsole_allErrors(unittest.TestCase):
    """Test stderr in console all cmd"""

    def test_allNonValid(self):
        """class name doesn’t exist"""
        cmd = 'echo "all MyModel" | ./console.py'
        output = "(hbnb) ** class doesn't exist **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)


class TestConsole_UpdateErrors(unittest.TestCase):
    """Test stderr in console update cmd"""

    def test_updateIdEmpty(self):
        """the id is missing,"""
        cmd = 'echo "update BaseModel" | ./console.py'
        output = "(hbnb) ** instance id missing **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)

    def test_updateNonValidId(self):
        """the instance of the class name doesn’t exist for the id"""
        cmd = 'echo "update BaseModel 12121211" | ./console.py'
        output = "(hbnb) ** no instance found **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)

    def test_updateEmpty(self):
        """the class name is missing"""
        cmd = 'echo "update " | ./console.py'
        output = "(hbnb) ** class name missing **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)

    def test_updateNonValid(self):
        """class name doesn’t exist"""
        cmd = 'echo "update MyModel" | ./console.py'
        output = "(hbnb) ** class doesn't exist **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)

    def test_updateNonattr(self):
        """attribute name is missing"""
        cmd = 'echo "update BaseModel " | ./console.py'
        output = "(hbnb) ** instance id missing **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)


class TestConsole_allErrors2(unittest.TestCase):
    """Test stderr in console all cmd (instances by class name)"""

    def test_allNonValid(self):
        """class name doesn’t exist"""
        cmd = 'echo "MyModel.all() " | ./console.py'
        output = "(hbnb) ** class doesn't exist **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)


class TestConsole_showErrors2(unittest.TestCase):
    """Test stderr in console Create cmd (instances by class name)"""

    def test_showNonValid(self):
        """class name doesn’t exist"""
        cmd = 'echo "MyModel.show() " | ./console.py'
        output = "(hbnb) ** class doesn't exist **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)

    def test_showIdEmpty(self):
        """the id is missing,"""
        cmd = 'echo "BaseModel.show()" | ./console.py'
        output = "(hbnb) ** instance id missing **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)

    def test_showNonValidId(self):
        """the instance of the class name doesn’t exist for the id"""
        cmd = 'echo "BaseModel.show(12121211)" | ./console.py'
        output = "(hbnb) ** no instance found **\n(hbnb) \n"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        self.assertEqual(stdout, output)


if __name__ == "__main__":
    unittest.main()
    with patch("sys.stdout", new=StringIO()) as f:
        HBNBCommand().onecmd("help show")
