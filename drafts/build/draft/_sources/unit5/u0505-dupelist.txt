.. qnum::
   :start: 1
   :prefix: u0505-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".


Lesson 05-05: Duplicating Lists
===============================

**Learning Target: I can duplicate a list.**

Algorithm for Duplicating
-------------------------

In order to write a function to modify a list without affecting the original one, we would need to make a copy of it.  Although there are shortcuts to make copies of lists, let's first see how we might do it manually.

We want to start by creating a new, blank list.  This ensures that it will have a different reference than the one we're trying to copy.

.. code-block:: python3
    
    old_list = [1,2,3,4]
    new_list = [] #this is an empty list

Then we need to manually loop through the old array and 'copy' every element into the new array.  We can do this by using ``append()``.  We can then look at the IDs and check if they are equal to each other using the following code:

.. raw:: html
    
    <script src="//repl.it/embed/DxVV/1.js"></script>

..  source:

    old_list = [1,2,3,4]
    new_list = []
    
    for element in old_list:
        new_list.append(element)
    
    print("old list: {}".format(str(old_list)))
    print("new list: {}".format(str(new_list)))
    
    old_id = id(old_list)
    new_id = id(new_list)
    print("old list reference ID: {}".format(old_id))
    print("new list reference ID: {}".format(new_id))
    print("old list ID == new list ID: {}".format(old_id == new_id))
    print("old list contents == new list contents: {}".format(old_list == new_list))

Using the ``copy.copy()`` Function
----------------------------------

Python also has a built-in ``copy`` library that has a bunch of functions related to copying things.  We can use the ``copy.copy()`` function to make a quick copy of a list.

.. raw:: html

    <script src="//repl.it/embed/DxVY/1.js"></script>
    
..  source:

    import copy

    old_list = [1,2,3,4]
    new_list = copy.copy(old_list)
    
    print("old list: {}".format(str(old_list)))
    print("new list: {}".format(str(new_list)))
    
    old_id = id(old_list)
    new_id = id(new_list)
    print("old list reference ID: {}".format(old_id))
    print("new list reference ID: {}".format(new_id))
    print("old list ID == new list ID: {}".format(old_id == new_id))
    print("old list contents == new list contents: {}".format(old_list == new_list)) 

As you can see, this much easier - but it's important to know how to copy lists anyway!