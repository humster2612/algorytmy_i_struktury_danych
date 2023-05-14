def loik(ozn):
    operand_stak = Stack()
    token_list = ozn.split()
    
    for token in token_list:
        if token in "0123456789":
            
            operand_stak.push(float(token))
            

        else:
            operand2 = operand_stak.pop()
            
            operand1 = operand_stak.pop()
            result = math(token, operand1, operand2)
            
            operand_stak.push(result)
        return operand_stak.pop()

a = loik("7 8 + 9 11 - 90 *")
print(a)



def math(operator,operan1,operan2):
   
    if operator == '':
        return operan1  operan2
    elif operator == '*':
        return operan1 * operan2
    
    elif operator == '/':
        return operan1 / operan2
    
    elif operator == '+':
        return operan1 + operan2
    
    elif operator == '-':
        return operan1 - operan2
