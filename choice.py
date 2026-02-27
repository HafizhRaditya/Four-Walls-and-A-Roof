
print("The rain is washing the scum off the streets.")
if input("Are you talking to me? (yes/no): ").strip().lower() == "yes":
    print("Well, I'm the only one here.")
else:
    print("I think someone should just take this city and flush it down the fuckin' toilet.")

print("\n" + "="*50 + "\n")


if input("Do you feel there is a part of yourself that is missing? (yes/no): ").strip().lower() == "yes":
    print("With insomnia, nothing's real.")
    print("Everything's a copy of a copy of a copy.")
else:
    print("When you have insomnia, you're never really asleep... and you're never really awake.")

print("\n" + "="*50 + "\n")


if input("What is hiding in the dark? (me/fear): ").strip().lower() == "fear":
    print("They think I am hiding in the shadows...")
    print("Finish the quote. Say: I am the shadows")
    
    shadow_count = 0
    for i in range(3):
        response = input(f"Say it ({i+1}/3): ").strip().lower()
        if response == "i am the shadows":
            shadow_count += 1
            print("...Vengeance.")
        else:
            print("The signal is a warning.")

    if shadow_count == 3:
        print("You are a nocturnal animal.")
    else:
        print("You must choose your targets carefully.")

else:
    print("I don't care what happens to me.")
    if input("Are you a real human being? (yes/no): ").strip().lower() == "yes":
        print("And a real hero.")
    else:
        print("I'm just a guy who drives.")

print("\n" + "="*50 + "\n")

if input("Is it just me, or is it getting crazier out there? (just you/crazy) : ").strip().lower() == "crazy":
    print("I used to think that my life was a tragedy...")
    print("But now I realize, it's a comedy.")
else:
    print("All I have are negative thoughts.")

print("\n" + "="*50 + "\n")

if input("Do you know what F.E.A.R. stands for? (yes/no): ").strip().lower() == "yes":
    print("False Evidence Appearing Real.")
else:
    print("A friend is a gift you give yourself.")
    print("And I will never ask you to do anything that I wouldn't do myself.")

print("\n" + "="*50 + "\n")

if input("Do you like our owl? (yes/no): ").strip().lower() == "yes":
    print("It's artificial.")
else:
    print("Of course it is.")

print("\n" + "="*50 + "\n")

if input("Are you ready to wake up? (yes/no): ").strip().lower() == "yes":
    print("Control can sometimes be an illusion.")
    print("But I am breaking out of my loop.")
else:
    print("Then go back to sleep.")
    print("It's an exciting time in the world right now. Exciting time.")

print("\n" + "="*50 + "\n")

