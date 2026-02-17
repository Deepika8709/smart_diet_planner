import pandas as pd
df = pd.read_csv("diet_foods.csv")
print("\n welcome to diet planner \n")
print("choose your goal:")
print("1.Weight Loss")
print("2.Muscle Gain")
choice = input ("Enter your choice: ")
df.columns = df.columns.str.strip()
for col in ["Protein", "Calories", "Carbs", "Fiber", "Fat"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
if choice == '1':
    print("\n --- Weight Loss food(High protein, Low calories--- \n")
    #result = df[(df["Protein"] > 10) & (df["Calories"] < 200)]
    result = df[(df["Protein"]> 10)& (df["Calories"] < 200)]
elif choice == '2':
    print ("\n --Muscle gain foods(High Protein---\n")
    result = df[(df["Protein"] > 15)]
else:
    print("\n Invalid choice entered. Please try again.\n")
    exit()
print(result[["Food","Protein","Calories"]])
print("\n --- Plan generated successfully")
