#Why!!
"""
 The guidelines provided here are intended to improve the readability of code 
 and make it consistent across the wide spectrum of Python code. As PEP 20 says, “Readability counts”.
"""

#When Avoid!!
"""
However, know when to be inconsistent – sometimes style guide recommendations just aren’t applicable. 
When in doubt, use your best judgment. Look at other examples and decide what looks best. And don’t hesitate to ask!

In particular: do not break backwards compatibility just to comply with this PEP!

Some other good reasons to ignore a particular guideline:

    -> When applying the guideline would make the code less readable, 
    even for someone who is used to reading code that follows this PEP.
    
    -> To be consistent with surrounding code that also breaks it (maybe for historic reasons)-
    although this is also an opportunity to clean up someone else’s mess (in true XP style).
    
    -> Because the code in question predates the introduction of the guideline and 
    there is no other reason to be modifying that code.
    
    -> When the code needs to remain compatible with older versions of Python 
    that don’t support the feature recommended by the style guide.
"""

#Notes :

"""
-> Package and Module Names: Modules should have short, all-lowercase names. 
                          Underscores can be used in the module name if it improves readability.

-> Class Names: Class names should normally use the CapWords convention.    

-> Function and Variable Names: Function names should be lowercase, 
                                with words separated by underscores as necessary to improve readability.
                                Variable names follow the same convention as function names.

-> DocString: Python docstrings are string literal that apear the right after the defination of the function,
              method, class, or in module.

              Example: def jadu():
                            '''This Is docsting and here you can write the type of the input, return etc.. of the function, 
                            module or class.'''
              And You can access this by using the __doc__ function like print(jadu.__doc__).

"""