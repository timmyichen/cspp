.. qnum::
   :start: 1
   :prefix: u0004-


Lesson 00-04: Basic Python
==========================

This lesson is just a quick lesson on a few python basics.

``print()`` statements
----------------------

The most basic way of seeing output is by using the ``print()`` statement.  Basic syntax is as follows:

.. activecode:: 0004_ex_1
   :nocodelens:
   :autorun:
   
   print("Print stuff!")
   print("Parentheses and Quotes are required, for now")
   print("Stuff you print goes in between the quotes")
   print('Single quotes work too.')

Whitespace
----------

Whitespace refers to spaces or tabs.  At this stage of knowledge, having whitespace before python commands will cause errors.  Try running the example below:

.. activecode:: 0004_ex_2
   :nocodelens:
   
   print("hello")
     print("world")
            print("howdy")

Whitespace has a very specific meaning in python, and we will cover this later - just know that for now, your code statements should not have any whitespace in front of it.

Comments
--------

See the code below:

.. activecode:: 0004_ex_3
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