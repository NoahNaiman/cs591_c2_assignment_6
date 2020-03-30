def multiply(x,y):
    #product of x y
    product=x*y
    #list to store the digits of x*y
    list_of_digit= []
    returnstring=""
    #dictionary that maps the digit to its corresponding string
    num_to_string={
        0:"0",
        1:"1",
        2:"2",
        3:"3",
        4:"4",
        5:"5",
        6:"6",
        7:"7",
        8:"8",
        9:"9"
    }
    if(product==0):
        list_of_digit.insert(0,0)
    #getting the digit 
    while (product>0):
        add_digit= product%10
        product=product//10
        list_of_digit.insert(0,add_digit)
    #getting the string value of each digit 
    for digits in list_of_digit:
        
        returnstring+= num_to_string.get(digits)

    
    return returnstring

