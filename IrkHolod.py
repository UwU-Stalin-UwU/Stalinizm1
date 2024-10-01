input_data = open('input.txt', 'r')
a=input_data.readline()
a=int(a)
sum=0
while a!=0 :
    sum=sum+a
    a=a-1
output_data=open('output.txt', 'w')
output_data.write(str(sum))
input_data.close()
output_data.close()