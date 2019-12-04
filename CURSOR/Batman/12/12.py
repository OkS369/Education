def getInput():
    text = input('\nВведіть щось\n')
    return text
    
def testInput(text):
    try:
        result = int(text)
        return True
    except ValueError:
        print('Підказка - введіть ціле число...')
        return False
        
def strToInt(text):
    result = int(text)
    return result
	    
def printInt(number):
    print(number)
		
		
while (True):
    text = getInput()
    if testInput(text) == True:
            printInt(strToInt(text))
