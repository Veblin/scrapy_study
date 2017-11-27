import re

# string filter
def clearInput(input):
    input = re.sub('\n+',"",input).lower
    input = re.sub('\[[0-9]*\]',"",input)
    input = re.sub(' +',"",input)
    input = bytes(input , "UTF-8")
    input = input.decode('ascii','ignore')
    clearInput = []
    input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower( == 'a' or item.lower() == 'i'):
            clearInput.append(item)
        
    return clearInput