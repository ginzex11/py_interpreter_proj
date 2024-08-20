"""
Unit tests for script execution in the REPL environment.

This test suite uses the unittest framework to validate that script files are correctly loaded
and accessible. The tests check for the presence of sample script files used in the REPL.

Classes:
- TestScriptExecution: Contains test methods to validate the loading of script files.

Methods:
- load_script: Helper method to load and return the content of a script file.
- Various test methods to check that specific sample scripts are found and loaded correctly.
"""

import os
import unittest

class TestScriptExecution(unittest.TestCase):
    """
    Test case class for validating the loading and accessibility of script files in the REPL environment.
    """

    def load_script(self, script_path):
        """
        Loads and returns the content of a script file.

        Args:
            script_path (str): The relative path to the script file.

        Returns:
            str or None: The content of the script file if found, otherwise None.
        """
        # Resolve the absolute path
        abs_path = os.path.join(os.path.dirname(__file__), '..', script_path)
        try:
            with open(abs_path, 'r') as file:
                script_content = file.read()
            return script_content
        except FileNotFoundError:
            print(f"File '{script_path}' not found.")
            return None

    def test_arithmetic_script(self):
        """
        Tests loading of the arithmetic script file.
        """
        output = self.load_script('samples/arithmetic.lambda')
        self.assertIsNotNone(output, "arithmetic.lambda file not found.")

    def test_boolean_ops_script(self):
        """
        Tests loading of the boolean operations script file.
        """
        output = self.load_script('samples/boolean_ops.lambda')
        self.assertIsNotNone(output, "boolean_ops.lambda file not found.")

    def test_func_def_script(self):
        """
        Tests loading of the function definition script file.
        """
        output = self.load_script('samples/func_def.lambda')
        self.assertIsNotNone(output, "func_def.lambda file not found.")

    def test_multi_commands_script(self):
        """
        Tests loading of the script file with multiple commands.
        """
        output = self.load_script('samples/multi_commands.lambda')
        self.assertIsNotNone(output, "multi_commands.lambda file not found.")

if __name__ == '__main__':
    unittest.main()
