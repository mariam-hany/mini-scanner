arr = []
out_arr1 = []
out_arr_identifier = []
out_arr_number = []
out_arr_reserved = []
out_arr_operator = []
out_arr_assign = []
out_arr_left_bracket= []
out_arr_right_bracket = []
out_arr2 = []
input_string = open("input.txt", "r")
arr = input_string.readlines()
input_string.close()
print(arr)
count =0
count1=0
x2=-2
out_arr = []
for i in arr :
###########################
    x=-1
    x1=-1
    x2=-1
    x3=-1
    flag =2
############################read
    if arr[count].find('read') >= 0:
        out_arr.append("read")
        y = arr[count][(arr[count].find(' ')+1 ): (arr[count].find(';') )]
        out_arr.append(y)
############################ write
    if arr[count].find('write')>=0 :
        out_arr.append("write")
        y = arr[count][(arr[count].find(' ')+1 ): (arr[count].find(';') )]
        out_arr.append(y)
#####################################################

#####################################################
    if arr[count].find('<') >= 0:
           x = arr[count].find('<')
    if arr[count].find('>') >= 0:
           x = arr[count].find('>')
    if arr[count].find('=') >= 0:
           x = arr[count].find('=')
    if arr[count].find(':=') >= 0:
           x2 = arr[count].find(':=')

###########################if else  elseif end until then
   # out_arr.append(count)
    if arr[count].find('if else') >= 0:
       out_arr.append("if else")
       #out_arr.append(count)
       flag = -1
    if arr[count].find('if') >= 0 and flag > 0  :
       flag=-1
       out_arr.append("if")
       if (x2 >= 0 or x >= 0) :
           if x2 < 0:
               c = 0
               x2 = x
           else:
               c = 1
       y = arr[count][(arr[count].find(' ') +1):( x2)]
       out_arr.append(y)
       out_arr.append(arr[count][x2:x2+1+c])
       out_arr.append(arr[count][x2+c+1: (arr[count].find('then') )])
       #
    if arr[count].find('else') >= 0 and (flag > 0):
       out_arr.append("else")

    if arr[count].find('then') >= 0:
       out_arr.append("then")
    if arr[count].find('until') >= 0:
       flag = -1
       out_arr.append("until")
       y = arr[count][(arr[count].find(' ')+1 ): x-1]
       out_arr.append(y)
       out_arr.append(arr[count][x])
       out_arr.append(arr[count][x+1: (arr[count].find('\n') )])

    if arr[count].find('end') >= 0:
       out_arr.append("end")
##################################################
    if arr[count].find('+') >= 0:
        x1 = arr[count].find('+')
    if arr[count].find('-') >= 0:
        x1 = arr[count].find('-')
    if arr[count].find('*') >= 0:
        x1 = arr[count].find('*')
    if arr[count].find('/') >= 0:
        x1 = arr[count].find('/')

##################################################
    if (x2>= 0 or x>=0) and flag>0:
        if  x2<0 :
            c=0
            x2 = x
        else :
            c=1

        y = arr[count][:x2]
        out_arr.append(y)
        out_arr.append(arr[count][x2:x2+1+c])
        if x1 >= 0:
            y = arr[count][x2+c+1: x1]
            out_arr.append(y)
            out_arr.append(arr[count][x1])
            out_arr.append(arr[count][x1 + 1: (arr[count].find(';'))])
        else :
            out_arr.append(arr[count][x2+c+1 : (arr[count].find(';'))])
##################################################

##################################################
    count = count + 1
print("out_arr")
print(out_arr)
##################################################
count3=0
####################


##############
for i1 in out_arr :

    out_arr[count3] = out_arr[count3].strip()
    if out_arr[count3] == 'read'or out_arr[count3] == 'write'or out_arr[count3] == 'if'or out_arr[count3] == 'else'or out_arr[count3] == 'if else' or out_arr[count3] == 'end'or out_arr[count3] == 'until' or  out_arr[count3] == 'then':
        out_arr1.append(out_arr[count3] +",reserved words")
        if not  out_arr[count3] in out_arr_reserved :
              out_arr_reserved.append( out_arr[count3])
    elif out_arr[count3].isdigit():
        out_arr1.append(out_arr[count3] + ",number")
        if not out_arr[count3] in out_arr_number  :
            out_arr_number.append(out_arr[count3])
    elif out_arr[count3].isalnum():
        out_arr1.append(out_arr[count3] + ",identifier")
        if not out_arr[count3] in out_arr_identifier:
            out_arr_identifier.append(out_arr[count3])
    if out_arr[count3]=='>'or out_arr[count3]=='<'or out_arr[count3]=='+'or out_arr[count3]=='-'or out_arr[count3]=='/'or out_arr[count3]=='*':
        out_arr1.append(out_arr[count3] + ",special symbols")
        if not out_arr[count3] in out_arr_operator:
            out_arr_operator.append(out_arr[count3])
        ###################################
    if out_arr[count3].find('[') >= 0:
            out_arr1.append( out_arr[count3][:out_arr[count3].find('[')]+",identifier")
            out_arr1.append( '['+",left bracket")
            out_arr_left_bracket.append('[')
            out_arr1.append(out_arr[count3][out_arr[count3].find('[')+1: out_arr[count3].find(']')]+",identifier")
            if not out_arr[count3] in out_arr_identifier:
                out_arr_identifier.append(out_arr[count3][out_arr[count3].find('[')+1: out_arr[count3].find(']')])
            out_arr1.append(']'+",right bracket")
            out_arr_right_bracket.append(']')

##################################################
    if  out_arr[count3]=='=' or  out_arr[count3]==':=':
        out_arr1.append(out_arr[count3] + ",assign")
        if not out_arr[count3] in out_arr_assign:
            out_arr_assign.append(out_arr[count3])
   # print(out_arr[count3])

    count3 += 1
print(out_arr1)

################################################### output format 2
if out_arr_reserved:
    for i in out_arr_reserved :
        out_arr2.append(i +",")
    out_arr2.append("reserved words\n")

if out_arr_identifier:
    for i in out_arr_identifier :
        out_arr2.append(i +"," )
    out_arr2.append("identifier\n")

if out_arr_left_bracket:
    for i in out_arr_left_bracket :
        out_arr2.append(i +"," )
    out_arr2.append("left bracket\n")

if out_arr_number:
    for i in out_arr_number :
        out_arr2.append(i +",")
    out_arr2.append("number\n")

if out_arr_right_bracket:
    for i in out_arr_right_bracket :
        out_arr2.append(i +"," )
    out_arr2.append("right bracket\n")

if out_arr_operator:
    for i in out_arr_operator:
        out_arr2.append(i +"," )
    out_arr2.append("special symbols\n")
if out_arr_assign:
    for i in out_arr_assign:
        if i == '=' :
            out_arr2.append(i +"," )
            out_arr2.append("equal\n")
        else :
            out_arr2.append(i + ",")
            out_arr2.append("assign\n")




print(out_arr2)
################################################## for i in out_arr2: for format 2
################################################## for i in out_arr1: for format 1
output_string = open("output.txt", "w")
for i in out_arr2:
    output_string.write(i)

output_string.close()
#print(output_string)

