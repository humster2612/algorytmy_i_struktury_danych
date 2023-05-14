def kod(symbStr):
    s = Stack()
    
    balanced = True
    ind = 0
    while ind < len(symbStr) and balanced:
        
        symbol = symbStr[ind]
        if symbol in '({[<':
            s.push(symbol)
        else:
            
            if s.isEmpty():
                balanced = False
            else:
                
                s.pop()
        ind += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False
