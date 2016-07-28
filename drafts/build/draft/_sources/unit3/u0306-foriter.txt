.. qnum::
   :start: 1
   :prefix: u0306-


Lesson 03-06: Iterating Over a Range
====================================

**Learning Target: I can use for loops to iterate over a range of numbers.**

Now that we've covered the ``range()`` function, what about the rest of the for loop?

An example of a for loop is: ``for x in range(5):`` - what does the ``x`` mean?

``for`` Loop Syntax, Extended
-----------------------------

The ``for`` loop syntax can be written as follows: ``for item in iterable:``.

   - ``iterable`` is something that is capable of returning its members one at a time, such as a range.
   - ``item`` is each member returned from the ``iterable``.

Take the example:

.. activecode:: 0306_ex_1
   :autorun:
   
   for x in range(3):
       print(x)

We know that ``range(3)`` represents a list of numbers ``[0,1,2]``.  When this ``for`` loop loops 3 times, each time, ``x`` will take on the next value from ``range(3)``, starting at the beginning.

This is why the 0 gets printed out, then the 1, then the 2.  First ``x`` takes a value of 0, then ``x`` takes a value of 1, then ``x`` takes a value of 2.

Additional Notes:
-----------------

The variable can be named whatever you want too.  Just make sure it doesn't conflict with any other variable, or it will overwrite it.

.. activecode:: 0306_ex_2
   :autorun:
   
   for number in range(5):
       print(number)

The variable can be used just like any other variable as well.

.. activecode:: 0306_ex_3
   :autorun:
   
   for number in range(5):
       print("the number is {}".format(number))
       number = number * 10
       print("ten times the number is {}".format(number))
       
Remember, this works for any range as well!

.. activecode:: 0306_ex_4
   :autorun:
   
   for num in range(5,0,-1):
       print("T-{}...".format(num))
   print("Blastoff!")

Checks For Understanding
------------------------

Q#1
~~~

Write a program that will print out the first 10 multiples of 3.  In the end you will know if you got it right if you printed out the following numbers, one per line: ``3,6,9,12,15,18,21,24,27,30``.

.. activecode:: 0306_cfu_1
   :nocodelens:
   
   #write your code here!

Q#2
~~~

Write a program that will print out a countdown from 5 to 0, then prints back the same numbers up to 5, counting up.  Here is what the output should look like:

.. code-block:: none
   
   5
   4
   3
   2
   1
   0
   1
   2
   3
   4
   5

You may use more than one for loop.

.. activecode:: 0306_cfu_2
   :nocodelens:
   
   #write your code here!

Q#3
~~~

Write a program that will print out the numbers from 1 to 10 inclusive, but if the number is divisible by 4, it will print ("<num> is divisible by 4").  Here is what the output should look like:

.. code-block:: none
   
   1
   2
   3
   4 is divisible by 4
   5
   6
   7
   8 is divisible by 4
   9
   10

.. activecode:: 0306_cfu_3
   :nocodelens:
   
   #write your code here!