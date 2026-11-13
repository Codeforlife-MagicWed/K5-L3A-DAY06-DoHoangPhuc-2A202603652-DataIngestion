# Manual Audit Packets (Chưa gán nhãn — Dùng cho chấm thủ công)

> Theo `GUIDE.md` & `BENCHMARK.md`: tự chấm thủ công (thang 0–2) cho **Chunk Coherence** (10 vị trí định sẵn trước khi xem điểm) và **Metadata Usefulness + Grounding Quality** (trên toàn bộ tập `test`), tuyệt đối không suy diễn từ exact string match.

## Phần 1 — Chunk Coherence (10 vị trí nguồn cố định trên A, B/C, D)

Các trang kiểm tra xác định trước: `[18, 25, 27, 32, 35, 49, 56, 64, 68, 72]` (mỗi vị trí lấy chunk đầu tiên/giữa đại diện của trang để đối chiếu khả năng tự hiểu trọn ý).

### Trang PDF 18 (Sách: 8, `ch1_statements`, mục `1.1`)
- **A (`openstax-python-2024_p018_c02`, 500 chars):**
  ```text
r can run. Programs help people accomplish everyday tasks, create new technology, and have fun.

The goal of this book is to teach introductory programming and problem solving. Writing programs is a creative activity, inherently useful, and rewarding! No prior background in computer science is necessary to read this book. Many different types of programs exist, as shown in the illustration below. This book will focus on general purpose programs that typically run "behind the scenes."

CHECKPOINT
  ```
- **B (`openstax-python-2024_p018_c02`, 320 chars):**
  ```text
A computer is an electronic device that stores and processes information. Examples of computers include smartphones, tablets, laptops, desktops, and servers. Technically, a program is a sequence of instructions that a computer can run. Programs help people accomplish everyday tasks, create new technology, and have fun.
  ```
- **D (`openstax-python-2024_p018_c02`, 639 chars):**
  ```text
The goal of this book is to teach introductory programming and problem solving.

Writing programs is a creative activity, inherently useful, and rewarding! No prior background in computer science is necessary to read this book.

Many different types of programs exist, as shown in the illustration below. This book will focus on general purpose programs that typically run "behind the scenes."

CHECKPOINT

Online music streaming

Online music streaming; ch 1, video 1 (https://www.openstax.org/r/music-streaming)

CONCEPTS IN PRACTICE

Computers and programs

1 . How many types of programs were described in the animation?
a. 3
b. 4
c. 5
  ```

### Trang PDF 25 (Sách: 15, `ch1_statements`, mục `1.3`)
- **A (`openstax-python-2024_p025_c01`, 500 chars):**
  ```text
a. temperature = 98.5
b. 98.5 = temperature
c. temperature - 23.2

Variable naming rules

A variable name can consist of letters, digits, and underscores and be of any length. The name cannot start with a digit. Ex: 101class is invalid. Also, letter case matters. Ex: Total is different from total. Python's style guide recommends writing variable names in snake case, which is all lowercase with underscores in between each word, such as first_name or total_price.

A name should be short and descri
  ```
- **B (`openstax-python-2024_p025_c01`, 465 chars):**
  ```text
a. temperature = 98.5
b. 98.5 = temperature
c. temperature - 23.2

Variable naming rules

A variable name can consist of letters, digits, and underscores and be of any length. The name cannot start with a digit. Ex: 101class is invalid. Also, letter case matters. Ex: Total is different from total. Python's style guide recommends writing variable names in snake case, which is all lowercase with underscores in between each word, such as first_name or total_price.
  ```
- **D (`openstax-python-2024_p025_c01`, 466 chars):**
  ```text
a. temperature = 98.5
b. 98.5 = temperature
c. temperature - 23.2

Variable naming rules

A variable name can consist of letters, digits, and underscores and be of any length. The name cannot start with a digit. Ex: 101class is invalid. Also, letter case matters. Ex: Total is different from total.

Python's style guide recommends writing variable names in snake case, which is all lowercase with underscores in between each word, such as first_name or total_price.
  ```

### Trang PDF 27 (Sách: 17, `ch1_statements`, mục `1.4`)
- **A (`openstax-python-2024_p027_c01`, 500 chars):**
  ```text
| Valid string | Invalid string |
| --- | --- |
| "I hope you aren't sad." | 'I hope you aren't sad.' |
| 'The teacher said "Correct!" ' | "The teacher said "Correct!" " |

Table 1.3 Rules for strings.

CONCEPTS IN PRACTICE

Valid and invalid strings

1 . Which of the following is a string?
a. Hello!
b. 29
c. "7 days"

2 . Which line of code assigns a string to the variable email?
a. "fred78@gmail.com"
b. "email = fred78@gmail.com"
c. email = "fred78@gmail.com"

3 . Which is a valid string?
a. I
  ```
- **B (`openstax-python-2024_p027_c01`, 465 chars):**
  ```text
| Valid string | Invalid string |
| --- | --- |
| "I hope you aren't sad." | 'I hope you aren't sad.' |
| 'The teacher said "Correct!" ' | "The teacher said "Correct!" " |

Table 1.3 Rules for strings.

CONCEPTS IN PRACTICE

Valid and invalid strings

1 . Which of the following is a string?
a. Hello!
b. 29
c. "7 days"

2 . Which line of code assigns a string to the variable email?
a. "fred78@gmail.com"
b. "email = fred78@gmail.com"
c. email = "fred78@gmail.com"
  ```
- **D (`openstax-python-2024_p027_c01`, 604 chars):**
  ```text
| Valid string | Invalid string |
| --- | --- |
| "I hope you aren't sad." | 'I hope you aren't sad.' |
| 'The teacher said "Correct!" ' | "The teacher said "Correct!" " |

Table 1.3 Rules for strings.

CONCEPTS IN PRACTICE

Valid and invalid strings

1 . Which of the following is a string?
a. Hello!
b. 29
c. "7 days"

2 . Which line of code assigns a string to the variable email?
a. "fred78@gmail.com"
b. "email = fred78@gmail.com"
c. email = "fred78@gmail.com"

3 . Which is a valid string?
a. I know you'll answer correctly!
b. 'I know you'll answer correctly!'
c. "I know you'll answer correctly!"
  ```

### Trang PDF 32 (Sách: 22, `ch1_statements`, mục `1.5`)
- **A (`openstax-python-2024_p032_c01`, 500 chars):**
  ```text
is 7 because multiplication takes precedence over addition. However, (1 + 2) * 3 is 9 because parentheses take precedence over multiplication.

| Operator | Description | Example | Result |
| --- | --- | --- | --- |
| () | Parentheses | (1 + 2) * 3 | 9 |
| ** | Exponentiation | 2 ** 4 | 16 |
| +, - | Positive, negative | -math.pi | -3.14159 |
| *, / | Multiplication, division | 2 * 3 | 6 |
| +, - | Addition, subtraction | 1 + 2 | 3 |

Table 1.4 Operator precedence from highest to lowest.

CHECKP
  ```
- **B (`openstax-python-2024_p032_c01`, 492 chars):**
  ```text
is 7 because multiplication takes precedence over addition. However, (1 + 2) * 3 is 9 because parentheses take precedence over multiplication.

| Operator | Description | Example | Result |
| --- | --- | --- | --- |
| () | Parentheses | (1 + 2) * 3 | 9 |
| ** | Exponentiation | 2 ** 4 | 16 |
| +, - | Positive, negative | -math.pi | -3.14159 |
| *, / | Multiplication, division | 2 * 3 | 6 |
| +, - | Addition, subtraction | 1 + 2 | 3 |

Table 1.4 Operator precedence from highest to lowest.
  ```
- **D (`openstax-python-2024_p032_c01`, 553 chars):**
  ```text
is 7 because multiplication takes precedence over addition. However, (1 + 2) * 3 is 9 because parentheses take precedence over multiplication.

| Operator | Description | Example | Result |
| --- | --- | --- | --- |
| () | Parentheses | (1 + 2) * 3 | 9 |
| ** | Exponentiation | 2 ** 4 | 16 |
| +, - | Positive, negative | -math.pi | -3.14159 |
| *, / | Multiplication, division | 2 * 3 | 6 |
| +, - | Addition, subtraction | 1 + 2 | 3 |

Table 1.4 Operator precedence from highest to lowest.

CHECKPOINT

Order of operations in an arithmetic expression
  ```

### Trang PDF 35 (Sách: 25, `ch1_statements`, mục `1.6`)
- **A (`openstax-python-2024_p035_c01`, 500 chars):**
  ```text
Common types of errors

Different types of errors may occur when running Python programs. When an error occurs, knowing the type of error gives insight about how to correct the error. The following table shows examples of mistakes that anyone could make when programming.

| Mistake | Error message | Explanation |
| --- | --- | --- |
| print("Have a nice day!" | SyntaxError: unexpected EOF while parsing | The closing parenthesis is missing. Python is surprised to reach the end of file (EOF) befor
  ```
