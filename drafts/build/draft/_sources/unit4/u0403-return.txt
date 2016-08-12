.. qnum::
   :start: 1
   :prefix: u0403-


Lesson 04-03: The ``return`` Statement
======================================

**Learning Target: I can utilize functions that return values.**

Functions Represent Values
--------------------------

Every function has a value representation.  Let's try printing a function instead of its 

.. activecode:: 0403_ex_1
   :autorun:
   
   def add2(num1,num2):
       print(num1 + num2)
   
   print(add2(1,2))
   print(add2(0,0))
   print("Program ended")
   
Notice that in addition to printing the results (3 and 0 respectively), it prints ``None`` every time.

Even though not every function takes in data (through arguments), :misc-hl:`every function sends back, or returns a value`, and that value is ``None`` by default.  You can override it by using the ``return`` keyword.

Using The ``return`` Keyword
----------------------------

Let's take our example from above, but instead of printing the sum of two numbers, we'll return it.

.. activecode:: 0403_ex_2
   :autorun:
   
   def add2(num1,num2):
       return num1 + num2
   
   add2(1,2)
   add2(0,0)
   print("Program ended")

You might notice that nothing got printed!  That's because there are no print statements anywhere.  Since the function ``add2`` returns a value, the the expression ``add2(1,2)`` "becomes" that value, and represents 3.  ``add2(10,10)`` represents the value 20.  We can then print these value representations as if they were numbers themselves:

.. activecode:: 0403_ex_3
   :autorun:
   
   def add2(num1,num2):
       return num1 + num2
      
   print(add2(1,2))
   print(add2(0,0))
   print(add2(10,10))
   print("Program ended")
   
This is extremely useful as functions are often used for calculations, without actually printing it.  Take the following as an example - a function that checks if a number is prime or not that will return ``True`` or ``False``.

.. activecode:: 0403_ex_4
   :autorun:
   
   def is_prime(n):
       if n == 1:
           return False
       if n == 2:
           return True
       if n % 2 == 0:
           return False
       for x in range(3, n//2, 2):
           if n % x == 0:
               return False
       return True
   
   print(is_prime(10))
   print(is_prime(11))

While this might look similar to other examples we've used in the past, now we can use the ``is_prime()`` for any general purpose!  For example, if we wanted to print all the prime numbers up to 50, we can run the following:

.. activecode:: 0403_ex_5
   :autorun:
   
   def is_prime(n):
       if n == 1:
           return False
       if n == 2:
           return True
       if n % 2 == 0:
           return False
       for x in range(3, n//2, 2):
           if n % x == 0:
               return False
       return True
   
   for num in range(1,51):
       if is_prime(num):
           print(num)
       #remember is_prime() represents a boolean, which is why we
       #  can use it in our if statement!
       
:misc-hl:`Writing functions with return statements allow us to create useful, general-purpose, re-usable functions!`

You might notice in the example above, there are multiple places where we use the ``return`` keyword.  It's important to know that **when you invoke the** ``return`` **keyword, the function ends immediately afterwards**.

Checks For Understanding
------------------------

Q#1
~~~

