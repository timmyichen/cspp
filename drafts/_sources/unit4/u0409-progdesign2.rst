.. qnum::
   :start: 1
   :prefix: u0409-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".


Lesson 04-09: Program Design Tips: Part II
==========================================

**Learning Target: I can design programs with maximum readability and maintainability.**

Naming Functions
----------------

Just like variables, it's very important that you give your functions names that make sense and are easy to understand.

When it comes to functions, it's important to remember that functions **do** things.  Therefore, :misc-hl:`the name of a function should be a verb that reflects what it does`.  Drawing on previous examples you've seen in this book, a function that tests to see if a number is prime or not is simply called ``is_prime``, returning True or False.  A function used to get a user's name might be called ``get_name``.

One of the most important things about how you write your code is how **readable** it is - the more readable, the better, and proper function names help with that.  

Try to avoid using acronyms for long functions names; instead, just figure out a way to make it shorter.  For example, if you have a function that might be ``check_if_sprite_is_within_bounds``, you don't want to call it ``cisiwb`` for short, because that tells the reader *nothing*.  Instead, you might want to call it ``check_sprite_bounds``.  You can always use supplements to help explain your code, but the goal is to have your code explain itself.

Function Length
---------------

The length (in terms of how many lines of code) of a function is also important.  Shorter functions are better.  A function that is long usually means that it's complicated, and that algorithm can probably be broken down into more functions.

:misc-hl:`Having many short functions is better than having fewer long functions`.  Shorter functions are easier to debug and easier to read.  For example, when you built your number guessing game, functions would have made it much easier to read!

Here's what a very simple number guessing game might have for a main body of code:

.. code-block:: python3
   :linenos:
   
   answer = generate_answer()
   guess = get_guess()
   while guess != answer:
       print_hint()
       guess = get_guess()
   print_ending()

One of the goals of functions is to delegate tasks to other processes.  :misc-hl:`Each function should generally have one clear goal, and if something can be it's own function, it probably should be.`

Changing Code Already Written
-----------------------------

Lastly, a quick point about when you can change your code - the answer is, *always*!  :misc-hl:`Once written, you should always be looking for ways to improve upon your code, even if it means rewriting it.`  Too many students I know have been resistant to changing their code because they feel like they're doing extra work - but it's important to realize that leaving bad code can create more problems in the future.