.. qnum::
   :start: 1
   :prefix: u0504-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".


Lesson 05-04: Value Representation of Lists
===========================================

**Learning Target: I can understand the value representation of a list.**

Stored by Reference
-------------------

Let's take the following program as an example:

.. activecode:: ex_0504_1
    :autorun:
    
    string1 = "hello"
    string2 = string1
    list1 = [1,2,3]
    list2 = list1
    print("Strings: {} {}".format(string1,string2))
    print("Lists: {} {}".format(str(list1),str(list2)))

And now let's step through the codelens for that code:

.. codelens:: cl_0504_1
    :showoutput:
    
    string1 = "hello"
    string2 = string1
    list1 = [1,2,3]
    list2 = list1
    print("Strings: {} {}".format(string1,string2))
    print("Lists: {} {}".format(str(list1),str(list2)))

You'll notice that the variables ``list1`` and ``list2`` are pointing to the same thing, while ``string1`` and ``string2`` have individual (but identical) values!

That's because list variables don't store the data from the list itself - instead, they store the :vocab-def:`location of the data within the memory`, often called the :vocab-word:`reference`.  We can see the actual location by using the ``id()`` function:

.. raw:: html
    
    <script src="//repl.it/embed/DxQw/0.js"></script>

..  original code:
    a_list = [1,2,3]
    same_ref = a_list
    new_list = [1,2,3]
    print(id(a_list))
    print(id(same_ref))
    print(id(new_list))

Notice how the IDs of ``a_list`` and ``same_ref`` are identical, because they're both pointing to the same object, but ``new_list`` was created with its own set of (identical) values, but has a different ID.

Why does it matter?
-------------------

This comes into play whenever you want to modify a list with functions.

.. activecode:: ex_0504_2
    :autorun:
    
    #this function doubles the value of every element in a given list
    def double_list(inp):
        for i in range(len(inp)):
            inp[i] = inp[i] * 2
        return inp
    
    some_list = [1,2,3]
    print("original list before: {}".format(str(some_list)))
    new_list = double_list(some_list)
    print("original list after: {}".format(str(some_list)))
    print("new list after: {}".format(str(new_list)))

We wrote a function ``double_list`` that takes in a list as an argument, doubles all the values, then returns the new list - except *there is no new list* - this function is modifying the original list - the one that exists outside the function!  This is an issue when we want to make modifications to the list *without changing the original list*.  In the next lesson, we will explore different methods of copying lists.

Checks for Understanding
------------------------

Q#1
~~~
.. mchoice:: cfu_0504_1
    :correct: b
    :answer_a: len()
    :answer_b: id()
    :answer_c: mem()
    :answer_d: ref()
    
    What built-in python function do you use to find the memory location of a variable?
