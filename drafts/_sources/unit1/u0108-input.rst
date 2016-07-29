.. qnum::
   :start: 1
   :prefix: ch0108-

Lesson 01-08: User Input
========================

**Learning Target: I can write a program to get user input.**

The best kinds of programs are often the interactive ones.  Basic interactivity is easy to implement in python using the ``input`` function.

:misc-hl:`An important note: using the input function in the ActiveCode windows in the browser may have unintended side effects.  For best results (and most accurate results), I highly advise you run this code in your own text-based python IDE.`

The ``input()`` Function
------------------------

The built-in ``input()`` function is a way to prompt the user to type something in.  In python, this would be done in the console (where the output is).  On this site, it will appear as a pop-up box.  Inside the parentheses, you would put the prompt as a string.  The prompt is what the user sees when you are asking for input.  Run the following two examples as a demonstration.

.. activecode:: ex_input1
   
   name = input("Hello, what's your name?")
   print("Hello " + name)

.. activecode:: ex_input2
   
   prompt = "Hello, what's your name?"
   name = input(prompt)
   print("Hello " + name)

They should both do the exact same thing.  Notice how we put the ``input()`` function as part of a **variable assignment** statement.  This is because the ``input()`` function actually represents a value - the value being whatever was typed in to the prompt.  

The Datatype of ``input()``
---------------------------

An important question here is: what *type of data* does ``input()`` give you?  We can easily find out using the ``type()`` function.  Try running the example below.

.. activecode:: ex_input3
   
   name = input("Hello, what's your name?")
   print(type(name))

So here, we're asking the user ``Hello, what's your name?`` and saving their input in a variable called ``name``.  We then print the datatype of ``name`` using the ``type()`` function.  The result is a string.  What if you had typed in a number?  Try running the example below.

.. activecode:: ex_input4
   
   age = input("Hello, what's your age?")
   print(type(age))

Still a string!  We then know that :misc-hl:`The input function will always return a string, no matter what you type in`.  This is important to know, because if we wanted to ask a user for a number, we would have to convert it using a conversion function before using.  See the following example:

.. activecode:: ex_input5
   
   num = input("Enter a number and I will tell you 10 times that number: ")
   new_num = float(num) * 10
   print(new_num)

Checks for Understanding
------------------------

Q#1
~~~

In the space below on line 2, write a statement that will ask the user to enter in their favorite food using ``input()`` and save it in a variable called ``fav_food``.

.. activecode:: cfu_0108_1
   
   #
   
   print("Your favorite food is " + fav_food)

Q#2
~~~

In the space below on line 2, write a statement that will ask the user to guess a number between 1 and 10 using ``input()``, convert it to an integer, and save it in a variable called ``guess``.

.. activecode:: cfu_0108_2
   
   #
   
   print("You guessed: " + str(guess))

