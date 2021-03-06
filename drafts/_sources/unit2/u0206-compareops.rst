.. qnum::
   :start: 1
   :prefix: ch0206-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".

Lesson 02-06: Comparison Operators
==================================

**Learning Target: I can use boolean operators to compare values.**

Comparison Operators
--------------------

Now that we've famliarized ourselves with the basic boolean operators, let's dive a little bit deeper.  These next set of boolean operators will enable us to compare values.  These comparison operators are:

   +--------------------------+----------+
   | Description              | Operator |
   +==========================+==========+
   | Equal To                 | ``==``   |
   +--------------------------+----------+
   | Not Equal To             | ``!=``   |
   +--------------------------+----------+
   | Greater Than             | ``>``    |
   +--------------------------+----------+
   | Less Than                | ``<``    |
   +--------------------------+----------+
   | Greater Than or Equal to | ``>=``   |
   +--------------------------+----------+
   | Less Than or Equal to    | ``<=``   |
   +--------------------------+----------+

With the exception of ``==`` and ``!=``, these operators should seem fairly familiar - you probably encountered them in your math class when discussing *inequalities*.  

You may be wondering why the "equals to" is two equal signs instead of one.  Pop quiz!

.. mchoice:: cfu_boolops_1
   :correct: b
   :answer_a: equals to
   :answer_b: variable assignment
   :answer_c: mathematical equation
   :feedback_a: Remember - equals to is a double equal sign!
   :feedback_b: Nice job!
   :feedback_c: Remember to think in the context of python code.  When would you see an equal sign?
   
   What does a single equal sign mean in Python?
   
Recall that a single equal sign indicates that *some value* is being saved into *some variable*.  Therefore, the computer needs a way to differentiate between variable assignment and "equals to" - so "equals to" is ``==``.

Note that while you can compare strings using ``>`` and ``<``, we will not be covering it in this book.

Examples
--------

Basic Examples
~~~~~~~~~~~~~~

Try to look through every example and make sure that you understand each one:

.. activecode:: ex_boolops_1
   :nocodelens:
   :autorun:

   print(3 > 5) # ==> false
   print(10 < 15) # ==> true
   print(5 >= 5) # ==> true
   print(6 >= 5) # ==> true
   print("hello" == "hello") # ==> true
   print("abc" != "abc") # ==> false

Special Examples
~~~~~~~~~~~~~~~~

These examples cover some special cases that may not be thought about at first:

.. activecode:: ex_booloops_2
   :nocodelens:
   :autorun:
   
   print(13.0000 == 13) # ==> true (example 1)
   print(13 == "13") # ==> false (example 2)
   print(14 > 10 + 2) # ==> true (example 3)
   print("hehehe" == "he" * 3) # ==> true (example 4)
   print(1 < 2 < 3) # ==> true (example 5)
   print(1 == 1 and False) # ==> false (example 6)

Examples 1 + 2
``````````````

::

   # example 1
   print(13.0000 == 13) # true
   
   # example 2
   print(13 == "13") # false

In example 1, although the left side is a float and the right side is an integer, it still prints ``True`` because their values are compared.  :misc-hl:`Values are compared with floats and ints because they are both numbers.`   However, as you can see in example 2, the same privilege doesn't extend to strings.  :misc-hl:`Types are considered when comparing values.`

Examples 3 + 4
``````````````

::
   
   # example 3
   print(14 > 10 + 2) # true
   
   # example 4
   print("hehe" + "he" == "he" * 3) # true

In both of these examples, the left and/or right side of the operator is an expression.  These are still valid because the :misc-hl:`expressions are evaluated before the boolean operator is handled`.

For example, in example 4, both ``"hehe" + "he"`` and ``"he" * 3`` are evaluated.  ``"hehe" + "he"`` becomes ``"hehehe"`` and ``"he" * 3`` becomes ``"hehehe"``, so the comparison in the end is ``"hehehe" == "hehehe"``, which is ``True``!

Example 5
`````````

::

   # example 5
   print(1 < 2 < 3) # true

You can chain together comparisons.  This is something unique to python and newer programming languages.  The important thing is to know that the chained comparison:

::

   a < b < c
   # or
   1 < 2 < 3

is the same thing as saying:

::

   a < b and b < c
   # or
   1 < 2 and 2 < 3

That is to say, :misc-hl:`chained comparisons are evaluated as separate boolean expressions connected with AND operators`.

Example 6
`````````

::

   # example 6
   print(1 == 1 and False) # false

Here, we are combining the comparison operators and boolean operators from before.  It is important to know the order in which things are evaluated.  In cases like these, please know that :misc-hl:`comparison operators always get evaluated BEFORE and/or/not`.  

Checks for Understanding
------------------------

Q#1
~~~

.. dragndrop:: 0206_cfu_1
   :feedback: Try again, review the lesson if you need to!
   :match_1: ==|||equal to
   :match_2: >|||greater than
   :match_3: <|||less than
   :match_4: !=|||not equal to
   :match_5: >=|||greater than or equal to
   :match_6: <=|||less than or equal to
   
   Drag the comparison operator to its description.

Q#2
~~~

.. fillintheblank:: 0206_cfu_2
   
   .. blank:: 0205_cfu_2_1
      :correct: ^12\.3 *== *x$|^x *== *12\.3$
      :feedback1: ("^12\.3 *= *x$|^x *= *12\.3$", "Close - what's the equals to operator?")
      :feedback2: (".*", "Try again!")
      
      Write an expression that tests if the variable ``x`` is equivalent to 12.3

Q#3
~~~

.. fillintheblank:: 0206_cfu_3_1

   .. blank:: 0206_cfu_3_1
      :correct: ^True$
      :feedback1: ("^true$", "Remember - uppercase T in True!")
      
      Evaluate True or False: ``1 == 1.0``

.. fillintheblank:: 0206_cfu_3_2
   
   .. blank:: 0206_cfu_3_2
      :correct: ^False$
      :feedback1: ("^false$", "Remember - uppercase F in False!")
      
      Evaluate True or False: ``1 > 1.01``

.. fillintheblank:: 0206_cfu_3_3

   .. blank:: 0206_cfu_3_3
      :correct: ^False$
      :feedback1: ("^false$", "Remember - uppercase F in False!")

      Evaluate True or False: ``-1 <= -2``
      
.. fillintheblank:: 0206_cfu_3_4

   .. blank:: 0206_cfu_3_4
      :correct: 
      :feedback1: ("^true$", "Remember - uppercase T in True!")
      
      Evaluate True or False: ``3 != "3"``
      