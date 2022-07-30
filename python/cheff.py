a = int(input())

b=[]

for x in range(a):
    b.append(input())
    
   
   
for case in b:
	count=0
	case=case.split()
	while int(case[0])<int(case[1]):
 
            if int(case[2])==1:
                case[1]=int(case[1])//int(case[3])
                count=count+1
            else:
                case[0]=int(case[0])*int(case[2])
                count=count+1
	print(count)                

