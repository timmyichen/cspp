.. qnum::
   :start: 1
   :prefix: u0413-


Lesson 04-13: ``main`` functions
================================

**Learning Target: I can incorporate main functions into my code.**

What is a ``main`` function?
----------------------------

Previously, when working with functions, any code that was not a part of a function would be called the "main body" of the code - the code that gets run first (and uses the functions that you've created).  However, this is not best practice.  We should have a separate function for the main body of our code, and this is typically put inside of a function called ``main``.

For example, if my code looked something like this:

.. code-block:: python3
   :linenos:
   
   def function1():
       #stuff
   
   def function2():
       #stuff
   
   def function3():
       #stuff
   
   function1()
   function2()
   function3()

Lines 10-12 would be the main body of my code, as it is what gets run first.  However, after moving everything into a ``main`` function, it will look like this:

.. code-block:: python3
   :linenos:
   
   def function1():
       #stuff
   
   def function2():
       #stuff
   
   def function3():
       #stuff
   
   def main():   
      function1()
      function2()
      function3()
   
   main()

Notice how we have an additional function call on line 15, which just calls ``main()``, which executes our functions.  This code does the same thing as above.

The ``__name__`` attribute
--------------------------

So why do we want to use a ``main`` function?  Well, the problem arises when we start to import functions from other python files, some of which you will be creating.

For example, when you run ``import random`` to access to random library, you are getting access to all the useful functions in ``random``, such as ``random.randint()``.  However, if that ``random.py`` file had code that didn't belong in any function, that code would be executed whenever someone imported the file!

We will be eventually creating :vocab-word:`libraries/modules`, which is :vocab-def:`a collection of useful code bundled together for other programs to use`.  Note that this is a general definition, and there are differences between python modules, libraries, and collections.  Because of this, it's important that none of our main code gets run when we are just importing it as a file.

To get it to run, we just include this snippet in our files, at the bottom:

.. code-block:: python3

   if __name__ == "__main__":
       main()

The ``__name__`` variable is a special variable set by the python interpreter.  If we are running a program directly, it will set ``__name__`` to ``"__main__"``.  But if we import it from another file, ``__name__`` will be set to that importing file's name instead.

So if we are only running the ``main()`` function when ``__name__`` is ``"__main__"``, we are only running the main code when we are **not** importing it as a function, which is a best practice when writing python code.