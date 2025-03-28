#1) List-ის შექმნა და ელემენტების გამოტანა
#შექმენით სია, რომელიც შეიცავს 5 რიცხვს. შემდეგ გამოიტანეთ პირველი, ბოლო და შუათანაში მყოფი ელემენტები.

numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0])
print("Middle element:", numbers[len(numbers) // 2])
print("Last element:", numbers[-1])

#2) List-ის შეცვლა
#შეასწორეთ შეცდომები რასაც ხედავთ არასწორს ჩაასწორედ აუციელბლად  num = [1, 3, 3, 4, 5, 6, 6, 8, 9, 12]

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
print("Corrected list:", num)

#3) Element-ის დამატება სიის ბოლოს
#შექმენით სია და დაამატეთ მას ახალი ელემენტი (მაგალითად, "apple").


#4) Index-ით წვდომა
#შექმენით სია, რომელშიც არის ცხოველები, შემდეგ გამოიტანეთ ცხოველის ინდექსი (მაგალითად, "dog").

animals = ["cat", "dog", "elephant", "tiger", "lion"]
dog_index = animals.index("dog")
print("Index of 'dog':", dog_index)