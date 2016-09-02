.. qnum::
   :start: 1
   :prefix: u0308-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".


Lesson 03-08: The ``while`` Loop
================================

**Learning Target: I can use while loops to repeat a set of instructions.**

While ``for`` loops are useful when you know exactly how many times you want to iterate, what if you don't?

``while`` Loop Syntax
---------------------

Here is a ``for`` loop and a ``while`` loop that does the exact same thing:

::

   for n in range(5):
       print(n)
   print("Done!")
   
   n = 0
   while n < 5:
       print(n)
       n = n + 1
   print("Done!")

Let's take the second one and look at the step-by-step process.  Click on "Show Codelens" below to step through the code:
   
.. activecode:: 0308_ex_1
   :autorun:
   
   n = 0
   while n < 5:
       print(n)
       n = n + 1
   print("Done!")

Let's go over how the ``while`` loop works:

A while loop works very similarly to an ``if`` statement, with one big difference: as long as the statemet following ``while`` is ``True``, it will loop the code inside!

:misc-hl:`WARNING: If you get caught in an infinite loop in the terminal, you can use CTRL+C to stop code execution!  But it's best to avoid infinite loops - which will be explored in the next lesson.`

Here's an example that isn't based on numbers.

.. activecode:: 0308_ex_2
   
   word = input("Enter any word that's not 'quit': ")
   
   # this loop will continue as long as the user's input
   #  is not "quit"
   while word != "quit":
       print("You said: {}".format(word))
       word = input("Now enter 'quit' to quit! Or enter anything else to keep going!")
   print("Quitting loop")

Here, we write a loop that waits for a user to type "quit" and repeatedly asks the user to type something in until that happens.  You might notice on line 1 that we actually ask the user for an input before we even start looping - this is because on line 5, our condition is ``word != "quit"``, so ``word`` needs a value (needs to be initialized).  Then, on line 7, we have to re-ask the user to type in something else, so that the user can type in "quit" to quit.

Write a while loop on line 4 below so that the loop will continue as long as ``x`` is less than 200.  If done correctly, it should print: ``2 4 8 16 32 64 128 done``

.. activecode:: 0308_cfu_1
   :nocodelens:
   
   x = 2
   
   
       print(x, end=" ")
       x = x * 2
   print("done")


``for`` VS. ``while``
---------------------

Now that we know how to use both ``for`` loops and ``while`` loops, it's important to understand when to use each one.  While they are both similar in the sense that they both repeat code, they are used in different situations.

In ``for`` loops, you know exactly how many times you are looping.  This is defined either within the ``range()`` function or in another iterable (which we will learn about later).  In ``while`` loops, you continue to loop until a certain condition is met - it is not always clear exactly how many times the code will loop.

Therefore, when choosing between ``for`` and ``while`` loops, you should follow the following guidelines:
   
- If you know exactly how many times you need to loop, use a ``for`` loop.
- If not, use a ``while`` loop.

.. mchoice:: 0308_cfu_2
   :correct: a
   :answer_a: for
   :answer_b: while
   :feedback_b: Do you know exactly how many times you'll need to loop?

   Let's say you need to create a program to add up all prime numbers up to 1000.  What kind of loop should you use?

.. mchoice:: 0308_cfu_3
   :correct: b
   :answer_a: for
   :answer_b: while
   :feedback_a: Do you know exactly how many times you'll need to loop? Be especially careful of the wording "as long as"
   :feedback_b: Nice job!  The key phrase is "as long as"

   Let's say you need to create a program to add up all powers of two as long as the sum is less than 5000.  What kind of loop should you use?