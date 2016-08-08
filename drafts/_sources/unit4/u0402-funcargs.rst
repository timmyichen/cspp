.. qnum::
   :start: 1
   :prefix: u0402-


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

Note that the ordering of the arguments matter.  When I run ``add(x,y,z)`` it prints out the numbers in the order of ``1, 2, and 3``.  However, when I run ``add(z,y,x)``, it prints out the numbers in the order of ``3, 1, and 2``.

What Actually Gets Passed?
--------------------------

Although it might seem like we are passing variables, it's very important to remember that we are just passing the value within a variable.