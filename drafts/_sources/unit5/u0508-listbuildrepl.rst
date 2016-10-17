.. qnum::
   :start: 1
   :prefix: u0508-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".


Lesson 05-08: Building List Methods: ``replace``
================================================

**Learning Target: I can create a python function that will replace a given element in a list with another given element.**

Assignment
----------

In the area below, create a method called ``replace()`` that will take in three arguments:

* ``orig`` - the original list
* ``find_value`` - the value you want to replace in the list
* ``replace_with`` - the value you want to replace it with in the list

and will replace ALL elements that in ``orig`` that match ``find_value`` and replace their value with that of ``replace_with``.  The function should then return the new list with the replaced values.  This should be done **without modifying the original list**.

Example:

``replace([1,2,1,2],1,"a")`` should return ``["a",2,"a",2]``

.. activecode:: cfu_0508_1
    :nocodelens:
    
    def replace(orig,find_value,replace_with):
        #write here
    
    ====

    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        
        def testOne(self):
            a = [1,2,3,2,1]
            b = replace(a,2,0)
            a.extend(b)
            self.assertEqual(a,[1,2,3,2,1,1,0,3,0,1],"inputs: [1,2,3,2,1],2,0")
            
            a = [5,5,5,5]
            b = replace(a,5,-5)
            a.extend(b)
            self.assertEqual(a,[5,5,5,5,-5,-5,-5,-5],"inputs: [5,5,5,5],5,-5")
            
    myTests().main()

Hints
-----

.. reveal:: reveal_0508_1
    :showtitle: Show Hint #1
    :hidetitle: Hide Hint #1
    
    It's kinda like copying a list, except you want to change some of the values.  You'll need a conditional somewhere... how do you know whether you should be changing the value or not?

.. reveal:: reveal_0508_2
    :showtitle: Show Hint #2
    :hidetitle: Hide Hint #2
    
    Since you need to copy everything into a new list, you might as well start by looping through all the elements and adding them... except for the ones where they are equal to ``find_value``!  Then you'll want to add something else..

.. reveal:: reveal_0508_3
    :showtitle: Show Answer
    :hidetitle: Hide Answer

    Here's one way to do it (I use ``e`` as short for "element"):
    
    .. code-block:: python3
    
        def replace(orig,find_value,replace_with):
            result = []
            for e in orig:
                if e == find_value:
                    result.append(replace_with)
                else:
                    result.append(e)
            return result

