import random
import hang_word
from hang_art import stages,logo
# from hang_art import logo
# word_list = ["aardvark", "baboon", "camel"]

print(logo)

chosen = random.choice(hang_word.word_list)
word_len = len(chosen)
end_of = False
lives=6

display = []
for letter in range(word_len):
    display += "_"
print(display)

while not end_of:
    guess = input("Guess a letter:").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_len):
        letter = chosen[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen:
        print(f"You guessd {guess}, that's not in the word.\n You loose a life")
        lives-=1
        if lives==0:
            end_of=True
            print("You loose")

    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of = True
        print("You Won")
    
    print(stages[lives])
