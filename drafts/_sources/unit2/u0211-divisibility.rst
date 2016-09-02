.. qnum::
   :start: 1
   :prefix: ch0211-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".

Lesson 02-11: Checking for Divisibility
=======================================

**Learning Target: I can create a conditional to check for divisibility.**

One of the first skills a programmer learns using conditionals is the skill of *testing for divisibility*.  The first most basic example is to check whether a number is odd or even.

Odd / Even
----------

Recall that a number is even if it is divisible by two, and a number is odd if it is not divisible by two.

To check whether a number is divisible by two, let's first explore our own thought processes.  Let's take a few examples and examine them.

   - :math:`5\div2 = 2.5 \Longrightarrow` is 5 divisible by 2?  How do you know?
   - :math:`37\div2 = 18.5 \Longrightarrow` is 5 divisible by 2?  How do you know?
   - :math:`14\div2 = 7.5 \Longrightarrow` is 5 divisible by 2?  How do you know?

   - :math:`100\div2 = 50 \Longrightarrow` is 5 divisible by 2?  How do you know?
   - :math:`26\div2 = 13 \Longrightarrow` is 5 divisible by 2?  How do you know?
   - :math:`44\div2 = 22 \Longrightarrow` is 5 divisible by 2?  How do you know?

Notice the pattern?  Whenever a number is not divisible by 2, it has a decimal - or in other words, it has a **remainder**.  We have something that can calculate remainder - what was it?

.. mchoice:: 0211_cfu_1
   :correct: c
   :answer_a: **
   :answer_b: float()
   :answer_c: %
   :answer_d: remainder()
   :feedback_a: That represents an exponent!
   :feedback_b: That's a conversion function!
   :feedback_c: That's Modulo!
   :feedback_d: That doesn't exist!
   
   What can we use to calculate remainder after division?
   
Great!  Except this time, we want to check if an expression has NO remainder.  Let's start by writing what we know.

In order to check whether an integer ``number`` is divisible by 2, the expression ``number % 2`` will give us the remainder after division.  If ``number`` is even, then it means 2 goes into it without remainder.  This means that the remainder should be zero.  So we want to check if ``number % 2`` will be zero.

.. fillintheblank:: 0211_cfu_2

   .. blank:: 0211_fitb_2
      :correct: ^ *number *% *2 *== *0 *$
      :feedback1: ("^ *number *% *2 *= *0 *$", "don't forget how to represent 'equals' in python!")
      :feedback2: (".*", "Try again! You should be writing a valid boolean expression.")
   
      How do you represent ``number % 2`` equals zero as a boolean expression?

If you're at this point, great job!  We have a boolean expression to represent whether a number is divisible by a 2 or not!  Feel free to try it out in the space below:

.. activecode:: 0211_ex_1
   
   number = 10 #replace this number with anything!
   if number % 2 == 0:
       print("{} is even!".format(number))
   else:
       print("{} is odd!".format(number))


Checking For Divisibility
-------------------------

Let's try to generalize this rule so it will work with any number:

Right now, ``number % 2 == 0`` checks for divisibility by 2.

   - If we wanted to check for divisibility by 3, we would use the expression ``number % 3 == 0``
   - If we wanted to check for divisibility by 4, we would use the expression ``number % 4 == 0``
   - If we wanted to check for divisibility by 5, we would use the expression ``number % 5 == 0``

Notice the pattern?

So we can generalize by saying: :misc-hl:`If we want to check for divisibility by N, we can use the expression` ``number % N == 0`` :misc-hl:`that will be True if it is divisible and False otherwise.`

Checks for Understanding
------------------------

Q#1
~~~

.. fillintheblank:: 0211_cfu_3

   .. blank:: 0211_fitb_3
      :correct: ^ *number *% *10 *== *0 *$
      :feedback1: ("^ *number *% *10 *= *0 *$", "don't forget how to represent 'equals' in python!")
      :feedback2: (".*", "Try again! You should be writing a valid boolean expression.")
   
      Write a boolean expression that represents divisibility by 10.

Q#2
~~~

.. fillintheblank:: 0211_cfu_4

   .. blank:: 0211_fitb_4
      :correct: ^ *number *% *7 *== *0 *$
      :feedback1: ("^ *number *% *7 *= *0 *$", "don't forget how to represent 'equals' in python!")
      :feedback2: (".*", "Try again! You should be writing a valid boolean expression.")
   
      Write a boolean expression that represents divisibility by 7.

Q#3
~~~

.. fillintheblank:: 0211_cfu_5

   .. blank:: 0211_fitb_5
      :correct: ^ *number *% *12 *== *0 *$
      :feedback1: ("^ *number *% *2 *= *0 *$", "don't forget how to represent 'equals' in python!")
      :feedback2: (".*", "Try again! You should be writing a valid boolean expression.")
   
      Write a boolean expression that represents divisibility by 12.