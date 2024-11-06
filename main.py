playing = True
def check_game():
        if cat_attributes['energy'] <= 0 or cat_attributes["weight"] > 25:
            print ("game over ")
            playing = False
swimming_strength = 0
running_strength = 0


import pyfiglet 
cat_attributes = {
    "intelligence": 2,
    "energy": 20,
    "weight": 10,
    # change the inital values above
}

title = pyfiglet.figlet_format("welcome to my cat game",font = "larry3d")
print (title)

# Take the user inputs for name and colour:
name = input("Enter name:")
colour = input("enter a colour:")
# ...

# start the while loop
starting_screen = input("would you like to play (yes or no)")
if starting_screen.lower() == "y" or "yes":
    playing == True
else:
    playing == False

while  playing == True:
    # Finish the string below
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. show stats")

    if option == '1':
        playing_option1 = [("option 1", "playing with fish toy"),("option 2","feed your cat"),("option 3","sit with cat")]
        print (playing_option1)
        playing_choice = input("select what option you would like to do(1, 2 or 3)")
        if playing_choice == "1":
            print("playing with fish toy for 10 min")
            (cat_attributes["energy"]) - 3
            check_game()
        elif playing_choice =="2":
            print ("fed the cat some treats")
            (cat_attributes["weight"]) + 3
            check_game()
        elif playing_choice == "3":
            print ("sitting with cat")
            (cat_attributes["energy"]) + 3
            check_game()
        else:
            print ("please select an option 1,2,3")
    
    elif option == '2':
        playing_option2 = [("option 1","put cat on a diet"),("option 2","make the cat swim"),("option 3","make the cat run")]
        print (playing_option2)
        playing_choice2 = input("select what option you would like to do(1,2 or 3)")
        if playing_choice2 == "1":
            print ("you put your cat on a diet for a day")
            (cat_attributes["energy"]) -2
            (cat_attributes["weight"]) -4
            check_game()
        elif playing_choice2 == "2":
            print ("your cat went for a swim")
            (cat_attributes["energy"]) - 5
            (cat_attributes["weight"]) - 3
            check_game()
            print ("you achived 1 skill point on swimming")
            swimming_strength = swimming_strength + 1
        elif playing_choice2 == "3":
            print ("your cat went for a run")
            (cat_attributes["energy"]) - 4
            (cat_attributes["weight"]) - 3
            check_game()
            print ("you achived 1 skill point on running")
            running_strength = running_strength + 1
        else:
            print ("please select an option 1,2,3")
    elif option == '3':
        print (cat_attributes)
        print ("your cats swimming strength is level: ", swimming_strength)
        print ("your cats running strength is level: ", running_strength)
    else:
        print ("please select an option 1,2,3")
    
    
    
    
    
    
    
    
    play_agian = input("would you like to play again")
    if play_agian.lower() == "y" or "yes":
        playing == True
    else:
        playing == False


