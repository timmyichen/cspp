.. qnum::
   :start: 1
   :prefix: ch0205-

Lesson 02-05: Boolean Expressions
=================================

**Learning Target: I can predict the outcome of boolean expressions.**

Right now the programs that we've been writing have beem very straightforward - they run instruction after instruction, in the order that it was written.  Computers act smart when they can make decisions, and in order to make decisions, we have to learn about **boolean expressions**.

Simple Boolean Operators
------------------------

A :vocab-word:`boolean expression` is simply :vocab-def:`any expression that evaluates to be True or False`.  While we learned about the PEMDAS operators before, none of those apply to boolean expressions.  There are three basic operators covered in this lesson:

   - ``and``
   - ``or``
   - ``not``

``and`` and ``or`` are both operators that require two boolean terms - like ``True and False``.  The ``not`` operator, however, is only applied to a single term.

We can evaluate the expression of boolean expressions with truth tables.

Truth Tables
------------

:vocab-word:`Truth Tables` are :vocab-def:`tables that list all possible outcomes for a given operator.`  The simplest example of a truth table is the table for the ``not`` operator.

``not``
~~~~~~~

The ``not`` operator takes a boolean expression and turns it into its opposite.  So if I have ``True`` as my statement, then using ``not`` would turn it into ``not True`` - which is ``False``.

Here's how the truth table for ``not`` looks:

   +--------------+---------------------+
   | If ``A`` is: | Then ``not A`` is:  |
   +==============+=====================+
   | ``True``     | ``False``           |
   +--------------+---------------------+
   | ``False``    | ``True``            |
   +--------------+---------------------+

The way this table is read is as follows:
   
   - if ``A`` is ``True``, then ``not A`` is ``False``
   - if ``A`` is ``False``, then ``not A`` is ``True``

``and``
~~~~~~~

With ``and``, we require two boolean terms - we'll call them ``A`` and ``B``.  This time, when we construct our truth table, we will have to list all possible combinations of ``A`` and ``B`` where either one of them can be ``True`` or ``False``.

   +---------------+---------------+-----------------------+
   | If ``A`` is:  | If ``B`` is:  | Then ``A and B`` is:  |
   +===============+===============+=======================+
   | ``True``      | ``True``      | ``True``              |
   +---------------+---------------+-----------------------+
   | ``True``      | ``False``     | ``False``             |
   +---------------+---------------+-----------------------+
   | ``False``     | ``True``      | ``False``             |
   +---------------+---------------+-----------------------+
   | ``False``     | ``False``     | ``False``             |
   +---------------+---------------+-----------------------+

I think it's important to understand the logic behind why this is.

Think of ``A`` and ``B`` being two independent statements that can be either ``True`` or ``False``.  ``A and B`` is a single statement that speaks to the truthiness or falseness of both statements together.  As an example, let's make the following statements:

   - ``A`` means that the Earth is roundish
   - ``B`` means that the sky is made of lemons

Individually, ``A`` is obviously ``True`` and ``B`` is obviously ``False``.  However, when we think about it in the context of our real-life examples, if you were to say them together as one statement: "The Earth is roundish AND the sky is made of lemons", then the statement as a whole is false.  This is why ``True and False ==> False``, and ``False and True ==> False``.

It should be pretty obvious that when you say two truthful statements together, then the entire thing is truthful.  Or if you say two false statements together, then the entire thing is false.

As a general rule for ``and`` statements: :misc-hl:`"A and B" is True as long as both of them are True`.

``or``
~~~~~~

With ``or``, we can logic our way through the truth table.  I like making statements for my ``A`` and ``B``, it makes it easier to understand.  Let's say that:

   - ``A`` means "it is raining outside"
   - ``B`` means "it is cloudy"

Individually, ``A`` and ``B`` could be ``True`` or ``False`` depending on the weather in your local area.  However, if we consider the statement ``A or B``, meaning "it is raining outside or it is cloudy", then *either one of those statements being* ``True`` *makes the whole statement* ``True``.

We can still maintain that both being ``True`` is truthful and both being ``False`` is false.  Here's how our truth table looks:

   +---------------+---------------+-----------------------+
   | If ``A`` is:  | If ``B`` is:  | Then ``A or B`` is:   |
   +===============+===============+=======================+
   | ``True``      | ``True``      | ``True``              |
   +---------------+---------------+-----------------------+
   | ``True``      | ``False``     | ``True``              |
   +---------------+---------------+-----------------------+
   | ``False``     | ``True``      | ``True``              |
   +---------------+---------------+-----------------------+
   | ``False``     | ``False``     | ``False``             |
   +---------------+---------------+-----------------------+
   
As a general rule for ``or`` statements: :misc-hl:`"A or B" is True whenever either one of them is True`.

Order of Operations & Sample Exercise
-------------------------------------

The :misc-hl:`order of operations for boolean operators` ``and``, ``or``, ``not`` are as follows:

   - Any parentheses ``()`` first
   - Then ``not``
   - Then ``and``
   - The ``or`` last

Make sure you memorize this information!  You will need it on the exercises below.

**Example:** Evaluate the following boolean expression: True and False and not False or True

   - Step 1: Evaluate all ``not`` operators:
   
      - True and False and :uline:`not False` or True
      - True and False and :uline:`True` or True
   
   - Step 2: Evaluate all ``and`` operators:
   
      - :uline:`True and False` and True or True
      - :uline:`False` and True or True
      - 
      - :uline:`False and True` or True
      - :uline:`False` or True
   
   - Step 3: Evaluate all ``or`` operators:
   
      - :uline:`False or True`
      - :uline:`True`
   
Thus our final answer is ``True``!

Checks for Understanding
------------------------

With booleans, each question really only has one answer - True or False.  Therefore, try to make sure you are *certain* of the answer before you attempt it, otherwise it will be ruined!  Try not to guess - guessing will not help you get more comfortable with booleans.  Use paper and pencil if you need it - it's good to show your steps, just like in math class. 

Q#1
~~~

.. parsonsprob:: cfu_orderops_1

   Drag the blocks in the order in which they would be evaluated.
   -----
   Parentheses
   NOT
   AND
   OR
  

Q#2
~~~

.. mchoice:: cfu_boolexp_1
   :correct: a
   :answer_a: True
   :answer_b: False
   :feedback_b: Feel free to check the charts above for reference.  Make sure you go step by step!
   
   Evaluate: True and False or True

Q#3
~~~

.. mchoice:: cfu_boolexp_2
   :correct: b
   :answer_a: True
   :answer_b: False
   :feedback_a: Feel free to check the charts above for reference.  Make sure you go step by step!
   
   Evaluate:  False or False and not True
   
Q#4
~~~

.. mchoice:: cfu_boolexp_3
   :correct: b
   :answer_a: True
   :answer_b: False
   :feedback_a: Feel free to check the charts above for reference.  Make sure you go step by step!
   
   Evaluate:  not (True or True and False and True)
   
Q#5
~~~

.. mchoice:: cfu_boolexp_4
   :correct: a
   :answer_a: True
   :answer_b: False
   :feedback_b: Feel free to check the charts above for reference.  Make sure you go step by step!
   
   Evaluate:  True and False and (True and False) or not False or False
   
Q#6
~~~

.. mchoice:: cfu_boolexp_5
   :correct: b
   :answer_a: True
   :answer_b: False
   :feedback_a: Feel free to check the charts above for reference.  Make sure you go step by step!
   
   Evaluate:  (False or True) and ((True and False) or not (True or False))