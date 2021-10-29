a = float(input('enter no.'))
b = str(a) #for ierating throgh number
c=int(a) #taking only integer part
d=str(c) #iterating through integer part
l = []   #list of separated digits
nu=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'] #list for handaling number

final=[]#list of numbers converted into text

digit=['@','#','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety'] #handaling digit place and hundreed place

for i in b:
    l.append(i) #getting list of each digit in input

n = len(d)

digit_place=int(l[-5]) #getting digit at digit place
thosand_place=int(l[3])#digit at thousand place
decimal=str(l[-2])+str(l[-1]) #digit after decimal point


for i in l:
    if i!='.':
        k=int(i)
    final.append(nu[k]) #converting number to text

if n==1:
    print('Rs {} {}/100 Only'.format(final[0],decimal)) #for one digit number
if n==2:
    print('Rs {} {} {}/100 Only'.format(digit[digit_place],final[0],decimal)) #hadaling two digit no
if n==3:
    print('Rs {} Hundred And {} {} {}/100 Only'.format(final[0],digit[digit_place],final[2],decimal)) #hadaling three digit no
if n==4:
    print('Rs {} Thousand {} Hundred And {} {} {}/100 Only'.format(final[0],final[1],digit[digit_place],final[3],decimal)) #hadaling four digit no
if n==5:
    print('Rs {} {} Thousand {} Hundred And {} {} {}/100 Only'.format(digit[int(l[0])],final[1],final[2],digit[digit_place],final[4],decimal)) #hadaling five digit no
if n==6:
    print('Rs {} Lakh {} {} Thousand {} Hundred And {} {} {}/100 Only'.format(final[0],digit[int(l[1])],final[2],final[3],digit[digit_place], final[5],decimal)) #hadaling six digit no
if n==8:
    print('Rs {} Crore {} {} Lakh {} {} Thousand {} Hundred And {} {} {}/100 Only'.format(final[0],digit[int(l[1])],final[2],digit[int(l[3])],final[4],final[5],digit[int(l[6])],final[7],decimal))#handaling eight digit no