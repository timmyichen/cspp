.. qnum::
   :start: 1
   :prefix: u0507-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".


Lesson 05-08: Building List Functions: ``replaceAll``
=====================================================

**Learning Target: I can create a python function that will replace a given element in a list with another given element.**

Assignment
----------


In the area below, create a function called ``replaceAll()`` that will take in three arguments:

* ``original`` - the original list
* ``find_value`` - the value you want to replace in the list
* ``replace_with`` - the value you want to replace it with in the list

and will replace ALL elements that in ``original`` that match ``find_value`` and replace their value with that of ``replace_with``.  This function should modify the value of ``original``.

You may only use the following list methods: ``append()``, ``insert()``, ``remove()``, ``len()``.

Example:

``replace([1,2,1,2],1,"a")`` should return ``["a",2,"a",2]``

.. activecode:: cfu_0507_1
    :nocodelens:
    
    def replace(original,find_value,replace_with):
        #write here
    
    ====

    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        
        def testOne(self):
            a = [1,2,3,2,1]
            replace(a,2,0)
            self.assertEqual(a,[1,0,3,0,1],"inputs: [1,2,3,2,1],2,0")
            
            a = [5,5,5,5]
            replace(a,5,-5)
            self.assertEqual(a,[-5,-5,-5,-5],"inputs: [5,5,5,5],5,-5")
            
    myTests().main()

Hints
-----

.. reveal:: reveal_0507_1
    :showtitle: Show Hint #1
    :hidetitle: Hide Hint #1
    
    It's kinda like copying a list, except you want to change some of the values.  You'll need a conditional somewhere... how do you know whether you should be changing the value or not?

.. reveal:: reveal_0507_2
    :showtitle: Show Hint #2
    :hidetitle: Hide Hint #2
    
    How do you check if the list element you're looking at matches the list element you want to replace?  How do you actually replace it?  You'll need to use a for loop that loops through the indexes of the list, since you want to alter values (using a for-each loop doesn't let you alter values).

.. reveal:: reveal_0507_3
    :showtitle: Show Answer
    :hidetitle: Hide Answer

    Here's one way to do it:
    
    .. code-block:: python3
    
        def replace(original,find_value,replace_with):
            for index in range(len(original)):
                if original[index] == find_value:
                    original[index] = replace_with
        