- **B (`openstax-python-2024_p035_c01`, 271 chars):**
  ```text
Common types of errors

Different types of errors may occur when running Python programs. When an error occurs, knowing the type of error gives insight about how to correct the error. The following table shows examples of mistakes that anyone could make when programming.
  ```
- **D (`openstax-python-2024_p035_c01`, 272 chars):**
  ```text
Common types of errors

Different types of errors may occur when running Python programs. When an error occurs, knowing the type of error gives insight about how to correct the error.

The following table shows examples of mistakes that anyone could make when programming.
  ```

### Trang PDF 49 (Sách: 39, `ch2_expressions`, mục `2.1`)
- **A (`openstax-python-2024_p049_c02`, 499 chars):**
  ```text
down arrow displays the next line. That way, the user can repeat a line without having to type the line again.

CHECKPOINT

Correcting a typo

Correcting a typo; ch 2, video 2 (https://www.openstax.org/r/correcting-typo)

CONCEPTS IN PRACTICE

Using the arrow keys

4 . Which arrow keys were needed to edit the typo?
a. only the up arrow key
b. the up and down arrows
c. the up and left arrows

5 . What keys would the user press to go back two lines?
a. press the up arrow twice
b. press the down a
  ```
- **B (`openstax-python-2024_p049_c02`, 450 chars):**
  ```text
Most shells maintain a history of every line of code the user types. Pressing the up or down arrow key on the keyboard displays the history. The up arrow displays the previous line; the down arrow displays the next line. That way, the user can repeat a line without having to type the line again.

CHECKPOINT

Correcting a typo

Correcting a typo; ch 2, video 2 (https://www.openstax.org/r/correcting-typo)

CONCEPTS IN PRACTICE

Using the arrow keys
  ```
- **D (`openstax-python-2024_p049_c02`, 640 chars):**
  ```text
CHECKPOINT

Correcting a typo

Correcting a typo; ch 2, video 2 (https://www.openstax.org/r/correcting-typo)

CONCEPTS IN PRACTICE

Using the arrow keys

4 . Which arrow keys were needed to edit the typo?
a. only the up arrow key
b. the up and down arrows
c. the up and left arrows

5 . What keys would the user press to go back two lines?
a. press the up arrow twice
b. press the down arrow twice
c. press the left arrow twice

TRY IT

Exploring the shell

Running code interactively is a great way to learn how Python works. Open a Python shell on your computer, or use the one at python.org/shell (https://openstax.org/r/100pythonshell).
  ```

### Trang PDF 56 (Sách: 46, `ch2_expressions`, mục `2.4`)
- **A (`openstax-python-2024_p056_c02`, 499 chars):**
  ```text
n numerical inaccuracies related to floating-point representation.
• Use the round() function to mitigate floating-point errors in output. Floating-point errors

Computers store information using 0's and 1's. All information must be converted to a string of 0's and 1's. Ex: 5 is converted to 101. Since only two values, 0 or 1, are allowed the format is called binary.

Floating-point values are stored as binary by Python. The conversion of a floating point number to the underlying binary results
  ```
- **B (`openstax-python-2024_p056_c02`, 377 chars):**
  ```text
• Explain numerical inaccuracies related to floating-point representation.
• Use the round() function to mitigate floating-point errors in output. Floating-point errors

Computers store information using 0's and 1's. All information must be converted to a string of 0's and 1's. Ex: 5 is converted to 101. Since only two values, 0 or 1, are allowed the format is called binary.
  ```
- **D (`openstax-python-2024_p056_c02`, 608 chars):**
  ```text
Computers store information using 0's and 1's. All information must be converted to a string of 0's and 1's. Ex: 5 is converted to 101. Since only two values, 0 or 1, are allowed the format is called binary.

Floating-point values are stored as binary by Python. The conversion of a floating point number to the underlying binary results in specific types of floating-point errors.

A round-off error occurs when floating-point values are stored erroneously as an approximation.

The difference between an approximation of a value used in computation and the correct (true) value is called a round-off error.
  ```

### Trang PDF 64 (Sách: 54, `ch2_expressions`, mục `2.6`)
- **A (`openstax-python-2024_p064_c01`, 500 chars):**
  ```text
| Function | Description | Examples |
| --- | --- | --- |
| **Number-theoretic** |  |  |
| math.ceil(x) | The ceiling of x: the smallest integer greater than or equal to x. | math.ceil(7.4) 8 math.ceil(-7.4) -7 |
| math.floor(x) | The floor of x: the largest integer less than or equal to x. | math.floor(7.4) 7 math.floor(-7.4) -8 |
| **Power and logarithmic** |  |  |
| math.log(x) | The natural logarithm of x (to base e). | math.log(math.e) 1.0 math.log(0) ValueError: math domain error |
| math.
  ```
- **B (`openstax-python-2024_p064_c01`, 492 chars):**
  ```text
| Function | Description | Examples |
| --- | --- | --- |
| **Number-theoretic** |  |  |
| math.ceil(x) | The ceiling of x: the smallest integer greater than or equal to x. | math.ceil(7.4) 8 math.ceil(-7.4) -7 |
| math.floor(x) | The floor of x: the largest integer less than or equal to x. | math.floor(7.4) 7 math.floor(-7.4) -8 |
| **Power and logarithmic** |  |  |
| math.log(x) | The natural logarithm of x (to base e). | math.log(math.e) 1.0 math.log(0) ValueError: math domain error |
  ```
- **D (`openstax-python-2024_p064_c01`, 599 chars):**
  ```text
| Function | Description | Examples |
| --- | --- | --- |
| **Number-theoretic** |  |  |
| math.ceil(x) | The ceiling of x: the smallest integer greater than or equal to x. | math.ceil(7.4) 8 math.ceil(-7.4) -7 |
| math.floor(x) | The floor of x: the largest integer less than or equal to x. | math.floor(7.4) 7 math.floor(-7.4) -8 |
| **Power and logarithmic** |  |  |
| math.log(x) | The natural logarithm of x (to base e). | math.log(math.e) 1.0 math.log(0) ValueError: math domain error |
| math.log(x, base) | The logarithm of x to the given base. | math.log(8, 2) 3.0 math.log(10000, 10) 4.0 |
  ```

### Trang PDF 68 (Sách: 58, `ch2_expressions`, mục `2.7`)
- **A (`openstax-python-2024_p068_c01`, 500 chars):**
  ```text
| Guideline | Example | Common Mistakes |
| --- | --- | --- |
| Parentheses: no space before or after. | print("Go team!") | print ("Go team!") print( "Go team!" ) |
| Commas: no space before, one space after. | print("Hello", name) | print("Hello" , name) print("Hello",name) |
| Assignment: one space before and after the =. | name = input("Your name? ") | name=input("Your name? ") name= input("Your name? ") name =input("Your name? ") |
| Concatenation: one space before and after the +. | print(
  ```
- **B (`openstax-python-2024_p068_c01`, 440 chars):**
  ```text
| Guideline | Example | Common Mistakes |
| --- | --- | --- |
| Parentheses: no space before or after. | print("Go team!") | print ("Go team!") print( "Go team!" ) |
| Commas: no space before, one space after. | print("Hello", name) | print("Hello" , name) print("Hello",name) |
| Assignment: one space before and after the =. | name = input("Your name? ") | name=input("Your name? ") name= input("Your name? ") name =input("Your name? ") |
  ```
- **D (`openstax-python-2024_p068_c01`, 589 chars):**
  ```text
| Guideline | Example | Common Mistakes |
| --- | --- | --- |
| Parentheses: no space before or after. | print("Go team!") | print ("Go team!") print( "Go team!" ) |
| Commas: no space before, one space after. | print("Hello", name) | print("Hello" , name) print("Hello",name) |
| Assignment: one space before and after the =. | name = input("Your name? ") | name=input("Your name? ") name= input("Your name? ") name =input("Your name? ") |
| Concatenation: one space before and after the +. | print("Hi", name + "!") | print("Hi", name+"!") print("Hi", name+ "!") print("Hi", name +"!") |
  ```

### Trang PDF 72 (Sách: 62, `ch2_expressions`, mục `2.8`)
- **A (`openstax-python-2024_p072_c01`, 500 chars):**
  ```text
2.8 Python careers

Learning objectives

By the end of this section you should be able to

• Summarize how Python is used in fields other than CS and IT.
• Describe two different kinds of applications made with Python. Fields and applications

Learning Python opens the door to many programming-related careers. Example job titles include software engineer, data scientist, web developer, and systems analyst. These jobs often require a degree in computer science (CS), information technology (IT), o
  ```
- **B (`openstax-python-2024_p072_c01`, 242 chars):**
  ```text
2.8 Python careers

Learning objectives

By the end of this section you should be able to

• Summarize how Python is used in fields other than CS and IT.
• Describe two different kinds of applications made with Python. Fields and applications
  ```
