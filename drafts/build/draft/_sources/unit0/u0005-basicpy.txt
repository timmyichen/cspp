.. qnum::
   :start: 1
   :prefix: u0005-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".


Lesson 00-05: Basic Python
==========================

This lesson is just a quick lesson on a few python basics.

``print()`` statements
----------------------

The most basic way of seeing output is by using the ``print()`` statement.  Basic syntax is as follows:

.. activecode:: ex_0005_1
   :nocodelens:
   :autorun:
   
   print("Print stuff!")
   print("Parentheses and Quotes are required, for now")
   print("Stuff you print goes in between the quotes")
   print('Single quotes work too.')

Whitespace
----------

Whitespace refers to spaces or tabs.  At this stage of knowledge, having whitespace before python commands will cause errors.  Try running the example below:

.. activecode:: ex_0005_2
   :nocodelens:
   
   print("hello")
     print("world")
            print("howdy")

Whitespace has a very specific meaning in python, and we will cover this later - just know that for now, your code statements should not have any whitespace in front of it.

Comments
--------

See the code below:

.. activecode:: ex_0005_3
   :nocodelens:
   :autorun:
   
   print("Only this line gets run")
   # because this is a comment and comments are not run
   # You will know it's a comment because of the # sign
   print("hi") # these comments can be on the same line as statements
   
   """ You can have
   multi-line comments
   using triple quotes"""
   
   '''Single quotes
   also
   work
   '''
   print("this line also gets run, but no comments will show")