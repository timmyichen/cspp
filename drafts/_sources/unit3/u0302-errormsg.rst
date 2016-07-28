.. qnum::
   :start: 1
   :prefix: u0302-


Lesson 03-02: Python's Error Messages
=====================================

**Learning Target: I can interpret error messages to debug code.**

*Note: All errors and screenshots in this lesson are from a python console, and may not be the exact same message from the errors you would get from this site.*

Error Messages
--------------

Over the course of learning programming, you will come across many different types of errors.  In most programming languages, whenever an error stops program execution, you will also see an :vocab-word:`error message` - which :vocab-def:`provides information about the error, including where it is and what type of error it is`.

For example, if we were to run the following code in a as a python program:

::
   
   print("hi")
   print "there"

When we execute this program, we would see:

.. code-block:: none
   
        File "/path/to/file.py", line 2
          print "there"
                      ^
   SyntaxError: Missing parentheses in call to 'print'

There is some very important information here!  Let's break it down.

.. image:: img/errormsg.svg
   :width: 700px
   :alt: Five parts to the error message
   :align: center

1. **Location** - This points to the file where the error is happening.  It's important because later on, we'll be working with multiple files, and we will want to pinpoint exactly where the error is.
2. **Location** (again) - This time, it tells you exactly which line on the file is causing the error.
3. **Location** (again) - And again, the message is telling you exactly where in the line the error is occurring.  Note that here, it may be a little inaccurate, but is generally in the right area.
4. **Type of Error** - The name of the error - covered in this lesson.
5. **Error Description** - It gives a short description as to where the error occurred.

As you can see, error messages provide a LOT of information about where the error is, so you can easily find the location and debug it!

The only thing that we haven't quite learned about yet are the Types of Errors.

Common Error Types
------------------

Now these are not going to be the only types of errors you come across, but the following list are errors that you will likely find to be the most common:

   - **ParseError / SyntaxError** - This is a normal syntax error, meaning that there is something wrong with the way that the code is written.  Exactly the same as in the last lesson.
   - **TypeError** - This typically has to do with incompatible datatypes.
   - **NameError** - "Names" refer to variable names - generally, you will often see this when you forget to initialize a variable, or if you incorrectly typed a variable name.
   - **ValueError** - Means that the given value will not work - for example, you will encounter this error if you try to use convert ``"five"`` to an integer with ``int("five")``.
   - **IndentationError** - This error usually has to do with spacing - either when there is an unexpected indent, or if it's supposed to be indented but isn't.  This is a type of SyntaxError.

It is valuable to quickly recognize what is wrong with your program and to slowly memorize these types of errors, as it will greatly speed up your debugging process.