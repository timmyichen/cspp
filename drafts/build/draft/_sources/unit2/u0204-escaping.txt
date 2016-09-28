.. qnum::
   :start: 1
   :prefix: ch0204-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".

Lesson 02-04: Escape Sequences
==============================

**Learning Target: I can use escape sequences to represent special characters in strings.**

You may have noticed that I sometimes include ``"\n"`` inside my print statements.  The backslash ``\`` is used to display special characters.  This method is called an :vocab-word:`escape sequence`.

Common Escape Sequences
-----------------------

Though there are many escape sequences, there are only a few that you will realistically be using in this book (you probably won't use the last one):

    +-----------------+-----------------------------------+
    | Escape Sequence | Result                            |
    +=================+===================================+
    | ``\n``          | New line                          |
    +-----------------+-----------------------------------+
    | ``\t``          | Tab                               |
    +-----------------+-----------------------------------+
    | ``\\``          | Single backslash \                |
    +-----------------+-----------------------------------+
    | ``\'``          | Single quote `                    |
    +-----------------+-----------------------------------+
    | ``\"``          | Double quote "                    |
    +-----------------+-----------------------------------+
    | ``\uXXXX``      | Special 32-bit unicode characters |
    +-----------------+-----------------------------------+
    
``\n`` and ``\t`` are especially useful for formatting text.  ``\\``, ``\'``, and ``\"`` are useful for printing out those symbols when you need them.  For example, you might need single quotation marks to correctly print words like "can't".  You might need double quotation marks if you're quoting a person and you need to print the quotes.

The last one is kind of a special case, but good to know in case you want to print out special unicode characters.  I'm sure you've seen this on the internet before:

.. code-block:: none

    ‾\_(ツ)_/‾

That can be printed using the following print statement:

.. code-block:: python

    print("\u203E\\_(\u30C4)_/\u203E")

*Note that it will not work through this site; you'll have to run it on your computer or through some other (actual) python interpreter.*

Checks For Understanding
------------------------

Q#1
~~~

.. fillintheblank:: 0204_cfu_1

   .. blank:: blank01
      :correct: ^"\\"$
      :feedback1: (".*", "Take it character by character.. remember what the backslash means!")
      
      What will the output of the following: ``print("\"\\\"")``?  You may treat tabs as four individual spaces.

Q#2
~~~

.. code-block:: none
    
    '"'"
    hello
    '"'"

Replicate the text above using a **single** ``print()`` statement.

.. activecode:: 0204_cfu_2

    #write solution here - remember, one print statement!

Q#3
~~~

.. code-block:: none
    
    Me: "Becky said 'I can't even!'"
    You: "I can't odd!"

Replicate the text above using a **single** ``print()`` statement.  This might be a rather long print statement, and it might look messy.

.. activecode:: 0204_cfu_3

    #write solution here - remember, one print statement!