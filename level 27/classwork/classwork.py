#1) შექმენით ფუნქცია რომელსაც გადასცემთ 2 არგუმენტს და შემდეგ დააბრუნეთ მათი ნამრავლი 
def multiply(a, b):
    return a * b

#2) შექმენით ფუნქცია რომელსაც არგუმენტად გადასცემთ ცვლადს სადაც შემდეგ შეინახავთ სახელს
#  ფუნქციაში კი მიესალმეთ ამ სახელს 
def greet(name):
    print(f"მოგესალმებით, {name}!")

#3) შექმენით ფუნქცია რომელსაც მიანიჭებთ 3 არგუმენტს და გამოიტანეთ მათი ჯამი
def sum_three(a, b, c):
    return a + b + c

#4) შექმენით ფუნქცია რომელსაც გადაეცემა 2 არგუმენტი და შემდეგ მათ გაუკეთეთ კონკატენაცია
def concatenate(a, b):
    return str(a) + str(b)

# მეორე საკლასო დავალება

#1) შექმენით ფუნქცია რომელსაც გადასცემთ 2 არგუმენტს და შემდეგ დააბრუნეთ მათი ნამრავლი 
def multiply(a, b):
    return a * b

print(multiply(4, 5))  

#2) შექმენით ფუნქცია რომელსაც არგუმენტად გადასცემთ ცვლადს სადაც შემდეგ შეინახავთ სახელს ფუნქციაში კი მიესალმეთ ამ სახელს
def greet(name):
    print(f"გამარჯობა, {name}!")

greet("რეზი") 

#3) შექმენით ფუნქცია რომელსაც მიანიჭებთ 3 არგუმენტს და გამოიტანეთ მათი ჯამი
def sum_three(a, b, c):
    return a + b + c

print(sum_three(2, 4, 6)) 

#4) შექმენით ფუნქცია რომელსაც გადაეცემა 2 არგუმენტი და შემდეგ მათ გაუკეთეთ კონკატენაცია
def concatenate(text1, text2):
    return text1 + text2

print(concatenate("Hello", "World"))  

#5) ახსემით რას აკეთებს replace მეთოდი და გააკეთეთ 2 მაგალითი
text = "hello world"
new_text = text.replace("world", "Python")
print(new_text)  #

#6) კომენტარის სახეით ახსენით რას აკეთებს .upper() and .lower() მეთოდები და თითოზე გააკეთეთ 2-2 მაგალითი 

print("hello".upper())  
print("Python123".upper())  

print("HELLO".lower()) 
print("PyThOn".lower())  

#7) კომენტარის სახით ახენით რას აკეთებს find ფუნქცია და გააკეთეთ 2 მაგალითი

text = "hello world"
print(text.find("world")) 

#8) ახსენით რას აკეთებს capitalize() და გააკეთეთ 2 მაგალითი 
text = "python"
print(text.capitalize())  

#9) ახსენით რას აკეთებს swapcase() და ამაზეც შეასრულეთ 2 მაგალითი 

text = "Python Is Fun"
print(text.swapcase())  
