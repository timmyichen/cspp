.. qnum::
   :start: 1
   :prefix: u0502-

..  Copyright (C) 2016 Timothy Chen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with the Invariant Sections being Contributor List, Lesson 00-01: 
    Introduction To The Course, no Front-Cover Texts, and no Back-Cover Texts.  
    A copy of the license is included in the section entitled "GNU Free 
    Documentation License".


Lesson 05-02: Looping over Lists
================================

| **Learning Target: I can use a for loop to iterate over every element in a list.**
| **Learning Target: I can use a for-each loop to iterate over every element in a list.**

Looping by Referencing Index
----------------------------

We know that we can use a for loop to iterate through a list of numbers.  This lets us iterate through every position in a list:

.. activecode:: ex_0502_1
    :autorun:
    :nocodelens:
    
    a = ['hi','hey','hello','howdy','holla']
    for i in range(len(a)):
        print(a[i])
    
However, in python, there's a much easier way!

Using a ``for-each`` loop
-------------------------

We can use a for each loop to do the same thing as above:

.. activecode:: ex_502_2
    :autorun:
    :nocodelens:
    
    a = ['hi','hey','hello','howdy','holla']
    for item in a:
        print(item)

In our first example with ``i``, ``i`` represented the index of each element of ``a``.  However, in this example, ``item`` represents the element itself!  This is called a :vocab-word:`for-each loop` because it :vocab-def:`runs a loop for each element in a list`.

In case you're wondering why this is, recall that ``range()`` is a function that generates a LIST of numbers!  All you're doing is iterating through that list!  So really, every for loop in python is a for-each loop!

Checks for Understanding
------------------------

Q#1
~~~

**INSTRUCTIONS**: Write a ``for`` loop below so it will print out every element in the list ``names``.

.. activecode:: cfu_0502_1
    :nocodelens:
    
    names = ['Bobert','Danny','Pat','Chris','Snacks']

    #write code below
    


Q#2
~~~

**INSTRUCTIONS**: Given a list of integers ``numbers``, return the sum of the elements in ``numbers``.

.. activecode:: cfu_0502_2
    :nocodelens:
    
    def sumList(numbers):
        #write here
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        
        def testOne(self):
            self.assertEqual(sumList([1,2,3,4]),10,"input: [1,2,3,4]")
            self.assertEqual(sumList([-3,3,-7,7,6,-6,100,-100]),0, "input: [-3,3,-7,7,6,-6,100,-100]")
            self.assertEqual(sumList([25,11,46,23,73]),178, "input: [25,11,46,23,73]")
    
    myTests().main()
    
Q#3
~~~

**INSTRUCTIONS**: Given a list of letters ``letters``, return the count of vowels in the list.

.. activecode:: cfu_0502_3
    :nocodelens:
    
    def sumVowels(letters):
        #write here
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            self.assertEqual(sumVowels(['h', 'e', 'l', 'l', 'o']),2,"input: ['h', 'e', 'l', 'l', 'o']")
            self.assertEqual(sumVowels(['c', 'o', 'm', 'p', 'u', 't', 'e', 'r', ' ', 's', 'c', 'i', 'e', 'n', 'c', 'e']),6, "input: ['c', 'o', 'm', 'p', \'u\', 't', 'e', 'r', ' ', 's', 'c', 'i', 'e', 'n', 'c', 'e']")
            self.assertEqual(sumVowels(['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e', 'e']),4, "input: ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e', 'e']")
    
    myTests().main()