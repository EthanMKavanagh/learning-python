# -------------------
# Standard Data Types
# -------------------
# Numbers
    # Int (signed integers)
    int = 10

    # Float (floating point real numbers)
    float = 0.0

    # Complex (complex numbers)
    complex = 3.14j

# String
    # Allows single or double quotes
    # '+' operation concatenates
    #  '*' amount of repetitions
    str = 'Hello World!'
    print (str)          # Prints complete string   -->   Hello World!
    print (str[0])       # Prints first character of the string   -->   H
    print (str[2:5])     # Prints characters starting from 3rd to 5th   -->   llo
    print (str[2:])      # Prints string starting from 3rd character   -->   llo World!
    print (str * 2)      # Prints string two times   -->   Hello World!Hello World!
    print (str + "TEST") # Prints concatenated string   -->   Hello World!TEST

# List
    list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
    tinylist = [123, 'john']

    print (list)                # Prints complete list   -->   ['abcd', 786, 2.23, 'john', 70.200000000000003]
    print (list[0])             # Prints first element of the list   -->   abcd
    print (list[1:3])           # Prints elements starting from 2nd till 3rd   -->   [786, 2.23]
    print (list[2:])            # Prints elements starting from 3rd element   -->   [2.23, 'john', 70.200000000000003]
    print (tinylist * 2)        # Prints list two times   -->   [123, 'john', 123, 'john']
    print (list + tinylist)     # Prints concatenated lists   -->   ['abcd', 786, 2.23, 'john', 70.200000000000003, 123, 'john']

# Tuple
    tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
    tinytuple = (123, 'john')

    print (tuple)               # Prints complete tuple   -->   ('abcd', 786, 2.23, 'john', 70.200000000000003)
    print (tuple[0])            # Prints first element of the tuple   -->   abcd
    print (tuple[1:3])          # Prints elements starting from 2nd till 3rd   -->   (786, 2.23)
    print (tuple[2:])           # Prints elements starting from 3rd element   -->   (2.23, 'john', 70.200000000000003)
    print (tinytuple * 2)       # Prints tuple two times   -->   (123, 'john', 123, 'john')
    print (tuple + tinytuple)   # Prints concatenated tuple   -->   ('abcd', 786, 2.23, 'john', 70.200000000000003, 123, 'john')

# Dictionary
    dict = {}
    dict['one'] = "This is one"
    dict[2]     = "This is two"

    tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

    print (dict['one'])       # Prints value for 'one' key   -->   This is one
    print (dict[2])           # Prints value for 2 key   -->   This is two
    print (tinydict)          # Prints complete dictionary   -->   {'name': 'john', 'dept': 'sales', 'code': 6734}
    print (tinydict.keys())   # Prints all the keys   -->   dict_keys(['name', 'dept', 'code'])
    print (tinydict.values()) # Prints all the values   -->   dict_values(['john', 'sales', 6734])