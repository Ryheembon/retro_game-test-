## Beginning of the Game ####

# Introduce the player and welcome them
name = input("Greetings, adventurer. What is your name? ")
print(f"Welcome, {name}, to a tale of mystery, danger, and destiny. Your choices will shape your fate.")

### Do you want to play? ####
should_we_play = input("Do you dare to embark on this journey? (yes/no) ").lower()

if should_we_play == "yes":
    print("\nThe winds howl, and the earth trembles. Your journey begins now. Brace yourself, adventurer!")

    # Initial setting and choice
    print("\nYou awaken in a clearing surrounded by towering trees. The forest whispers secrets as if alive.")
    print("In front of you is a crumbling stone path, with two routes diverging.")
    print("To the left lies a glowing, ethereal forest, its trees glimmering with light. To the right, a rocky, stormy canyon stretches into darkness.")
    direction = input("Do you choose the glowing forest or the stormy canyon? (forest/canyon) ").lower()

    if direction == "forest":
        print("\nYou step into the glowing forest, and the air becomes thick with magic.")
        print("You soon encounter a beautiful stag with golden antlers, who watches you curiously.")
        print("The stag speaks, offering you guidance but requiring payment.")
        payment = input("Do you offer the stag a lock of your hair or a coin from your pocket? (hair/coin) ").lower()

        if payment == "hair":
            print("\nThe stag nods and consumes the lock of your hair, granting you insight into the forest.")
            print("You are shown visions of a hidden path leading to an ancient ruin filled with untold treasures.")
            print("But along the way, you encounter a riddle-bearing sprite who blocks your path.")
            riddle_answer = input("The sprite asks: 'I am not alive, yet I grow. I do not have lungs, but I need air. What am I?' ").lower()
            
            if riddle_answer == "fire":
                print("\nThe sprite claps its tiny hands in delight and grants you passage.")
                print("You find the ruin and claim a magical staff that hums with ancient power. Your journey has only begun!")
            else:
                print("\nThe sprite shakes its head and vanishes. The forest shifts, and you lose your way.")
                print("You wander aimlessly until you are back where you started. Game over.")

        elif payment == "coin":
            print("\nThe stag takes the coin and tells you of a dark entity stalking the forest.")
            print("As you journey further, you come across a shimmering pool and must choose:")
            pool_choice = input("Do you drink from the pool or continue on your path? (drink/continue) ").lower()

            if pool_choice == "drink":
                print("\nThe water grants you visions of the future, but you feel a strange presence looming over you.")
                print("You are confronted by the dark entity—a towering shadow with glowing red eyes.")
                print("You must decide to fight or flee.")
                fight_or_flee = input("Do you fight the entity or flee into the woods? (fight/flee) ").lower()

                if fight_or_flee == "fight":
                    print("\nYou stand your ground, using your wits and strength to outsmart the shadow.")
                    print("After a fierce battle, you drive it away and discover a hidden amulet within the pool.")
                    print(f"Congratulations, {name}! You have conquered the darkness and gained a powerful artifact!")
                else:
                    print("\nYou flee into the woods, but the entity pursues you relentlessly.")
                    print("Eventually, you grow tired, and the darkness consumes you. Game over.")
            else:
                print("\nYou ignore the pool and continue on your way.")
                print("Soon, you come upon a forgotten temple guarded by sentient vines.")
                print("You struggle against the vines but are captured, your fate unknown. Game over.")

    elif direction == "canyon":
        print("\nYou venture into the stormy canyon, where lightning cracks across the sky.")
        print("The path is treacherous, but you find a wooden bridge spanning a deep chasm.")
        print("On the other side of the bridge, a hooded figure waits, holding a lantern.")
        bridge_choice = input("Do you cross the bridge or take another path down the canyon? (bridge/path) ").lower()

        if bridge_choice == "bridge":
            print("\nAs you cross the bridge, the hooded figure calls out to you.")
            print("They offer to share their knowledge in exchange for something you value.")
            sacrifice = input("Do you offer your weapon, your memory of home, or refuse? (weapon/memory/refuse) ").lower()

            if sacrifice == "weapon":
                print("\nThe figure takes your weapon and enchants it, returning it stronger than ever.")
                print("You continue your journey, now armed with a blade that can cut through any obstacle.")
                print("Deeper in the canyon, you uncover a hidden cave filled with ancient artifacts.")
                print(f"Congratulations, {name}! You have gained immense power and found a treasure trove!")
            elif sacrifice == "memory":
                print("\nThe figure takes your memory of home, leaving you with a strange emptiness.")
                print("But this emptiness allows you to resist the illusions of the canyon.")
                print("You find a powerful relic guarded by a spectral guardian, whom you defeat with your willpower.")
                print(f"Well done, {name}! You have overcome great challenges and claimed a legendary relic!")
            else:
                print("\nYou refuse the figure's offer, and they vanish into the storm.")
                print("The bridge collapses behind you, and you are left stranded in the canyon. Game over.")

        elif bridge_choice == "path":
            print("\nYou take a narrow path winding down the canyon, avoiding the bridge.")
            print("The storm intensifies, and you find shelter in a cave, but it is inhabited by a sleeping dragon.")
            dragon_choice = input("Do you attempt to sneak past the dragon or wake it to ask for help? (sneak/wake) ").lower()

            if dragon_choice == "sneak":
                print("\nYou carefully sneak past the dragon, finding a hidden passage leading to a treasure hoard.")
                print(f"Congratulations, {name}! You have escaped danger and claimed the dragon's gold!")
            elif dragon_choice == "wake":
                print("\nThe dragon awakens, its fiery eyes glaring at you.")
                print("To your surprise, it does not attack but offers you a choice: wisdom or wealth.")
                dragon_reward = input("Do you choose wisdom or wealth? (wisdom/wealth) ").lower()

                if dragon_reward == "wisdom":
                    print("\nThe dragon grants you ancient knowledge, revealing the secrets of the world.")
                    print(f"Congratulations, {name}! You have gained wisdom beyond measure and become a legend!")
                else:
                    print("\nThe dragon gives you mountains of gold but warns that greed carries a price.")
                    print("As you leave the cave, the gold vanishes, leaving you with nothing. Game over.")
            else:
                print("\nYou hesitate, and the dragon awakens in anger.")
                print("With a single fiery breath, your journey ends. Game over.")

    else:
        print("\nYou hesitate at the crossroads, unsure of which path to take.")
        print("The ground beneath you crumbles, and you fall into darkness. Game over.")

else:
    print(f"\nAnother time, perhaps, {name}. The adventure will await your return. Farewell!")
