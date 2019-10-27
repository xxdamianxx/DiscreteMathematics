def insert(element, sorted):

    if len(sorted) == 0:   
        return [element]    
    else:                   
        if sorted[0] >= element:  
            new_copy = sorted[:]    
            new_copy.insert(0, element) 
            return new_copy            
        else:
            return [sorted[0]] + insert(element, sorted[1:])

def sort(list):
    
    if len(list) == 1:  
        return list
    else:
        head = list[0]  
        tail = list[1:]
        
        temp = sort(tail)   
                           
        return insert(head, temp)