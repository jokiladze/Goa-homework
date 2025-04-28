#1) შექმენით ფუნცქიცა რომელსაც გადასცემთ რაღაც სახელს შემდეგ გადაუარეთ ამ სახელს for loop'ით და დააბრუნეთ თითოეული ელემენტი upper ქეისში
def name_to_upper(name):
    for letter in name:
        print(letter.upper())

name_to_upper("rezi")

#2) შემქენით ფუნქცია რომელსაც გადასცემთ რაღაც სიას შემდეგ ამ სიას გადაუარეთ for loop'ით და გამოიტანეთ თითოეული ელემენტი 
def list_elements(my_list):
    for element in my_list:
        print(element)

list_elements(["ვაშლი", "ბანანი", "მსხალი"])