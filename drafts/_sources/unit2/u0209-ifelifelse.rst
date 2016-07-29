.. qnum::
   :start: 1
   :prefix: ch0209-

Lesson 02-09: If/Elif/Else Statements
=====================================

**Learning Target: I can use if/elif/else statements to execute code conditionally.**

The ``elif`` Keyword
--------------------

Any series of ``if`` statements are inefficient.  Take the following for example (use Show Codelens to step through code):

.. activecode:: 0209_ex_1

   state = "California"
   
   if state == "New York":
       initials = "NY"
   if state == "California":
       initials = "CA"
   if state == "Georgia":
       initials = "GA"
   if state == "Texas":
       initials = "TX"
       
   print(initials)

This code is inefficient because each of these four ``if`` statements will be checked, regardless of which one is actually True!  For example, if ``state`` is ``"New York"``, then there's no reason to check the other ``if`` statements, because we know they are false!

This is where the ``elif`` statement comes into play.  The ``elif`` statement is short for "else if", and has similarities to both ``else`` and ``if``.  The syntax looks something like this:

::
   
   if some_condition:
       #do stuff if some_condition is True
   elif some_other_condition:
       #do stuff if some_other_condition is True
   #the else is optional
   else:
       #do stuff if neither some_condition nor some_other_condition are True

A few things to note:
   
   - The ``elif`` is optional!  Only use it if you need it.
   - Similar to ``else``, each ``elif`` statement must directly follow an ``if`` statement.
   - Each ``elif`` statement must have a condition.
   - Tabbing rules and etiquette for ``elif`` statements are the same as ``if`` and ``else`` statements.

Additionally, you can have as many ``elif`` statements as you want!  Walk through the following example and carefully note which ``if`` statements are "checked"  (use Show Codelens to step through code):

.. activecode:: 0209_ex_2

   state = "California"
   
   if state == "New York":
       initials = "NY"
   if state == "California":
       initials = "CA"
   if state == "Georgia":
       initials = "GA"
   if state == "Texas":
       initials = "TX"
       
   print(initials)

Can now be rewritten as the following.  Walk through the example again, but this time, watch which ``if`` statements are checked  (use Show Codelens to step through code):

.. activecode:: 0209_ex_3

   state = "California"
   
   if state == "New York":
       initials = "NY"
   elif state == "California":
       initials = "CA"
   elif state == "Georgia":
       initials = "GA"
   elif state == "Texas":
       initials = "TX"
       
   print(initials)

You may have noticed that the check for "Georgia" and "Texas" were skipped - and it makes sense that they were!  The important thing here is that :misc-hl:`Given any single set of if-elif-else statements, only one block of code will execute`.

Also note that an ``elif`` cannot come after an ``else``, because ``else`` is used to capture **all other possibilities**.  The ordering is always ``if``-``elif(s)``-``else``.

Checks For Understanding
------------------------

TODO