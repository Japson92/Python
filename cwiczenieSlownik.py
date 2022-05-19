dictionary = {}

while(True):
    print("Wellcome!")
    print("Add new definition - Add")
    print("Get existing definition - Get")
    print("Delete existing definition - Del")
    print("Exit program - Exit")


    choice = input("What You want to do? ").capitalize()

    if choice == "Add":
        id = input("Insert new index for definition: ").capitalize()
        definition = input("Insert new definition: ").capitalize()
        dictionary.update({id:definition})
        print("Definition", id, "was added to dictionary")
        
    elif choice == "Get":
        for id in dictionary:
            print(id)
        id = input("Type id of definition You are looking for: ").capitalize()
        print("Your definition is:")
        print(dictionary.get(id))

    elif choice ==  "Del":
        for id in dictionary:
            print(id)
        id = input("Which definition You want to delete?").capitalize()
        print("Definition named", id, "was deleted!")
        dictionary.pop(id)

    elif choice == "Exit":
        print("Good Bye!")
        break
    else:
        print("Something gone wrong")   

