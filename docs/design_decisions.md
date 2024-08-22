# Design Decisions and Assumptions

This document describes the key design decisions and assumptions made during the development of the functional programming language interpreter.

## 1. Language Syntax

### Immutability
- **Decision:** The language enforces immutability by design, meaning variables cannot be reassigned once defined. This simplifies reasoning about code and ensures consistency across function calls.
- **Assumption:** Immutability is critical for functional programming, so variable reassignment is not allowed. This decision guides the design of the `Environment` class, which raises an error if an attempt is made to redefine a variable.

### No Variable Assignments
- **Decision:** The language does not support variable assignments within the function body. This aligns with functional programming paradigms that avoid mutable state.
- **Assumption:** The primary goal is to encourage pure functions without side effects. Therefore, traditional variable assignment (`x = 10`) is limited to parameters passed to functions.

### Function Definitions and Calls
- **Decision:** Function definitions are represented with the `FunctionDef` AST node, which includes a name, a list of parameters, and a body expression.
- **Assumption:** Functions may only operate on their parameters and do not have access to external mutable state. The body of the function must be an expression that returns a value.

### Lambda Expressions
- **Decision:** Lambda expressions are supported and allow for anonymous functions to be defined inline. The `Lambda` AST node represents these expressions, and the `Interpreter` handles them by capturing the environment at the time of definition.
- **Assumption:** Lambda expressions are a key feature in functional programming, providing flexibility in function definitions. Capturing the environment ensures that the variables used within the lambda retain their values as expected.

### Unary and Binary Operations
- **Decision:** The language supports both unary (e.g., `!x`) and binary operations (e.g., `x + y`). The operations are represented in the AST by `UnaryOp` and `BinaryOp` nodes, respectively.
- **Assumption:** Including a wide range of operations (arithmetic, logical, comparison) ensures the language is expressive and can handle typical programming tasks effectively.

### Logical Operations and Short-Circuiting
- **Decision:** Logical operations (`&&`, `||`) support short-circuiting, meaning the right-hand side of the operation is only evaluated if necessary. This is implemented within the `Interpreter` class.
- **Assumption:** Short-circuiting is a standard behavior in many programming languages, and implementing it ensures that unnecessary computations are avoided.

### Comparison and Boolean Operations
- **Decision:** The language supports a variety of comparison operations (`==`, `!=`, `>`, `<`, `>=`, `<=`) and boolean operations (`&&`, `||`, `!`). These are essential for control flow and logical conditions.
- **Assumption:** These operations are fundamental to decision-making within the language and must behave predictably, following standard logic rules.

## 2. Function Definitions and Calls

### Recursive Function Calls
- **Decision:** Recursive functions are supported, and the interpreter checks for base cases explicitly within the function body.
- **Assumption:** Recursive functions should follow a standard pattern, with a base case that terminates recursion. This is crucial for implementing concepts like factorial calculations and other recursive algorithms.

### Higher-Order Functions
- **Decision:** The language supports higher-order functions, meaning functions can be passed as arguments, returned as values, and stored in variables. This is managed through the `FunctionDef` and `Lambda` nodes.
- **Assumption:** Higher-order functions are a powerful feature in functional programming, allowing for more abstract and flexible code.

## 3. Error Handling

### Comprehensive Error Messages
- **Decision:** The interpreter provides detailed error messages to help users diagnose issues.
- **Assumption:** Clear error messages are essential for debugging, so the interpreter checks for common errors like division by zero, undefined variables, and invalid syntax.

### Type Safety
- **Decision:** The interpreter checks for type consistency during evaluation, especially in comparison and arithmetic operations. Mismatched types raise an error.
- **Assumption:** Type safety ensures that operations are meaningful and prevents unexpected behaviors during program execution.

## 4. Interpreter Design

### Evaluation Strategy
- **Decision:** The interpreter uses a recursive evaluation strategy, where each AST node is evaluated based on its type.
- **Assumption:** This approach is straightforward for the language's functional nature and ensures that expressions are evaluated in a clear and predictable manner.

### Environment Management
- **Decision:** The environment is represented as a stack of scopes, with nested functions having access to their parent scopes.
- **Assumption:** This design allows for variable scoping in a way that supports closures and nested functions effectively. It ensures that variables maintain their intended scope and lifetime.

### REPL (Read-Eval-Print Loop) Support
- **Decision:** A REPL interface is provided to allow interactive evaluation of expressions, function definitions, and commands. The REPL supports loading scripts, executing commands, and managing user input dynamically.
- **Assumption:** The REPL is crucial for an interactive user experience, allowing for experimentation and immediate feedback, which is essential in educational and development contexts.

### Script Execution
- **Decision:** The interpreter can execute scripts loaded from files, with each line of the script being parsed and evaluated sequentially. This is handled by the `run_script` function in the REPL.
- **Assumption:** Script execution allows for batch processing of commands, making the language practical for larger programs and repeated tasks.

## 5. Testing and Validation

### Comprehensive Unit Testing
- **Decision:** Extensive unit tests cover all aspects of the language, including the lexer, parser, interpreter, and REPL. Tests ensure that each component functions correctly in isolation and when integrated.
- **Assumption:** Unit testing is essential for maintaining reliability and catching regressions. The tests cover typical use cases, edge cases, and error conditions to ensure robustness.

### Test Cases for Edge Conditions
- **Decision:** Special attention is given to edge cases, such as deeply nested function calls, recursive definitions without proper base cases, and malformed input. These are tested rigorously to ensure stability.
- **Assumption:** Handling edge cases effectively prevents common pitfalls and enhances the interpreter's resilience in real-world usage.

