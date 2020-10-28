# 'elif' in Python3 === 'else if' in Javascript

# syntax
    # if expression1:
    #    statement(s)
    # elif expression2:
    #    statement(s)
    # elif expression3:
    #    statement(s)
    # else:
    #    statement(s)

var = 100
if var == 200:
   print ("1 - Got a true expression value")
   print (var)
elif var == 150:
   print ("2 - Got a true expression value")
   print (var)
elif var == 100:
   print ("3 - Got a true expression value")
   print (var)
else:
   print ("4 - Got a false expression value")
   print (var)

# Prints   -->   3 - Got a true expression value
#                100