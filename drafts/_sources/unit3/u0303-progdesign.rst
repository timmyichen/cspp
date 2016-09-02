.. qnum::
   :start: 1
   :prefix: u0303-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".


Lesson 03-03: Program Design Tips: Part I
=========================================

**Learning Target: I can document my code with appropriate comments.**
**Learning Target: I can use good naming conventions with variables.**
**Learning Target: I can know when to use variables instead of hard-coding numbers.**

The Use of Comments
-------------------

Comments can be used in a number of ways.  The most important thing to remember is that :misc-hl:`comments are used to enhance readability of your program to other programmers, not to non-programmers`.  This means that ideally, especially with python, since it is such an easy-to-read language, people should be able to know what your program is doing simply by reading your code.  Good variables names and good code structure will help them understand.

However, it also helps to put little comments here and there to explain an algorithm, especially if it's tricky or hard to understand on its own.  If you're ever not sure whether you should be commenting something - just comment it.  It's a lot easier to read code with a lot of explanation than it is to read code with no explanation.

Variable Naming Conventions
---------------------------

Although there is an `entire guide <https://www.python.org/dev/peps/pep-0008/#naming-conventions>`_ on python naming conventions, we're going to keep it simple and give you only a few guidelines to follow in order to improve your code readability.

1. :misc-hl:`Variable names should be descriptive of what they are, but not too long in length.`
2. :misc-hl:`Variable names should be all lowercase, with words separated by underscores.`
   
      - For example, ``sum_of_prices`` is preferrable to ``sumofprices`` or ``SumOfPrices``.
   
Following these guidelines will improve your code readability, which is useful when others are reviewing your code, or when you look back on your code after a while - when you use single letters or nondescriptive names in your code, you will eventually forget what they mean.

Variables vs Hard-Coding Numbers
--------------------------------

Sometimes you will have programs that have a constant value.  For example, let's say that you're writing a program that checks your age to see if you are allowed to drive (assuming 17 is the minimum).

.. activecode:: 0303_ex_1
   :nocodelens:
   
   age = int(input("Enter your age: "))
   if age >= 17:
       print("You can drive!")
   else:
       print("Sorry!")

On line 2, when you put ``age >= 17``, we are making the assumption that 17 will never change.  In this context, we are :vocab-word:`hard-coding` the number 17 into the program.  This means that it :vocab-def:`cannot be changed at all without diving into the source code`.  Let's say that this number is used again and again throughout the program.  It's better to put the value in a variable, and use the variable instead.  Like so:

.. activecode:: 0303_ex_2
   :nocodelens:
   
   age_min = 17
   
   age = int(input("Enter your age: "))
   if age >= age_min:
       print("You can drive!")
   else:
       print("Sorry!")
      
This way, if the minimum age to drive were to ever change, we would only need to change one variable instead of all of them.  Additionally, a user could be given the opportunity to change the value of ``age_min`` - no need to change the source code.

:misc-hl:`It is generally good practice to avoid hard-coding constant values, especially if those values are repeated throughout the program.`