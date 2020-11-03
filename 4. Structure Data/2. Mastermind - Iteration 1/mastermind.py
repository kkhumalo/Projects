import random

def run_game():
    code = [0,0,0,0]
    for i in range(4):
        num = random.randint(1, 8)
        while num in code:
            num = random.randint(1, 8)     
        code[i] = num

    #print(code)        
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    right = False
    turns = 0
    while not right and turns < 12:
        user_input = ""
        
        user_input = input("Input 4 digit code: ")
        if len(user_input) < 4 or len(user_input) > 4:
            print("Please enter exactly 4 digits.")
            continue
        correct_digits_and_position = 0
        correct_digits_only = 0
        for i in range(len(user_input)):
            if code[i] == int(user_input[i]):
                correct_digits_and_position += 1
            elif int(user_input[i]) in code:
                correct_digits_only += 1

        print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
        print('Number of correct digits not in correct place: '+str(correct_digits_only))
        turns += 1

        if correct_digits_and_position == 4:
            right = True
            print('Congratulations! You are a codebreaker!')
        else:
            print('Turns left: '+str(12 - turns))

    print('The code was: ', end="")
    for i in range(4):
        print(str(code[i]), end = "")
           

if __name__ == "__main__":
    run_game()