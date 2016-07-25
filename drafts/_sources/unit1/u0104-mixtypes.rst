.. qnum::
   :start: 1
   :prefix: ch0104-

Lesson 01-04: Mixing Datatypes
==============================

**Learning Target: I can predict the behavior of two different datatypes that are operated upon.**

**Highlighting Key**: :vocab-word:`vocab term`, :vocab-def:`vocab definition`, :misc-hl:`important concept`

Now that we know that we can use operators to combine values, what happens if we combine values of different types?

Mixing Ints with Floats
-----------------------

When you mix integers and floats together, you will always get a float back.  Integer and integer gives integer, float and float gives float, but :misc-hl:`combining an integer and float will result in a float.`

To observe, run the following code:

.. activecode:: ac_mixtype_1
	:nocodelens:
	:caption: Note that everything after the # is a comment and is not run as code

	print 1 + 1	#int + int => int
	print 1.0 + 1.0	#float + float => float
	print 1 + 1.0 	#int + float => float

As an example, consider the expression ``1 + 2 / 4 + 0.5``.

You might look at this expression and think of the following steps:
	- There is a float in there, so the result should be a float.
	- ``2 / 4`` is ``0.5``, so the entire thing is ``1 + 0.5 + 0.5``, or ``2``.
	- The result is ``2``!

However, :misc-hl:`types change as they are evaluated`.  This means that the steps for the above are more like this:
	- Order of operations says that division happens first.
	- ``2 / 4`` involves two integers, so the result is ``0.5``, removing everything after the decimal, or just ``0``
	- All that's left is addition, so we can evaluate it left to right.
	- ``1 + 0 + 0.5`` will be evaluated from left to right, making the ``1 + 0`` happen first (which equals ``1``)
	- ``1 + 0.5`` is what remains, which is an int plus a float, so the result will be a float (decimal): ``1.5``
	- The result is ``1.5``

This may get tricky in specific formulas that require certain numbers to already have a decimal place.

Check For Understanding
-----------------------

.. mchoice:: cfu_mixtype_1
	:correct: c
	:answer_a: Boolean
	:answer_b: Integer
	:answer_c: Float
	:feedback_a: Remember that a boolean is True/False, which isn't in this expression.
	:feedback_b: Which is greater, Floats or Integers?
	:feedback_c: The float turns everything into an integer!

	What datatype will result from the following expression? ``4 * 2.0``

.. fillintheblank:: cfu_mixtype_2
	
	.. blank:: blank1
		:correct: 2.0
		:feedback1: ("2", "Have you considered the ending datatype?")
		:feedback2: ("16.0", "Don't forget about order of operations!")
		:feedback3: ("16", "Don't forget about order of operations!")
		:feedback4: (".*", "Try again!")

		Evaluate the following expression: ``8 / 2 ** 2.0``.  Don't forget to consider order of operations as well as the datatypes.

.. fillintheblank:: cfu_mixtype_3
	
	.. blank:: blank2
		:correct: 6.0
		:feedback1: ("6.5", "Remember, integer division!")
		:feedback2: ("6", "Have you considered the ending datatype?")
		:feedback3: ("1.25", "Don't forget about order of operations!")
		:feedback4: (".*", "Try again!")

		Evaluate the following expression: ``10 / 4 + 4.0``.  Don't forget to consider order of operations as well as the datatypes.

Mixing Strings with Anything
----------------------------

We already know that we can multiply Strings with integers.  This seems to be the exception, because in every other case, we'll get an error!  Let's look at string addition (recall: concatenation).

In the following code, replace the ``1`` with any other value that is not a String, then run the code.  You should find a common theme.

.. activecode:: ac_mixtype_2
	:nocodelens:

	print "hello" + 1
	#replace the second part with anything that is not a String

You should find that you get a ``TypeError`` every time!

The rule can basically be broken down into three parts:
	- Adding a string to another string is allowed
	- Multiplying a string by an integer is allowed
	- **Everything else is not allowed**

Any time we encounter code that generates an error, it's usually a good idea to find a way to make the code work without any errors.  So the big overarching question in our next lesson is: **How do we combine different types?**