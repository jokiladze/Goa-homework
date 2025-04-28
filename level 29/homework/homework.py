#1) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს სიას შემდეგ კი ამ სიიდან დააბრუნედ მხოლოდ კენტი რიცხვების ჯამი
def sum_of_odds(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total

print(sum_of_odds([1, 2, 3, 4, 5]))  

#2) შექმენით ფუნქცია რომელიც მიიღებს სახელებით სავსე სიას შემდეგ კი დააბრუნეთ ყველა ის სახელი რომელიც შედგება მხოლოდ 4 ასოსგან
def names_with_four_letters(names):
    result = []
    for name in names:
        if len(name) == 4:
            result.append(name)
    return result


print(names_with_four_letters(["rezi", "luka", "giorgi", "giga"]))  # ['niko', 'luka']

#3) შექმენით ფუნქცია რომელიც მიიღებს რიცხვებით სავსე სიას შემდეგ კი გამოიტანეთ ისეთი რიცხვები რომლებიც იყოფა 3'ზეც და 5'ზეც
def divisible_by_3_and_5(numbers):
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            print(num)


divisible_by_3_and_5([15, 30, 10, 9, 45, 22])  


#4) ახსენით როგორ გამოიყენება f'სტრინგი
#როცა ტექსტში გვინდა ცვლადები ჩავამატოთ პირდაპირ, ვიყენებთ f"..." სინტაქსს.
name = "rezi"
age = 18
print(f"მე ვარ {name} და ჩემი ასაკია {age}")

#5) კიდევ ერთხე უყურეთ ჩანაწერს 
