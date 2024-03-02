import tkinter as tk 
from tkinter import messagebox
import time
import random


class Door1Challenge:
    def __init__(self, master, game_instance):
        self.master = master
        self.master.title("Door 1 Challenge")
        self.master.geometry("400x300")

        self.game_instance = game_instance
        self.target_sorted_array = None

        random_array = random.sample(range(1, 11), 5)
        self.intro_text = f"You see an array of integers on the wall.\n" \
                          f"Your task is to arrange the elements in ascending order. Can you do it?\n" \
                          f"Enter the sorted array for the following list: {random_array}"
        self.label = tk.Label(self.master, text=self.intro_text)
        self.label.pack(pady=10)

        self.answer_entry = tk.Entry(self.master)
        self.answer_entry.pack(pady=10)

        self.target_sorted_array = sorted(random_array)  # Store target_sorted_array here

        self.button = tk.Button(self.master, text="Submit Answer", command=self.check_answer)
        self.button.pack(pady=10)

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        try:
            user_sorted_array = [int(num) for num in user_answer.split(",")]
            if user_sorted_array == self.target_sorted_array:
                self.game_instance.challenge_text.delete(1.0, tk.END)
                self.game_instance.challenge_text.insert(tk.END, "Congratulations! You've successfully arranged the elements.")
                self.game_instance.ask_next_door()
                self.master.destroy()
            else:
                self.game_instance.challenge_text.delete(1.0, tk.END)
                self.game_instance.challenge_text.insert(tk.END, "Oops! That's not the correct arrangement. Try again.")
        except ValueError:
            self.game_instance.challenge_text.delete(1.0, tk.END)
            self.game_instance.challenge_text.insert(tk.END, "Please enter a valid list of integers separated by commas.")

class Door2Challenge:
    def __init__(self, master, game_instance):
        self.master = master
        self.master.title("Door 2 Challenge")
        self.master.geometry("800x500")

        self.game_instance = game_instance

        self.label = tk.Label(self.master, text="Guess the book.")
        self.label.pack(pady=20)

        self.display_guessing_book_challenge()

    def mysterious_old_man_challenge_logic(self):
        magical_books = [
            "Celestial", "Chronicle", "Eclipse", "Enigma", "Frostbite",
            "Illusion", "Mystify", "Sorcerer", "Whisper",
        ]

        selected_book = random.choice(magical_books)

        correct_position = magical_books.index(selected_book) + 1

        shuffled_books = list(magical_books)
        random.shuffle(shuffled_books)

        return selected_book, correct_position, shuffled_books

    def display_guessing_book_challenge(self):
        selected_book, correct_position, shuffled_books = self.mysterious_old_man_challenge_logic()

        ordinal_suffix = "th"

        if 11 <= correct_position <= 13:
            ordinal_suffix = "th"
        else:
            last_digit = correct_position % 10
            if last_digit == 1:
                ordinal_suffix = "st"
            elif last_digit == 2:
                ordinal_suffix = "nd"
            elif last_digit == 3:
                ordinal_suffix = "rd"
        
        message = (
            f"The old warrior turns to you with a knowing gaze and says:"
            f"\n\"Ah, young seeker of strategy, I am in search of a tome that holds the secrets of the battlefield. "
            f"Canst thou fathom the name of the book I seek?\"\n"
            f"\n\"Methinks the correct book is the {correct_position}{ordinal_suffix} book if sorted alphabetically.\"\n"
        )

        self.label.config(text=message)

        shuffled_books_label = tk.Label(self.master, text="\nShuffled Books:")
        shuffled_books_label.pack()

        for book in shuffled_books:
            book_label = tk.Label(self.master, text=book)
            book_label.pack()

        entry = tk.Entry(self.master)
        entry.pack(pady=10)

        def check_guess():
            user_guess = entry.get()

            if user_guess.lower() == selected_book.lower():
                self.game_instance.challenge_text.delete(1.0, tk.END)
                self.game_instance.challenge_text.insert(tk.END, "Congratulations! The old warrior nods approvingly.\n"
                                                       "\"Indeed, thou possesseth insight. That book is what I desire.\"\n"
                                                       "\"Well done, seeker of tactics!\"")
                self.game_instance.ask_next_door()
                self.master.destroy()
            else:
                incorrect_guess_message = (
                    "Thou hast not guessed correctly. The old warrior remains patient."
                )
                messagebox.showinfo("Incorrect Guess", incorrect_guess_message)

        submit_button = tk.Button(self.master, text="Submit Guess", command=check_guess)
        submit_button.pack()
        

