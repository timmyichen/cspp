.. qnum::
   :start: 1
   :prefix: ch0201-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".

Lesson 02-01: Printing with String Formatting
=============================================

**Learning Target: I can use string formatting to print strings with variables.**

The Old Way
-----------

In order to print variables in a sentence, we know to use the ``+`` operator to combine strings.

.. code-block:: none
    :emphasize-lines: 2

    >>> name = "Mark"
    >>> print("His name is " + name)
    His name is Mark

However, this gets complicated when a lot of variables get involved, especially numbers - like so:

.. code-block:: none
    :emphasize-lines: 5

    >>> name = "Mark"
    >>> lastname = "Twain"
    >>> job = "Author"
    >>> age = 74
    >>> print("His name is " + name + " " + lastname + " and he was an " + job + " and he died at age " + str(age))
    His name is Mark Twain and he was an Author and he died at age 74

The New Way
-----------

We can simplify this greatly by using **string formatting**.  String formatting uses a special ``.format()`` function on a string that will allow us to implement placeholders.  I think it's best shown through example:

.. activecode:: ex_strformat_1
    :autorun:
    
    name = "Mark"
    print("His name is {}".format(name))
    
This time, we use the curly brace characters ``{}`` as a placeholder in our string.  After the string, we immediately put ``.format()`` and then the name of the variable that will go into the ``{}`` placeholder.  When you have multiple variables to insert, you put a ``{}`` for each one and then in the ``.format()`` function, list the variables in order.  Here's how it looks with the more complicated example:

.. activecode:: ex_strformat_2
    :autorun:

    name = "Mark"
    lastname = "Twain"
    job = "Author"
    age = 74
    print("His name is {} {} and he was an {} and he died at age {}".format(name,lastname,job,age))

.. image:: img/strformat.svg
    :scale: 100%
    :alt: This image shows which variable correlates with which placeholder
    :align: center

While it isn't much shorter in terms of length, it is much easier to read!  Not only that, but notice that we didn't have to convert the variable ``age``, which holds an integer, into a string to print it!

:misc-hl:`In general, you should always use string formatting when printing strings with variables.`  Other methods are messier and this is just best practice.  For the rest of this course you will be expected to use string formatting in print statements.

Note that there are other ways to use string formatting, but we will not be covering them at this time.

Checks for Understanding
------------------------

.. mchoice:: cfu_strformat_1
    :correct: a
    :answer_a: It's easier to read and write
    :answer_b: It takes up less power
    :answer_c: It's much much shorter
    :feedback_a: You can compare it against the older, harder-to-read way!
    :feedback_b: Nothing was mentioned here about power and efficiency.
    :feedback_c: While it is shorter, it's not that much shorter.  Try again!
    
    What is the main advantage to using string formatting when printing strings?

In the following area, complete the code so that it runs according to the instructions ``#``.

.. activecode:: cfu_strformat_2
    
    firstname = "" #put your first name in the quotes
    lastname = "" #put your last name in the quotes
    
    # complete the print statement so it says:
    #   My name is <firstname> <lastname>
    print() 

In the following area, complete the code so that it runs according to the instructions ``#``.

.. activecode:: cfu_strformat_3
    
    firstname = "James"
    lastname = "Bond"
    
    # complete the print statement so it uses the above variables to say:
    #   The name is Bond. James Bond.
    print() 