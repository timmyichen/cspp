.. qnum::
   :start: 1
   :prefix: ch0106-

Lesson 01-06: Introduction to Variables
=======================================

**Learning Target: I can use variables to store Python data.**

Now we know ow to express data in python.  But what if we need to save it for later?  What if we to ask the user for a lot of information, then do something with that information all at once?  We need some method of keeping data readily available.

Luckily, we can save data using :vocab-word:`variables`.

Think of variables as a storage box with labels.  Variables have the following characteristics:
	- They can only hold one value at a time (although the value could be a list of values, which we will learn later)
	- They have a name which you can use to reference its held value (like the label on the box)
	- The name given to a variable cannot be changed
	- They can hold values of any type (not true for all programming languages)

There's two actions that we're going to learn:
	- Saving something into a variable
	- Getting something from a variable

Variable Creation
-----------------

Let's start with how to name variables.  There are a few rules we have to follow when naming variables:
	- Variable names can only consist of uppercase letters, lowercase letters, digits, and underscores ( the character _ ).
	- Variable names cannot start with digits
	- Variable names cannot be any special keyword (such as ``print``)

.. mchoice:: cfu_var_1
	:multiple_answers:
	:correct: a,b,e
	:answer_a: NAME
	:answer_b: n4m3
	:answer_c: |\|4M3
	:answer_d: 1_name
	:answer_e: ______name_
	:feedback_a: Great job!
	:feedback_b: Great job!
	:feedback_c: Check the rules of what the name can contain!
	:feedback_d: What can variables not start with?
	:feedback_e: Great job!

	Select all valid variable names.

Variable Assignment
-------------------

To store a value into a variable, you must use what's called a :vocab-word:`variable assignment statement`.

Such a statement has three parts:
	- :vocab-def:`Left side: the name of the variable to store into`
	- :vocab-def:`Equal sign in the middle`
	- :vocab-def:`Right side: the value or expression to store into the variable name on the left`

As an example, ``name = "Bob"`` would store the string ``"Bob"`` into a variable called ``name``.
The code ``name = "Leeroy" + "Jenkins"`` would store the string ``"LeeroyJenkins"`` into a variable called ``name``.  :misc-hl:`Note that the entire expression to the right of the equal sign is evaluated before getting saved into the variable.`

Run the code below to observe the behavior of multiple assignment statements lining up.

.. activecode:: ac_var_1
	:nocodelens:

	num = 10
	print("\n") #this is to make the output line up, ignore this line
	print(num)
	num = 15
	print("\n") #same as before, ignore this line!
	print(num)

The four steps this code is executing are:
	- Set ``num`` to 10
	- Print the value of ``num`` (which is 10)
	- Set ``num`` to 15
	- Print the value of ``num`` (which is now 15)

Try the problem below to solidify your understanding.

.. parsonsprob:: cfu_var_1

	Order the code in the correct order that will correct set the variable saying to "hello", then set saying to "goodbye", then print saying.
	-----
	saying = "hello"
	saying = "goodbye"
	print saying

Retrieving From a Variable
--------------------------

To get a value from a variable, you just have to reference the variable name, either alone or as part of an expression.  We have been doing this quite frequently by using ``print`` statements.  Let's explore some examples in which we reference variables.

The following code will create three variables, ``x``, ``y``, and ``z``, setting ``x`` to the value of ``1``, setting ``y`` to the value of ``2.0``, and setting ``z`` to the sum of ``x`` and ``y``.

.. activecode:: ac_var_2
	:nocodelens:
	:caption: Try changing the values of x and y, run the code, and observe how it changes!

	x = 1
	y = 2.0
	z = x + y
	print z
	
	a = 10
	print a + 3.5

If you tried changing the values of ``x`` and ``y`` and running the code again, you will have noticed that the output (``z``) changed.  That's because when it gets to ``line 3`` and we are executing a variable assignment statement for ``z``, we first have to evaluate the right side, which is ``x + y``.  Since ``x`` and ``y`` are variables, we pull the values from within the variables to use in their place.  So if ``x`` was ``1`` and ``y`` was ``2.0``, ``x + y`` would be the same as ``1 + 2.0``.

The important takeaway here is that :misc-hl:`variable names, when used in an expression, always represents the value stored inside`.