- **D (`openstax-python-2024_p072_c01`, 584 chars):**
  ```text
2.8 Python careers

Learning objectives

By the end of this section you should be able to

• Summarize how Python is used in fields other than CS and IT.
• Describe two different kinds of applications made with Python. Fields and applications

Learning Python opens the door to many programming-related careers. Example job titles include software engineer, data scientist, web developer, and systems analyst.

These jobs often require a degree in computer science (CS), information technology (IT), or a related field. However, programming is not limited to these fields and careers.
  ```

## Phần 2 — Metadata Usefulness & Grounding Quality (Tập `test`)

### q16 (`direct` | gold_page=30 | valid_pages=[30] | filter=None)
- **Câu hỏi:** Python hỗ trợ hai định dạng số cơ bản (basic number formats) nào, và mỗi định dạng biểu diễn loại số gì?
- **Đáp án chuẩn:** Python hỗ trợ hai định dạng số cơ bản là số nguyên (integer) biểu diễn số nguyên tròn (whole number) và số thực dấu phẩy động (floating-point) biểu diễn số thập phân (decimal number).
- **Evidence gốc:** `Python supports two basic number formats, integer and floating-point. An integer represents a whole number, and a floating-point format represents a decimal number.`

#### Chiến lược A (Auto proxy: `Hit@1=True`, `Hit@3=True`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p030_c01` | `score=0.7161` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=30` (`book=20`, `chapter=ch1_statements`, `section=1.5`)
  ```text
• Explain the precedence of arithmetic operators. Numeric data types

Python supports two basic number formats, integer and floating-point. An integer represents a whole number, and a floating-point format represents a decimal number. The format a language uses to represent data is called a data type. In addition to integer and floating-point types, programming languages typically have a string type for representing text.

CHECKPOINT

Integer and floating-point

Integer and floating point; ch 1,
  ```
- **Rank 2** | `openstax-python-2024_p056_c04` | `score=0.6828` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=56` (`book=46`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
015625)10 when converted back, which is not exactly equal to (0.1)10.

| Col 1 | Col 2 |
| --- | --- |
| # Print floats with 30 decimal places print(f'{0.1:.30f}') # prints 0.1 print(f'{0.2:.30f}') # prints 0.2 print(f'{0.4:.30f}') # prints 0.4 | 0.100000000000000005551115123126 0.200000000000000011102230246252 0.400000000000000022204460492503 |

Table 2.1 Round-off error. (The example above shows a formatted string or f-string, which are introduced in the Objects chapter.)

An overflow error oc
  ```
- **Rank 3** | `openstax-python-2024_p047_c04` | `score=0.6824` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=47` (`book=37`, `chapter=ch2_expressions`, `section=2.0`)
  ```text
details about integers and floating-point numbers, explain how to import and use the math module, and show how to make long lines of code easier to read.
  ```
#### Chiến lược B (Auto proxy: `Hit@1=True`, `Hit@3=True`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p030_c01` | `score=0.7179` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=30` (`book=20`, `chapter=ch1_statements`, `section=1.5`)
  ```text
• Explain the precedence of arithmetic operators. Numeric data types

Python supports two basic number formats, integer and floating-point. An integer represents a whole number, and a floating-point format represents a decimal number. The format a language uses to represent data is called a data type. In addition to integer and floating-point types, programming languages typically have a string type for representing text.

CHECKPOINT

Integer and floating-point
  ```
- **Rank 2** | `openstax-python-2024_p030_c03` | `score=0.6844` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=30` (`book=20`, `chapter=ch1_statements`, `section=1.5`)
  ```text
a. string
b. int
c. float

Basic arithmetic

Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, and division.

Four basic arithmetic operators exist in Python:

1. Addition (+)
2. Subtraction (-)
  ```
- **Rank 3** | `openstax-python-2024_p056_c03` | `score=0.6819` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=56` (`book=46`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
Floating-point values are stored as binary by Python. The conversion of a floating point number to the underlying binary results in specific types of floating-point errors.

A round-off error occurs when floating-point values are stored erroneously as an approximation. The difference between an approximation of a value used in computation and the correct (true) value is called a round-off error.
  ```
#### Chiến lược C (Auto proxy: `Hit@1=True`, `Hit@3=True`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p030_c01` | `score=0.7179` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=30` (`book=20`, `chapter=ch1_statements`, `section=1.5`)
  ```text
• Explain the precedence of arithmetic operators. Numeric data types

Python supports two basic number formats, integer and floating-point. An integer represents a whole number, and a floating-point format represents a decimal number. The format a language uses to represent data is called a data type. In addition to integer and floating-point types, programming languages typically have a string type for representing text.

CHECKPOINT

Integer and floating-point
  ```
- **Rank 2** | `openstax-python-2024_p030_c03` | `score=0.6844` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=30` (`book=20`, `chapter=ch1_statements`, `section=1.5`)
  ```text
a. string
b. int
c. float

Basic arithmetic

Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, and division.

Four basic arithmetic operators exist in Python:

