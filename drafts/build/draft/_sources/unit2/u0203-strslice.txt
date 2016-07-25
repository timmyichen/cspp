.. qnum::
   :start: 1
   :prefix: ch0203-

Lesson 02-03: Substrings with String Slicing
============================================

**Learning Target: I can string slicing notation to reference substrings.**

Substrings
----------

We can use string indexing to get a single character from a string.  Sometimes, though, we will want to get multiple letters, maybe a part of a string.  :vocab-def:`Any "string within a string"` is called a :vocab-word:`substring`.

For example, the ``"pizza"`` contains the substrings:

::

   "piz"
   "iz"
   "izza"
   "zz"

and so on (there's more)!

String Slicing Notation
-----------------------

To get a substring from a string, we still use **string indexing**, but this time, instead of giving a single number in the ``[]`` brackets, we give a range - two numbers, separated by a colon.  The syntax for string slicing is as follows:

::
   
   some_string[a:b]

Where:

   - ``some_string`` is the original string
   - ``a`` is the index of where to begin slicing (includes this index)
   - ``b`` is the index of where to end slicing (**excludes** this index)

Let's look at some examples:

.. activecode:: ex_strslice_1
   :nocodelens:
   :autorun:
   
   phrase = "pants are cool"
   # index:  0123456789 123
   print("\n\n") #ignore this line
   print(phrase[0:4])
   print(phrase[6:8])
   print(phrase[10:13])
   print()
   print(phrase[3:7])
   print(phrase[2:3])

The important thing to remember when slicing strings is that :misc-hl:`The range goes up to but does not include the second number`.

.. fillintheblank:: cfu_strslice_1

   .. blank:: blank01
      :correct: \\b[2:7]\\b
      :feedback1: ("\\b[2:6]\\b", "Remember, the last index is not included!")
      :feedback2: (".*", "It helps to count through the indexes!")
      
      What string slice would we have to use on "hippopotamus" to get the substring "ppopo"?  Give you answer in the form [a:b], where a and b are numbers.
      
Special Python Syntax
---------------------

Similar to how python has negative indexes, it also has some tricks for quick slicing.  You don't *need* to know this, but it might be helpful.
   
   +----------------+-----------------------------------------+
   | Special Syntax | Meaning                                 |
   +================+=========================================+
   | ``[:x]``       | The first x letters                     |
   +----------------+-----------------------------------------+
   | ``[:-x]``      | Everything except the last x letters    |
   +----------------+-----------------------------------------+
   | ``[x:]``       | Everything except the first x letters   |
   +----------------+-----------------------------------------+
   | ``[-x:]``      | The last 3 letters                      |
   +----------------+-----------------------------------------+

Check For Understanding
-----------------------

TODO