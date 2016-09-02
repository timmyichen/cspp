.. qnum::
   :start: 1
   :prefix: u0406-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".


Lesson 04-06: Functions & Synchronous Execution
===============================================

**Learning Target: I can predict function code execution.**

One Instruction At A Time
-------------------------

In this book, we'll be running python synchronously on a single thread.  What this means is that :misc-hl:`our programs will only ever be executing one instruction at a time, going in the exact order that we tell it to`.  Before we learned functions, programs were easy to follow.  We would read instructions top-down, occasionally going back up to repeat a loop, or skipping some code in a conditional.  However, with functions, suddenly we're all over the place!  Being able to manually trace through our code is vital to efficient debugging.

In learning how the code moves around, our best friend here is codelens, or `PythonTutor <http://pythontutor.com/visualize.html#mode=edit>`_.

Let's look at a simple example of a function call and determine what the program is doing:

.. codelens:: cl_0406_1
   
   def add2(x,y):
       return x + y
   
   sum = add2(5,6)
   print(sum)

There are six steps here.  Let's break them down (following the red arrow):

1. Define the function ``add2``.
2. Call the function ``add2`` with arguments ``5`` and ``6``.
3. Entering the function assign the arguments ``5`` and ``6`` to the variables ``x`` and ``y`` respectively.
4. Return the sum of ``x+y``, which is ``11``.
5. ``11`` gets returned to the function call on line 4.
6. Now that we've evaluated the function, we continue with line 4 by storing the value ``11`` in ``sum``.
7. (last) We print out the value of ``sum``, which is ``11``.

Notice how on line 4, when we reach the function call, we save our spot while we execute the function - and when we're done with the function, we go right back to where we were (on line 4).  This principle is very important when trying to trace through code.  Here's a slightly more complex one:

.. codelens:: cl_0406_2

   def is_integer(n):
       if int(n) == n:
           return True
       else:
           return False
   
   def is_even(n):
       if n % 2 == 0:
           return True
       else:
           return False
   
   num = 10
   if is_integer(num) and is_even(num):
       print("The number {} is an even whole number!".format(num))
   else:
       print("The number {} is either not even or not an integer".format(num))
   
In this one, as you step through the code, you'll notice that the function ``is_integer()`` is called first, and ``is_even()`` is called right after it.  That's because the conditional ``is_integer(num) and is_even(num)`` requires both functions to be evaluated in order to be evaluated as a whole, so it goes through each function in the order of operations (in this case, ``and``, which is just left-to-right).  Each time, when the function completes, it returns to where it was called to look for its next instruction.

Checks For Understanding
------------------------

Q#1
~~~

.. code-block:: python3
   :linenos:
   
   def func1(n):
       if n > 0:
           return True
       else:
           return False
   
   def func2(n):
       if n < 0:
           return True
       else:
           return False
   
   num = -2
   if func1(n):
       print("alpha")
   elif func2(n):
       print("beta")
   else:
       print("gamma")
   
.. fillintheblank:: cfu_0406_1
   
   .. blank:: cfu_0406_1_1
      :correct: ^beta$
      :feedback1: ("^(b|B)(e|E)(t|T)(a|A)$", "Answer should be case sensitive.")
      :feedback2: (".*", "Try again!  Try to trace through the code, line by line.")

      What will be printed from running the code above?

.. fillintheblank:: cfu_0406_2
   
   .. blank:: cfu_0406_1_1
      :correct: ^gamma$
      :feedback1: ("^(g|G)(a|A)(m|M){2}(a|A)$", "Answer should be case sensitive.")
      :feedback2: (".*", "Try again!  Try to trace through the code, line by line.")

      What will be printed from running the code above if line 13 was ``num = 0`` instead?