.. qnum::
   :start: 1
   :prefix: u0410-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".


Lesson 04-10: Pseudocode
========================

**Learning Target: I can use pseudocode to plan out an algorithm/solution to a problem.**

Planning Your Algorithm
-----------------------

When solving a problem, regardless of whether it's a big one or a small one, it always helps to plan.  

Dwight D. Eisenhower once said, *"Plans are worthless, but planning is everything."*  A plan can (and probably will) change as you work through a problem, but that does not mean that it's a waste.  It's the planning process itself that is valuable - having you work through a potential solution, getting ideas down, having something to fall back on.

When it comes to planning algorithms, it doesn't have to be written in Python (or whatever coding language you are using).  In fact, it's better that you don't have to worry about syntax while you're planning - remember, it's the *ideas* that are important.

It helps to try to think of what you want to do as a set of processes.  Let's take the number guessing game as an example.  When planning for a project like that, take the role of the computer and ask yourself - "What would I have to do if I wanted to play a number guessing game with someone?"  Your steps might look something like this:

1. Think of a random number in my head
2. Ask the user to guess a number
3. If it's right, then we end the game
4. If it's wrong, then we give them a hint

What we wrote above is our first step to writing :vocab-word:`pseudocode`, which is basically :vocab-def:`"fake-code", used to get ideas and processes down on paper`.

What Does Pseudocode Look Like?
-------------------------------

Pseudocode can look different, depending on who is writing it.  It's also largely personal preference, since something that *you* are writing for *yourself*.

If I were to create pseudocode for the number guessing game, it might look something like above, except it would be more structured:

.. code-block:: none
   :linenos:
   
   generate random number
   get player's guess
   repeat while game is going:
      check if player is right or wrong
      if right, stop loop
      if wrong, check if higher or lower
      if higher, tell player
      if lower, tell the player
      get another guess
   if right, congratulate the player

Now, obviously, my solution might look very different from this, but it's fine - these are just first ideas; they don't have to be the final product.

Just remember that pseudocode can look however you like, so long as it is helpful to you!