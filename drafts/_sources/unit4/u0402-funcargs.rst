.. qnum::
   :start: 1
   :prefix: u0402-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".


Lesson 04-02: Passing Data to Functions
=======================================

**Learning Target: I can pass data to functions using arguments.**

Accepting Function Arguments
----------------------------

Our previous functions weren't very useful, and rightly so - all it was doing was repeating code or printing something static (unchanging).  In this lesson, we will learn how to pass data to a function.

:vocab-word:`Arguments` are :vocab-def:`data that is passed to a function`.  To allow a function to accept arguments, we have to include it in the function definition (header).  An example:

::
   
   def say_hello(name):
       print("Hello {}!".format(name))

The arguments in the function arguments are **variable names**.  These variables are declared as part of the function header, and are basically telling the function to expect some data to be sent.  You can have more than one argument too - they would just be separated by variables.

::
   
   def add(a,b,c):
       sum = a + b + c
       print("The sum of {}, {}, and {}, is {}!".format(a,b,c,sum))

The above function takes three pieces of data and saves it in the variables ``a``, ``b``, and ``c`` respectively.  So how do we actually send data to a function that's ready to accept data?

Passing Function Arguments
--------------------------

When we call upon a function that has arguments, we have to supply the same number of arguments.  Let's take a look at a few examples from above:

.. activecode:: 0402_ex_1
   :autorun:

   def say_hello(name):
       print("Hello {}!".format(name))
   
   say_hello("Bob")
   
   other_name = "Hannah"
   say_hello(other_name)

Notice that I call this function twice - one just by passing a string ("Bob") and another by passing a variable (other_name) that represents a string ("Hannah").  Both ways work, for now.

.. activecode:: 0402_ex_2
   :autorun:   
   
   def add(a,b,c):
       sum = a + b + c
       print("The sum of {}, {}, and {}, is {}!".format(a,b,c,sum))
   
   add(1,2,3)
   
   x = 1
   y = 2
   z = 3
   add(x,y,z)
   add(z,y,x)

Note that the ordering of the arguments matter.  When I run ``add(x,y,z)`` it prints out the numbers in the order of ``1, 2, and 3``.  However, when I run ``add(z,y,x)``, it prints out the numbers in the order of ``3, 2, and 1``.

What Actually Gets Passed?
--------------------------

Although it might seem like we are passing variables, it's very important to remember that we are just passing the value within a variable.  The variable itself will not be changed.  Let's look at this example:

.. activecode:: 0402_ex_3
   :autorun:
   
   def add_one(a):
       print("in function: a is {}".format(a))
       a = a + 1
       print("in function: a is now {}".format(a))
   
   x = 20
   print("before function: x is {}".format(x))
   add_one(x)
   print("after function: x is now {}".format(x))
   
In this code, we are sending (the value of) ``x`` to the function ``add_one``, which stores it in a variable ``a`` and increases is by one.  We can see that ``a`` was increased by 1 because of the output.  However, the value of ``x`` is not changed.

Checks For Understanding
------------------------

Q#1
~~~

In the space below, write a function called ``times_10`` that takes in a single number argument and prints the value of the number times ten (you can assume that the data passed to the function will be a number).  Do not change any of the function calls.  If done correctly, you should see the following as output:

.. code-block:: none

   30
   500
   15.0

.. activecode:: 0402_cfu_1
   
   #write function below
   
   
   #dont change tests below
   times_10(3)
   times_10(50)
   times_10(1.5)

Q#2
~~~

In the space below, write a function called ``compare`` that takes two number arguments and prints the value of the higher one.  You can assume that the data passed to the function will be numbers.  Do not change any of the function calls.  If done correctly, you should see the following as output:

.. code-block:: none

   5
   100
   10.001

.. activecode:: 0402_cfu_2
   
   #write function below
   
   
   #dont change tests below
   compare(5,2)
   compare(100,100)
   compare(10,10.001)

Q#3
~~~

In the space below, write a function called ``compare3`` that takes three number arguments and prints out the highest one.  You can assume that the data passed to the function will be numbers.  Do not change any of the function calls.  If done correctly, you should see the following as output:

.. code-block:: none

   3
   10
   -6

As a hint, given ``a``, ``b``, and ``c``, you would know that ``a`` is the highest number if ``a`` is greater than both ``b`` and ``c``.

.. activecode:: 0402_cfu_3
   
   #write function below
   
   
   #dont change tests below
   compare3(1,2,3)
   compare3(7,3,10)
   compare3(-6,-22,-6)