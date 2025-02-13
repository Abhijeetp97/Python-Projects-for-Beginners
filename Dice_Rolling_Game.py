import random

def roll_dice(dice_num):
    rolls = [random.randint(1, 6) for _ in range(dice_num)]
    return rolls

def main():
    roll_count = 0

    while True:
        roll = input("Roll the dice? (y/n): ").lower()
        if roll == 'y':
            dice_num = int(input("How many dice would you like to roll? : "))
            rolls = roll_dice(dice_num)
            roll_count += 1
            print(f"You rolled:{','.join(map(str, rolls))}")
            print(f"Total rolls so far: {roll_count}")
        
        elif roll == 'n':
            print("Thank you for playing!")
            print(f"You rolled the dice {roll_count} times during this session.")
            break

        else:
            print("Invalid input! Please enter 'y' or 'n'.")

if __name__ == '__main__':
    main()