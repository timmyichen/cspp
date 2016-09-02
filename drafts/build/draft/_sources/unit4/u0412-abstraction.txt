.. qnum::
   :start: 1
   :prefix: u0412-


Lesson 04-12: CT Pillar: Abstraction
====================================

**Learning Target: I can implement abstraction through functions and describe its role in computational thinking.**

Pillars of Computational Thinking:
   - Decomposition
   - **Abstraction**
   - Pattern Recognition
   - Algorithms
   
What is Abstraction?
--------------------

The following is an answer by user miraculixx on StackOverflow, responding to the question "What does abstraction mean in programming?"

   Abstraction is a core concept in all of computer science. Without abstraction, we would still be programming in machine code or worse not have computers in the first place. So IMHO that's a really good question.
   
   **What is abstraction**
   
   *Abstracting* something means to give names to things, so that the name captures the core of what a function or a whole program does.
   
   One example is given in the book you reference, where it says
   
      Suppose we’re working with turtles, and a common operation we need is to draw squares. “Draw a square” is an abstraction, or a mental chunk, of a number of smaller steps. So let’s write a function to capture the pattern of this “building block”:
   
   Forget about the turtles for a moment and just think of drawing a square. If I tell you to draw a square (on paper), you immediately know what to do:
      
   * draw a square => *draw a rectangle with all sides of the same length.*
   
.. image:: img/abs-square.svg
   :align: center
   :alt: picture of a square
   
|

   You can do this without further questions because you know by heart what a square is, without me telling you step by step. Here, the word square is the abstraction of "draw a rectangle with all sides of the same length".
   
   **Abstractions run deep**
   
   But wait, how do you know what a *rectangle* is? Well, that's another abstraction for the following:
   
   * rectangle => draw two lines parallel to each other, of the same length, and then add another two parallel lines perpendicular to the other two lines, again of the same length but possibly of different length than the first two.

.. image:: img/abs-lines.svg
   :align: center
   :alt: building a rectangle
   
|

   Of course it goes on and on - *lines, parallel, perpendicular, connecting* are all *abstractions* of well-known concepts.
   
   Now, imagine each time you want a rectangle or a square to be drawn you have to give the full definition of a rectangle, or explain lines, parallel lines, perpendicular lines and connecting lines -- it would take far too long to do so.
   
   **The real power of abstraction**
   
   That's the first *power* of abstractions: they make talking and getting things done much easier.
   
   The second power of abstractions comes from the nice property of *composability*: once you have defined abstractions, you can compose two or more abstractions to form a new, larger abstraction: say you are tired of drawing squares, but you really want to draw a *house*. Assume we have already defined the *triangle*, so then we can define:
   
   * *house* => draw a *square* with a *triangle* on top of it

.. image:: img/abs-house.svg
   :align: center
   :alt: house from a square and a triangle
   
|

   Next, you want a village:
   
   * *village* => draw multiple *houses* next to each other

.. image:: img/abs-village.svg
   :align: center
   :alt: village from multiple houses

|

   Oh wait, we want a *city* -- and we have a new concept *street*:
   
   * city => draw many *villages* close to each other, fill empty spaces with more *houses*, but leave room for *streets*
   * street => (some definition of street)
   
   and so on...
   
   **How does this all apply to programmming?**
   
   If in the course of planning your program (a process known as analysis and design), you find good abstractions to the problem you are trying to solve, your programs become shorter, hence easier to write and - maybe more importantly - easier to read. The way to do this is to try and grasp the major concepts that define your problems -- as in the (simplified) example of drawing a *house*, this was *squares* and *triangles*, to draw a *village* it was *houses*.
   
   In programming, we define abstractions as functions (and some other constructs like classes and modules, but let's focus on functions for now). A function essentially names a set of single statements, so a function essentially is an abstraction -- see the examples in your book for details.

(credit: `miraculixx on StackOverflow: What does Abstraction mean in programming? <http://stackoverflow.com/questions/21220155/what-does-abstraction-mean-in-programming>`_ )