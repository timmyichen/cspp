.. qnum::
   :start: 1
   :prefix: u0405-


Lesson 04-05: Functions are Values
==================================

**Learning Target: I can understand the value representation of a function.**

*NOTE: This lesson involves computer memory addresses.  Since the activecode windows uses a javascript implementation of python, we won't be able to provide interactive examples here.  However, all the code shown is valid python, and you should feel free to experiment with this code in your own python IDE.*

Printing Functions Without Parentheses
--------------------------------------

A common error that people make when first learning about functions is to call the function without parentheses.  So what happens if we do that?  Here's an example:

.. code-block:: python3
   :linenos:
   
   def func():
       return 1
   
   print(func())
   print(func)

Running this block of code will give us:

.. code-block:: none

   1
   <function func at 0x7fe2d338abf8>

When you try to access the function name without parentheses, it will give you the **location of the function in the computer's memory**.  This is where the computer stores the instructions of the function name, just as any other variable.  We can use the built-in ``id()`` function to give us the memory address of any variable or function.  For example:

.. code-block:: python3
   :linenos:
   
   def func():
       return 1
   
   var1 = 100
   var2 = "string!"
   print(id(var1))
   print(id(var2))
   print(id(func))
   
This will print out:

.. code-block:: none

   10108992
   140074418775912
   140074418949112

These numbers, while correct, look way different from what we were getting earlier.  That's because these numbers are in decimal (base 10), and the number ``0x7fe2d338abf8`` above is in hexadecimal (base 16) - don't worry, we'll learn about binary, decimal, and hexadecimal later.  We can use the built-in ``hex()`` function to convert these numbers to hexadecimal:

.. code-block:: python3
   :linenos:
   
   def func():
       return 1
   
   var1 = 100
   var2 = "string!"
   print(hex(id(var1)))
   print(hex(id(var2)))
   print(hex(id(func)))

This will print:

.. code-block:: none
   
   0x9a4040
   0x7f8728ebf768
   0x7f8728ee9bf8

Notice that it's not the same as above.  That's because since we're talking about locations in computer memory, a computer is processing lots of stuff at a time and every time we run the program, it may give our variables a different location.  We can use the python shell to demonstrate that this is true:

.. code-block:: none
   :linenos:
   :emphasize-lines: 5,9
   
   >>> def a():                                                                                                                                
   ...   return 10
   ... 
   >>> a
   <function a at 0x7f1298518400>
   >>> id(a)
   139717841617920
   >>> hex(id(a))
   '0x7f1298518400'

(reminder: the ``>>>`` are my inputs, and the line underneath are outputs.  The first three lines are just a function definition)

:misc-hl:`You won't be working with memory addresses in the scope of this course, but it's important to know what you're looking at.`