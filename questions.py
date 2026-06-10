QUESTIONS = [
{
    "id": 0,
    "text": "Which keyword is used to define a function in Python?",
    "options": ["func", "define", "def", "function"],
    "answer": "C",
    "explanation": "'def' is used to define a function."
},
{
    "id": 1,
    "text": "What is the output of print(type(10))?",
    "options": ["<class 'int'>", "<class 'float'>", "<class 'number'>", "<class 'integer'>"],
    "answer": "A",
    "explanation": "10 is an integer value."
},
{
    "id": 2,
    "text": "Which of the following is mutable?",
    "options": ["Tuple", "String", "List", "Integer"],
    "answer": "C",
    "explanation": "Lists can be modified after creation."
},
{
    "id": 3,
    "text": "Which operator performs floor division?",
    "options": ["/", "//", "%", "**"],
    "answer": "B",
    "explanation": "'//' returns the integer quotient."
},
{
    "id": 4,
    "text": "What is the output of len('Python')?",
    "options": ["5", "6", "7", "Error"],
    "answer": "B",
    "explanation": "The string contains 6 characters."
},
{
    "id": 5,
    "text": "Which collection does not allow duplicates?",
    "options": ["List", "Tuple", "Dictionary", "Set"],
    "answer": "D",
    "explanation": "Sets store unique elements."
},
{
    "id": 6,
    "text": "What is the output of 2**4?",
    "options": ["6", "8", "16", "24"],
    "answer": "C",
    "explanation": "2 raised to the power 4 is 16."
},
{
    "id": 7,
    "text": "Which statement skips the current iteration of a loop?",
    "options": ["break", "continue", "pass", "return"],
    "answer": "B",
    "explanation": "'continue' skips the current iteration."
},
{
    "id": 8,
    "text": "Which keyword creates a class?",
    "options": ["object", "new", "class", "Class"],
    "answer": "C",
    "explanation": "'class' is the keyword used."
},
{
    "id": 9,
    "text": "What is the output of bool([])?",
    "options": ["True", "False", "None", "Error"],
    "answer": "B",
    "explanation": "An empty list evaluates to False."
},
{
    "id": 10,
    "text": "Which function converts a string to an integer?",
    "options": ["str()", "float()", "int()", "integer()"],
    "answer": "C",
    "explanation": "int() converts values to integers."
},
{
    "id": 11,
    "text": "What is the index of the first element in a Python list?",
    "options": ["0", "1", "-1", "Depends"],
    "answer": "A",
    "explanation": "Python uses zero-based indexing."
},
{
    "id": 12,
    "text": "Which loop is used when the number of iterations is known?",
    "options": ["while", "for", "do-while", "repeat"],
    "answer": "B",
    "explanation": "for loops are commonly used for fixed iterations."
},
{
    "id": 13,
    "text": "What is the output of 'abc'.upper()?",
    "options": ["abc", "ABC", "Abc", "Error"],
    "answer": "B",
    "explanation": "upper() converts letters to uppercase."
},
{
    "id": 14,
    "text": "Which function returns the ASCII value of a character?",
    "options": ["chr()", "ascii()", "ord()", "asc()"],
    "answer": "C",
    "explanation": "ord() returns the Unicode/ASCII code."
},
{
    "id": 15,
    "text": "Which function converts an ASCII code to a character?",
    "options": ["char()", "chr()", "ord()", "ascii()"],
    "answer": "B",
    "explanation": "chr() converts an integer code to a character."
},
{
    "id": 16,
    "text": "What is the output of list('abc')?",
    "options": ["['abc']", "['a','b','c']", "abc", "Error"],
    "answer": "B",
    "explanation": "Each character becomes an element."
},
{
    "id": 17,
    "text": "Which symbol is used for comments in Python?",
    "options": ["//", "#", "/* */", "--"],
    "answer": "B",
    "explanation": "# starts a single-line comment."
},
{
    "id": 18,
    "text": "What is the output of 10 % 3?",
    "options": ["3", "1", "0", "10"],
    "answer": "B",
    "explanation": "% returns the remainder."
},
{
    "id": 19,
    "text": "Which data type stores key-value pairs?",
    "options": ["List", "Tuple", "Dictionary", "Set"],
    "answer": "C",
    "explanation": "Dictionaries store data as key-value pairs."
},
{
    "id": 20,
    "text": "What is the output of len([1,2,3,4])?",
    "options": ["3", "4", "5", "Error"],
    "answer": "B",
    "explanation": "The list contains 4 elements."
},
{
    "id": 21,
    "text": "Which keyword exits a loop completely?",
    "options": ["continue", "skip", "break", "return"],
    "answer": "C",
    "explanation": "break immediately terminates the loop."
},
{
    "id": 22,
    "text": "What is the output of 'python'[0]?",
    "options": ["p", "y", "python", "0"],
    "answer": "A",
    "explanation": "Index 0 refers to the first character."
},
{
    "id": 23,
    "text": "Which function is used to take user input?",
    "options": ["scan()", "input()", "read()", "get()"],
    "answer": "B",
    "explanation": "input() reads input from the user."
},
{
    "id": 24,
    "text": "What is the output of type([1,2,3])?",
    "options": ["tuple", "list", "array", "set"],
    "answer": "B",
    "explanation": "The object is a list."
},
# QUESTIONS 25-49 (OOP + Exception Handling)

{
    "id": 25,
    "text": "What does 'self' represent in a class method?",
    "options": ["Class", "Current Object", "Parent Class", "Module"],
    "answer": "B",
    "explanation": "'self' refers to the current object instance."
},
{
    "id": 26,
    "text": "Which method is called automatically when an object is created?",
    "options": ["__main__", "__init__", "__newobj__", "__create__"],
    "answer": "B",
    "explanation": "__init__ is the constructor."
},
{
    "id": 27,
    "text": "What is a constructor?",
    "options": ["Variable", "Loop", "Special method used to initialize objects", "Module"],
    "answer": "C",
    "explanation": "Constructors initialize object data."
},
{
    "id": 28,
    "text": "Which OOP concept allows code reuse?",
    "options": ["Inheritance", "Polymorphism", "Encapsulation", "Abstraction"],
    "answer": "A",
    "explanation": "Inheritance enables code reuse."
},
{
    "id": 29,
    "text": "Single inheritance means:",
    "options": ["One child many parents", "One parent one child", "Many parents one child", "Many children many parents"],
    "answer": "B",
    "explanation": "A child inherits from one parent."
},
{
    "id": 30,
    "text": "Multiple inheritance means:",
    "options": ["One parent", "No parent", "Multiple parents", "Multiple children"],
    "answer": "C",
    "explanation": "A child inherits from multiple parents."
},
{
    "id": 31,
    "text": "Which inheritance type forms a chain of classes?",
    "options": ["Single", "Multiple", "Multilevel", "Hybrid"],
    "answer": "C",
    "explanation": "Grandparent → Parent → Child."
},
{
    "id": 32,
    "text": "Which inheritance has one parent and multiple children?",
    "options": ["Hierarchical", "Single", "Multiple", "Hybrid"],
    "answer": "A",
    "explanation": "One parent class is inherited by multiple children."
},
{
    "id": 33,
    "text": "What is encapsulation?",
    "options": ["Inheritance", "Wrapping data and methods together", "Overloading", "Looping"],
    "answer": "B",
    "explanation": "Encapsulation binds data and methods."
},
{
    "id": 34,
    "text": "How do you indicate a private variable in Python?",
    "options": ["var", "_var", "__var", "private var"],
    "answer": "C",
    "explanation": "Double underscore indicates private members."
},
{
    "id": 35,
    "text": "Which OOP concept hides implementation details?",
    "options": ["Encapsulation", "Inheritance", "Abstraction", "Association"],
    "answer": "C",
    "explanation": "Abstraction hides internal details."
},
{
    "id": 36,
    "text": "Which module supports abstraction?",
    "options": ["abc", "oop", "abstract", "pyabs"],
    "answer": "A",
    "explanation": "abc stands for Abstract Base Classes."
},
{
    "id": 37,
    "text": "What is polymorphism?",
    "options": ["One interface, many forms", "Data hiding", "Inheritance", "Constructor"],
    "answer": "A",
    "explanation": "Polymorphism allows multiple behaviors."
},
{
    "id": 38,
    "text": "Method overriding occurs when:",
    "options": ["Child redefines parent method", "Method deleted", "Method overloaded", "Method imported"],
    "answer": "A",
    "explanation": "The child provides its own implementation."
},
{
    "id": 39,
    "text": "Python supports method overloading through:",
    "options": ["Multiple methods", "Default arguments", "Compiler", "Templates"],
    "answer": "B",
    "explanation": "Python uses default arguments instead."
},
{
    "id": 40,
    "text": "Which decorator defines a class method?",
    "options": ["@staticmethod", "@classmethod", "@property", "@override"],
    "answer": "B",
    "explanation": "Class methods receive cls."
},
{
    "id": 41,
    "text": "Which decorator defines a static method?",
    "options": ["@classmethod", "@staticmethod", "@property", "@static"],
    "answer": "B",
    "explanation": "Static methods don't use self or cls."
},
{
    "id": 42,
    "text": "What does cls refer to?",
    "options": ["Current object", "Class itself", "Constructor", "Parent class"],
    "answer": "B",
    "explanation": "cls references the class."
},
{
    "id": 43,
    "text": "Which method is used to customize object printing?",
    "options": ["__print__", "__show__", "__str__", "__display__"],
    "answer": "C",
    "explanation": "__str__ controls string representation."
},
{
    "id": 44,
    "text": "Which method overloads the + operator?",
    "options": ["__plus__", "__sum__", "__add__", "__concat__"],
    "answer": "C",
    "explanation": "__add__ handles +."
},
{
    "id": 45,
    "text": "What is composition?",
    "options": ["IS-A relationship", "HAS-A relationship", "Inheritance", "Overriding"],
    "answer": "B",
    "explanation": "Composition models HAS-A relationships."
},
{
    "id": 46,
    "text": "Which block is used to handle exceptions?",
    "options": ["catch", "except", "error", "handle"],
    "answer": "B",
    "explanation": "Python uses except."
},
{
    "id": 47,
    "text": "Which block always executes?",
    "options": ["try", "except", "raise", "finally"],
    "answer": "D",
    "explanation": "finally executes regardless of exceptions."
},
{
    "id": 48,
    "text": "Which keyword raises an exception?",
    "options": ["throw", "raise", "error", "exception"],
    "answer": "B",
    "explanation": "raise manually generates exceptions."
},
{
    "id": 49,
    "text": "What exception occurs when dividing by zero?",
    "options": ["TypeError", "IndexError", "ZeroDivisionError", "ValueError"],
    "answer": "C",
    "explanation": "Division by zero raises ZeroDivisionError."
},
# QUESTIONS 50-74 (Modules, Iterators, Generators, Closures, Decorators, Regex)

{
    "id": 50,
    "text": "Which keyword is used to import a module?",
    "options": ["include", "using", "import", "require"],
    "answer": "C",
    "explanation": "'import' is used to include modules."
},
{
    "id": 51,
    "text": "Which module provides mathematical functions?",
    "options": ["random", "math", "os", "sys"],
    "answer": "B",
    "explanation": "The math module provides mathematical functions."
},
{
    "id": 52,
    "text": "Which function returns the square root of a number?",
    "options": ["math.root()", "math.sqrt()", "sqrt()", "root()"],
    "answer": "B",
    "explanation": "math.sqrt() calculates square roots."
},
{
    "id": 53,
    "text": "Which module generates random numbers?",
    "options": ["math", "random", "os", "datetime"],
    "answer": "B",
    "explanation": "The random module generates random values."
},
{
    "id": 54,
    "text": "Which function generates a random integer?",
    "options": ["random()", "rand()", "randint()", "integer()"],
    "answer": "C",
    "explanation": "random.randint(a,b) generates a random integer."
},
{
    "id": 55,
    "text": "Which module works with dates and times?",
    "options": ["time", "calendar", "datetime", "date"],
    "answer": "C",
    "explanation": "datetime handles dates and times."
},
{
    "id": 56,
    "text": "Which module interacts with the operating system?",
    "options": ["os", "sys", "platform", "io"],
    "answer": "A",
    "explanation": "os provides operating system functionality."
},
{
    "id": 57,
    "text": "A package is:",
    "options": ["A file", "A folder containing modules", "A function", "A class"],
    "answer": "B",
    "explanation": "Packages organize related modules."
},
{
    "id": 58,
    "text": "Which statement imports only sqrt from math?",
    "options": ["import sqrt", "from math import sqrt", "math.sqrt", "include sqrt"],
    "answer": "B",
    "explanation": "from math import sqrt imports only sqrt."
},
{
    "id": 59,
    "text": "What does 'as' do in imports?",
    "options": ["Deletes module", "Creates alias", "Compiles code", "Exports module"],
    "answer": "B",
    "explanation": "'as' creates an alias name."
},
{
    "id": 60,
    "text": "What is an iterator?",
    "options": ["A loop", "An object producing values one at a time", "A function", "A module"],
    "answer": "B",
    "explanation": "Iterators return elements one by one."
},
{
    "id": 61,
    "text": "Which function converts an iterable into an iterator?",
    "options": ["next()", "iter()", "yield()", "iterator()"],
    "answer": "B",
    "explanation": "iter() returns an iterator."
},
{
    "id": 62,
    "text": "Which function gets the next iterator value?",
    "options": ["next()", "iter()", "yield()", "move()"],
    "answer": "A",
    "explanation": "next() retrieves the next item."
},
{
    "id": 63,
    "text": "Which exception occurs when an iterator is exhausted?",
    "options": ["ValueError", "IteratorError", "StopIteration", "IndexError"],
    "answer": "C",
    "explanation": "StopIteration indicates no more values."
},
{
    "id": 64,
    "text": "Which keyword creates a generator?",
    "options": ["return", "yield", "generate", "iterator"],
    "answer": "B",
    "explanation": "yield turns a function into a generator."
},
{
    "id": 65,
    "text": "Why are generators memory efficient?",
    "options": ["Store all values", "Generate values lazily", "Use cache", "Use recursion"],
    "answer": "B",
    "explanation": "Values are produced only when needed."
},
{
    "id": 66,
    "text": "What is a generator expression?",
    "options": ["(x for x in range(5))", "[x for x in range(5)]", "{x for x in range(5)}", "None"],
    "answer": "A",
    "explanation": "Parentheses create generator expressions."
},
{
    "id": 67,
    "text": "A closure is:",
    "options": ["A loop", "A function remembering outer variables", "A class", "A package"],
    "answer": "B",
    "explanation": "Closures retain access to outer scope variables."
},
{
    "id": 68,
    "text": "Which function is returned in a closure?",
    "options": ["Outer function", "Inner function", "Class method", "Generator"],
    "answer": "B",
    "explanation": "Closures typically return inner functions."
},
{
    "id": 69,
    "text": "What is a decorator?",
    "options": ["A loop", "A module", "A function modifying another function", "A class"],
    "answer": "C",
    "explanation": "Decorators add functionality to functions."
},
{
    "id": 70,
    "text": "Which symbol is commonly used to apply a decorator?",
    "options": ["#", "@", "$", "&"],
    "answer": "B",
    "explanation": "@decorator_name applies a decorator."
},
{
    "id": 71,
    "text": "Which module supports regular expressions?",
    "options": ["regex", "re", "pattern", "regexp"],
    "answer": "B",
    "explanation": "The re module provides regex support."
},
{
    "id": 72,
    "text": "Which function finds all matches in a string?",
    "options": ["find()", "search()", "findall()", "matchall()"],
    "answer": "C",
    "explanation": "findall() returns all matching patterns."
},
{
    "id": 73,
    "text": "What does the pattern [0-9] represent?",
    "options": ["Letters", "Digits", "Spaces", "Symbols"],
    "answer": "B",
    "explanation": "[0-9] matches digits from 0 to 9."
},
{
    "id": 74,
    "text": "What does '^' mean in regex?",
    "options": ["Ends with", "Starts with", "Any character", "Optional"],
    "answer": "B",
    "explanation": "^ matches the start of a string."
},
# QUESTIONS 75-99 (Collections, NumPy, Pandas)

{
    "id": 75,
    "text": "Which module provides Counter?",
    "options": ["math", "collections", "itertools", "statistics"],
    "answer": "B",
    "explanation": "Counter is available in the collections module."
},
{
    "id": 76,
    "text": "What does Counter do?",
    "options": ["Sort data", "Count frequencies", "Generate numbers", "Remove duplicates"],
    "answer": "B",
    "explanation": "Counter counts occurrences of elements."
},
{
    "id": 77,
    "text": "Which collection allows efficient insertion from both ends?",
    "options": ["List", "Tuple", "deque", "Set"],
    "answer": "C",
    "explanation": "deque supports fast insertions/removals at both ends."
},
{
    "id": 78,
    "text": "Which method adds an element to the left side of a deque?",
    "options": ["append()", "push()", "appendleft()", "insert()"],
    "answer": "C",
    "explanation": "appendleft() inserts at the beginning."
},
{
    "id": 79,
    "text": "What is defaultdict used for?",
    "options": ["Sorting", "Default values for missing keys", "Encryption", "Inheritance"],
    "answer": "B",
    "explanation": "defaultdict avoids KeyError by providing defaults."
},
{
    "id": 80,
    "text": "Which default factory returns 0?",
    "options": ["str", "list", "int", "set"],
    "answer": "C",
    "explanation": "int() returns 0 by default."
},
{
    "id": 81,
    "text": "What is NumPy mainly used for?",
    "options": ["Web development", "Numerical computing", "Networking", "GUI"],
    "answer": "B",
    "explanation": "NumPy is designed for numerical and scientific computing."
},
{
    "id": 82,
    "text": "How is NumPy commonly imported?",
    "options": ["import numpy", "import np", "import numpy as np", "include numpy"],
    "answer": "C",
    "explanation": "The standard alias is np."
},
{
    "id": 83,
    "text": "Which function creates a NumPy array?",
    "options": ["np.list()", "np.array()", "np.create()", "np.vector()"],
    "answer": "B",
    "explanation": "np.array() creates arrays."
},
{
    "id": 84,
    "text": "What does ndarray stand for?",
    "options": ["New Data Array", "N-Dimensional Array", "Numeric Data", "None"],
    "answer": "B",
    "explanation": "ndarray means N-Dimensional Array."
},
{
    "id": 85,
    "text": "Which attribute returns the shape of an array?",
    "options": ["size", "shape", "length", "ndim"],
    "answer": "B",
    "explanation": "shape returns rows and columns."
},
{
    "id": 86,
    "text": "Which attribute returns the number of dimensions?",
    "options": ["shape", "size", "ndim", "dtype"],
    "answer": "C",
    "explanation": "ndim returns dimensions."
},
{
    "id": 87,
    "text": "Which function creates an array of zeros?",
    "options": ["np.empty()", "np.zeros()", "np.null()", "np.zero()"],
    "answer": "B",
    "explanation": "np.zeros() creates arrays filled with zeros."
},
{
    "id": 88,
    "text": "Which function creates an identity matrix?",
    "options": ["np.identity()", "np.eye()", "Both A and B", "None"],
    "answer": "C",
    "explanation": "Both can create identity matrices."
},
{
    "id": 89,
    "text": "What does reshape() do?",
    "options": ["Changes values", "Changes dimensions", "Deletes data", "Sorts array"],
    "answer": "B",
    "explanation": "reshape changes the array structure."
},
{
    "id": 90,
    "text": "Which operation performs matrix multiplication?",
    "options": ["+", "-", "np.dot()", "%"],
    "answer": "C",
    "explanation": "np.dot() performs matrix multiplication."
},
{
    "id": 91,
    "text": "What is broadcasting in NumPy?",
    "options": ["Sending data", "Array expansion during operations", "Sorting", "Filtering"],
    "answer": "B",
    "explanation": "Broadcasting applies operations across arrays of different shapes."
},
{
    "id": 92,
    "text": "Which function calculates the mean?",
    "options": ["np.average()", "np.mean()", "Both A and B", "np.sum()"],
    "answer": "C",
    "explanation": "Both can calculate averages."
},
{
    "id": 93,
    "text": "Which library is built on top of NumPy?",
    "options": ["Flask", "Pandas", "Django", "Tkinter"],
    "answer": "B",
    "explanation": "Pandas relies heavily on NumPy."
},
{
    "id": 94,
    "text": "What is a Pandas Series?",
    "options": ["2D structure", "1D labeled array", "Database", "Tuple"],
    "answer": "B",
    "explanation": "Series is a one-dimensional labeled data structure."
},
{
    "id": 95,
    "text": "What is a Pandas DataFrame?",
    "options": ["1D array", "2D tabular structure", "Function", "Iterator"],
    "answer": "B",
    "explanation": "DataFrame stores data in rows and columns."
},
{
    "id": 96,
    "text": "Which function reads a CSV file?",
    "options": ["pd.read()", "pd.csv()", "pd.read_csv()", "pd.import_csv()"],
    "answer": "C",
    "explanation": "pd.read_csv() loads CSV data."
},
{
    "id": 97,
    "text": "Which function shows the first 5 rows?",
    "options": ["head()", "top()", "first()", "show()"],
    "answer": "A",
    "explanation": "head() displays the first rows."
},
{
    "id": 98,
    "text": "Which attribute returns rows and columns count?",
    "options": ["shape", "size", "count", "info"],
    "answer": "A",
    "explanation": "shape returns (rows, columns)."
},
{
    "id": 99,
    "text": "Which function is commonly used to detect missing values?",
    "options": ["isnull()", "missing()", "empty()", "detectnull()"],
    "answer": "A",
    "explanation": "isnull() identifies missing values in a DataFrame."
}
]