1. Addition (+)
2. Subtraction (-)
  ```
- **Rank 3** | `openstax-python-2024_p056_c03` | `score=0.6819` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=56` (`book=46`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
Floating-point values are stored as binary by Python. The conversion of a floating point number to the underlying binary results in specific types of floating-point errors.

A round-off error occurs when floating-point values are stored erroneously as an approximation. The difference between an approximation of a value used in computation and the correct (true) value is called a round-off error.
  ```
#### Chiến lược D (Auto proxy: `Hit@1=True`, `Hit@3=True`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p030_c01` | `score=0.7079` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=30` (`book=20`, `chapter=ch1_statements`, `section=1.5`)
  ```text
• Explain the precedence of arithmetic operators. Numeric data types

Python supports two basic number formats, integer and floating-point. An integer represents a whole number, and a floating-point format represents a decimal number.

The format a language uses to represent data is called a data type. In addition to integer and floating-point types, programming languages typically have a string type for representing text.

CHECKPOINT

Integer and floating-point

Integer and floating point; ch 1, video 8 (https://www.openstax.org/r/integer-and-floating-point)

CONCEPTS IN PRACTICE

Integers, floats, and strings
  ```
- **Rank 2** | `openstax-python-2024_p056_c03` | `score=0.6878` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=56` (`book=46`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
Ex: Storing the float (0.1)10 results in binary values that actually produce (0.1000000000000000055511151231257827021181583404541015625)10 when converted back, which is not exactly equal to (0.1)10.

| Col 1 | Col 2 |
| --- | --- |
| # Print floats with 30 decimal places print(f'{0.1:.30f}') # prints 0.1 print(f'{0.2:.30f}') # prints 0.2 print(f'{0.4:.30f}') # prints 0.4 | 0.100000000000000005551115123126 0.200000000000000011102230246252 0.400000000000000022204460492503 |

Table 2.1 Round-off error. (The example above shows a formatted string or f-string, which are introduced in the Objects chapter.)
  ```
- **Rank 3** | `openstax-python-2024_p056_c02` | `score=0.6831` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=56` (`book=46`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
Computers store information using 0's and 1's. All information must be converted to a string of 0's and 1's. Ex: 5 is converted to 101. Since only two values, 0 or 1, are allowed the format is called binary.

Floating-point values are stored as binary by Python. The conversion of a floating point number to the underlying binary results in specific types of floating-point errors.

A round-off error occurs when floating-point values are stored erroneously as an approximation.

The difference between an approximation of a value used in computation and the correct (true) value is called a round-off error.
  ```

### q17 (`paraphrase` | gold_page=39 | valid_pages=[39, 44] | filter=None)
- **Câu hỏi:** Chuỗi văn bản tùy chọn đặt ở đầu một chương trình Python dùng để làm tài liệu mô tả được gọi là gì, và thường được viết bằng cú pháp nào khi nội dung dài?
- **Đáp án chuẩn:** Chuỗi đó được gọi là docstring, và vì tài liệu mô tả có thể dài nên docstring thường được viết dưới dạng chuỗi nhiều dòng (multi-line strings) sử dụng cặp 3 dấu nháy kép (""").
- **Evidence gốc:** `Python programs may optionally begin with a string known as a docstring. ... Documentation can be long, so docstrings are generally written as multi-line strings (""").`

#### Chiến lược A (Auto proxy: `Hit@1=True`, `Hit@3=True`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p039_c01` | `score=0.7397` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=39` (`book=29`, `chapter=ch1_statements`, `section=1.7`)
  ```text
c. insert a # at the beginning of the line.

Documentation

Python programs may optionally begin with a string known as a docstring. A docstring is documentation written for others who will use the program but not necessarily read the source code. Most of the official documentation at docs.python.org (https://openstax.org/r/100docstrings) is generated from docstrings.

Documentation can be long, so docstrings are generally written as multi-line strings ("""). Common elements of a docstring inclu
  ```
- **Rank 2** | `openstax-python-2024_p044_c03` | `score=0.7337` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=44` (`book=34`, `chapter=ch1_statements`, `section=1.9`)
  ```text
Used for documentation, often in multi-line strings, to summarize a program's purpose or usage. |

Table 1.6 Chapter 1 reference.

TRY IT

Fun facts

Write a program that assigns a variable named number to any integer of your choice. Ex: number = 74. Then, use this variable to calculate and output the following results:
  ```
- **Rank 3** | `openstax-python-2024_p039_c02` | `score=0.7257` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=39` (`book=29`, `chapter=ch1_statements`, `section=1.7`)
  ```text
trings ("""). Common elements of a docstring include a one-line summary, a blank line, and a longer description.

CHECKPOINT

Vacations docstring

Vacations docstring; ch 1, video 13 (https://www.openstax.org/r/docstring)

CONCEPTS IN PRACTICE

Documentation

7 . The main purpose of writing docstrings is to . . .
a. summarize the program's purpose or usage.
b. explain how each part of the code works.
c. maintain a list of ideas for new features.

8 . Which of the following is NOT a docstring?
a.
  ```
#### Chiến lược B (Auto proxy: `Hit@1=False`, `Hit@3=False`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p039_c01` | `score=0.7381` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=39` (`book=29`, `chapter=ch1_statements`, `section=1.7`)
  ```text
c. insert a # at the beginning of the line.

Documentation

Python programs may optionally begin with a string known as a docstring. A docstring is documentation written for others who will use the program but not necessarily read the source code. Most of the official documentation at docs.python.org (https://openstax.org/r/100docstrings) is generated from docstrings.
  ```
- **Rank 2** | `openstax-python-2024_p039_c02` | `score=0.7348` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=39` (`book=29`, `chapter=ch1_statements`, `section=1.7`)
  ```text
Documentation can be long, so docstrings are generally written as multi-line strings ("""). Common elements of a docstring include a one-line summary, a blank line, and a longer description.

CHECKPOINT

Vacations docstring

Vacations docstring; ch 1, video 13 (https://www.openstax.org/r/docstring)

CONCEPTS IN PRACTICE

Documentation
  ```
- **Rank 3** | `openstax-python-2024_p040_c02` | `score=0.7229` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=40` (`book=30`, `chapter=ch1_statements`, `section=1.8`)
  ```text
Write a docstring for the following program. The first line of the docstring should explain, in one short sentence, what the program is. The second line of the docstring should be blank. The third and subsequent lines should include a longer explanation of what the program does. At the end of the docstring, add a line that says "Author: " followed by your name.

Access multimedia content (http://openstax.org/books/introduction-python-programming/pages/1-7-comments)

1.8 Why Python?
  ```
#### Chiến lược C (Auto proxy: `Hit@1=False`, `Hit@3=False`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p039_c01` | `score=0.7381` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=39` (`book=29`, `chapter=ch1_statements`, `section=1.7`)
  ```text
c. insert a # at the beginning of the line.

Documentation

Python programs may optionally begin with a string known as a docstring. A docstring is documentation written for others who will use the program but not necessarily read the source code. Most of the official documentation at docs.python.org (https://openstax.org/r/100docstrings) is generated from docstrings.
  ```
- **Rank 2** | `openstax-python-2024_p039_c02` | `score=0.7348` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=39` (`book=29`, `chapter=ch1_statements`, `section=1.7`)
  ```text
Documentation can be long, so docstrings are generally written as multi-line strings ("""). Common elements of a docstring include a one-line summary, a blank line, and a longer description.

CHECKPOINT

Vacations docstring

Vacations docstring; ch 1, video 13 (https://www.openstax.org/r/docstring)

CONCEPTS IN PRACTICE

Documentation
  ```
- **Rank 3** | `openstax-python-2024_p040_c02` | `score=0.7229` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=40` (`book=30`, `chapter=ch1_statements`, `section=1.8`)
  ```text
Write a docstring for the following program. The first line of the docstring should explain, in one short sentence, what the program is. The second line of the docstring should be blank. The third and subsequent lines should include a longer explanation of what the program does. At the end of the docstring, add a line that says "Author: " followed by your name.

Access multimedia content (http://openstax.org/books/introduction-python-programming/pages/1-7-comments)

1.8 Why Python?
  ```
#### Chiến lược D (Auto proxy: `Hit@1=True`, `Hit@3=True`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p039_c01` | `score=0.7390` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=39` (`book=29`, `chapter=ch1_statements`, `section=1.7`)
  ```text
c. insert a # at the beginning of the line.

Documentation

Python programs may optionally begin with a string known as a docstring. A docstring is documentation written for others who will use the program but not necessarily read the source code.

Most of the official documentation at docs.python.org (https://openstax.org/r/100docstrings) is generated from docstrings.

Documentation can be long, so docstrings are generally written as multi-line strings ("""). Common elements of a docstring include a one-line summary, a blank line, and a longer description.

CHECKPOINT

Vacations docstring
  ```
- **Rank 2** | `openstax-python-2024_p039_c03` | `score=0.7189` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=39` (`book=29`, `chapter=ch1_statements`, `section=1.7`)
  ```text
c. # Vacations Madlib. # # This program asks the user for two adjectives # and two nouns, which are then used to print # a funny story about a vacation.

9 . Which docstring is most useful for this program?
a. """Vacations Madlib."""

b. """Vacations Madlib. This program asks the user for two adjectives and two nouns, which are then used to print a funny story about a vacation. """

c. """Vacations Madlib. This program asks the user for two adjectives and two nouns, which are then used to print a funny story about a vacation.
  ```
- **Rank 3** | `openstax-python-2024_p037_c01` | `score=0.7078` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=37` (`book=27`, `chapter=ch1_statements`, `section=1.7`)
  ```text
1.7 Comments

Learning objectives

By the end of this section you should be able to

• Write concise, meaningful comments that explain intended functionality of the code.
• Write a docstring (more verbose comment) that describes the program functionality. The hash character

Comments are short phrases that explain what the code is doing. Ex: Lines 1, 8, and 10 in the following program contain comments. Each comment begins with a hash character (#).

All text from the hash character to the end of the line is ignored when running the program. In contrast, hash characters inside of strings are treated as regular text.
  ```

### q18 (`conditional` | gold_page=54 | valid_pages=[54] | filter=None)
- **Câu hỏi:** Những phép toán số học nào không tương thích giữa kiểu chuỗi (string) và kiểu số (numeric), và toán tử * hoạt động thế nào khi dùng giữa một chuỗi và một số nguyên?
- **Đáp án chuẩn:** Kiểu chuỗi và kiểu số không tương thích trong các phép cộng, trừ và chia; tuy nhiên toán tử * đóng vai trò là toán tử lặp (repetition operator), nhận một toán hạng chuỗi và một toán hạng số nguyên để lặp lại chuỗi đó.
- **Evidence gốc:** `Strings and numeric data types are incompatible for addition, subtraction, and division. ... The * operator also serves as the repetition operator, which accepts a string operand and an integer operand and repeats the string.`

#### Chiến lược A (Auto proxy: `Hit@1=True`, `Hit@3=True`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p054_c02` | `score=0.7794` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=54` (`book=44`, `chapter=ch2_expressions`, `section=2.3`)
  ```text
s the number in a calculation. This results in an error in the program because the input() function by default stores the number as a string. Strings and numeric data types are incompatible for addition, subtraction, and division. One of the operands needs to be explicitly converted depending on the goal of arithmetic or string concatenation.

The * operator also serves as the repetition operator, which accepts a string operand and an integer operand and repeats the string. Ex: "banjo" * 3 produ
  ```
- **Rank 2** | `openstax-python-2024_p054_c03` | `score=0.7271` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=54` (`book=44`, `chapter=ch2_expressions`, `section=2.3`)
  ```text
rand and repeats the string. Ex: "banjo" * 3 produces "banjobanjobanjo".

CHECKPOINT

Adding a string and an integer

Adding a string and an integer; ch 2, video 6 (https://www.openstax.org/r/adding-str-int)
  ```
- **Rank 3** | `openstax-python-2024_p055_c01` | `score=0.7232` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=55` (`book=45`, `chapter=ch2_expressions`, `section=2.3`)
  ```text
CONCEPTS IN PRACTICE

Operations combining numeric types and strings

8 . int('34') + 56
a. '3456'
b. 90
c. '90'

9 . str(12) + ' red roses'
a. '12 red roses'
b. '12'
c. Error

10 . '50' * 3
a. '150'
b. 150
c. '505050'

11 . str(5.2) + 7
a. 12.2
b. '12.2'
c. Error

12 . 80.0 + int('100')
a. 180
b. 180.0
c. '180'

13 . str(3.14) + '159'
a. 162.14
b. '3.14159'
c. Error

14 . 2.0 * 'this'
a. 'this'
b. 'thisthis'
c. Error

TRY IT

After the point

Write a program that reads in a string of digits tha
  ```
#### Chiến lược B (Auto proxy: `Hit@1=False`, `Hit@3=False`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p054_c03` | `score=0.7715` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=54` (`book=44`, `chapter=ch2_expressions`, `section=2.3`)
  ```text
One of the operands needs to be explicitly converted depending on the goal of arithmetic or string concatenation.

The * operator also serves as the repetition operator, which accepts a string operand and an integer operand and repeats the string. Ex: "banjo" * 3 produces "banjobanjobanjo".

CHECKPOINT

Adding a string and an integer

Adding a string and an integer; ch 2, video 6 (https://www.openstax.org/r/adding-str-int)
  ```
- **Rank 2** | `openstax-python-2024_p055_c01` | `score=0.7214` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=55` (`book=45`, `chapter=ch2_expressions`, `section=2.3`)
  ```text
CONCEPTS IN PRACTICE

Operations combining numeric types and strings

8 . int('34') + 56
a. '3456'
b. 90
c. '90'

9 . str(12) + ' red roses'
a. '12 red roses'
b. '12'
c. Error

10 . '50' * 3
a. '150'
b. 150
c. '505050'

11 . str(5.2) + 7
a. 12.2
b. '12.2'
c. Error

12 . 80.0 + int('100')
a. 180
b. 180.0
c. '180'

13 . str(3.14) + '159'
a. 162.14
b. '3.14159'
c. Error

14 . 2.0 * 'this'
a. 'this'
b. 'thisthis'
c. Error

TRY IT

After the point
  ```
- **Rank 3** | `openstax-python-2024_p044_c01` | `score=0.7198` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=44` (`book=34`, `chapter=ch1_statements`, `section=1.9`)
  ```text
| Function | Description |
| --- | --- |
| = (Assignment) | Assigns (or updates) the value of a variable. In Python, variables begin to exist when assigned for the first time. |
| + (Concatenation) | Appends the contents of two strings, resulting in a new string. |
| + (Addition) | Adds the values of two numbers. |
| - (Subtraction) | Subtracts the value of one number from another. |
| * (Multiplication) | Multiplies the values of two numbers. |
  ```
#### Chiến lược C (Auto proxy: `Hit@1=False`, `Hit@3=False`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p054_c03` | `score=0.7715` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=54` (`book=44`, `chapter=ch2_expressions`, `section=2.3`)
  ```text
One of the operands needs to be explicitly converted depending on the goal of arithmetic or string concatenation.

The * operator also serves as the repetition operator, which accepts a string operand and an integer operand and repeats the string. Ex: "banjo" * 3 produces "banjobanjobanjo".

CHECKPOINT

Adding a string and an integer

Adding a string and an integer; ch 2, video 6 (https://www.openstax.org/r/adding-str-int)
  ```
- **Rank 2** | `openstax-python-2024_p055_c01` | `score=0.7214` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=55` (`book=45`, `chapter=ch2_expressions`, `section=2.3`)
  ```text
CONCEPTS IN PRACTICE

Operations combining numeric types and strings

8 . int('34') + 56
a. '3456'
b. 90
c. '90'

9 . str(12) + ' red roses'
a. '12 red roses'
b. '12'
c. Error

10 . '50' * 3
a. '150'
b. 150
c. '505050'

11 . str(5.2) + 7
a. 12.2
b. '12.2'
c. Error

12 . 80.0 + int('100')
a. 180
b. 180.0
c. '180'

13 . str(3.14) + '159'
a. 162.14
b. '3.14159'
c. Error

14 . 2.0 * 'this'
a. 'this'
b. 'thisthis'
c. Error

TRY IT

After the point
  ```
- **Rank 3** | `openstax-python-2024_p044_c01` | `score=0.7198` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=44` (`book=34`, `chapter=ch1_statements`, `section=1.9`)
  ```text
| Function | Description |
| --- | --- |
| = (Assignment) | Assigns (or updates) the value of a variable. In Python, variables begin to exist when assigned for the first time. |
| + (Concatenation) | Appends the contents of two strings, resulting in a new string. |
| + (Addition) | Adds the values of two numbers. |
| - (Subtraction) | Subtracts the value of one number from another. |
| * (Multiplication) | Multiplies the values of two numbers. |
  ```
#### Chiến lược D (Auto proxy: `Hit@1=True`, `Hit@3=True`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p054_c02` | `score=0.7747` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=54` (`book=44`, `chapter=ch2_expressions`, `section=2.3`)
  ```text
This results in an error in the program because the input() function by default stores the number as a string. Strings and numeric data types are incompatible for addition, subtraction, and division.

One of the operands needs to be explicitly converted depending on the goal of arithmetic or string concatenation.

The * operator also serves as the repetition operator, which accepts a string operand and an integer operand and repeats the string. Ex: "banjo" * 3 produces "banjobanjobanjo".

CHECKPOINT

Adding a string and an integer

Adding a string and an integer; ch 2, video 6 (https://www.openstax.org/r/adding-str-int)
  ```
- **Rank 2** | `openstax-python-2024_p055_c01` | `score=0.7215` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=55` (`book=45`, `chapter=ch2_expressions`, `section=2.3`)
  ```text
CONCEPTS IN PRACTICE

Operations combining numeric types and strings

8 . int('34') + 56
a. '3456'
b. 90
c. '90'

9 . str(12) + ' red roses'
a. '12 red roses'
b. '12'
c. Error

10 . '50' * 3
a. '150'
b. 150
c. '505050'

11 . str(5.2) + 7
a. 12.2
b. '12.2'
c. Error

12 . 80.0 + int('100')
a. 180
b. 180.0
c. '180'

13 . str(3.14) + '159'
a. 162.14
b. '3.14159'
c. Error

14 . 2.0 * 'this'
a. 'this'
b. 'thisthis'
c. Error

TRY IT

After the point

Write a program that reads in a string of digits that represents the digits after the decimal point of a number, num. Concatenate the input string together with '.' and num, and print the result.
  ```
- **Rank 3** | `openstax-python-2024_p044_c01` | `score=0.7060` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=44` (`book=34`, `chapter=ch1_statements`, `section=1.9`)
  ```text
| Function | Description |
| --- | --- |
| = (Assignment) | Assigns (or updates) the value of a variable. In Python, variables begin to exist when assigned for the first time. |
| + (Concatenation) | Appends the contents of two strings, resulting in a new string. |
| + (Addition) | Adds the values of two numbers. |
| - (Subtraction) | Subtracts the value of one number from another. |
| * (Multiplication) | Multiplies the values of two numbers. |
| /(Division) | Divides the value of one number by another. |
| ** (Exponentiation) | Raises a number to a power. Ex: 3**2 is three squared. |
| Syntax | Description |
  ```

### q19 (`conditional` | gold_page=57 | valid_pages=[57, 74] | filter=None)
- **Câu hỏi:** Hàm round() trong Python dùng để làm gì, và điều gì xảy ra nếu đối số thứ hai không được truyền vào?
- **Đáp án chuẩn:** Hàm round() dùng để làm tròn một số thực dấu phẩy động đến một số chữ số thập phân nhất định. Nếu đối số thứ hai không được cung cấp, số đó sẽ được làm tròn đến số nguyên gần nhất (closest integer).
- **Evidence gốc:** `Python's round() function is used to round a floating-point number to a given number of decimal places. The function requires two arguments. The first argument is the number to be rounded. The second argument decides the number of decimal places to which the number is rounded. If the second argument is not provided, the number will be rounded to the closest integer.`

#### Chiến lược A (Auto proxy: `Hit@1=True`, `Hit@3=True`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p057_c03` | `score=0.7285` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=57` (`book=47`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
b. overflow

Floating point round() function

Python's round() function is used to round a floating-point number to a given number of decimal places. The function requires two arguments. The first argument is the number to be rounded. The second argument decides the number of decimal places to which the number is rounded. If the second argument is not provided, the number will be rounded to the closest integer. The round() function can be used to mitigate floating-point errors.

Ex:

• round(2.
  ```
- **Rank 2** | `openstax-python-2024_p057_c04` | `score=0.7169` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=57` (`book=47`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
o mitigate floating-point errors.

Ex:

• round(2.451, 2) = 2.45
• round(2.451) = 2

CHECKPOINT

Examples of round() function

Examples of a round () function; ch 2, video 7 (https://www.openstax.org/r/round-function)
  ```
- **Rank 3** | `openstax-python-2024_p058_c01` | `score=0.7029` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=58` (`book=48`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
CONCEPTS IN PRACTICE

Examples of round() function

3 . What is the output of round(6.6)?
a. 6
b. 6.6
c. 7

4 . What is the output of round(3.5, 2)?
a. 3
b. 3.5
c. 3.50

5 . What is the output of round(12)?
a. 12.0
b. 12
c. 12.00

6 . What is the output of round(0.1, 1)?
a. 0.1
b. 0.10
c. 0.1000000000000000055511151231257827021181583404541015625

TRY IT

Inaccurate tips

The following code calculates the tip amount, given a bill amount and the tip ratio. Experiment with the following bill amount
  ```
#### Chiến lược B (Auto proxy: `Hit@1=True`, `Hit@3=True`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p057_c04` | `score=0.7840` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=57` (`book=47`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
Python's round() function is used to round a floating-point number to a given number of decimal places. The function requires two arguments. The first argument is the number to be rounded. The second argument decides the number of decimal places to which the number is rounded. If the second argument is not provided, the number will be rounded to the closest integer. The round() function can be used to mitigate floating-point errors.

Ex:

• round(2.451, 2) = 2.45
• round(2.451) = 2

CHECKPOINT
  ```
- **Rank 2** | `openstax-python-2024_p058_c01` | `score=0.7107` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=58` (`book=48`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
CONCEPTS IN PRACTICE

Examples of round() function

3 . What is the output of round(6.6)?
a. 6
b. 6.6
c. 7

4 . What is the output of round(3.5, 2)?
a. 3
b. 3.5
c. 3.50

5 . What is the output of round(12)?
a. 12.0
b. 12
c. 12.00

6 . What is the output of round(0.1, 1)?
a. 0.1
b. 0.10
c. 0.1000000000000000055511151231257827021181583404541015625

TRY IT

Inaccurate tips
  ```
- **Rank 3** | `openstax-python-2024_p074_c02` | `score=0.6861` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=74` (`book=64`, `chapter=ch2_expressions`, `section=2.9`)
  ```text
| Function | Description |
| --- | --- |
| abs(x) | Returns the absolute value of x. |
| int(x) | Converts x (a string or float) to an integer. |
| float(x) | Converts x (a string or integer) to a float. |
| str(x) | Converts x (a float or integer) to a string. |
| round(x, ndigits) | Rounds x to ndigits places after the decimal point. If ndigits is omitted, returns the nearest integer to x. |
| Operator | Description |
  ```
#### Chiến lược C (Auto proxy: `Hit@1=True`, `Hit@3=True`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p057_c04` | `score=0.7840` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=57` (`book=47`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
Python's round() function is used to round a floating-point number to a given number of decimal places. The function requires two arguments. The first argument is the number to be rounded. The second argument decides the number of decimal places to which the number is rounded. If the second argument is not provided, the number will be rounded to the closest integer. The round() function can be used to mitigate floating-point errors.

Ex:

• round(2.451, 2) = 2.45
• round(2.451) = 2

CHECKPOINT
  ```
- **Rank 2** | `openstax-python-2024_p058_c01` | `score=0.7107` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=58` (`book=48`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
CONCEPTS IN PRACTICE

Examples of round() function

3 . What is the output of round(6.6)?
a. 6
b. 6.6
c. 7

4 . What is the output of round(3.5, 2)?
a. 3
b. 3.5
c. 3.50

5 . What is the output of round(12)?
a. 12.0
b. 12
c. 12.00

6 . What is the output of round(0.1, 1)?
a. 0.1
b. 0.10
c. 0.1000000000000000055511151231257827021181583404541015625

TRY IT

Inaccurate tips
  ```
- **Rank 3** | `openstax-python-2024_p074_c02` | `score=0.6861` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=74` (`book=64`, `chapter=ch2_expressions`, `section=2.9`)
  ```text
| Function | Description |
| --- | --- |
| abs(x) | Returns the absolute value of x. |
| int(x) | Converts x (a string or float) to an integer. |
| float(x) | Converts x (a string or integer) to a float. |
| str(x) | Converts x (a float or integer) to a string. |
| round(x, ndigits) | Rounds x to ndigits places after the decimal point. If ndigits is omitted, returns the nearest integer to x. |
| Operator | Description |
  ```
#### Chiến lược D (Auto proxy: `Hit@1=False`, `Hit@3=False`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p057_c03` | `score=0.7370` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=57` (`book=47`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
The second argument decides the number of decimal places to which the number is rounded. If the second argument is not provided, the number will be rounded to the closest integer.

The round() function can be used to mitigate floating-point errors.

Ex:

• round(2.451, 2) = 2.45
• round(2.451) = 2

CHECKPOINT

Examples of round() function

Examples of a round () function; ch 2, video 7 (https://www.openstax.org/r/round-function)
  ```
- **Rank 2** | `openstax-python-2024_p058_c01` | `score=0.6993` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=58` (`book=48`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
CONCEPTS IN PRACTICE

Examples of round() function

3 . What is the output of round(6.6)?
a. 6
b. 6.6
c. 7

4 . What is the output of round(3.5, 2)?
a. 3
b. 3.5
c. 3.50

5 . What is the output of round(12)?
a. 12.0
b. 12
c. 12.00

6 . What is the output of round(0.1, 1)?
a. 0.1
b. 0.10
c. 0.1000000000000000055511151231257827021181583404541015625

TRY IT

Inaccurate tips

The following code calculates the tip amount, given a bill amount and the tip ratio. Experiment with the following bill amounts and tip ratios and see if any inaccuracies may result in calculating the tip amount.
  ```
- **Rank 3** | `openstax-python-2024_p074_c02` | `score=0.6888` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=74` (`book=64`, `chapter=ch2_expressions`, `section=2.9`)
  ```text
| Function | Description |
| --- | --- |
| abs(x) | Returns the absolute value of x. |
| int(x) | Converts x (a string or float) to an integer. |
| float(x) | Converts x (a string or integer) to a float. |
| str(x) | Converts x (a float or integer) to a string. |
| round(x, ndigits) | Rounds x to ndigits places after the decimal point. If ndigits is omitted, returns the nearest integer to x. |
| Operator | Description |
| s * n (Repetition) | Creates a string with n copies of s. Ex: "Ha" * 3 is "HaHaHa". |
| x / y (Real division) | Divides x by y and returns the entire result as a float. Ex: 7 / 4 is 1.75. |
  ```

### q20 (`metadata_filter` | gold_page=70 | valid_pages=[70] | filter={'chapter': 'ch2_expressions'})
- **Câu hỏi:** Trong chương Expressions, Python cung cấp hai cách nào để viết câu lệnh trên nhiều dòng (multi-line statements), và chuẩn PEP 8 khuyên nên tránh dùng cách nào?
- **Đáp án chuẩn:** Python cung cấp hai cách là nối dòng tường minh (explicit line joining dùng ký tự \) và nối dòng ngầm định (implicit line joining dùng dấu ngoặc đơn). Chuẩn PEP 8 khuyến nghị tránh sử dụng nối dòng tường minh (explicit line joining) bất cứ khi nào có thể.
- **Evidence gốc:** `Python provides two ways to write multi-line statements: ... Explicit line joining, using \ characters: ... Implicit line joining, using parentheses: ... PEP 8 recommends avoiding the use of explicit line joining whenever possible.`

#### Chiến lược A (Auto proxy: `Hit@1=False`, `Hit@3=False`, `filter_ok=True`)
- **Rank 1** | `openstax-python-2024_p070_c02` | `score=0.7816` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
eople to dissolve the political bands..."
• Implicit line joining, using parentheses:

decl = ("The unanimous Declaration of the thirteen united States of " "America, When in the Course of human events, it becomes " "necessary for one people to dissolve the political bands...")

Implicit line joining is more common, since many statements and expressions use parentheses anyway. PEP 8 recommends avoiding the use of explicit line joining whenever possible.

CONCEPTS IN PRACTICE

Multi-line statemen
  ```
- **Rank 2** | `openstax-python-2024_p070_c03` | `score=0.7577` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
ssible.

CONCEPTS IN PRACTICE

Multi-line statements

8 . Which character is used for explicit line joining?
a. /
b. \
c. |

9 . What is the best way to print a very long string?
a. Break up the string into multiple smaller strings. print("..." # first part of string "..." # next part of string "...")
b. Print the string using multiple print statements. print("...") # first part of string print("...") # next part of string print("...")
c. Assign the string to a variable and print the variable. t
  ```
- **Rank 3** | `openstax-python-2024_p070_c01` | `score=0.7401` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
a. Hello,Ada
b. Hello, Ada
c. SyntaxError

Multi-line statements

Most statements in a Python program need only one line of code. But occasionally longer statements need to span multiple lines. Python provides two ways to write multi-line statements:

• Explicit line joining, using \ characters:

decl = "The unanimous Declaration of the thirteen united States of " \ "America, When in the Course of human events, it becomes " \ "necessary for one people to dissolve the political bands..."
• Implic
  ```
#### Chiến lược B (Auto proxy: `Hit@1=False`, `Hit@3=False`, `filter_ok=True`)
- **Rank 1** | `openstax-python-2024_p070_c03` | `score=0.7679` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
Implicit line joining is more common, since many statements and expressions use parentheses anyway. PEP 8 recommends avoiding the use of explicit line joining whenever possible.

CONCEPTS IN PRACTICE

Multi-line statements

8 . Which character is used for explicit line joining?
a. /
b. \
c. |
  ```
- **Rank 2** | `openstax-python-2024_p070_c02` | `score=0.7508` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
decl = "The unanimous Declaration of the thirteen united States of " \ "America, When in the Course of human events, it becomes " \ "necessary for one people to dissolve the political bands..."
• Implicit line joining, using parentheses:

decl = ("The unanimous Declaration of the thirteen united States of " "America, When in the Course of human events, it becomes " "necessary for one people to dissolve the political bands...")
  ```
- **Rank 3** | `openstax-python-2024_p070_c01` | `score=0.7442` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
a. Hello,Ada
b. Hello, Ada
c. SyntaxError

Multi-line statements

Most statements in a Python program need only one line of code. But occasionally longer statements need to span multiple lines. Python provides two ways to write multi-line statements:

• Explicit line joining, using \ characters:
  ```
#### Chiến lược C (Auto proxy: `Hit@1=False`, `Hit@3=False`, `filter_ok=True`)
- **Rank 1** | `openstax-python-2024_p070_c03` | `score=0.7679` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
Implicit line joining is more common, since many statements and expressions use parentheses anyway. PEP 8 recommends avoiding the use of explicit line joining whenever possible.

CONCEPTS IN PRACTICE

Multi-line statements

8 . Which character is used for explicit line joining?
a. /
b. \
c. |
  ```
- **Rank 2** | `openstax-python-2024_p070_c02` | `score=0.7508` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
decl = "The unanimous Declaration of the thirteen united States of " \ "America, When in the Course of human events, it becomes " \ "necessary for one people to dissolve the political bands..."
• Implicit line joining, using parentheses:

decl = ("The unanimous Declaration of the thirteen united States of " "America, When in the Course of human events, it becomes " "necessary for one people to dissolve the political bands...")
  ```
- **Rank 3** | `openstax-python-2024_p070_c01` | `score=0.7442` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
a. Hello,Ada
b. Hello, Ada
c. SyntaxError

Multi-line statements

Most statements in a Python program need only one line of code. But occasionally longer statements need to span multiple lines. Python provides two ways to write multi-line statements:

• Explicit line joining, using \ characters:
  ```
#### Chiến lược D (Auto proxy: `Hit@1=False`, `Hit@3=False`, `filter_ok=True`)
- **Rank 1** | `openstax-python-2024_p070_c02` | `score=0.7718` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
• Implicit line joining, using parentheses:

decl = ("The unanimous Declaration of the thirteen united States of " "America, When in the Course of human events, it becomes " "necessary for one people to dissolve the political bands...")

Implicit line joining is more common, since many statements and expressions use parentheses anyway. PEP 8 recommends avoiding the use of explicit line joining whenever possible.

CONCEPTS IN PRACTICE

Multi-line statements

8 . Which character is used for explicit line joining?
a. /
b. \
c. |
  ```
- **Rank 2** | `openstax-python-2024_p070_c03` | `score=0.7633` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
Multi-line statements

8 . Which character is used for explicit line joining?
a. /
b. \
c. |

9 . What is the best way to print a very long string?
a. Break up the string into multiple smaller strings. print("..." # first part of string "..." # next part of string "...")

b. Print the string using multiple print statements. print("...") # first part of string print("...") # next part of string print("...")

c. Assign the string to a variable and print the variable. text = "..." # the entire string print(text)

10 . Which example consists of two statements?
a. print("Happy " "New Year")
b. saying = ("Happy " "New Year")
  ```
- **Rank 3** | `openstax-python-2024_p070_c01` | `score=0.7454` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
a. Hello,Ada
b. Hello, Ada
c. SyntaxError

Multi-line statements

Most statements in a Python program need only one line of code. But occasionally longer statements need to span multiple lines. Python provides two ways to write multi-line statements:

• Explicit line joining, using \ characters:

decl = "The unanimous Declaration of the thirteen united States of " \ "America, When in the Course of human events, it becomes " \ "necessary for one people to dissolve the political bands..."

• Implicit line joining, using parentheses:
  ```

### q24 (`table_lookup` | gold_page=68 | valid_pages=[68] | filter={'chapter': 'ch2_expressions'})
- **Câu hỏi:** Trong chương Expressions, theo bảng hướng dẫn dùng khoảng trắng (Table 2.7 Guidelines for spaces), quy tắc đặt khoảng trắng quanh dấu phẩy (,), dấu gán (=) và phép toán số học (Arithmetic) là gì?
- **Đáp án chuẩn:** Với dấu phẩy: không có khoảng trắng trước và có một khoảng trắng sau (ví dụ print("Hello", name)). Với phép gán (=): có một khoảng trắng trước và sau dấu = (ví dụ name = input("Your name? ")). Với biểu thức số học: dùng khoảng trắng để thể hiện phép toán có độ ưu tiên thấp hơn (ví dụ x**2 + 5*x - 8).
- **Evidence gốc:** `| Commas: no space before, one space after. | print("Hello", name) | ... | Assignment: one space before and after the =. | name = input("Your name? ") | ... | Arithmetic: use space to show lower precedence. | x**2 + 5*x - 8 |`

#### Chiến lược A (Auto proxy: `Hit@1=False`, `Hit@3=False`, `filter_ok=True`)
- **Rank 1** | `openstax-python-2024_p068_c02` | `score=0.7823` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=68` (`book=58`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
nation: one space before and after the +. | print("Hi", name + "!") | print("Hi", name+"!") print("Hi", name+ "!") print("Hi", name +"!") |
| Arithmetic: use space to show lower precedence. | x**2 + 5*x - 8 | x ** 2 + 5 * x - 8 x ** 2+5 * x-8 x**2+5*x-8 |

Table 2.7 Guidelines for spaces.

CONCEPTS IN PRACTICE

Recommended spacing

1 . Which statement is formatted properly?
a. name = input("What is your name? ")
b. name = input ("What is your name? ")
c. name = input( "What is your name? " )

2
  ```
- **Rank 2** | `openstax-python-2024_p068_c01` | `score=0.7584` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=68` (`book=58`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
| Guideline | Example | Common Mistakes |
| --- | --- | --- |
| Parentheses: no space before or after. | print("Go team!") | print ("Go team!") print( "Go team!" ) |
| Commas: no space before, one space after. | print("Hello", name) | print("Hello" , name) print("Hello",name) |
| Assignment: one space before and after the =. | name = input("Your name? ") | name=input("Your name? ") name= input("Your name? ") name =input("Your name? ") |
| Concatenation: one space before and after the +. | print(
  ```
- **Rank 3** | `openstax-python-2024_p067_c04` | `score=0.7184` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=67` (`book=57`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
, how to break up long lines, and other important topics.

PYTHON STYLE GUIDE

PEP 8 (https://openstax.org/r/100PEP8) is the official style guide for Python. PEP stands for Python Enhancement Proposal. Members of the Python community write PEPs to document best practices and propose new features. The table below is based on guidelines from PEP 8 under the heading Whitespace in Expressions and Statements (https://openstax.org/r/100whitespace).
  ```
#### Chiến lược B (Auto proxy: `Hit@1=False`, `Hit@3=False`, `filter_ok=True`)
- **Rank 1** | `openstax-python-2024_p068_c02` | `score=0.7978` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=68` (`book=58`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
| Concatenation: one space before and after the +. | print("Hi", name + "!") | print("Hi", name+"!") print("Hi", name+ "!") print("Hi", name +"!") |
| Arithmetic: use space to show lower precedence. | x**2 + 5*x - 8 | x ** 2 + 5 * x - 8 x ** 2+5 * x-8 x**2+5*x-8 |

Table 2.7 Guidelines for spaces.

CONCEPTS IN PRACTICE

Recommended spacing
  ```
- **Rank 2** | `openstax-python-2024_p068_c01` | `score=0.7555` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=68` (`book=58`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
| Guideline | Example | Common Mistakes |
| --- | --- | --- |
| Parentheses: no space before or after. | print("Go team!") | print ("Go team!") print( "Go team!" ) |
| Commas: no space before, one space after. | print("Hello", name) | print("Hello" , name) print("Hello",name) |
| Assignment: one space before and after the =. | name = input("Your name? ") | name=input("Your name? ") name= input("Your name? ") name =input("Your name? ") |
  ```
- **Rank 3** | `openstax-python-2024_p067_c05` | `score=0.7397` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=67` (`book=57`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
PEP 8 (https://openstax.org/r/100PEP8) is the official style guide for Python. PEP stands for Python Enhancement Proposal. Members of the Python community write PEPs to document best practices and propose new features. The table below is based on guidelines from PEP 8 under the heading Whitespace in Expressions and Statements (https://openstax.org/r/100whitespace).
  ```
#### Chiến lược C (Auto proxy: `Hit@1=False`, `Hit@3=False`, `filter_ok=True`)
- **Rank 1** | `openstax-python-2024_p068_c02` | `score=0.7978` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=68` (`book=58`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
| Concatenation: one space before and after the +. | print("Hi", name + "!") | print("Hi", name+"!") print("Hi", name+ "!") print("Hi", name +"!") |
| Arithmetic: use space to show lower precedence. | x**2 + 5*x - 8 | x ** 2 + 5 * x - 8 x ** 2+5 * x-8 x**2+5*x-8 |

Table 2.7 Guidelines for spaces.

CONCEPTS IN PRACTICE

Recommended spacing
  ```
- **Rank 2** | `openstax-python-2024_p068_c01` | `score=0.7555` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=68` (`book=58`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
| Guideline | Example | Common Mistakes |
| --- | --- | --- |
| Parentheses: no space before or after. | print("Go team!") | print ("Go team!") print( "Go team!" ) |
| Commas: no space before, one space after. | print("Hello", name) | print("Hello" , name) print("Hello",name) |
| Assignment: one space before and after the =. | name = input("Your name? ") | name=input("Your name? ") name= input("Your name? ") name =input("Your name? ") |
  ```
- **Rank 3** | `openstax-python-2024_p067_c05` | `score=0.7397` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=67` (`book=57`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
PEP 8 (https://openstax.org/r/100PEP8) is the official style guide for Python. PEP stands for Python Enhancement Proposal. Members of the Python community write PEPs to document best practices and propose new features. The table below is based on guidelines from PEP 8 under the heading Whitespace in Expressions and Statements (https://openstax.org/r/100whitespace).
  ```
#### Chiến lược D (Auto proxy: `Hit@1=False`, `Hit@3=False`, `filter_ok=True`)
- **Rank 1** | `openstax-python-2024_p068_c02` | `score=0.7771` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=68` (`book=58`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
| Arithmetic: use space to show lower precedence. | x**2 + 5*x - 8 | x ** 2 + 5 * x - 8 x ** 2+5 * x-8 x**2+5*x-8 |

Table 2.7 Guidelines for spaces.

CONCEPTS IN PRACTICE

Recommended spacing

1 . Which statement is formatted properly?
a. name = input("What is your name? ")
b. name = input ("What is your name? ")
c. name = input( "What is your name? " )

2 . Which statement is formatted properly?
a. name=name+"!"
b. name = name+"!"
c. name = name + "!"

3 . Which statement is formatted properly?
a. print("Hello",name)
b. print("Hello", name)
c. print("Hello " , name)
  ```
- **Rank 2** | `openstax-python-2024_p068_c01` | `score=0.7549` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=68` (`book=58`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
| Guideline | Example | Common Mistakes |
| --- | --- | --- |
| Parentheses: no space before or after. | print("Go team!") | print ("Go team!") print( "Go team!" ) |
| Commas: no space before, one space after. | print("Hello", name) | print("Hello" , name) print("Hello",name) |
| Assignment: one space before and after the =. | name = input("Your name? ") | name=input("Your name? ") name= input("Your name? ") name =input("Your name? ") |
| Concatenation: one space before and after the +. | print("Hi", name + "!") | print("Hi", name+"!") print("Hi", name+ "!") print("Hi", name +"!") |
  ```
- **Rank 3** | `openstax-python-2024_p067_c03` | `score=0.7185` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=67` (`book=57`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
To encourage consistency, the Python community has a set of guidelines about where to put spaces and blank lines, what to name variables, how to break up long lines, and other important topics.

PYTHON STYLE GUIDE

PEP 8 (https://openstax.org/r/100PEP8) is the official style guide for Python. PEP stands for Python Enhancement Proposal.

Members of the Python community write PEPs to document best practices and propose new features.

The table below is based on guidelines from PEP 8 under the heading Whitespace in Expressions and Statements (https://openstax.org/r/100whitespace).
  ```

### q25 (`table_lookup` | gold_page=72 | valid_pages=[72] | filter=None)
- **Câu hỏi:** Theo bảng ví dụ về Python ngoài lĩnh vực CNTT và các ứng dụng xây dựng bằng Python (Table 2.8 và Table 2.9), nhà sinh học (biologist) dùng Python để làm gì và thư viện Matplotlib dùng cho lĩnh vực ứng dụng nào?
- **Đáp án chuẩn:** Trong lĩnh vực Khoa học (Science), nhà sinh học dùng Python để phân tích chuỗi DNA tìm ung thư; còn thư viện Matplotlib được dùng trong ứng dụng trực quan hóa dữ liệu (Data visualization) giúp nhà thống kê tạo biểu đồ.
- **Evidence gốc:** `| Science | A biologist writes a Python program to analyze DNA sequences for cancer. | ... | Data visualization | A statistician creates charts to make sense of large amounts of data. Ex: Matplotlib library (https://openstax.org/r/100matplotlib). |`

#### Chiến lược A (Auto proxy: `Hit@1=False`, `Hit@3=False`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p072_c05` | `score=0.7728` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
age and voice recognition. Ex: TensorFlow library (https://openstax.org/r/100tensorflow). |
| Data visualization | A statistician creates charts to make sense of large amounts of data. Ex: Matplotlib library (https://openstax.org/r/100matplotlib). |
| General purpose | Most programs in this book are general. Ex: Read inputs, perform calculations, print results. |

Table 2.9 Applications built with Python.
  ```
- **Rank 2** | `openstax-python-2024_p072_c04` | `score=0.7686` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
rk submissions. |
| Fine arts | An artist writes a Python program to operate an interactive art display. |
| Humanities | A linguist writes a Python program to analyze changes in slang word usage. |
| Science | A biologist writes a Python program to analyze DNA sequences for cancer. |

Table 2.8 Python outside of CS and IT.

| Application | Example use of Python |
| --- | --- |
| Artificial intelligence | An engineer develops models to support image and voice recognition. Ex: TensorFlow library
  ```
- **Rank 3** | `openstax-python-2024_p072_c03` | `score=0.7427` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
nds of applications. Table 2.9 shows a few examples of programs that can be written in Python. Given Python's usefulness and popularity, Python is a great language to learn. A supportive community of professionals and enthusiasts is ready to help.

| Field | Example use of Python |
| --- | --- |
| Business | An accountant writes a Python program to generate custom sales reports. |
| Education | A teacher writes a Python program to organize homework submissions. |
| Fine arts | An artist writes a
  ```
#### Chiến lược B (Auto proxy: `Hit@1=False`, `Hit@3=False`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p072_c08` | `score=0.7682` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
Table 2.9 Applications built with Python.
  ```
- **Rank 2** | `openstax-python-2024_p072_c06` | `score=0.7544` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
Table 2.8 Python outside of CS and IT.
  ```
- **Rank 3** | `openstax-python-2024_p072_c04` | `score=0.7390` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
Python is a versatile language that supports many kinds of applications. Table 2.9 shows a few examples of programs that can be written in Python. Given Python's usefulness and popularity, Python is a great language to learn. A supportive community of professionals and enthusiasts is ready to help.
  ```
#### Chiến lược C (Auto proxy: `Hit@1=False`, `Hit@3=False`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p072_c08` | `score=0.7682` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
Table 2.9 Applications built with Python.
  ```
- **Rank 2** | `openstax-python-2024_p072_c06` | `score=0.7544` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
Table 2.8 Python outside of CS and IT.
  ```
- **Rank 3** | `openstax-python-2024_p072_c04` | `score=0.7390` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
Python is a versatile language that supports many kinds of applications. Table 2.9 shows a few examples of programs that can be written in Python. Given Python's usefulness and popularity, Python is a great language to learn. A supportive community of professionals and enthusiasts is ready to help.
  ```
#### Chiến lược D (Auto proxy: `Hit@1=False`, `Hit@3=False`, `filter_ok=None`)
- **Rank 1** | `openstax-python-2024_p072_c04` | `score=0.7643` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
Table 2.8 Python outside of CS and IT.

| Application | Example use of Python |
| --- | --- |
| Artificial intelligence | An engineer develops models to support image and voice recognition. Ex: TensorFlow library (https://openstax.org/r/100tensorflow). |
| Data visualization | A statistician creates charts to make sense of large amounts of data. Ex: Matplotlib library (https://openstax.org/r/100matplotlib). |
| General purpose | Most programs in this book are general. Ex: Read inputs, perform calculations, print results. |

Table 2.9 Applications built with Python.
  ```
- **Rank 2** | `openstax-python-2024_p072_c03` | `score=0.7615` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
| Field | Example use of Python |
| --- | --- |
| Business | An accountant writes a Python program to generate custom sales reports. |
| Education | A teacher writes a Python program to organize homework submissions. |
| Fine arts | An artist writes a Python program to operate an interactive art display. |
| Humanities | A linguist writes a Python program to analyze changes in slang word usage. |
| Science | A biologist writes a Python program to analyze DNA sequences for cancer. |

Table 2.8 Python outside of CS and IT.
  ```
- **Rank 3** | `openstax-python-2024_p073_c02` | `score=0.7589` | `source=data/Introduction_to_Python_Programming-WEB.pdf` | `page=73` (`book=63`, `chapter=ch2_expressions`, `section=2.9`)
  ```text
2 . Which of the following Python libraries creates charts and plots?
a. Matplotlib
b. SciPy
c. TensorFlow

3 . Which of the following applications were built with Python?
a. Facebook
b. Instagram
c. WhatsApp

EXPLORING FURTHER

For more examples of applications that can be built with Python, see "Top 12 Fascinating Python Applications in Real-World" (https://openstax.org/r/100top12apps) by Rohit Sharma.

For more information about Python related careers, see "What Does a Python Developer Do?" (https://openstax.org/r/100careers) in BrainStation's career guide.

2.9 Chapter summary

Highlights from this chapter include:
  ```
