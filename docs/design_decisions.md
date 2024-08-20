
### `design_decisions.md`

```markdown
# Design Decisions and Assumptions

This document describes the key design decisions and assumptions made during the development of the functional programming language interpreter.

## 1. Language Syntax

### Immutability
- **Decision:** The language enforces immutability by design, meaning variables cannot be reassigned once defined. This simplifies reasoning about code and ensures consistency across function calls.
- **Assumption:** Immutability is critical for functional programming, so variable reassignment is not allowed. This decision guides the design of the `Environment` class, which raises an error if an attempt is made to redefine a variable.

### No Variable Assignments
- **Decision:** The language does not support variable assignments within the function body. This aligns with functional programming paradigms that avoid mutable state.
- **Assumption:** The primary goal is to encourage pure functions without side effects. Therefore, traditional variable assignment (`x = 10`) is limited to parameters passed to functions.

## 2. Function Definitions and Calls

### Function Parameters and Body
- **Decision:** Function definitions are represented with the `FunctionDef` AST node, which includes a name, a list of parameters, and a body expression.
- **Assumption:** Functions may only operate on their parameters and do not have access to external mutable state. The body of the function must be an expression that returns a value.

### Recursive Function Calls
- **Decision:** Recursive functions are supported, and the interpreter checks for base cases explicitly within the function body.
- **Assumption:** Recursive functions should follow a standard pattern, with a base case that terminates recursion.

## 3. Error Handling

### Comprehensive Error Messages
- **Decision:** The interpreter provides detailed error messages to help users diagnose issues.
- **Assumption:** Clear error messages are essential for debugging, so the interpreter checks for common errors like division by zero, undefined variables, and invalid syntax.

## 4. Interpreter Design

### Evaluation Strategy
- **Decision:** The interpreter uses a recursive evaluation strategy, where each AST node is evaluated based on its type.
- **Assumption:** This approach is straightforward for the language's functional nature and ensures that expressions are evaluated in a clear and predictable manner.

### Environment Management
- **Decision:** The environment is represented as a stack of scopes, with nested functions having access to their parent scopes.
- **Assumption:** This design allows for variable scoping in a way that supports closures and nested functions effectively.
