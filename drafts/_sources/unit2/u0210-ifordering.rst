.. qnum::
   :start: 1
   :prefix: ch0210-

Lesson 02-10: Ordering of Conditionals
======================================

**Learning Target: I can predict the outcome of if/elif/else statements based on their order.**

Order Matters
-------------

What happens if multiple conditions throughout the ``if``/``/elif`` conditions are being satisfied?  Run the code below:

.. activecode:: 0210_ex_1
   
   number = 10
   
   if number > 2:
       print("Greater than 2!")
   elif number > 5:
       print("Greater than 5!")
   elif number > 8:
       print("Greater than 8!")
      
Notice that even though ``number`` is greater than 2, 4, and 8, satisfying all three conditions, only ``"Greater than 2!"`` gets printed.  Why is that?

.. mchoice:: 0210_cfu_1
   :correct: a
   :answer_a: the "if number greater than 2" is checked first
   :answer_b: 2 is the smallest of (2,5,8)
   :answer_c: it only checks the if statement
   :feedback_a: Order matters!
   :feedback_b: The value itself doesn't matter much here.
   :feedback_c: If the if statement were false, it would still continue!

   Why is "Greater than 2!" printed instead of any of the other options?

Here we can see clearly that :misc-hl:`the ordering within if statements matter!  This is especially true for conditionals that "overlap" in some ways`

Checks For Understanding
------------------------

TODO