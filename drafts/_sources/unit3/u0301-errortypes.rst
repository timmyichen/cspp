.. qnum::
   :start: 1
   :prefix: u0301-


Lesson 03-01: Categories of Errors
==================================

**Learning Target: I can differentiate between semantic, runtime, and syntax errors.**

Types of Errors
---------------

In most programming languages, errors can be split up into three different types of categories:

    - **Syntax Errors** are errors in the way your code is structured.  Either there's a typo or an issue with spacing - in other words, the computer does not understand what the code is trying to do.
    - **Runtime Errors** are errors that occur when the program is running.  This means that there aren't any syntax errors - we passed that part.
    - **Semantic Errors** are errors that occur when your program does something that is different from what you wanted it to.  These errors aren't program-stopping errors like the others, and therefore are the most difficult to solve - it usually indicates an issue with the logic of the code.

Some examples of Syntax and Runtime errors include:

    - Syntax Errors
        - Not having a colon after an if statement
        - Not having a tab on the next line after a colon
        - Having ``=`` instead of ``==`` for equality
        - Not having parentheses after your print statement
        - Forgetting to close a quote or parentheses
    - Runtime Errors
        - Not initializing a variable
        - Trying to divide by zero
        - Trying to modulo by zero
        - Trying to access a string index that doesn't exist
        - Trying to concatenate a string to a number
    
How to tell which is which?
---------------------------

It's easy to tell if something is a semantic error - your code will run without stopping the program, and it will simply do something that you don't want it to do.  Both syntax and runtime errors will stop your code from executing.  So how do we differentiate between them?

Syntax errors stop program execution *before it even starts*.  This means that nothing will occur at all.  For example, run the following program, which has a valid print statement on line 1, and an invalid statement on line 2:

.. activecode:: 0301_ex_1
    
    print("hi")
    print "there"

You can see that there isn't any output at all, because nothing is run.  However, let's take an example of a runtime error.  This time, our first line will have a valid print statement, and our second line will print a variable that doesn't exist yet.

.. activecode:: 0301_ex_2

    print("hi")
    print(there)
    
You'll notice that the ``"hi"`` gets printed before we come across the error.  This means that the program execution has started, and therefore, this is a runtime error (an error when the program is running).

Checks For Understanding
------------------------

Q#1
~~~

.. code-block:: python
    :linenos:
    
    num = input("Enter a number: ")
    print(num % 3)
    print(num % 2)
    print(num % 1)
    print(num % 0)

.. mchoice:: 0301_cfu_1_1
    :correct: e
    :answer_a: Line 1
    :answer_b: Line 2
    :answer_c: Line 3
    :answer_d: Line 4
    :answer_e: Line 5
    
    What line in the above code will produce an error?

.. mchoice:: 0301_cfu_1_2
    :correct: b
    :answer_a: Syntax
    :answer_b: Runtime
    :answer_c: Semantic
    
    What type of error is produced from above?
    
Q#2
~~~

.. code-block:: python
    :linenos:
    
    y = 10
    z = 20
    #increment all variables
    x = x + 1
    y = y + 1
    z = z + 1

.. mchoice:: 0301_cfu_2_1
    :correct: c
    :answer_a: Line 1
    :answer_b: Line 2
    :answer_c: Line 4
    :answer_d: Line 5
    :answer_e: Line 6
    
    What line in the above code will produce an error?

.. mchoice:: 0301_cfu_2_2
    :correct: b
    :answer_a: Syntax
    :answer_b: Runtime
    :answer_c: Semantic
    
    What type of error is produced from above?

Q#1
~~~

.. code-block:: python
    :linenos:
    
    name = raw_input("Enter your name: )
    print("Hello there!")
    print("Your name is {}".format(name)

.. mchoice:: 0301_cfu_3_1
    :correct: a
    :answer_a: Syntax
    :answer_b: Runtime
    :answer_c: Semantic
    
    The above code contains which kinds of errors?

.. mchoice:: 0301_cfu_3_2
    :multiple_answers:
    :correct: c
    :answer_a: Line 1
    :answer_b: Line 2
    :answer_c: Line 3
    
    Which lines contain those errors?
    
.. fillintheblank:: 0301_cfu_3_1
    
    .. blank:: 0301_blank_3_1
        :correct: ^name = raw_input("Enter your name: *" *)$
        :feedback1: (".*", "Try again!")
        
        Copy and paste the FIRST line that has an error and correct it so there is no error by adding a single character.  Adding more than a single character may throw off the answer detection.
    
    .. blank:: 0301_blank_3_2
        :correct: ^print("Your name is {}".format(name))$
        :feedback1: (".*", "Try again!")
        
        Copy and paste the FIRST line that has an error and correct it so there is no error by adding a single character.  Adding more than a single character may throw off the answer detection.