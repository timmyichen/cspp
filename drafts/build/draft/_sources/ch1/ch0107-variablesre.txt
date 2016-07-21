.. qnum::
   :start: 1
   :prefix: ch0107-

Lesson 01-07: Variable Reassignment
===================================

**Learning Target: I can reference a variable in its own reassignment statement.**

With lots of experience in math and little experience in programming, when you see something like this:

``x = x + 1``

Red flags should instantly go off in your head.  How can ``x`` be equal to itself plus 1??  Can ``5`` be equal to ``6``?  No, of course not!

Increasing or Decreasing a Variable
-----------------------------------

What you should not forget, however, is that the ``=`` symbol in programming is different from the ``=`` symbol in mathematics.

To review, the equal sign means **variable assignment** - it has a very specific purpose.

Recall the meaning of the left and right side of a variable assignment statement:
	- Left side: the variable to store into
	- Right side: the value **or expression** to store

An important thing to note is that the right side is always evaluated **before** being saved into the variable on the left.  This gives the line of code ``x = x + 1`` a whole new meaning.  Let's break it down:

Given a statement ``x = x + 1``, let's assume the value of ``x`` is currently ``0``.  Since it is an assignment statement, the right side of the equal sign, or ``x + 1``, gets evaluated first.  Since ``x`` is a variable being used in an expression, we use its actual value instead, which is ``0``.  So the expression being evaluated is ``0 + 1``, which is just ``1``.  

This leaves us with the statement ``x = 1``, which then allows us to store ``1`` in ``x``, basically increasing the value of ``x`` by ``1``.  Up until the beginning of this paragraph, ``x`` was still ``0``!  It doesn't actually change until you complete the assignment statement.

However, this would have worked with any value of ``x``!  Let's say ``x`` was ``28``.  The expression ``x + 1`` would then be ``28 + 1``, or ``29``, which then gets saved back into ``x``.  ``x`` is  changed from ``28`` to ``29``, which is the same thing as increasing it by ``1``.

Let's run through some example code below, step by step.

.. codelens:: cl_reassign_1
	:question: What is the value of num that will get printed?
	:breakline: 4
	:feedback: Go through line by line, with num starting at 10.
	:correct: globals.num

	num = 10
	num = num + 5
	num = num * 2
	print num

::

    x = 10
    x = 10 * 5
    x = x - 5
    x = x / 9

.. fillintheblank:: fill1512

    .. blank:: cfu_reassign_2
        :correct: \\b5\\b
        :feedback1: ("\\b10\\b", "That's just the first line..")
        :feedback2: (".*", "Try again - be sure to go step by step!")
        
        What will the result of ``x`` be after the code above is run?
	    

Warning: Error Ahead!
---------------------

You'll want to be careful about how you use variable reassignment.  For example, take the following program:

.. activecode:: ac_reassign_1
	:nocodelens:
	:caption: Errors with reassignment

	x = x + 1
	print "x is now " + str(x)

Notice how you get an error.  That's because of how *regular variable assignment* works.

Remember that the right side of the equal sign is evaluated **first**.  So it's trying to evaluate ``x + 1``, but ``x`` doesn't have a value yet!  So it will give you a ``NameError``.

You would have to :vocab-def:`give variables an initial value`.  This is called :vocab-word:`initializing` a variable.  So before you can use ``x = x + 1``, you will have to give ``x`` a value, using a regular assignment statement.  Maybe with ``x = 0``.  The new code will look like this:

.. activecode:: ac_reassign_2
	:nocodelens:
	:caption: No error here!

	x = 0
	x = x + 1
	print "x is now " + str(x)

:misc-hl:`Always make sure that your variables are initialized!`

