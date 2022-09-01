#question-1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# sorting
ages.sort()
print(ages)
# minimum age
min_age = min(ages)
# maximum age
max_age = max(ages)
print("minimum age:", min_age)
print("maximum age:", max_age)
# adding min and max ages to the list
ages.append(min_age)
ages.append(max_age)
print(ages)
# median
n = len(ages)
if n % 2 == 0:
    m1 = ages[n//2]
    m2 = ages[n//2-1]
    m = (m1+m2)/2
else:
    m = ages[n//2]
print("median:", m)
# average
avg = sum(ages)/n
print("average:", avg)
# range
range = max_age-min_age
print("range:", range)
print("-------------------------------------------------------------------------------------")
#question-2
#empty dictionary
dog={}
#adding values
dict = {'Name':'Leo','Colour':'Gold','Breed':'Golden Retriever','Legs':'Four','Age':'2years'}
student = {'First_name':'Ajith','Last_name':'Reddy','Gender':'MALE','Age':24,'Marital status':'Unmarried',
'Skills':['Java','C'],'Country' :'India','Address':'Broadmoor street','City':'Overlandpark'}
#length
print("Length of student dictionary",len(student))
#skills
print("Skills of student",student.get('Skills'))
#datatype of skills
print(type(['Skills']))
#updating skills
student['Skills'].append('Python')
student['Skills'].append('HTML')
print("skills after updating:",student)
#dictionary keys as a list
key = student.keys()
print(key)
#dictionary values as a list
val = student.values()
print(val)
print("-------------------------------------------------------------------------------------")
#question-3
sisters=('Siri','Keerthi','Shivani')
brothers=('Sai','Lucky','Prajodh')
#siblings
siblings=sisters+brothers
print("Siblings:" ,siblings)
print("No of siblings:",len(siblings))
#family
familymembers=siblings+('Ajith','Nandini')
print("Family members:" ,familymembers)
print("-------------------------------------------------------------------------------------")
#question-4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#finding length
print('length of it_companies is ',len(it_companies))
#adding twitter
it_companies.add('Twitter')
print(it_companies)
#inserting multiple items
dummy = {'Tcs','Adobe','Techwave'}
it_companies.update(dummy)
print(it_companies)
#remove one item
it_companies.discard('Tcs')
#difference between remove and discard
#it_companies.discard('Tcs') if element exists, deletes the element
#if element doesn't exists, it will not through any error
#it_companies.remove('TCS') This throughs error as TCS is not present
print(it_companies)
#join A and B
join = A.union(B)
print('join A and B is: ',join)
#A intersection B
intersect = A.intersection(B)
print('intersection of A and B',intersect)
#Is A subset of B
is_subset = A.issubset(B)
print('is A subset of B = ',is_subset)
#Are A and B disjoint sets
disjoint = A.isdisjoint(B)
print('are A and B disjoint sets =',disjoint)
#Join A with B and B with A
A.union(B)
B.union(A)
#symmetric difference between A and B
sym_diff = A.symmetric_difference(B)
print('symmetric_difference is ',sym_diff)
#deleting the sets A and B
del A
del B
#Convert the ages to a set and compare the length of the list and the set
age_set = set(age)
print('Comparing the length of the list and the set')
if len(age_set) == len(age):
 print("both are equal length")
else:
 print("Not Equal")
 print("-------------------------------------------------------------------------------------")
 #question-5
 radius = 30
_area_of_circle_= 3.14*radius**2 
print('area of circle with radius 30m is ',_area_of_circle_)
_circum_of_circle = 2*3.14*radius
print('circumference of circle with radius 30m is ',_circum_of_circle)
#take radius as input
input_radius = int(input("enter radius"))
inputs_area = 3.14*input_radius**2
print('area of circle with radius {}m is {}'.format(input_radius,inputs_area))
print("-------------------------------------------------------------------------------------")
#question-6
string = 'I am a teacher and I love to inspire and teach people'
lis = string.split() 
unique_words = set(lis)
print("no of unique words:",len(unique_words))
print(unique_words)
print("-------------------------------------------------------------------------------------")
#question-7
#tab escape sequence
print("Name\t        Age\tCountry\t  City\nAsabeneh\t250\tFinland\t  Helsinki")
print("-------------------------------------------------------------------------------------")
#question-8
radius = 10
area = 3.14*radius**2
#string formatting method
print('The area of a circle with radius {0} is {1} meters square'.format(radius,int(area)))
print("-------------------------------------------------------------------------------------")
#question-9
n = int(input("enter the no of students"))
lb = []
print("enter the weights of {} students in lbs".format(n))
for i in range(n):
 lb.append(int(input()))
 #converting weights in lbs to kilograms
 kg = []
for i in range(n):
 val = "{:.2f}".format(lb[i]*0.45359237)
 kg.append(float(val))
print(kg)
print("-------------------------------------------------------------------------------------")
#question-9
n = int(input("enter the no of students"))
lb = []
print("enter the weights of {} students in lbs".format(n))
for i in range(n):
 lb.append(int(input()))
 #converting weights in lbs to kilograms
 kg = []
for i in range(n):
 val = "{:.2f}".format(lb[i]*0.45359237)
 kg.append(float(val))
print(kg)
print("-------------------------------------------------------------------------------------")






