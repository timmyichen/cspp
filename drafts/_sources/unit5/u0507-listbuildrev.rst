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


Lesson 05-07: Building List Methods: ``reverse``
================================================

**Learning Target: I can create a python function that will reverse a list.**

Assignment
----------

In the area below, create a method called ``reverse()`` that will take in one list argument, and will reverse the order of the elements.  This should be done **without modifying the original list**.

Example:

``reverse([1,2,3,4])`` should return ``[4,3,2,1]``

.. activecode:: cfu_0507_1
    :nocodelens:
    
    def reverse(orig):
        #write here
    
    ====

    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        
        def testOne(self):
            a = [6,7,8]
            b = reverse(a)
            a.extend(b)
            self.assertEqual(a,[6,7,8,8,7,6],"inputs: [6,7,8]")
            
            a = [False,False,True]
            b = reverse(a)
            a.extend(b)
            self.assertEqual(a,[False,False,True,True,False,False],"inputs: [False,False,True]")
            
    myTests().main()

Hints
-----

.. reveal:: reveal_0507_1
    :showtitle: Show Hint #1
    :hidetitle: Hide Hint #1
    
    Similar to the last one, you'll be adding things to your result.  Except this time, you're doing it in reverse.  You'll want to reference the **indexes** - how do you reference a bunch of numbers in reverse order?

.. reveal:: reveal_0507_2
    :showtitle: Show Hint #2
    :hidetitle: Hide Hint #2
    
    In whichever loop you're using (``for`` or ``while``), keep in mind the following questions:
    
    * What index (relative to the length of the list) do you want to start at?
    * What index do you want to end at?

.. reveal:: reveal_0507_3
    :showtitle: Show Hint #3
    :hidetitle: Hide Hint #3
    
    Don't forget that the last index will be ``len(orig)-1``!  Anything greater than that (like just ``len(orig)``) will result in an error!

.. reveal:: reveal_0507_4
    :showtitle: Show Answer
    :hidetitle: Hide Answer

    Here's one way to do it:
    
    .. code-block:: python3
    
        def reverse(orig):
            result = []
            index = len(orig)-1
            while index >= 0:
                result.append(orig[index])
                index = index - 1
                
            return result
    
    And here's the 'super pythonic' way to do it:
    
    .. code-block:: python3
    
        def reverse(orig):
            return orig[::-1]
    
    (but this wouldn't work in any other language - make sure you're confident with the solution provided above)