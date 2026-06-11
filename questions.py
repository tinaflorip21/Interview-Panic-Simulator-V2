easy_questions = [
    {"question": "What is Python?", "options": ["Programming Language", "Snake", "Operating System", "Database"], "answer": "Programming Language"},
    {"question": "Which keyword is used for loops?", "options": ["repeat", "for", "loop", "iterate"], "answer": "for"},
    {"question": "Which symbol is used for comments?", "options": ["//", "#", "--", "/*"], "answer": "#"},
    {"question": "Which keyword creates a function?", "options": ["func", "define", "def", "function"], "answer": "def"},
    {"question": "How do you print 'Hello World' in Python?", "options": ["echo('Hello World')", "printf('Hello World')", "print('Hello World')", "console.log('Hello World')"], "answer": "print('Hello World')"},
    {"question": "Which data type is used to store text?", "options": ["int", "float", "str", "bool"], "answer": "str"},
    {"question": "What is the correct file extension for Python files?", "options": [".py", ".python", ".pt", ".pyt"], "answer": ".py"},
    {"question": "Which of these is a valid variable name?", "options": ["2myvar", "my-var", "my_var", "my var"], "answer": "my_var"},
    {"question": "How do you start an 'if' statement in Python?", "options": ["if x > y then:", "if (x > y)", "if x > y:", "if x > y;"], "answer": "if x > y:"},
    {"question": "Which operator is used for multiplication?", "options": ["x", "multi", "*", "^"], "answer": "*"}
]

medium_questions = [
    {"question": "Which data structure uses key-value pairs?", "options": ["List", "Tuple", "Dictionary", "Array"], "answer": "Dictionary"},
    {"question": "Which method is used to add an element to the end of a list?", "options": ["add()", "push()", "append()", "insert()"], "answer": "append()"},
    {"keyword": "Which of these is a mutable data type?", "options": ["String", "Tuple", "List", "Integer"], "answer": "List"},
    {"question": "What is the purpose of the 'self' parameter in a class method?", "options": ["Refers to the class itself", "Refers to the instance of the class", "It is a reserved keyword for static methods", "It defines a private variable"], "answer": "Refers to the instance of the class"},
    {"question": "Which of these is used to handle exceptions in Python?", "options": ["try-except", "catch-throw", "do-while", "if-else"], "answer": "try-except"},
    {"question": "How do you start a list comprehension?", "options": ["(x for x in list)", "{x for x in list}", "[x for x in list]", "<x for x in list>"], "answer": "[x for x in list]"},
    {"question": "Which operator is used for floor division?", "options": ["/", "//", "%", "**"], "answer": "//"},
    {"question": "What does the 'map()' function do?", "options": ["Filters a list", "Applies a function to all items in an input list", "Sorts a dictionary", "Joins two strings"], "answer": "Applies a function to all items in an input list"},
    {"question": "Which module is used for regular expressions in Python?", "options": ["regex", "pyreg", "re", "expression"], "answer": "re"},
    {"question": "What is the output of bool([])?", "options": ["True", "False", "None", "Error"], "answer": "False"}
]

hard_questions = [
    {"question": "What is the time complexity of binary search?", "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"], "answer": "O(log n)"},
    {"question": "What is the primary difference between a shallow copy and a deep copy?", "options": ["Shallow copy is faster", "Deep copy creates new objects for nested structures", "Shallow copy only works on lists", "There is no difference"], "answer": "Deep copy creates new objects for nested structures"},
    {"question": "What is a 'decorator' in Python?", "options": ["A tool to format strings", "A function that modifies the behavior of another function", "A way to define global variables", "A specific type of class"], "answer": "A function that modifies the behavior of another function"},
    {"question": "Which of the following is true about Python's Global Interpreter Lock (GIL)?", "options": ["It allows multiple threads to execute Python bytecodes at once", "It prevents multiple native threads from executing Python bytecodes at once", "It is used only in multi-processing", "It speeds up CPU-bound tasks"], "answer": "It prevents multiple native threads from executing Python bytecodes at once"},
    {"question": "What does the '__init__' method do?", "options": ["Deletes an object", "Initializes the attributes of a class instance", "Imports a module", "Inherits from a parent class"], "answer": "Initializes the attributes of a class instance"},
    {"question": "What is the purpose of 'yield' in a function?", "options": ["Ends the function and returns a list", "Turns the function into a generator", "Pauses the execution for a set time", "Increases performance of loops"], "answer": "Turns the function into a generator"},
    {"question": "What is 'MRO' in Python?", "options": ["Method Resolution Order", "Main Run Object", "Module Registration Office", "Memory Retrieval Operation"], "answer": "Method Resolution Order"},
    {"question": "Which of these is a built-in Python function used for introspection?", "options": ["dir()", "inspect()", "view()", "show()"], "answer": "dir()"},
    {"question": "How is memory managed in Python?", "options": ["Manual allocation", "Automatic garbage collection and reference counting", "Only through stacks", "It isn't managed"], "answer": "Automatic garbage collection and reference counting"},
    {"question": "What does the '@staticmethod' decorator signify?", "options": ["The method cannot be called", "The method belongs to the class and doesn't require an instance", "The method is private", "The method can only be used in inheritance"], "answer": "The method belongs to the class and doesn't require an instance"}
]