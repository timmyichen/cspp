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


Lesson 05-09: Building List Functions: ``removeall``
====================================================

**Learning Target: I can create a python function that will remove all elements of a given value.**

Assignment
----------

In the area below, create a method called ``removeAll()`` that will take in two arguments:

* ``original`` - the original list
* ``del_value`` - the value you want to replace in the list

and will remove ALL elements that in ``original`` that match ``del_value``.  The function should modify the value of ``original``.

Example:

``removeAll([1,2,1,2,3,1,2],1)`` should return ``[2,2,3,2]``

.. activecode:: cfu_0508_1
    :nocodelens:
    
    def removeAll(orig,del_value):
        #write here
    
    ====

    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        
        def testOne(self):
            a = [1,2,3,2,1]
            removeAll(a,1)
            self.assertEqual(a,[2,3,2],"inputs: [1,2,3,2,1],1")
            
            a = [0,0,1,1,0,1,0,0]
            removeAll(a,0)
            self.assertEqual(a,[1,1,1],"inputs: [0,0,1,1,0,1,0,0],0")
            
    myTests().main()

Hints
-----

.. reveal:: reveal_0508_1
    :showtitle: Show Hint #1
    :hidetitle: Hide Hint #1
    
    This time, you're probably going to want a loop, but be careful!  Remember that when you remove an element, it shifts the index of all the remaining elements down by 1!

.. reveal:: reveal_0508_2
    :showtitle: Show Hint #2
    :hidetitle: Hide Hint #2
    
    You'll probably want to use a ``while`` loop here.  Also consider: In a while loop, you're likely going to have a variable that keeps track of the index.  When do you want the index to move up?  Conversely, when do you want the index to *not* change?

.. reveal:: reveal_0508_3
    :showtitle: Show Answer
    :hidetitle: Hide Answer

    Here's one way to do it:
    
    .. code-block:: python3
    
        def removeAll(original,del_value):
            index = 0
            
            while(index < len(original)):
                if original[index] == del_value:
                    original.remove(del_value)
                else:
                    index = index + 1
    
    Here's another way where we use for loops to count the occurrences of ``del_value``, then another for loop do delete all of them at once.
    
    .. code-block:: python3
    
        def removeAll(original,del_value):
            count = 0
            for e in original:
                if e == del_value:
                    count = count + 1
            
            for x in range(count):
                original.remove(del_value)
