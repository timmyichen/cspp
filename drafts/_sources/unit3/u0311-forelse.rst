.. qnum::
   :start: 1
   :prefix: u0311-


Lesson 03-11: ``for``-``else`` Loops
====================================

**Learning Target: I can use for-else loops to test whether a for loop has completed or not.**

Now that we've learned the ``break`` keyword, we're going to add something to our friend, the ``for`` loop - an ``else`` statement.

``for``-``else``
----------------

It may seem weird, but it has a purpose.  Adding an ``else`` to a ``for`` loop is not as intuitive as the typical ``if``-``else`` usage.

The ``else`` keyword when used with a ``for`` loop can be described as: "Do this if the loop was allowed to run its full course."  As an example:

.. activecode:: 0311_ex_1
   :autorun:
   
   for x in range(5):
       print(x)
       if x == 2:
           print("Reached 2, breaking")
           break
   else:
       print("This won't get printed")
       print("Since we broke out of the loop")
       
Here's another example, where we don't break out of the loop:


.. activecode:: 0311_ex_2
   :autorun:
   
   for x in range(5):
       print(x)
   else:
       print("This will get printed!")
       print("Since the for loop was able to complete.")

When to use it?
---------------

You might be thinking: "Well, that's some really specific usage.  When would I ever need this?"

Here's an example where we test if a number is prime or not:

(The ``//`` is integer division, which means it divides, but always rounds down)

.. activecode:: 0311_ex_3
   :autorun:
   
   num = 20
   for x in range(2,num//2):
       if num % x == 0: #if x divides num evenly
           print("{} is not prime".format(num))
           break
   else:
       print("{} is prime".format(num))

Here's that same code, except with ``num`` as a prime number.  I highly recommend going through the codelens to see how the program determines execution.

.. activecode:: 0311_ex_4
   :autorun:
   
   num = 19
   for x in range(2,num//2):
       if num % x == 0: #if x divides num evenly
           print("{} is not prime".format(num))
           break
   else:
       print("{} is prime".format(num))
       
Our algorithm for this program can be written as the following:

1. Start looping x starting at 2 and ending at the number divided by 2, rounded down
2. If x divides the number evenly, it means that it's not prime, so:
   
   a. print that it's not prime, and then break out of the loop

3. If we completed the loop (means we tested all values of x and none divided the number), then we can safely say that the number is prime.

Don't worry if you can't think of many places where you would use it.  As a programmer, it is important to know which tools are available for you to use, even if you don't end up using them!  Eventually (and perhaps in an upcoming lab), you will find the ``for``-``else`` loop to be useful.