.. qnum::
   :start: 1
   :prefix: u0414-


Lesson 04-14: Simple Input Validation
=====================================

**Learning Target: I can validate a user's input by checking its datatype and value.**

Why Validate Input?
-------------------

Up until this point, we've been writing programs with the assumption that the user will enter in the exact type of data that we want, and within the exact range that we want.

One of the basics of cybersecurity and writing code is that: nobody should be able to crash your code.  Whenever you ask a user for input, you have to assume every possible case that they can throw at you.  Breakable code is not secure code.  Not to mention, not validating inputs will result in unpredictable code.

For example, let's say we want to ask the user for a number.  When you run the following code, enter in a word or letter instead.

.. activecode:: 0414_ex_1
   :nocodelens:
   
   num = int(input("Enter a number"))
   print("You entered {}".format(num))

You'll notice that it came up with an error.  No good!  In this lesson, we'll show you a way to make your code input-proof when asking for numbers.

Validating Numbers
------------------

Normally, when we ask for input and we want to use it as a number, we would convert it using the ``float()`` or ``int()`` conversion functions.  However, if you try to convert a word or letter into a float or int, it will give you an error, as demonstrated above.  There are a few ways to combat this, and here we will show you one of those ways.

Strings have specific functions - you already know of one and use it often (hopefully), ``.format()``.  We will cover many string functions later, but today we will only show you two.  The first is called ``.isdigit()`` and represents True or False based on whether all the characters are digits or not.  See the following example:

.. activecode:: 0414_ex_2
   :autorun:
   
   print("hi".isdigit())
   print("100".isdigit())
   print(".".isdigit())
   print("123456789".isdigit())

Looks like it works pretty well.  We can then use the following to get user input:

.. activecode:: 0414_ex_3
   
   num = input("Enter a number: ")
   while not num.isdigit(): # while the number is not made of digits
       num = input("Invalid! Enter another: ")
   
   # at this point, num is made of digits, so it is safe to convert it
   num = float(num)

However, with a few examples, we can see that this doesn't work as well as we'd like:

.. activecode:: 0414_ex_4
   :autorun:
   
   print("-20".isdigit())
   print("1.6".isdigit())
   print("-3.0".isdigit())
   print("-".isdigit())
   print(".".isdigit())

As you can see, it doesn't handle decimals or negative numbers very well, probably because neither ``-`` nor ``.`` are digits.  Let's handle each case one at a time.

Negative Numbers
~~~~~~~~~~~~~~~~

With negative numbers, we know that the negative sign will always be in the front of the number.  This is good because we know how to check the first character in a string.

.. fillintheblank:: cfu_0414_1

   .. blank:: cfu_0414_1_1
      :correct: ^string\[0\]$|^string\[0:1\]$
      :feedback1: ("\[1\]", "Remember, indeces start counting at 0!")
      :feedback2: (".*", "Try again! Think of string indexing.")
   
      Given a string called ``string``, what expression would give us the first character of ``string``?

Highlight for answer: :ans-hl:`string[0]`

Great!  Now come up with an expression that checks whether the first character of string is equal to ``"-"``.  As a reminder, you use ``==`` to check for equality.

.. fillintheblank:: cfu_0414_2

   .. blank:: cfu_0414_2_1
      :correct: ^string\[0\] *== *(('-')|("-"))$|^string\[0:1\] *== *(('-')|("-"))$
      :feedback1: ("[^=]=[^=]", "Remember - two equal signs for equality!")
      :feedback2: (".*", "Try again!")
   
      What boolean expression can you use to check  whether the first character of ``string`` is equal to ``"-"``?

Highlight for answer: :ans-hl:`string[0] == "-"`

But this only checks if the first 