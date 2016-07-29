.. qnum::
   :start: 1
   :prefix: u0309-


Lesson 03-09: Danger: Infinite Loops!
=====================================

**Learning Target: I can ensure that my while loop does not run forever.**

Recognizing an Infinite Loop
----------------------------

Given the following code:

::
   
   x = 5
   
   while x < 10:
       print("x is less than 10!")
   
   print("end")

What is wrong with this code?  ``x`` is initialized at 5, and ``x < 10`` is the condition in which to run the loop.  5 is indeed less then 10, and so we enter the loop - but inside the loop, the value of ``x`` never changes.  We don't have any reassignment statement to change the value of ``x``, so the boolean ``x < 10`` will always be ``5 < 10`` which will always be True.

To fix this, we need to make sure that ``x`` changes in a way that gives it a chance to make the ``while`` condition False.

And that is the general strategy behind preventing infinite loops - :misc-hl:`inside your loop, variables should change (or at least be given a chance to change) so that the loop condition might become False.`  If you don't do this, then as soon as your ``while`` condition becomes True, it will always be True, creating an infinite loop.

What Happens If You Run an Infinite Loop?
-----------------------------------------

If you run an activecode module on this site that has an infinite loop, it will crash the page.  You'll have to close the tab/page and re-open it.

If you run an infinite loop in a python IDE or through the terminal, you can use CTRL+C to stop it.  If it slows down your entire computer to the point where you can't act, you may have to make more drastic measures (varies from case to case).

In general, it's a good idea to avoid infinite loops. :)

Sample Problem - Solving with For Loops
---------------------------------------

Write a program that repeatedly asks the user for a number and keeps track of the sum of all the numbers that the user has entered.  The loop should only run as long as the sum is less than 100.

We would start by initializing our sum variable, since that should be set to 0 outside the loop:

.. code-block:: python3
   :linenos:
   :emphasize-lines: 1
   
   sum = 0
   
Now our condition for running the loop is "as long as the sum is less than 100" - or in other words, when ``sum < 100``.  We can write in our for loop.

.. code-block:: python3
   :linenos:
   :emphasize-lines: 2
   
   sum = 0
   while sum < 100:
       
Next, what is the action that we want to repeat?  Well, we want to get a number from the user - and we want to add it to the sum.  When we ask them for a number, let's also print out the sum, just so the user knows where he/she stands.

.. code-block:: python3
   :linenos:
   :emphasize-lines: 3,4
   
   sum = 0
   while sum < 100:
       num = float(input("Your total is {}. Enter a number: ".format(sum)))
       sum = sum + num

Finally, at the end, let's print out our final total.

.. code-block:: python3
   :linenos:
   :emphasize-lines: 5
   
   sum = 0
   while sum < 100:
       num = float(input("Your total is {}. Enter a number: ".format(sum)))
       sum = sum + num
   print("Loop ended, your total is {}".format(sum))

We know that we are safe from an infinite loop because ``sum`` is changing within the loop, changing by the value of ``num``, which the user has full control over.  Feel free to try it out by copy-pasting the code into your own IDE!

Checks For Understanding
------------------------

*Please note - feel free to write these in your own separate IDE if you're not comfortable with writing it using the ActiveCode module!  You can always paste it back in afterwards.*

Q#1
~~~

Given the following block of code:

::
   
   counter = 0
   while (counter > 10):
       print("The counter is at {}".format(counter))
       counter = counter + 1
   print("end")

.. mchoice:: 0309_cfu_1
   :correct: b
   :answer_a: It has an infinite loop
   :answer_b: The while loop is false to start with
   :answer_c: The loop won't run due to a syntax error
   :feedback_a: Double-check to see if counter changes inside the loop!
   :feedback_b: Nice job!  0 is not > 10!
   :feedback_c: Can you identify any syntax errors?
   
   What's wrong with the while loop written above?

Q#2
~~~

Write the output produced by the following while loop:

::
   
   start = 12
   while start >= 3:
       print(start,end="")
       # the ,end="" part means that there is no new line after
       # each print statement, so your answer should be all in a
       # row, no spaces
       start = start / 2 

I would recommend using pencil and paper to work through the output.

.. fillintheblank:: 0309_cfu_2
   
   .. blank:: 0309_cfu_2_1
      :correct: ^12631\.5$
      :feedback1: (" +","Remember - no spaces!")
      :feedback2: ("^1263$","Double check the condition in the while loop!")
      :feedback3: (".*","Try again!")
   
      What is the output produced by the code above?

Q#3
~~~

Write a program that asks the user to enter a positive number.  The program will then repeatedly subtract 0.9 until as long as the number is positive.  For example, if the user enters 4 as their number, it will print:

.. code-block:: none
   
   4
   3.1
   2.2
   1.3
   0.4

At the end, it calculates ``0.4 - 0.9`` and stops because it results in a negative number.  As a reminder, only numbers greater than 0 are considered positive: 0 is not considered positive.  Don't forget to convert the input to a number!

Feel free to write your solution below:

.. activecode:: 0309_cfu_3
   :nocodelens:
   
   #write your code here!