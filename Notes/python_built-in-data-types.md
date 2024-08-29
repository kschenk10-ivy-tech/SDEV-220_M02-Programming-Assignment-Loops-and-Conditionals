# Python’s simplest built-in data types:

**Booleans** (which have the value True or False)

**Integers** (whole numbers such as 42 and 100000000)

**Floats** (numbers with decimal points such as 3.14159, or sometimes exponents like 1.0e8, which means one times ten to the eighth power, or 100000000.0)

### Booleans
In Python, the only values for the boolean data type are True and False. Sometimes, you’ll use these directly; other times you’ll evaluate the “truthiness” of other types from their values. The special Python function bool() can convert any Python data type to a boolean.

Functions get their own chapter in Chapter 9, but for now you just need to know that a function has a name, zero or more comma-separated input arguments surrounded by parentheses, and zero or more return values. The bool() function takes any value as its argument and returns the boolean equivalent.

> Nonzero numbers are considered True:
```python
>>> bool(True)
True
>>> bool(1)
True
>>> bool(45)
True
>>> bool(-45)
True
```

> And zero-valued ones are considered False:

```python
>>> bool(False)
False
>>> bool(0)
False
>>> bool(0.0)
False
```

---

### Integers
Integers are whole numbers—no fractions, no decimal points, nothing fancy. Well, aside from a possible initial sign. And bases, if you want to express numbers in other ways than the usual decimal (base 10).

### Literal Integers
Any sequence of digits in Python represents a literal integer:
```python
>>> 5
5
A plain zero (0) is valid:

>>> 0
0
```
But you can’t have an initial 0 followed by a digit between 1 and 9:
```python
>>> 05
  File "<stdin>", line 1
    05
     ^
SyntaxError: invalid token
```
**NOTE**
*This Python exception warns that you typed something that breaks Python’s rules. I explain what this means in “Bases”. You’ll see many more examples of exceptions in this book because they’re Python’s main error handling mechanism.*

> You can start an integer with 0b, 0o, or 0x. See “Bases”.

A sequence of digits specifies a positive integer. If you put a + sign before the digits, the number stays the same:

```python
>>> 123
123
>>> +123
123
```
To specify a negative integer, insert a – before the digits:
```python
>>> -123
-123
```
You can’t have any commas in the integer:
```python
>>> 1,000,000
(1, 0, 0)
```

Instead of a million, you’d get a tuple (see Chapter 7 for more information on tuples) with three values. But you can use the underscore (_) character as a digit separator:1
```python
>>> million = 1_000_000
>>> million
1000000
```
Actually, you can put underscores anywhere after the first digit; they’re just ignored:
```python
>>> 1_2_3
123
```
### Integer Operations
For the next few pages, I show examples of Python acting as a simple calculator. You can do normal arithmetic with Python by using the math operators in this table:

```python
Addition and subtraction work as you’d expect:

>>> 5 + 9
14
>>> 100 - 7
93
>>> 4 - 10
-6
```

```python
You can include as many numbers and operators as you’d like:

>>> 5 + 9 + 3
17
>>> 4 + 3 - 2 - 1 + 6
10
```

**Note:** *you’re not required to have a space between each number and operator:*

```python
>>> 5+9   +      3
17
```
It just looks better stylewise and is easier to read.

Multiplication is also straightforward:

```python
>>> 6 * 7
42
>>> 7 * 6
42
>>> 6 * 7 * 2 * 3
252
```

Division is a little more interesting because it comes in two flavors:

/ carries out floating-point (decimal) division

// performs integer (truncating) division

Even if you’re dividing an integer by an integer, using a / will give you a floating-point result (floats are coming later in this chapter):

```python
>>> 9 / 5
1.8
```

Truncating integer division returns an integer answer, throwing away any remainder:

```python
>>> 9 // 5
1
```

Instead of tearing a hole in the space-time continuum, dividing by zero with either kind of division causes a Python exception:


```python
>>> 5 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 7 // 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by z
Integers and Variables
All of the preceding examples used literal integers. You can mix literal integers and variables that have been assigned integer values:
```python
>>> a = 95
>>> a
95
>>> a - 3
92
```
You’ll remember from Chapter 2 that a is a name that points to an integer object. When I said a - 3, I didn’t assign the result back to a, so the value of a did not change:
```python
>>> a
95
```
If you wanted to change a, you would do this:
```python
>>> a = a - 3
>>> a
92
```

Again, this would not be a legal math equation, but it’s how you reassign a value to a variable in Python. In Python, the expression on the right side of the = is calculated first, and then assigned to the variable on the left side.

If it helps, think of it this way:

Subtract 3 from a

Assign the result of that subtraction to a temporary variable

Assign the value of the temporary variable to a:

```python
>>> a = 95
>>> temp = a - 3
>>> a = temp
```

> So, when you say


```python
>>> a = a - 3
```

    Python is calculating the subtraction on the righthand side, remembering the result, and then assigning it to a on the left side of the + sign. It’s faster and neater than using a temporary variable.

    You can combine the arithmetic operators with assignment by putting the operator before the =. Here, a -= 3 is like saying a = a - 3:

```python
>>> a = 95
>>> a -= 3
>>> a
92

