.. qnum::
   :start: 1
   :prefix: u0310-


Lesson 03-10: The ``break`` Keyword
===================================

**Learning Target: I can use the break keyword to end a loop early.**

What does ``break`` do?
-----------------------

On occasion, there comes a time when you want to stop your loop *right away*.  That's what the ``break keyword`` does.  Take the following as an example:

.. activecode:: 0310_ex_1
   :autorun:
   
   x = 7
   
   while True:
       print(x)
       if x < 3:
           break
       x = x - 1
   print("end")

This also works for ``for`` loops as well:

.. activecode:: 0310_ex_2
   :autorun:
   
   for x in range(7,0,-1):
       print(x)
       if x < 3:
           break
   print("end")
   
The ``break`` keyword only quits out of the "innermost" loop.  This means that if you have a loop inside of a loop (also covered later), using ``break`` will only quit out of the most recently-used loop.

When to use ``break``?
----------------------

``break`` is not a keyword you should be using often in your programs.  In general, you want to follow the following guidelines when you are thinking about using ``break``:

- Use ``break`` to exit a ``for`` loop early - because there is no other way to do this.

   - This is nice because it allows us to provide two ways for a for loop to end - either it loops through everything, or it breaks due to some condition.

- In general, you should avoid using ``break`` in a ``while`` loop, because it is an indicator that you could just write a better condition for the loop.

   - Take the first example above as an example of BAD ``break`` usage.  Instead of using a conditional to break out of the loop, you could've rewritten line 3 to ``while x >= 3:``.  This makes it easier to read and understand the purpose of the loop, and it eliminates the need of the ``break`` keyword.

