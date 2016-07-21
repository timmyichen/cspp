.. qnum::
   :start: 1
   :prefix: ch0103-

Lesson 01-03: Operators on Strings
==================================

**Learning Target: I can predict the result of operations on strings.**

Not all operators work with strings.  In Python, you can only use strings with the ``+`` addition and ``*``  multiplication operators.

Addition with Strings
---------------------

Run the code below.  Notice the differences in the two print statements that are run.

.. activecode:: ac_addstring_1
	:nocodelens:

	print(1 + 3)
	print("1" + "3")
	print("")
	print(1200 + 23)
	print("1200" + "23")

.. mchoice:: cfu_addstring_1
	:correct: b
	:answer_a: It will add them as numbers
	:answer_b: It will connect them together
	:feedback_a: Try running the code again! Each line of output should correspond with the lines of input.
	:feedback_b: Good job!

	How do you think addition works with Strings?

Great!  So notice that there is a clear difference between the two values: ``100`` and ``"100"``.  That's because the first is an integer, and the second is a string!  The string, when used with addition, will just join them together to be one string.

.. mchoice:: cfu_addstring_2
	:correct: b
	:answer_a: "John Smith"
	:answer_b: "JohnSmith"
	:answer_c: "John" "Smith"
	:answer_d: An error will occur
	:feedback_a: Careful - where do you see a space?
	:feedback_b: Nice job!  There's no space in either of the strings, so there's no space in the result either!
	:feedback_c: That is actually two different values. When we combine values we should only have one remaining!
	:feedback_d: No error occurs! :) If you don't believe that, you can always run the code in the activecode box above!

	What will be the result of the following code? print "John" + "Smith"

Using :vocab-def:`addition with strings, or joining them together`, is called :vocab-word:`string concatenation`.

One important thing to note when using string concatenation is that they are combined character for character.  That means that if you are combining a first and last name, one of your strings has to have a space, or the result will not have any spaces!

See the following examples:
	-  ``"hi" + "there" ==> "hithere"``
	-  ``"hi " + "there" ==> "hi there"``
	-  ``"hi" + " there" ==> "hi there"``
	-  ``"hi " + " there" ==> "hi  there"`` (note there are two spaces now)

Multiplication with Strings
---------------------------

Run the code below.

.. activecode:: ac_multstring_1

	print(1 * 3)
	print("1" * 3)
	print("hi" * 5)
	print("ha " * 3)
	print("hue " * 3 * 2)

What can be concluded from your observations from above?  Use your observations to predict the next bit of code.

.. fillintheblank:: cfu_multstring_1

	.. blank:: blank1
		:correct: heyheyheythere
		:feedback1: (".*", "Keep in mind the order of operations!")

		What will be the result of the following code? ``print "hey" * 3 + "there"``

Multiplication with strings will just repeat that string. Order of operation still applies - multiplication before addition!

Practice: Check Your Understanding
----------------------------------

TODO