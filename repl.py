"""
REPL (Read-Eval-Print Loop) and script runner for a simple functional programming language.

This module allows users to interactively enter code or load script files for evaluation
by the Interpreter. The REPL provides basic commands like loading files, exiting, and
getting help.

Functions:
- run_interactive: Starts the interactive REPL.
- run_script: Loads and executes a script file.
- main: Entry point for running the script or starting the REPL.
"""

import sys
from interpreter_logic.lexer import Lexer
from interpreter_logic.parser import Parser
from interpreter_logic.interpreter import Interpreter

def run_interactive():
    """
    Starts the interactive REPL (Read-Eval-Print Loop) for the functional programming language.

    Users can type commands or code, which will be evaluated immediately. The REPL
    supports loading scripts from files, exiting, and providing help.
    """
    print("Interactive Functional Language Shell")
    print("Type ':load <filename>' to load a file.")
    print("Type ':exit' to quit.")
    print("Type ':help' for a list of commands.")

    buffer = []  # To accumulate multi-line input
    interpreter = Interpreter()  # Initialize the interpreter

    while True:
        try:
            user_input = input(">>> ").strip()

            if user_input.lower() in {'exit', 'quit', ':exit'}:
                print("Exiting the REPL.")
                break

            if user_input.startswith(':load '):
                filename = user_input.split(maxsplit=1)[1]
                run_script(filename, interpreter)
                continue

            if user_input == ':help':
                print("Available commands:")
                print(":load <filename> - Load and execute a script file")
                print(":exit - Exit the REPL")
                print(":help - Show this help message")
                continue

            if user_input == "":
                continue  # Ignore empty lines

            buffer.append(user_input)

            # Check if the input is complete
            if (user_input.endswith(')') or
                    not any(char in user_input for char in '({[')):
                full_input = ' '.join(buffer)
                buffer = []  # Clear the buffer for the next input

                lexer = Lexer(full_input)
                tokens = lexer.tokenize()
                print("Tokens:", tokens)

                parser = Parser(tokens)
                ast = parser.parse_program()
                print("AST:", ast)

                result = interpreter.eval(ast)
                print("Result:", result)

        except Exception as e:
            print(f"Error: {e}")

def run_script(filename, interpreter):
    """
    Loads and executes a script file.

    Args:
        filename (str): The name of the file to load and execute.
        interpreter (Interpreter): The interpreter instance used to evaluate the script.
    """
    try:
        with open(filename, 'r') as file:
            source_code = file.read().strip()  # Read the whole file

            # Split the source code into separate commands based on some delimiter
            # Assuming commands are separated by newlines for simplicity
            commands = source_code.split('\n')

            for command in commands:
                if command.strip() == "":
                    continue  # Skip empty lines

                lexer = Lexer(command)
                tokens = lexer.tokenize()
                print("Tokens:", tokens)

                parser = Parser(tokens)
                ast = parser.parse_program()
                print("AST:", ast)

                result = interpreter.eval(ast)
                print("Result:", result)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """
    Main entry point for the REPL and script execution.

    If a filename is provided as a command-line argument, the script is executed.
    Otherwise, the interactive REPL is started.
    """
    if len(sys.argv) > 1:
        # If a filename is provided, run the script
        interpreter = Interpreter()
        run_script(sys.argv[1], interpreter)
    else:
        # Otherwise, start the interactive shell
        run_interactive()

if __name__ == "__main__":
    main()
