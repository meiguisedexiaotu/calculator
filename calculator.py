def cal():
    number1 = float(raw_input())
    i = raw_input()
    number2 = float(raw_input())
    if i == '+':
       print "result: ",number1+number2
    elif i == '-':
           print "result: ",number1-number2
    elif i == '/':
           print "result: ",number1/number2
    elif i == '*': 
           print "result: ",number1*number2
    elif i == '**': 
           print "result: ",number1**number2
    else:
           print "NO"		

if__name__ == '__main__':
   while True:
       cal()       