# [ ] create, call and test the str_analysis() function  
# then PASTE THIS CODE into edX

def str_analysis(string):
    
    if string.isdigit():

        string = int(string)
        
        if string > 99:
            
            return str(string) + ' is pretty big number.'
        
        else:
            
            return str(string) + ' is a smaller number than expected.'

    elif string.isalpha():
        
        return '\"' + string + '\" ' + 'is alphabetical characters.'
    
    else:
        
        return '\"' + string + '\" ' + 'is a surprise! It\'s neither all alpha nor all digit characters.'

#########################################
########## PROGRAM BEGINS HERE ##########
#########################################

str_input = ''

while str_input == '':
    
    str_input = input('Enter word or integer: ')

print(str_analysis(str_input))
