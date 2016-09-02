.. qnum::
   :start: 1
   :prefix: u0312-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".


Lesson 03-12: The ``random`` module
===================================

**Learning Target: I can use the random module to generate random numbers.**

Importing The ``random`` Module
-------------------------------

When you import modules, you should always do so at the beginning of your file, at the very top.  The syntax is usually:

::
   
   import module_name

In this case, our module is named ``random``, so we would use this:

::

   import random

Once we have this code, this gives us access to a bunch of functions that are packaged within the ``random`` module.  Although there are many, the one we are probably going to use the most is called ``randint()``.

Using ``randint()``
-------------------

Using the function ``random.randint(a,b)`` will give you a random integer between ``a`` and ``b``, inclusive.  Here are a few examples.  Feel free to re-run them to generate different numbers.

.. activecode:: 0312_ex_1
   :autorun:
   :nocodelens:
   
   import random
   #this will generate 5 #s between 1 and 10
   for x in range(5):
       print(random.randint(1,10))

Please note that unlike the ``range()`` function, where ``range(1,10)`` would not include 10, ``random.randint(1,10)`` DOES include the 10.

An Example Of Randomness
------------------------

The following is an example of a bit of code that uses random number generation.  This code will continuously roll two imaginary dice until it rolls a double (two of the same number).

.. activecode:: 0312_ex_2
   :autorun:
   
   import random
   
   die1 = 1
   die2 = 2
   while die1 != die2:
       die1 = random.randint(1,6)
       die2 = random.randint(1,6)
       print("Rolled a {},{}".format(die1,die2))
   
   print("Got doubles!")