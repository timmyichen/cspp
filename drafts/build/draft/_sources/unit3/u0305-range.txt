.. qnum::
   :start: 1
   :prefix: u0305-


Lesson 03-05: The ``range()`` Function
======================================

**Learning Target: I can use the range function to generate a specific list of numbers.**

In the last lesson, we learned about basic ``for`` loop syntax, using the ``range()`` function.  But what does the ``range()`` function actually do?

A Basic ``range()``
-------------------

If we print ``list(range(5))``, we'll see the following (don't worry about ``list`` yet, that's just how we visualize it):

::

   [0, 1, 2, 3, 4]

If we print ``list(range(8))``, we'll see the following:

::
   
   [0, 1, 2, 3, 4, 5, 6, 7]
   
Notice a pattern?

.. mchoice:: 0305_cfu_1
   :correct: b
   :answer_a: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
   :answer_b: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   :answer_c: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   :feedback_a: In the examples above, what do you notice about the last number compared to the number in range?
   
   What will list(range(11)) be?

So the ``range()`` function returns a list of numbers, which we use the ``for`` loop to loop through.  This is very powerful, because it allows us to specify almost any range of numbers.

Generating Ranges
-----------------

The ``range()`` function can take anywhere between one and three numbers.  Let's review how each one works.

With ``range(b)``
~~~~~~~~~~~~~~~~~

The rule for ``range(b)`` should be familiar. ``range(b)`` can be referred to as ``range(end)``.

**Using** ``range(end)`` **will produce a list of integers starting at 0 and ending at** ``end-1``.


With ``range(a,b)``
~~~~~~~~~~~~~~~~~~~

Let's look at a few examples when we feed the ``range()`` function two numbers:

.. activecode:: 0305_ex_1
   :autorun:
   
   print(list(range(5,7)))
   print(list(range(2,10)))
   print(list(range(-5,5)))
   print(list(range(10,20)))
   print(list(range(10,3)))

Notice the pattern?  Let's see if you got it:

.. mchoice:: 0305_cfu_2
   :correct: c
   :answer_a: [3, 4, 5, 6, 7, 8]
   :answer_b: [4, 5, 6, 7, 8]
   :answer_c: [3, 4, 5, 6, 7]
   :answer_d: [4, 5, 6, 7]
   :feedback_a: In the examples above, what do you notice about the first and last number compared to the two numbers in range?
   :feedback_b: In the examples above, what do you notice about the last number compared to the two numbers in range?
   :feedback_d: In the examples above, what do you notice about the first number compared to the two numbers in range?
   
   What will list(range(3,8)) be?

A ``range()`` function with 2 numbers can be referred to as ``range(start, end)``

As a general rule for ``range(start,end)``, **Using** ``range(start,end)`` **will produce a list of integers starting at** ``start`` **and ending at** ``end-1``.



With ``range(a,b,c)``
~~~~~~~~~~~~~~~~~~~~~

Let's look at a few examples when we feed the ``range()`` function three numbers:

.. activecode:: 0305_ex_2
   :autorun:
   
   print(list(range(1,10,1)))
   print(list(range(1,10,2)))
   print(list(range(1,10,3)))
   print(list(range(20,5,-2)))
   print(list(range(20,71,10)))

Notice the pattern?  Let's see if you got it:

.. mchoice:: 0305_cfu_3
   :correct: b
   :answer_a: [10, 7, 4, 1, -2, -5, -8]
   :answer_b: [10, 7, 4, 1, -2, -5]
   :answer_c: [7, 4, 1, -2, -5]

   What will list(range(10,-8,-3)) be?

Hopefully you noticed that the third number determines how much the next number in the list will change by.  This is called the **step**.  A step can be positive or negative.
   
A ``range()`` function with 3 numbers can be referred to as ``range(start, end, step)``

As a general rule for ``range(start,end,step)``, **Using** ``range(start,end,step)`` **will produce a list of integers starting at** ``start``, **changing by** ``step`` **with each number, and stopping before we get past** ``end``.

Checks For Understanding
------------------------

Q#1
~~~

.. fillintheblank:: 0305_cfu_4
   
   .. blank:: 0305_4_1
      :correct: ^range\( *-2 *, *5 *\)$|^range\( *-2 *, *5 *, *1 *\)$
      :feedback1: ("list", "Make sure you aren't including any list conversions!")
      :feedback2: (".*","Try again!")
      
      Come up with a range function that will produce the following numbers: ``[-2,-1,0,1,2,3,4]``


Q#2
~~~

.. fillintheblank:: 0305_cfu_5
   
   .. blank:: 0305_5_1
      :correct: ^range\( *1 *, *23 *, *3 *\)$|^range\( *1 *, *24 *, *3 *\)$|^range\( *1 *, *25 *, *3 *\)$
      :feedback1: ("list", "Make sure you aren't including any list conversions!")
      :feedback2: (".*","Keep in mind how much the numbers are changing by!")
      
      Come up with a range function that will produce the following numbers: ``[1,4,7,10,13,16,19,22]``