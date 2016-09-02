.. qnum::
   :start: 1
   :prefix: u0408-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".


Lesson 04-08: Functions within Functions
========================================

**Learning Target: I can write functions that call other functions.**
**Learning Target: I can explain how the call stack works.**

You can call functions from within functions!  Check it out:

.. activecode:: ex_0408_1
   :autorun:
   
   def f1():
       print("we need")
       f2()
   
   def f2():
       print("to go")
       f3()
   
   def f3():
       print("deeper!")
   
   f1()

Now if we look at the codelens for the same code:

.. codelens:: cl_0408_2
   :showoutput:
   
   def f1():
       print("we need")
       f2()

   def f2():
       print("to go")
       f3()
   
   def f3():
       print("deeper!")
   
   f1()
   
You'll notice a few things:

   - Steps 5 through 12 start from ``f1()`` all the way into ``f3()``, printing out the strings.
   - During this time, we see ``f1``, ``f2``, ``f3``, all stacked on top of each other.
   - Steps 13 through 15 show each function returning ``None`` as each of ``f1``/``f2``/``f3`` disappears.

The stack of function names you see is called the :vocab-word:`call stack`.

The Call Stack
--------------

Every time you call a function, that function is added to the **call stack**.  The call stack keeps track of where the program will return to when a function ends.

In the above example, since ``f2()`` is called inside of ``f1()``, ``f1()`` can't be complete until ``f2()`` completes.  Same with ``f2()`` and ``f3()``.

A call stack can only behave in two ways, either by:
   - adding a new function onto the top of the stack (when a function is called)
   - removing the current function from the top of the stack (when a function completes and returns a value)

True to its name, a call stack just "stacks" functions on top of each other, in the order that it was called.  We always know which function we will be returning to, since it is the next function in the stack.