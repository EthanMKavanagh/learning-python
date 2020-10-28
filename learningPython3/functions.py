# Basic syntax for a function
    # def functionname( parameters ):
    #    "function_docstring"
    #    function_suite
    #    return [expression]

def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

printinfo( age = 18, name = "Ethan" )

# would return -->
Name: Ethan
Age: 18