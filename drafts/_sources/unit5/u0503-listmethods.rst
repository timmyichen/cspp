.. qnum::
   :start: 1
   :prefix: u0503-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".


Lesson 05-03: Basic List Functions
==================================

**Learning Target: I can use python documentation to properly use list methods.**

Python Documentation
--------------------

The `Python 3 documentation <https://docs.python.org/3/tutorial/datastructures.html>`_ contains all the information you need to know about python - this includes what list functions are available to you!  In the area below, using the documentation link above, try to figure out how to use these functions.  Remember to use CTRL+F (Windows) or CMD+F (Mac) to find specific words on a page.

Using The Functions
-------------------

``list.append()``
~~~~~~~~~~~~~~~~~

.. activecode:: cfu_0503_1
    :nocodelens:
    
    #this should append x, y, and z (in that order) to the end of the list arr
    def append3(arr,x,y,z):
        #write here
    
    ====

    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        
        def testOne(self):
            self.assertEqual(append3([1,2,3],4,5,6),[1,2,3,4,5,6],"inputs: [1,2,3],4,5,6")
            self.assertEqual(append3([2,87,-3],'d',3,True),[2,87,-3,'d',3,True],"inputs: [2,87,-3],'d',3,True")
    myTests().main()

``list.remove()``
~~~~~~~~~~~~~~~~~

.. activecode:: cfu_0503_2
    :nocodelens:
    
    #
    def remove

``list.insert()``
~~~~~~~~~~~~~~~~~


``len(list)``
~~~~~~~~~~~~~

