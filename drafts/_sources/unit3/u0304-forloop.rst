.. qnum::
   :start: 1
   :prefix: u0304-


Lesson 03-04: The ``for`` Loop
================================

**Learning Target: I can use for loops to repeat a set of instructions.**

``for`` Loop Syntax
-------------------

In addition to conditionals (``if`` statements), another type of control structure are loops. Loops, as the name implies, will repeat some code based on certain conditions!  The first loop we are going to learn is the ``for`` loop.

At a very basic level, the syntax of a ``for`` loop looks like this:

::
   
   for x in range(times_to_repeat):
       #code to repeat
   
So for example, running the code below will print ``"Hello!"`` five times:

.. activecode:: 0304_ex_1
   :autorun:
   
   for x in range(5):
       print("Hello!")

Note that similar to ``if`` statements, ``for`` loops require a colon at the end and a tab on the next line.  This is true anytime you see a colon.  But what it also means is, :misc-hl:`the only part that is looped is the part that is tabbed in!`.  Take the following as an example:

.. activecode:: 0304_ex_2
   :autorun:
   
   for x in range(5):
       print("Inside the loop")
   print("Outside the loop")

Hopefully you notice that the "Outside the loop" is only printed once - because it is not considered within the loop.  When looping, you wait for the loop to continue executing, then you continue on after the loop.

Checks For Understanding
------------------------

Q#1
~~~

::
   
   print("boo")
   for x in range(5):
       print("boo")
   print("boo")

.. mchoice:: 0304_cfu_1
   :correct: d
   :answer_a: 3
   :answer_b: 5
   :answer_c: 6
   :answer_d: 7
   :answer_e: 9
   :feedback_b: Don't forget to count the ones outside the loop!
   
   How many times does "boo" get printed in the block of code above?

Q#2
~~~

In the space below, write a ``for`` loop that will print out ``"Baking soda!"`` three times.

.. activecode:: 0304_cfu_2
   :nocodelens:
   
   #write your code here!

Your code should only contain two lines.  The output when run will look like:

.. code-block:: none

   Baking soda!
   Baking soda!
   Baking soda!

Q#3
~~~

Beyonce's hit single, *Single Ladies*, starts off like this:

.. code-block:: none

   All the single ladies (All the single ladies)
   All the single ladies (All the single ladies)
   All the single ladies (All the single ladies)
   All the single ladies
   Now put your hands up

Write a short program using ``print()`` statements and a ``for`` loop that will print out the lyrics to the introduction of this song.  You can have ``print()`` statement outside the loop, but no two ``print()`` statements can be the same.

.. activecode:: 0304_cfu_3
   :nocodelens:
   
   #write your code here!