# This is like a = a + 8:

>>> a = 92
>>> a += 8
>>> a
100

# And this is like a = a * 2:

>>> a = 100
>>> a *= 2
>>> a
200
```

Here’s a floating-point division example, like a = a / 3:

```python
>>> a = 200
>>> a /= 3
>>> a
66.66666666666667
```

Now let’s try the shorthand for a = a // 4 (truncating integer division):

```python
>>> a = 13
>>> a //= 4
>>> a
3
```

The % character has multiple uses in Python. When it’s between two numbers, it produces the remainder when the first number is divided by the second:

```python
>>> 9 % 5
4
```

Here’s how to get both the (truncated) quotient and remainder at once:
```python
>>> divmod(9,5)
(1, 4)
```

Otherwise, you could have calculated them separately:

```python
>>> 9 // 5
1
>>> 9 % 5
4
```

You just saw some new things here: a function named divmod is given the integers 9 and 5 and returns a two-item tuple. As I mentioned earlier, tuples will take a bow in Chapter 7; functions debut in Chapter 9.

One last math feature is exponentiation with **, which also lets you mix integers and floats:

```python
>>> 2**3
8
>>> 2.0 ** 3
8.0
>>> 2 ** 3.0
8.0
>>> 0 ** 3
0
```

Precedence
What would you get if you typed the following?

>>> 2 + 3 * 4


If you do the addition first, 2 + 3 is 5, and 5 * 4 is 20. But if you do the multiplication first, 3 * 4 is 12, and 2 + 12 is 14. In Python, as in most languages, multiplication has higher precedence than addition, so the second version is what you’d see:


>>> 2 + 3 * 4
14


How do you know the precedence rules? There’s a big table in Appendix E that lists them all, but I’ve found that in practice I never look up these rules. It’s much easier to just add parentheses to group your code as you intend the calculation to be carried out:
"""
>>> 2 + (3 * 4)
14
This example with exponents

>>> -5 ** 2
-25
is the same as

>>> - (5 ** 2)
-25
and probably not what you wanted. Parentheses make it clear:

>>> (-5) ** 2
25

This way, anyone reading the code doesn’t need to guess its intent or look up precedence rules.

Bases
Integers are assumed to be decimal (base 10) unless you use a prefix to specify another base. You might never need to use these other bases, but you’ll probably see them in Python code somewhere, sometime.

We generally have 10 fingers and 10 toes, so we count 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. Next, we run out of single digits and carry the one to the “ten’s place” and put a 0 in the one’s place: 10 means “1 ten and 0 ones.” Unlike Roman numerals, Arabic numbers don’t have a single character that represents “10” Then, it’s 11, 12, up to 19, carry the one to make 20 (2 tens and 0 ones), and so on.

A base is how many digits you can use until you need to “carry the one.” In base 2 (binary), the only digits are 0 and 1. This is the famous bit. 0 is the same as a plain old decimal 0, and 1 is the same as a decimal 1. However, in base 2, if you add a 1 to a 1, you get 10 (1 decimal two plus 0 decimal ones).

> In Python, you can express literal integers in three bases besides decimal with these integer prefixes:

    0b or 0B for binary (base 2).

    0o or 0O for octal (base 8).

    0x or 0X for hex (base 16).

**These bases are all powers of two, and are handy in some cases, although you may never need to use anything other than good old decimal integers.**

The interpreter prints these for you as decimal integers. Let’s try each of these bases. First, a plain old decimal 10, which means 1 ten and 0 ones:

>>> 10
10
Now, a binary (base two) 0b10, which means 1 (decimal) two and 0 ones:

>>> 0b10
2
Octal (base 8) 0o10 stands for 1 (decimal) eight and 0 ones:

>>> 0o10
8
Hexadecimal (base 16) 0x10 means 1 (decimal) sixteen and 0 ones:

>>> 0x10
16
You can go the other direction, converting an integer to a string with any of these bases:

>>> value = 65
>>> bin(value)
'0b1000001'
>>> oct(value)
'0o101'
>>> hex(value)
'0x41'
The chr() function converts an integer to its single-character string equivalent:

>>> chr(65)
'A'
And ord() goes the other way:

>>> ord('A')
65
```

> In case you’re wondering what “digits” base 16 uses, they are: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, and f. 0xa is a decimal 10, and 0xf is a decimal 15. Add 1 to 0xf and you get 0x10 (decimal 16).


> Why use different bases from 10? They’re useful in bit-level operations, which are described in Chapter 12, along with more details about converting numbers from one base to another.