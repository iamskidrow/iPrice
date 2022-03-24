import models

# Taking model name from users and fixing improper inputs
model = input("\nEnter the model name: ")
choice = model.lstrip().rstrip().lower()

if choice == "iphone 11":
    models.iphone_11()

elif choice == "iphone 11 pro":
    models.iphone_11_pro()

elif choice == "iphone 11 pro max":
    models.iphone_11_pro_max()

elif choice == "iphone 12 mini":
    models.iphone_12_mini()

elif choice == "iphone 12":
    models.iphone_12()

elif choice == "iphone 12 pro":
    models.iphone_12_pro()

elif choice == "iphone 12 pro max":
    models.iphone_12_pro_max()

elif choice == "iphone 13 mini":
    models.iphone_13_mini()

elif choice == "iphone 13":
    models.iphone_13()

elif choice == "iphone 13 pro":
    models.iphone_13_pro()

elif choice == "iphone 13 pro max":
    models.iphone_13_pro_max()

else:
    print("There is no such model")
