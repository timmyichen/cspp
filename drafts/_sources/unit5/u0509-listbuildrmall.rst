.. qnum::
   :start: 1
   :prefix: u0509-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".


Lesson 05-09: Building List Methods: ``removeall``
==================================================

**Learning Target: I can create a python function that will remove all elements of a given value.**

Assignment
----------

In the area below, create a method called ``removeAll()`` that will take in two arguments:

* ``orig`` - the original list
* ``del_value`` - the value you want to replace in the list

and will remove ALL elements that in ``orig`` that match ``del_value``.  The function should then return the new list without the removed values.  This should be done **without modifying the original list**.

Example:

``removeAll([1,2,1,2,3,1,2],1)`` should return ``[2,2,3,2]``

.. activecode:: cfu_0509_1
    :nocodelens:
    
    def removeAll(orig,del_value):
        #write here
    
    ====

    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        
        def testOne(self):
            a = [1,2,3,2,1]
            b = removeAll(a,1)
            a.extend(b)
            self.assertEqual(a,[1,2,3,2,1,2,3,2],"inputs: [1,2,3,2,1],1")
            
            a = [0,0,1,1,0,1,0,0]
            b = removeAll(a,0)
            a.extend(b)
            self.assertEqual(a,[0,0,1,1,0,1,0,0,1,1,1],"inputs: [0,0,1,1,0,1,0,0],0")
            
    myTests().main()

Hints
-----

.. reveal:: reveal_0509_1
    :showtitle: Show Hint #1
    :hidetitle: Hide Hint #1
    
    Just like the previous few, you're going to be looping through the list and selectively adding elements to your final list.  However, this time, whenever you find your ``del_value``,  you won't want to add anything at all!

.. reveal:: reveal_0509_2
    :showtitle: Show Hint #2
    :hidetitle: Hide Hint #2
    
    To avoid empty if/else statements, this time you'll want to check if an element ``e`` is NOT equal to ``del_value`` - what do you want to do with an element if it's not the one you want to delete?

.. reveal:: reveal_0509_3
    :showtitle: Show Answer
    :hidetitle: Hide Answer

    Here's one way to do it (I use ``e`` as short for "element"):
    
    .. code-block:: python3
    
        def removeAll(orig,del_value):
            final = []
            for e in orig:
                if e != del_value:
                    final.append(e)
            return final
