.. qnum::
   :start: 1
   :prefix: u0506-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".


Lesson 05-06: Building List Methods: ``extend``
===============================================

**Learning Target: I can create a python function that will combine two lists.**

Assignment
----------

In the area below, create a method called ``extend()`` that will take in two list arguments, and will add all the elements of the second list to the first list, in the same order, then return the list.  This should be done **without modifying the original list**. 

Example:

``extend([1,2,3],[7,8,9])`` should return ``[1,2,3,7,8,9]``

.. activecode:: cfu_0506_1
    :nocodelens:
    
    def extend(orig,ext):
        #write here
    
    ====

    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        
        def testOne(self):
            a = [1,2,3]
            b = [5,6,7]
            extended = extend(a,b)
            a.extend(extended)
            self.assertEqual(a,[1,2,3,1,2,3,5,6,7],"inputs: [1,2,3],[5,6,7]")
            
            a = ['a','c','e']
            b = ['h','e','y']
            extended = extend(a,b)
            a.extend(extended)
            self.assertEqual(a,['a','c','e','a','c','e','h','e','y'],"inputs: ['a','c','e'],['h','e','y']")
            
    myTests().main()

Hints
-----

.. reveal:: reveal_0506_1
    :showtitle: Show Hint #1
    :hidetitle: Hide Hint #1
    
    This works very similarly to the algorithm for copying lists in lesson 05-05!

.. reveal:: reveal_0506_2
    :showtitle: Show Hint #2
    :hidetitle: Hide Hint #2
    
    ...Except you have to do it twice!  Once for the old list, once for the new!

.. reveal:: reveal_0506_3
    :showtitle: Show Answer
    :hidetitle: Hide Answer

    Here's one way to do it (I use ``e`` as short for "element"):
    
    .. code-block:: python3
    
        def extend(orig,ext):
            #write here
            result = []
            for e in orig:
                result.append(e)
            for e in ext:
                result.append(e)
            return result