# create a function that returns a dictionary containing all the Unicode characters from 40 to 200.  For example, returnASCdictionary(min=40, max=200) would return { 40: "(", 41: ")", ... , 199: 'Ç', 200: 'È' }

def returnASCdictionary(min=40, max=40):
    dict = {}
    for i in range(150,201):
        dict[i] = chr(i)
    print(dict)
    return dict
returnASCdictionary()

# create a function that returns the upper case version of the string it received.  For example upCase("hello joe") should return "HELLO JOE".  Accomplish this without using python's built-in upper() but simply by using ord() and/or chr().

