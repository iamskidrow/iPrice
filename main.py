import models

# Taking model name from users and fixing improper inputs
model = input("\nEnter the model name: ")
choice = model.lstrip().rstrip().lower()

if choice == "iphone 13":
    models.iphone_13()
    print("")

elif choice == "iphone 14 pro":
    print("Iphone 14 pro")

else:
    print("There is no such model")
