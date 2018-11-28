def adding_report(report = 'T'):
    
    items = ''
    total = 0
    
    print('Input an integer to add to the total or "Q" to quit.')
            
    while True:
        
        item = input('Enter an integer or \"Q\": ')
        
        if item.isdigit():
            
            total += int(item)
            
            if report == 'A':
                
                items += item + '\n'
            
            else:
                
                pass
        
        elif item.upper().startswith('Q'):
            
            if report == 'A':
                
                print('[ITEMS]\n' + items)
                print('[TOTAL]\n' + str(total))
                break
            
            else:
                
                print('[TOTAL]\n' + str(total))
                break
                
        else:
            print('Invalid input.')
            

#########################################
########## PROGRAM BEGINS HERE ##########
#########################################

#hash number for headers and ends
hash_num = 75

print(hash_num * '#')

#header
print('Report Types include All Itens (\"A\") or Total Only (\"T\").')

print(hash_num * '#')

while True:
    #input report type
    report_type = input('Choose Report Type (\"A\") or (\"T\"): ')

    if report_type.upper() == 'A':
    
        #call function adding_report(report)
        adding_report(report_type.upper())
        break
    
    elif report_type.upper() == 'T':
    
        #call function adding_report(report)
        adding_report(report_type.upper())
        break

    elif report_type.upper() == 'Q':
    
        break
    
    else:
        
        print('Invalid Report Type. Run again.')

print(hash_num * '#' + '\nQUIT...\n' + hash_num * '#')
