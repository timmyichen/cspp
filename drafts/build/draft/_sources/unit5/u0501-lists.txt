.. qnum::
   :start: 1
   :prefix: u0501-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".


Lesson 05-01: Python Lists
==========================

**Learning Target: I can utilize python lists to hold various data.**
**Learning Target: I can reference specific elements within a list.**

Data Type of Multiple Values
----------------------------

So far, each variable can only hold one value at a time - one integer or one float or one string.  What if we wanted to hold multiple values?  Like a list of prime numbers under 50?  Or a list of names of students?

You can do this in python by creating a list!  A list is a python datatype that can hold multiple values and has special functions, like a String.  Here's how you create a list:

.. code-block:: python3
    
    numbers = [1,2,3,4,5,6]
    names = ["Sally","Harry"]

Notice that it's similar to a variable assignment statement, except the value uses square brackets (``[]``), and each value is separated by a comma (``,``).

Note that lists can hold values of different datatypes!

.. code-block:: python3
    
    mixed_list = [1,2,"three",4,"5",true,None]

So once we have a list of values, how do we access them again?

Specific Elements in a List
---------------------------

Funnily enough, we do it exactly the same as we access strings!  Just like each character in a string, each element in a list has an index and we use that index to access that value.

.. image:: img/listindex.svg
    :width: 400px
    :align: center
    :alt: indexes of a list

Here's an example:

.. activecode:: ex_0501_1
    :autorun:
    :nocodelens:
    
    fruits = ["apple","banana","strawberry","grape","pineapple","watermelon"]
    print(fruits) #entire list
    print(fruits[0]) #apple
    print(fruits[3]) #grape
    print(fruits[-1]) #watermelon

Notice how when the list is printed, it prints the entire list, including the brackets and quotes (if it's a string).

List Slicing
------------

Similar to strings, you can also slice lists using the same notation.

.. activecode:: ex_0501_2
    :autorun:
    :nocodelens:
    
    numbers = [0,1,2,3,4,5,6,7,8,9]
    print(numbers)
    print(numbers[0:3]) #0,1,2
    print(numbers[5:8]) #5,6,7
    print(numbers[-5:]) #5,6,7,8,9
    print(numbers[4:5]) #4
    
An important note - please see that in our last example, printing ``numbers[4:5]`` returned a **list** with the value in the 4th index.  This is not the same as printing ``numbers[4]``!

.. activecode:: ex_0501_3
    :autorun:
    :nocodelens:
    
    numbers = [0,1,2,3,4,5,6,7,8,9]
    
    #list slice
    print(numbers[4:5])
    
    #list index
    print(numbers[4])
    
    #are they equivalent?
    print(numbers[4] == numbers[4:5])

``numbers[4:5]`` returns a list with the value at the 4th index.
``numbers[4]`` just returns the value at the 4th index.

We won't be using list indexing as much in this course, but it was an interesting tidbit to share.

Checks For Understanding
------------------------

Q#1
~~~
.. activecode:: cfu_0501_1
    :nocodelens:
    
    #complete line 3 to return the 1st element in the given list a_list
    def getFirstElement(a_list):
        return 
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            self.assertEqual(getFirstElement([1,2,3,4]),1,"input: [1,2,3,4]")
            self.assertEqual(getFirstElement(['h','e','l','l','o']),'h', "input: ['h','e','l','l','o']")
    
    myTests().main()
    
Q#2
~~~
.. activecode:: cfu_0501_2
    :nocodelens:
    
    #complete line 3 to return the last element in the given list a_list
    def getFirstElement(a_list):
        return 
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            self.assertEqual(getFirstElement([1,2,3,4]),4,"input: [1,2,3,4]")
            self.assertEqual(getFirstElement(['h','e','l','l','o']),'o', "input: ['h','e','l','l','o']")
    
    myTests().main()