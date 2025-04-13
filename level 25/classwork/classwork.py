#1) List-ის შექმნა და ელემენტების გამოტანა
#შექმენით სია, რომელიც შეიცავს 5 რიცხვს. შემდეგ გამოიტანეთ პირველი, ბოლო და
#  შუათანაში მყოფი ელემენტები.

numbers = [10, 20, 30, 40, 50]

first_element = numbers[0]

last_element = numbers[-1]

middle_element = numbers[len(numbers) // 2]

print("პირველი ელემენტი:", first_element)
print("მეორე ელემენტი:", middle_element)
print("მესამე ელემენტი:", last_element)

#2) List-ის შეცვლა
#შეასწორეთ შეცდომები რასაც ხედავთ არასწორს ჩაასწორედ აუციელბლად  num = [1, 3, 3, 4, 5, 6, 6, 8, 9, 12]
num = [1, 3, 3, 4, 5, 6, 6, 8, 9, 12]

corrected_num = list(dict.fromkeys(num))

print(" სია:", corrected_num)

#3) Element-ის დამატება სიის ბოლოს
#შექმენით სია და დაამატეთ მას ახალი ელემენტი (მაგალითად, "apple").

fruits = ["banana", "orange", "grape"]
fruits.append("apple")
print(" სია:", fruits)

#4) Index-ით წვდომა
#შექმენით სია, რომელშიც არის ცხოველები, შემდეგ გამოიტანეთ ცხოველის ინდექსი (მაგალითად, "dog").

animals = ["cat", "dog", "rabbit", "elephant"]

dog_index = animals.index("dog")

print("dog-ის ინდექსი:", dog_index)
