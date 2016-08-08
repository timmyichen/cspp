.. qnum::
   :start: 1
   :prefix: u0401-


Lesson 04-01: Functions in Python
=================================

**Learning Target: I can identify parts of a function header.**
**Learning Target: I can create functions to perform a given task.**

Two of the core pillars of computational thinking are the concepts of :vocab-word:`decomposition` and :vocab-word:`abstraction`.  Through functions, you will learn to implement both in your work.

What are Functions?
-------------------

Functions are a way of setting aside code that you can use repeatedly.  They exist in almost every programming language, and are a huge part of learning how to program.  While there are many things you can do with functions, this lesson will only cover the basics: how to create a function and how to use (call) a function.

Creating a Function
-------------------

To create a function, you would have to first write a function header.  A function header looks like this:

::
   
   def function_name(args):
       #code in function
   
Let's break it down:

.. image:: img/funcheader.svg
   :width: 500px
   :alt: parts of a function header
   :align: center

1. The ``def`` keyword just indicates that we are starting to write a function header
2. The name of the function goes here. You can name a function in the same ways you can name a variable.
3. Arguments go here. This is covered in the next lesson, so here you would usually leave it as blank parentheses ``()``
4. Colon is required! Don't forget!
5. The code underneath that is tabbed is the code inside the function.

Here's an example of a function that will print "Hey bestest buddy" every time it is run.  We'll call it ``say_hi``.  The function definition might look something like this:

::
   
   def say_hi():
       print("Hey bestest buddy")
       
Our function could have multiple lines of code in it as well:

::
   
   def say_hi():
       print("Hey bestest buddy")
       print("You're the best")
       print("Super best")

But if you try to run this code, you'll notice that nothing happens.

.. activecode:: 0401_ex_1
   :autorun:

   def say_hi():
       print("Hey bestest buddy")
       print("You're the best")
       print("Super best")
   
   print("Program ended.")

Using a Function
----------------

When you define a function, you are creating a block of code that can be used later on.  Just defining a function will NOT use that function!  To use a function, we have to :vocab-word:`call` it - using a :vocab-word:`function call`.

A function call is performed by using the function's name, followed by parentheses.  In our above example, to call the function, we would use the command ``say_hi()``.

Observe:

.. activecode:: 0401_ex_2
   :autorun:

   def say_hi():
       print("Hey bestest buddy")
       print("You're the best")
       print("Super best")
   
   say_hi()
   print("Program ended.")

This is where the repeatability comes into play.  We can call upon three lines of code just by using one!  What if we wanted to call it a bunch of times?

.. activecode:: 0401_ex_3
   :autorun:

   def say_hi():
       print("Hey bestest buddy")
       print("You're the best")
       print("Super best")
   
   say_hi()
   say_hi()
   say_hi()
   say_hi()
   print("Program ended.")

However, note that :misc-hl:`we cannot call a function before it is defined`.  Try running the following; you will get an error.

.. activecode:: 0401_ex_4

   say_hi()

   def say_hi():
       print("Hey bestest buddy")
       print("You're the best")
       print("Super best")
   
   print("Program ended.")



Checks For Understanding
------------------------

Q#1
~~~

On lines 1 and 2, write a function called ``print_hw`` that just prints ``"Hello World!"``.  Running the code below should result in the following output:

::

   Hello World!
   Hello World!
   Hello World!

.. activecode:: 0401_cfu_1
   
   #write here
   
   
   for x in range(3):
       print_hw()

Q#2
~~~

Starting on line 1, write a function called count_to_5 that will print the numbers 1 up to 5, one on each line, using a for loop.  Running the code below should result in the following output:

::
   
   1
   2
   3
   4
   5

.. activecode:: 0401_cfu_2

   #write here
   
   
   count_to_5()