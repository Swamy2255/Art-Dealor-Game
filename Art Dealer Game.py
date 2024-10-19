import tkinter as tk
import random

class MultiplayerGame:
    def __init__(self, players, grade_level):
        self.players = players
        self.current_player_index = 0
        self.scores = {player: 0 for player in players}
        self.difficulty_level = grade_level
        self.card_labels = []

    def create_game_window(self):
        window = tk.Tk()
        window.title(f"Art Dealer Game - Grade {self.difficulty_level}")

        # Set background color for the main window
        window.configure(bg="#f0f0f0")

        # Game instructions label
        instructions_label = tk.Label(
            window,
            text=f"Welcome to Grade {self.difficulty_level}! Each player will take turns.",
            bg="#4CAF50",
            font=("Arial", 14, "bold"),
            fg="white"
        )
        instructions_label.pack(pady=10, padx=10, fill="x")

        # Card deck frame with a colored background
        card_deck_frame = tk.Frame(window, bg="#d9d9d9", padx=10, pady=10)
        card_deck_frame.pack(pady=10)

        # Card display labels
        self.card_labels = []
        for _ in range(4):
            card_label = tk.Label(
                card_deck_frame,
                bg="#ffffff",
                width=5,
                height=3,
                font=("Arial", 16, "bold"),
                relief="solid"
            )
            card_label.pack(side="left", padx=10)
            self.card_labels.append(card_label)

        # Guess input label and entry
        guess_label = tk.Label(
            window,
            text="Enter your guess for the pattern:",
            bg="#f0f0f0",
            font=("Arial", 12)
        )
        guess_label.pack(pady=5)
        guess_entry = tk.Entry(window, font=("Arial", 12))
        guess_entry.pack(pady=5)

        # Submit guess button
        submit_button = tk.Button(
            window,
            text="Submit Guess",
            command=lambda: self.check_guess(guess_entry.get(), window, guess_entry),
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold")
        )
        submit_button.pack(pady=10)

        # Feedback label
        feedback_label = tk.Label(window, text="", bg="#f0f0f0", font=("Arial", 12, "bold"))
        feedback_label.pack(pady=10)

        # Score label
        score_label = tk.Label(window, text=self.get_score_text(), bg="#f0f0f0", font=("Arial", 12, "bold"))
        score_label.pack(pady=10)

        # Exit button
        exit_button = tk.Button(
            window,
            text="Exit",
            command=window.destroy,
            bg="#FF5722",
            fg="white",
            font=("Arial", 12, "bold")
        )
        exit_button.pack(pady=10)

        # Store references for updating
        self.guess_entry = guess_entry
        self.feedback_label = feedback_label
        self.score_label = score_label

        self.generate_cards()
        window.mainloop()

    def check_guess(self, guess, window, guess_entry):
        card_values = [card_label.cget("text") for card_label in self.card_labels]
        is_correct = False

        # Implement pattern checking (simplified for this example)
        if guess.lower() == "all red":
            is_correct = all(card[0] in ["H", "D"] for card in card_values)
        elif guess.lower() == "all black":
            is_correct = all(card[0] in ["S", "C"] for card in card_values)

        if is_correct:
            self.scores[self.players[self.current_player_index]] += 1
            feedback_text = "🎉 Great job! You guessed it!"
        else:
            feedback_text = "😞 Oops! Try again!"

        self.feedback_label.config(text=feedback_text)
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.score_label.config(text=self.get_score_text())

        # Clear the guess entry after checking
        guess_entry.delete(0, tk.END)
        self.generate_cards()

    def get_score_text(self):
        return "Scores: " + ", ".join(f"{player}: {score}" for player, score in self.scores.items())

    def generate_cards(self):
        cards = [random.choice(["H", "D", "S", "C"]) + random.choice(["2", "3", "4", "5", "6"]) for _ in range(4)]

        # Update card labels and set their colors based on suits
        for i, card in enumerate(cards):
            self.card_labels[i].config(text=card)
            if card[0] in ["H", "D"]:  # Hearts and Diamonds
                self.card_labels[i].config(bg="red", fg="white")
            else:  # Clubs and Spades
                self.card_labels[i].config(bg="black", fg="white")

def start_game(players, grade_level):
    game = MultiplayerGame(players, grade_level)
    game.create_game_window()

def main():
    main_window = tk.Tk()
    main_window.title("Art Dealer Game")
    main_window.configure(bg="#f0f0f0")

    # Game title
    title_label = tk.Label(
        main_window,
        text="Welcome to the Art Dealer Game!",
        bg="#4CAF50",
        font=("Arial", 16, "bold"),
        fg="white"
    )
    title_label.pack(pady=20, padx=10, fill="x")

    # Button to start the game
    start_button = tk.Button(
        main_window,
        text="Start",
        command=lambda: show_game_modes(main_window),
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12, "bold")
    )
    start_button.pack(pady=20)

    # Exit button
    exit_button = tk.Button(
        main_window,
        text="Exit",
        command=main_window.destroy,
        bg="#FF5722",
        fg="white",
        font=("Arial", 12, "bold")
    )
    exit_button.pack(pady=10)

    main_window.mainloop()

def show_game_modes(main_window):
    main_window.destroy()

    game_mode_window = tk.Tk()
    game_mode_window.title("Select Game Mode")
    game_mode_window.configure(bg="#f0f0f0")

    # Single Player Mode button
    single_player_button = tk.Button(
        game_mode_window,
        text="Single Player",
        command=lambda: show_grade_selection(["Player 1"], game_mode_window),
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12, "bold")
    )
    single_player_button.pack(pady=10)

    # Multiplayer Mode button
    multiplayer_button = tk.Button(
        game_mode_window,
        text="Multiplayer",
        command=lambda: show_grade_selection(["Player 1", "Player 2"], game_mode_window),
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12, "bold")
    )
    multiplayer_button.pack(pady=10)

    # Exit button
    exit_button = tk.Button(
        game_mode_window,
        text="Exit",
        command=game_mode_window.destroy,
        bg="#FF5722",
        fg="white",
        font=("Arial", 12, "bold")
    )
    exit_button.pack(pady=10)

    game_mode_window.mainloop()

def show_grade_selection(players, game_mode_window):
    game_mode_window.destroy()

    grade_selection_window = tk.Tk()
    grade_selection_window.title("Select Grade Level")
    grade_selection_window.configure(bg="#f0f0f0")

    # Button for each grade
    k2_button = tk.Button(
        grade_selection_window,
        text="Grades K-2",
        command=lambda: start_game(players, "K-2"),
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12, "bold")
    )
    k2_button.pack(pady=10)

    grade35_button = tk.Button(
        grade_selection_window,
        text="Grades 3-5",
        command=lambda: start_game(players, "3-5"),
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12, "bold")
    )
    grade35_button.pack(pady=10)

    grade68_button = tk.Button(
        grade_selection_window,
        text="Grades 6-8",
        command=lambda: start_game(players, "6-8"),
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12, "bold")
    )
    grade68_button.pack(pady=10)

    # Exit button
    exit_button = tk.Button(
        grade_selection_window,
        text="Exit",
        command=grade_selection_window.destroy,
        bg="#FF5722",
        fg="white",
        font=("Arial", 12, "bold")
    )
    exit_button.pack(pady=10)

    grade_selection_window.mainloop()

if __name__ == "__main__":
    main()
