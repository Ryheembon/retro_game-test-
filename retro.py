## Beginning of the game ####

# Introduce the player and welcome them
name = input("Hello, type your name: ")
print(f"Hello {name}, welcome to my game!")

### Do you wanna play? ####
should_we_play = input("Do you want to play? (yes/no) ").lower()

if should_we_play == "yes": 
    print("Get ready to play something beyond your wildest dreams!")
    
    # The first decision: Left or Right?
    print("\nYou find yourself standing at a crossroad deep in an ancient forest. The air is thick with mystery.")
    direction = input("Do you want to go left or right? (left/right) ").lower()
    
    if direction == "left": 
        print("\nYou decide to go left. The path seems safe, but the trees grow denser with every step.")
        print("Suddenly, you come across a rickety bridge spanning a deep chasm. It looks old and worn.")
        print("You take a careful step onto the bridge, but halfway across, a loud creak echoes through the air.")
        print("The bridge snaps under your feet, and you plummet into the abyss below.")
        print("\nSadly, you didn’t make it... But there's always another chance. Perhaps another adventurer will come along.")
    
    elif direction == "right": 
        print("\nYou choose to go right, towards the distant peaks of the mysterious mountains.")
        print("As you walk, the air grows colder, and the trees start to thin out. A thick fog begins to settle.")
        print("After hours of Walking, you come upon a hidden cave, its entrance partially obscured by moss and vines.")
        print("Something about this cave calls to you... It could be the answer to the ancient legends of hidden treasure.")

        # The quest for gold begins!
        print("\nInside the cave, the air is damp and cool. You can feel the weight of centuries pressing down on you.")
        print("As you walk deeper, you discover something incredible a weathered parchment pinned to the wall.")
        print("It’s an old map, but it’s not just any map. It’s said to lead to the fabled 'Golden cavern' a treasure hidden away for centuries.")
        
        # Decision to continue the quest or not
        quest_choice = input("Do you want to continue searching for the gold cavern? (yes/no) ").lower()
        
        if quest_choice == "yes":
            print("\nYour heart races with excitement as you unfurl the map. There are strange symbols, and the path is unclear.")
            print("But you know this is a chance of a lifetime. You begin your journey deeper into the cave.")
            print("The walls narrow, and the further you go, the more you hear the sound of distant, rushing water.")
            
            # New obstacle: A magical obstacle!
            print("\nSuddenly, the path splits into two, each direction offering a new challenge.")
            challenge = input("On the left, you hear the sound of rushing water; on the right, a strange glowing mist. Which path do you choose?(left/right) ").lower()
            
            if challenge == "left":
                print("\nYou take the left path, which leads you to a fast-flowing underground river.")
                print("The current is strong, but you spot an old wooden boat tied to a nearby dock.")
                print("Do you try to cross the river, or do you turn back?")
                
                river_choice = input("Do you want to take the boat across? (yes/no) ").lower()
                if river_choice == "yes":
                    print("\nYou decide to take the boat, carefully navigating through the rapid currents.")
                    print("After what seems like an eternity, you reach the other side, soaked but alive.")
                    print("Ahead of you lies the final stretch to the treasure—but the journey isn’t over yet...")
                    
                    # The gold cavern final challenge
                    gold_chance = input("\nYou’ve come across a massive cavern. The walls sparkle faintly. Do you want to go left or right to follow the golden trail? (left/right) ").lower()
                    if gold_chance == "left":
                        print("\nYou follow the shimmering path, your heart racing as the walls gleam with a golden glow.")
                        print("After hours of walking, you find yourself standing before a massive golden cavern, deep within the earth.")
                        print(f"Congratulations, {name}! You’ve struck gold! The treasures of the ancients are now yours!")
                    elif gold_chance == "right":
                        print("\nYou choose the right path and discover a giant chest, its surface encrusted with jewels and ancient runes.")
                        print("With trembling hands, you unlock the chest, revealing an unimaginable fortune—gold coins, precious gems, and rare artifacts!")
                        print(f"Congratulations, {name}! You’ve become richer than you ever imagined!")
                    else:
                        print("\nYou hesitate, unsure of where to go... and before you know it, the ground trembles.")
                        print("A mysterious shadow emerges from the darkness, taking you away into the depths. You’ve met your end. Game over.")
                
                else:
                    print("\nYou decide not to risk the river crossing. As you turn back, the ground beneath your feet shifts.")
                    print("The cave collapses, and you’re trapped in the darkness forever. Game over.")
            
            elif challenge == "right":
                print("\nYou walk into the glowing mist. It’s thick and makes your head spin. Suddenly, a voice echoes in your mind.")
                print("The voice warns you of a terrible curse—only those pure of heart can pass safely.")
                
                purity_check = input("Do you think your heart is pure enough to continue? (yes/no) ").lower()
                if purity_check == "yes":
                    print("\nYou bravely push forward, and the mist begins to clear, revealing a beautiful underground garden.")
                    print("At the center of the garden, there’s a pedestal with an ancient golden artifact—a key to the treasure.")
                    print("With the key in hand, you walk to a hidden door, which leads you to the gold you’ve been searching for!")
                    print(f"Congratulations, {name}! You’ve unlocked the ultimate treasure, and your name will go down in history!")
                else:
                    print("\nThe mist envelops you further, and you feel a heavy weight in your chest.")
                    print("The curse takes hold, and the cave begins to collapse around you. You’ve failed the trial. Game over.")
            else:
                print("\nYou hesitated too long, and the shadows of the cave crept up on you.")
                print("A dark force pulls you deeper into the earth, and your adventure comes to a tragic end. Game over.")
        else:
            print("\nYou decide to turn back. The treasure will have to wait for someone else.")
            print("You leave the cave, but the mystery of the golden cavern will always haunt your dreams.")
            
else:
    print(f"\nMaybe next time, {name}! Thanks for playing!")