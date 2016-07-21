.. qnum::
   :start: 1
   :prefix: ch0102-


Lesson 01-02: Python Operators
==============================

**Learning Target: I can describe the ways in which Python can represent data.**

Basic Operators
---------------

Let's first review the four common math operators:
	+-----------------+--------+----------------------+
	| Operator        | Symbol | Example              |
	+=================+========+======================+
	| Addition        | ``+``  | ``3+7`` (result: 10) |
	+-----------------+--------+----------------------+
	| Subtraction     | ``-``  | ``5-8`` (result: -3) |
	+-----------------+--------+----------------------+
	| Multiplication  | ``*``  | ``3*5`` (result: 15) |
	+-----------------+--------+----------------------+
	| Division        | ``/``  | ``6/2`` (result: 3)  |
	+-----------------+--------+----------------------+

New Operators
-------------

In Python, there are two other operators we need to know.

	+-----------------+--------+------------------------+
	| Operator        | Symbol | Example                |
	+=================+========+========================+
	| Power           | ``**`` | ``3**2`` (result: 9)   |
	+-----------------+--------+------------------------+
	| Modulo (mod)    | ``%``  | ``10%3`` (result: 1)   |
	+-----------------+--------+------------------------+

:vocab-word:`Power` is simply :vocab-def:`an exponent`.  ``3**2`` can be described as ``3 raised to the 2nd power``, or 3^2

*Note: You can do square roots by using a power of one-half.  For example, the square root of 16 is the same as 16 raised to the 1/2th power, or ``16**(1/2)``*

:vocab-word:`Modulo` represents :vocab-def:`remainder after division`. ``10%3`` can be described as ``the extra parts when 10 divided by 3``, or ``how much of 10 is not divisible by 3``.  In this case, 10 divided by 3 is 3 remainder 1 (or 3 fits into 10, 3 times, with 1 left over), so ``10 mod 3 = 1``.

Three more examples:
	- 20 % 6

	  6 fits into 20 three (3) times.  ``3 * 6 = 18``, which means that there is ``20 (total) - 18 (result) = 2 (remainder)`` left over.  The remainder of this expression is 2, so ``20 % 6 = 2``.

	  Another way of saying it is: 20 divided by 6 is 2.666, rounded down is 3, and 20 - (6 * 3) = 2.

	- 27 % 9

	  9 fits into 27 five (3) times.  ``9 * 3 = 27``, which means that there is ``27 (total) - 27 (result) = 0 (remainder)`` left over.  Since 9 divides 27 evenly, there is no remainder, so ``27 % 9 = 0``.

	  Another way of saying it is: 27 divided by 9 is exactly 3, so there is no remainder, so it is 0.

	- 4 % 7

	  7 fits into 4 zero (0) times.  ``7 * 0 = 0``, which we can follow with ``4 (total) - 0 (result) = 4 (remainder)``.  Since 7 doesn't fit into 4 at all, the remainder is just ``0``.

	  Another way of saying it is: 4 divided by 7 is .571, rounded down is 0, and 4 - (7 * 0) = 4.

	  We can develop a general rule for this case, which is this: **Given the expression** ``a % b`` **, where** ``a`` **and** ``b`` **are positive integers, if** ``a < b`` **, the result is always** ``a``.

Order of Operations
-------------------

:vocab-word:`Order of operations` determines which operator is done first.  PEMDAS is followed by most programming languages, where the order of operations are:

	- :vocab-def:`P - Parentheses first, then`
	- :vocab-def:`E - Exponents, then`
	- :vocab-def:`M/D - Multiplication/Division/Modulo, then`
	- :vocab-def:`A/S - Addition/Subtraction last`

Note that Modulo is on the same level as multiplication and division.

Practice: Check Your Understanding
----------------------------------

.. fillintheblank:: question_01_05_01

	.. blank:: blank1
		:correct: \\b12\\b
		:feedback1: (".*", "Don't forget your PEMDAS!")

		Evaluate the following expression: ``3 ** 2 + 3``

.. fillintheblank:: question_01_05_02

	.. blank:: blank2
		:correct: \\b9\\b
		:feedback1: (".*", "Make sure you do the parentheses first!")

		Evaluate the following expression: ``3 ** (2 % 3)``

.. parsonsprob:: question_01_05_03
	
	Order the groups of operations in the order that they should be evaluated.  Top is evaluated first, while bottom is evaluated last.
	-----
	parentheses
	exponents
	mult/div/mod
	add/sub
