#1) შექმენით ფუნქცია რომელსაც გადასცემთ 2 არგუმენტს და შემდეგ დააბრუნეთ მათი ნამრავლი 
def num(a, b):
    return a * b

print(num(3, 4)) 
#2) შექმენით ფუნქცია რომელსაც არგუმენტად გადასცემთ ცვლადს სადაც შემდეგ შეინახავთ სახელს ფუნქციაში კი მიესალმეთ ამ სახელს 
def greet(name):
    print(f"გამარჯობა, {name}!")

greet("რეზი") 
 

#3) შექმენით ფუნქცია რომელსაც მიანიჭებთ 3 არგუმენტს და გამოიტანეთ მათი ჯამი
def sum_three(a, b, c):
    return a + b + c

print(sum_three(2, 5, 7))  

#4) შექმენით ფუნქცია რომელსაც გადაეცემა 2 არგუმენტი და შემდეგ მათ გაუკეთეთ კონკატენაცია
def concatenate(str1, str2):
    return str1 + str2

print(concatenate("hello", "world!"))  

#5) ახსემით რას აკეთებს replace მეთოდი და გააკეთეთ 2 მაგალითი
#ტექსტში მოიძიებს კონკრეტულ სიტყვას ან ასოს და ცვლის მას სხვა 
# სიტყვით ან ასოთი
text = "მიყვარს ზაფხული"
new_text = text.replace("ზაფხული", "გაზაფხული")
print(new_text)  

#6) კომენტარის სახეით ახსენით რას აკეთებს .upper() and .lower()
#  მეთოდები და თითოზე გააკეთეთ 2-2 მაგალითი 

text = "გამარჯობა"
print(text.upper()) 

text2 = "hello world"
print(text2.upper())  


text3 = "სალამი"
print(text3.lower())  

text4 = "HELLO WORLD"
print(text4.lower())  




#7) კომენტარის სახით ახენით რას აკეთებს find ფუნქცია და გააკეთეთ 2 მაგალითი

text = "მე ვსწავლობ პროგრამირებას"
print(text.find("პროგრამირებას"))  # 10

text2 = "სკოლა არის კარგი"
print(text2.find("სახლი"))  # 13

#8) ახსენით რას აკეთებს capitalize() და გააკეთეთ 2 მაგალითი 
text = "გამარჯობა ყველას"
print(text.capitalize())  

text2 = "HELLO world"
print(text2.capitalize()) 

#9) ახსენით რას აკეთებს swapcase() და ამაზეც შეასრულეთ 2 მაგალითი 
text = "გამარჯობა SAMQARO"
print(text3.swapcase())  # გΑΜΑΡჯΟΒΑ samqaro

text2 = "Hello WORLD"
print(text4.swapcase())  # hELLO world
