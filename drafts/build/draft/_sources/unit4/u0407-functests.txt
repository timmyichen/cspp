.. qnum::
   :start: 1
   :prefix: u0407-


Lesson 04-07: Testing Functions
===============================

**Learning Target: I can write thorough tests for functions.**

Why Test Functions?
-------------------

Functions allow you to write your program in parts.  For example, if I were to write a simple quiz program, I might have functions that handle the following, one per function:

   - Display the question to the user
   - Get the user to type in their answer
   - Check if their answer is correct
   - Calculate their final score

The benefit of writing them in functions is that it allows you to test each part individually.

Creating Tests
--------------

Let's say that we have a program that requires us to check if a number is a natural number (a natural number is a positive whole number - 1,2,3,...), and we were to call it ``is_natural()``:

.. code-block:: python3

   def is_natural(n):
       if n > 0 and int(n) == n:
           return True
       else:
           return False

We can test this function by feeding it a bunch of numbers and testing it against our results:

   - ``is_natural(5)`` should return True
   - ``is_natural(3.6)`` should return False
   - ``is_natural(0)`` should return False
   - ``is_natural(1)`` should return True
   - ``is_natural(0.999)`` should return False
   - ``is_natural(-4)`` should return False
   - ``is_natural(-2.6)`` should return False
   - ``is_natural(9999999)`` should return True

:misc-hl:`When creating tests, you generally want to test for every possible case` - notice how I chose a positive integer, a negative integer, a positive decimal, a negative decimal, 0, 1, a number between 0 and 1, and a very large number.

So if we run these:

.. activecode:: ex_0407_1
   :autorun:
   
   def is_natural(n):
    if n > 0 or int(n) == n:
        return True
    else:
        return False

   #tests
   print(is_natural(5))       #True
   print(is_natural(3.6))     #False
   print(is_natural(0))       #False
   print(is_natural(1))       #True
   print(is_natural(0.999))   #False
   print(is_natural(-4))      #False
   print(is_natural(-2.6))    #False
   print(is_natural(9999999)) #True

We can see that not all our numbers match!  That's a problem - examine the code and see what's wrong with it.

.. fillintheblank:: cfu_0407_1
   
   .. blank:: cfu_0407_1_1
      :correct: ^2$
      :feedback1: (".*", "Remember what it means to be a natural number!")
      
   Which line in the function definition of ``is_natural`` contains the error?
   
Spoiler alert!  Don't read below until you've finished!

The line is on line 2 - I put ``or`` when it really should be ``and``.  So now let's fix that:

.. activecode:: ex_0407_2
   :autorun:
   
   def is_natural(n):
    if n > 0 and int(n) == n:
        return True
    else:
        return False

   #tests
   print(is_natural(5))       #True
   print(is_natural(3.6))     #False
   print(is_natural(0))       #False
   print(is_natural(1))       #True
   print(is_natural(0.999))   #False
   print(is_natural(-4))      #False
   print(is_natural(-2.6))    #False
   print(is_natural(9999999)) #True

Now we see that all our tests pass!  Score!  Now we can use this function safely, knowing that it works for all the examples we need it to handle!

To recap - the big points:
   - Functions are good because it allows you to break your code down into parts.
   - Testing functions is good because it's eaiser to debug a small part than an entire program.
   - Testing functions is also good because after it passes all tests, you know it works.
   - When coming up with tests, make sure you try all the possibilities that you need it to handle.

Checks For Understanding
------------------------

Q#1
~~~

The given function checks to see if a number is between 10 and 20 inclusive.  Write at least three test cases along with their predictions, and run your code to make sure that your tests are accurate (or that the function itself works).  If the function is broken, fix the function so it works as expected.

.. activecode:: cfu_0407_2
   :nocodelens:
   
   def mystery(n):
       if n >= 10 or n <= 20:
           return True
       else:
           return False
   
   #write tests below
   

Q#2
~~~

The given function takes in a string as an argument and prints out the length of the string times 2.  Write at least three test cases along with their predictions, and run your code to make sure that your tests are accurate (or that the function itself works).    If the function is broken, fix the function so it works as expected.

.. activecode:: cfu_0407_2
   :nocodelens:
   
   def mystery(s):
       return len(s) * 2 + 1
   
   #write tests below
   

Q#3
~~~

Write a function called ``repeat5`` that that takes in a string as input, and repeats the first two letters of the string three times (example: ``repeat5('hello')`` will return ``'hehehe'``.  Write at least three test cases along with their predictions, and run your code to make sure that your tests are accurate (or that the function itself works).

.. activecode:: cfu_0407_4
   :nocodelens:
   
   #write function below
   
   
   #write tests below
   