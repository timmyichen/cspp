.. qnum::
   :start: 1
   :prefix: ch0207-

Lesson 02-07: If Statements
===========================

**Learning Target: I can use if statements to execute code conditionally**

If Statement Syntax
-------------------

We encounter "if statements" in real life all the time.  When you log into a website, it checks to see **if** your username and password are correct.  When you check your email, it checks to see **if** there are any new messages to display.  The icon on your weather app will be a sun **if** the weather is nice, or some clouds **if** it's rainy.  Learning to implement it in code is essential to making cool programs!

In this lesson, you will be learning your first :vocab-word:`control-structure` - or :vocab-def:`code that controls when, how, and whether code is run.`  The first control structure is called the ``if`` statement, which executes code :vocab-word:`conditionally`, which means :vocab-def:`based on certain conditions/situations`.

The syntax of an if statement can be broken down into five parts:

.. image:: img/ifsyntax.svg
   :scale: 60%
   :alt: the keyword, condition, colon, whitespace, and code to be executed
   :align: center

1. The ``if`` **keyword** - this is a special word in python that indicates the beginning of an ``if`` statement.
2. The **condition** - a boolean expression goes here.
3. The **colon** - this is required at the end of every ``if`` statement line.
4. The **whitespace** - this is a tab, which is typically four spaces.  This is required on the line after the ``if`` statement, because it tells us (and the computer) which code is the code to be executed conditionally.
5. The **code to be executed** - this is the code that will run if the condition (#2) is ``True``.  If the condition is ``False``, all this code gets skipped.

Here's an example of an if statement being used.  Run the code below, then try changing the value of ``num`` and run it again.  Observe the output.

.. activecode:: ex_ifsyntax_1
   :nocodelens:

   num = 10
   if num > 0:
       print("{} is positive!".format(num))
   
.. mchoice:: cfu_ifsyntax_1
   :multiple_answers:
   :correct: b,c
   :answer_a: 3
   :answer_b: -3
   :answer_c: 0
   :answer_d: 0.009
   
   Which of the following values of "num" will print NO output? Feel free to experiment before answering.

Whitespace
----------

Readability of Whitespace
~~~~~~~~~~~~~~~~~~~~~~~~~

The whitespace that is required when dealing with ``if`` statements, or control structures as a whole, is very important in programming.

In Python and other languages where it is required, it is important because having improper whitespace will result in an ``error``.

In other languages where whitespace is not required, like Javascript or C/C++, it is still important, because it makes the code easier to read.

What if we had many if statements?  Which of the following is easier to read, this (no whitespace):

::
   
   if name == "Jess":
   print("Hey best friend!")
   if name == "Billy":
   print("Hey guy from class")
   if name == "Ron":
   print("Who are you")

or, this? (with whitespace):

::
   
   if name == "Jess":
       print("Hey best friend!")
       
   if name == "Billy":
       print("Hey guy from class")
       
   if name == "Ron":
       print("Who are you")

It should be pretty clear that the second one is easier to read.  It allows us to immediately see which lines are in each if statement and which lines are not.  In the next section, things get real crazy with nested if statements.

To recap, :misc-hl:`whitespace is important because it is required in Python, but it also helps organize our code and make it easier to read and follow.`

Word of Caution on Whitespace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Although a tab is typically four spaces in text editors, Python will interpret it differently.  As we learned in the escape characters lesson, a space and a tab are two different characters.  Specifically in Python, a tab is equivalent to 8 spaces.  This means that :misc-hl:`if you mix tabs and spaces, you may end up with errors and/or unexpected results`.

Note that this is very dependent on the editor.  For example, if you are using Sublime Text, it will keep everything you typed exactly as it is, and therefore cause errors if you mix tabs and spaces.  However, in editors such as the c9 editor, IDLE, or PyCharm CE, it will automatically covert the tabs to spaces, preventing any consistency errors.  This is not to say that any one editor is better than another; simply that you should be aware of how each handles spacing.

Nested If Statements
--------------------

If statements can go inside other if statements!

.. image:: img/nestedif.svg
   :alt: three if statements inside of one large if statement
   :align: center
   :width: 400px

In the example above, each if statement is colored with the code that it controls.  Note how the blue, red, and pink if statements are all inside the green if statement.  This simply means that the green condition has to be true in order for the blue/red/pink conditions to even be looked at.  

If the green condition is false, it will skip to the end of the code and be done.
The blue/red/pink ``if`` statements have no affect on each other.  They are checked individually and in order.

Checks for Understanding
------------------------

.. parsonsprob:: cfu_if_1
   
   Rearrange the blocks of code to create an error-free if statement.
   -----
   name = "Bob"
   if len(name) > 5:
       print("What a long name!")

::

   if 5 < x < 10 and x != 9:
      print(x)
   

.. mchoice:: cfu_if_2
   :multiple_answers:
   :correct: b,c
   :answer_a: 5
   :answer_b: 6
   :answer_c: 7
   :answer_d: 9
   :answer_e: 10
   
   In the if statement above, for which values of x will x be printed? Check all that apply.

.. mchoice:: cfu_if_3
   :correct: b
   :answer_a: x is less than 5 and greater than 10 and not equal to 9
   :answer_b: x is greater than 5 and less than 10 and not equal to 9
   :answer_c: x is greater than 5 and less than or equal to 10 and not equal to 9
   
   In the if statement above, which of the following accurately describes the boolean expression?

Write an ``if`` statement on line 2 to check if the variable ``pwrd`` is equal to ``pass1234``.  Do not change lines 1 or 3.  If done correctly, the output should say ``Access Granted``.  If not done correctly, it will say ``Access Denied``.

.. activecode:: cfu_if_4
   
   pwrd = "pass1234"
   
       print("Access Granted")
   ====
   else:
       print("Access Denied")