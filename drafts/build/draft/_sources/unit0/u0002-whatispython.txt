.. qnum::
   :start: 1
   :prefix: u0003-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".


Lesson 00-02: What is Python?
=============================


Python is a high level, general purpose programming language named after Monty Python, the British comedy group.  What does it mean for a language to be "high-level"?

"High Level"
------------

When you write some code, the computer doesn't interpret it as the words you write.  When computers receive instructions to do anything, like run an application, or even to respond to a keystroke, it receives instructions in machine code.  Machine code is nearly unreadable by humans.  It might look something like this:

.. image:: img/machinecode.png
   :align: center
   :scale: 40%
   :alt: Image of machine code
   
.. Image courtesy of Wikimedia Commons

Pretty unintelligible, right?  This is the lowest level of code there is.  Code written in other languages have to be translated into machine code before being fed to the CPU - the brain of the computer.  Plus, machine code is different for each type of CPU (CPU architecture)!  That's a lot of work you don't want to deal with.

Assembly language is the staple example of a "low level language" - those who are familiar with it can read it and write in it, but it is still CPU-architecture dependent!  A simple "Hello World!" program in NASM Assembly language might look something like this (`source <http://cs.lmu.edu/~ray/notes/x86assembly/>`_):

.. code-block:: none
    
    ;
    
           global  _start
   
           section .text
   _start:
           mov     rax, 1                
           mov     rdi, 1                
           mov     rsi, message          
           mov     rdx, 13               
           syscall                       
   
           mov     eax, 60               
           xor     rdi, rdi              
           syscall                       
   message:
           db      "Hello, World", 10    

While it looks a little more understandable, it's still pretty unreadable.  When you write in high level languages, on the other hand, you don't have to worry about what CPU architecture you're writing for.  It's also more human-readable to make writing it easier.  Here's an example in C (a high level programming language):

.. code-block:: c
   
   #include <stdio.h>
   int main()
   {
       printf("Hello world!");
       return(0);
   }
   
This looks much better - I recognize some words there.  Then here's "Hello World!" in python:

.. code-block:: python3
    
   print("Hello World!")

Doesn't get much simpler than that!

While high-level languages are easier to read, easier to write, and work across many platforms, they tend to be slower than low-level languages since there's more happening behind the hood.  However, modern technology is fast enough so that unless you really need to optimize your code for speed *(like if you're writing a game engine that does a lot of fancy graphics processing)*, you don't have to worry about the speed differences.

Now we move onto how python is...

"Multi-purpose"
---------------

Python a pretty popular language used for many different things.  Here's just a few examples - You can use python to...

- Scrape (automatically collect) data off the web!
- Build fully developed websites! (examples: Google, YouTube, DropBox, Reddit, Instagram)
- Build games! (full list `here <https://wiki.python.org/moin/PythonGames>`_)
- Run scientific and mathematical computations!
- Automation - you can write scripts to automate your life!
- And more!

Python is used for a fairly large variety of things!  But most importantly, it's a relatively easy language to pick up, which is why we use it in this course.  We'll be covering the basics of computer science and programming, and these concepts can be transferred to almost any other language.  So you're not *just* learning python - you're learning computer science and programming.