class Door3Challenge:
    def __init__(self, master, game_instance):
        self.master = master
        self.master.title("Door 3 Challenge")
        self.master.geometry("400x300")

        self.game_instance = game_instance

        self.label = tk.Label(self.master, text="Guess the Number Challenge")
        self.label.pack(pady=20)

        self.guess_the_number()

        self.button = tk.Button(self.master, text="Close Door", command=self.master.destroy)
        self.button.pack()

    def guess_the_number(self):
        self.secret_number = random.randint(1, 10)
        self.lower_bound = 1

        self.upper_bound = 10

        self.attempts_left = 3


        self.display_guess_number_challenge()

    def display_guess_number_challenge(self):
        message = (
            "Your quest begins: Guess the number from 1 - 10. The Guardian will provide clues, "

            "guiding you on the path to revelation. Venture forth, seeker, and may your intuition be your guiding light."

        )

        challenge_window = tk.Tk()
        challenge_window.title("Number Guessing Challenge")

        label = tk.Label(challenge_window, text=message, padx=10, pady=10)
        label.pack()

        entry = tk.Entry(challenge_window)
        entry.pack(pady=10)

        def check_guess():
            user_guess = entry.get()

            if not user_guess.isdigit():
                messagebox.showwarning("Invalid Input", "Please enter a valid number.")
                return

            user_guess = int(user_guess)

            if user_guess < self.lower_bound or user_guess > self.upper_bound:
                messagebox.showwarning("Out of Range", "Please enter a number within the specified range.")
                return

            if user_guess == self.secret_number:
                messagebox.showinfo("Congratulations", "Congratulations! You've guessed the correct number.")
                self.game_instance.challenge_text.insert(tk.END, "Congratulations! You've successfully guessed the number.\n")
                self.game_instance.ask_next_door()
                challenge_window.destroy()
            else:
                if self.attempts_left == 0:
                    messagebox.showinfo("Out of Attempts", f"Sorry, you're out of attempts. The correct number was {self.secret_number}.")
                    self.game_instance.challenge_text.insert(tk.END, f"Out of attempts. The correct number was {self.secret_number}.\n")
                    self.game_instance.ask_next_door()
                    challenge_window.destroy()
                else:
                    hint = "Higher" if user_guess < self.secret_number else "Lower"

                    messagebox.showinfo("Incorrect Guess", f"Try again! The correct number is {hint}.")

        submit_button = tk.Button(challenge_window, text="Submit Guess", command=check_guess)
        submit_button.pack()

        challenge_window.mainloop()


class MagicalStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

class Door4Challenge:
    def __init__(self, master, game_instance):
        self.master = master
        self.master.title("Door 4 Challenge")
        self.master.geometry("400x300")

        self.game_instance = game_instance

        self.label = tk.Label(self.master, text="Challenge for Door 4 goes here.")
        self.label.pack(pady=20)

        # Directly call the method to start the Stenchurion challenge
        self.start_stenchurion_challenge()

    def stenchurion_challenge_logic(self):
        word_list = ["strategy", "warrior", "sorcery", "challenge", "formation", "tactics"]
        word_challenge = random.choice(word_list)
        shuffled_word = ''.join(random.sample(word_challenge, len(word_challenge)))
        correct_answer = word_challenge

        return shuffled_word, correct_answer

    def start_stenchurion_challenge(self):
        shuffled_word, correct_answer = self.stenchurion_challenge_logic()

        message = (
            "'Feel the strength within each letter. Arrange them wisely, and the way shall be revealed.'\n"
            "\nBefore thee lies Stenchurion, a formidable enigma, its surface pulsating with hidden energy.\n"
            "The air around it tingles with anticipation.\n"

            "Listen to the echoes of the battlefield, where whispers of:\n"
            "A strategy unfolding, a warrior's tale bolding,\n"
            "Sorcery's dance in a challenge's trance,\n"
            "Formation's grace, tactics embrace.\n"
            "Stenchurion beckons thee, seeker, unravel the dance.\n"
            f"Inscribed upon Stenchurion is a sequence of letters awaiting thy understanding:\n"
        )

        stenchurion_window = tk.Toplevel(self.master)
        stenchurion_window.title("Stenchurion Challenge")

        label = tk.Label(stenchurion_window, text=message, padx=10, pady=10)
        label.pack()

        shuffled_label = tk.Label(stenchurion_window, text=f"Scrambled Word: {shuffled_word}",
                                   font=("Arial", 12, "italic"), fg="gray")
        shuffled_label.pack()

        stack = MagicalStack()
        for letter in shuffled_word:
            stack.push(letter)

        entry = tk.Entry(stenchurion_window)
        entry.pack(pady=10)

        def check_unscramble():
            user_input = entry.get()

            unscrambled_word = ""
            for _ in shuffled_word:
                unscrambled_word += stack.pop()

            if user_input.lower() == correct_answer.lower():
                self.game_instance.challenge_text.insert(tk.END, "\n\nVictory! Thou hast wisely used the strategic stack to unveil the true order. Stenchurion acknowledges thy mastery. Proceed, seeker of the battlefield. May victory guide thy every step.")
                messagebox.showinfo("Victory!", f"'Thou hast wisely used the strategic stack to unveil the true order. "
                                                f"Stenchurion acknowledges thy mastery. Proceed, seeker of the battlefield.'\n"
                                                "'May victory guide thy every step.'")
                self.game_instance.ask_next_door()
                self.master.destroy()
            else:
                messagebox.showinfo("Defeat",
                                    f"Stenchurion remains a formidable enigma, the word elusive. Seek the true order, "
                                    "and the way shall unfold.'\n'Thy journey through the battlefield awaits, seeker. "
                                    "Prepare for the next encounter!'")

        submit_button = tk.Button(stenchurion_window, text="Submit Answer", command=check_unscramble)
        submit_button.pack()


class AlgorithmOdysseyGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Algorithm Odyssey")
        self.master.geometry("800x600")

        self.challenge_text = tk.Text(self.master, wrap="word", width=70, height=10)
        self.challenge_text.pack(pady=10)

        self.answer_entry = tk.Entry(self.master)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.master, text="Submit Answer", command=self.submit_answer)
        self.submit_button.pack(pady=10)

        self.current_challenge_index = 0
        self.challenges = [
            "You find yourself in a dark and mysterious dungeon. In front of you, there are four[1][2][3][4] doors. Each door leads to a different path. Choose wisely.",
            "You open the first door and find yourself in a room filled with magical symbols. A wise wizard appears and presents you with a task:",
            "As you open the second door, you encounter a mysterious old warrior surrounded by an aura of ancient tactics.",
            "As you step through Door 3, you find yourself in a mystical chamber filled with ancient engravings and magical symbols. A mysterious presence reveals itself - the Guardian of Numerical Secrets. The guardian has conjured a number between 1 and 10, and only the true seeker can unravel its mystery.",
            "In the realm of challenges, you face the cunning strategist Stenchurion. Shrouded in shadows, Stenchurion presents a trial testing your analytical skills. 'Dost thou have the courage to face my game?' sneers Stenchurion, a glint of cunning in his eyes."
        ]

        self.display_challenge()

    def display_challenge(self):
        challenge = self.challenges[self.current_challenge_index]
        self.challenge_text.delete(1.0, tk.END)
        self.typing_effect(challenge)

    def typing_effect(self, text, delay=0.03):
        for char in text:
            time.sleep(delay)
            self.challenge_text.insert(tk.END, char)
            self.challenge_text.update()

    def submit_answer(self):
        user_answer = self.answer_entry.get().strip().lower()

        if self.current_challenge_index == 0 and user_answer in ['1', '2', '3', '4']:
            self.current_challenge_index = int(user_answer)
            self.display_challenge()
        elif self.current_challenge_index == 1:
            door1_challenge_window = tk.Toplevel(self.master)
            Door1Challenge(door1_challenge_window, self)


        elif self.current_challenge_index == 2:
            door2_challenge_window = tk.Toplevel(self.master)
            Door2Challenge(door2_challenge_window, self)

        elif self.current_challenge_index == 3:
            door3_challenge_window = tk.Toplevel(self.master)
            Door3Challenge(door3_challenge_window, self)

            # Add logic for door 3

        elif self.current_challenge_index == 4:
            door4_challenge_window = tk.Toplevel(self.master)
            Door4Challenge(door4_challenge_window, self)

            # Add logic for door 4

        else:
            self.display_challenge()

    def ask_next_door(self):
        self.challenge_text.insert(tk.END, "\n\nWhere do you want to go next? Choose a door (1-4)")
        self.answer_entry.config(state="normal")
        self.submit_button.config(command=self.choose_next_door)

    def choose_next_door(self):
        user_choice = self.answer_entry.get().strip()
        if user_choice in ['1', '2', '3', '4']:
            self.current_challenge_index = int(user_choice)
            self.display_challenge()
        else:
            self.challenge_text.delete(1.0, tk.END)
            self.challenge_text.insert(tk.END, "Invalid choice. Please choose a door (1-4).")


class HomePage:
    def __init__(self, master):
        self.master = master
        self.master.title("Algorithm Odyssey - Home Page")
        self.master.geometry("400x300")

        self.welcome_label = tk.Label(self.master, text="Welcome to the \n Algorithm Odyssey!", font=("Algerian", 16))
        self.welcome_label.pack(pady=20)

        self.start_button = tk.Button(self.master, text="Start Game", command=self.start_game)
        self.start_button.pack()

    def start_game(self):
        self.master.destroy()  # Close the home page window
        root = tk.Tk()
        game = AlgorithmOdysseyGame(root)
        root.mainloop()


def main():
    root = tk.Tk()
    home_page = HomePage(root)
    root.mainloop()


if __name__ == "__main__":
    main()
