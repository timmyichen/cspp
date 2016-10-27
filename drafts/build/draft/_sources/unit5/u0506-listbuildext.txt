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


Lesson 05-06: Building List Functions: ``extend``
=================================================

**Learning Target: I can create a python function that will combine two lists.**

Assignment
----------

In the area below, create a function called ``extend()`` that will take in two arguments, a list called ``original`` and a list called ``extension``.  The function should alter ``original`` by adding the elements of ``extension`` onto ``original``, keeping the same order.

You may only use the following list methods: ``append()``, ``insert()``, ``remove()``, ``len()``.

Example:

.. code-block:: python3
    
    list1 = [1,2,3]
    list2 = [7,8,9]
    extend(list1,list2)
    print(list1)

This should print the following: ``[1,2,3,7,8,9]``.


.. activecode:: cfu_0506_1
    :nocodelens:
    
    def extend(original,extension):
        #write here
    
    ====

    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        
        def testOne(self):
            a = [1,2,3]
            b = [5,6,7]
            extend(a,b)
            self.assertEqual(a,[1,2,3,5,6,7],"inputs: [1,2,3],[5,6,7]")
            
            a = ['a','c','e']
            b = ['h','e','y']
            extend(a,b)
            self.assertEqual(a,['a','c','e','h','e','y'],"inputs: ['a','c','e'],['h','e','y']")
            
    myTests().main()

Hints
-----

.. reveal:: reveal_0506_1
    :showtitle: Show Hint #1
    :hidetitle: Hide Hint #1
    
    Remember that you can modify lists within functions and it will stay modified when you're done with the function!

.. reveal:: reveal_0506_2
    :showtitle: Show Hint #2
    :hidetitle: Hide Hint #2
    
    You'll have to add elements from ``extension`` to ``original``, one by one, using the ``append()`` list function.

.. reveal:: reveal_0506_3
    :showtitle: Show Answer
    :hidetitle: Hide Answer

    Here's one way to do it:
    
    .. code-block:: python3
    
        def extend(original,extension):
            for element in extension:
                original.append(element)