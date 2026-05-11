class food_item:
    def __init__(self, name, calories, protein, carbohydrates, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat
def total_consumption(food):
    total_calories = 0
    total_protein = 0
    total_carbohydrates = 0
    total_fat = 0
    for i in food:
       total_calories+= i.calories
       total_protein+= i.protein
       total_carbohydrates+= i.carbohydrates
       total_fat+= i.fat
    print(f"Total consumption: {total_calories} calories, {total_protein}g protein, {total_carbohydrates}g carbohydrates, {total_fat}g fat")
    if total_calories > 2500:
        print("Warning: calorie intake is more than 2500.")
    if total_fat > 90:
        print("Warning: fat intake is more than 90 g.")

print(f'Example: apple = food_item("apple", 60, 0.3, 15, 0.5), bread = food_item("bread", 80, 3, 15, 1)')
apple = food_item("apple", 60, 0.3, 15, 0.5)
bread = food_item("bread", 80, 3, 15, 1)
food_example = [apple, bread]
total_consumption(food_example)

print("Enter the food consumption details, if there is no more food, type 'done'")
food=[]
while True:
    name = input("Enter the name of food item: ")
    if name == 'done':
        break
    calories = float(input(f"Enter the calories for {name}: "))
    protein = float(input(f"Enter the protein content for {name} (in grams): "))
    carbohydrates = float(input(f"Enter the carbohydrates content for {name} (in grams): "))
    fat = float(input(f"Enter the fat content for {name} (in grams): "))  
    item = food_item(name, calories, protein, carbohydrates, fat)
    food.append(item)
total_consumption(food)



