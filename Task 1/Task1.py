class NimVariationGame:
    def __init__(self, red_count, blue_count, game_type, starting_player, max_depth):
        self.red_count = red_count
        self.blue_count = blue_count
        self.game_type = game_type  
        self.active_player = starting_player
        self.max_depth = max_depth
        self.human_score = 0
        self.computer_score = 0

    def display_game_status(self):
        print(f"Red marbles: {self.red_count}, Blue marbles: {self.blue_count}")
        print(f"Now playing: {self.active_player}")

    def game_is_over(self):
        return self.red_count == 0 and self.blue_count == 0

    def evaluate_game(self):
        if self.game_type == 'standard':
            return 1 if self.game_is_over() else -1
        else:  
            return -1 if self.game_is_over() else 1

    def update_marbles(self, red_taken, blue_taken):
        self.red_count -= red_taken
        self.blue_count -= blue_taken

    def player_turn(self):
        self.display_game_status()
        while True:
            try:
                red_taken = int(input("Enter the number of red marbles to take: "))
                blue_taken = int(input("Enter the number of blue marbles to take: "))
                if red_taken <= self.red_count and blue_taken <= self.blue_count and (red_taken > 0 or blue_taken > 0):
                    break
                else:
                    print("Invalid move! Ensure you're taking valid marble counts.")
            except ValueError:
                print("Please enter valid numbers.")
        self.update_marbles(red_taken, blue_taken)

    def ai_turn(self):
        self.display_game_status()
        optimal_score = -float('inf')
        best_action = None

        for red in range(self.red_count + 1):
            for blue in range(self.blue_count + 1):
                if red == 0 and blue == 0:
                    continue
                self.update_marbles(red, blue)
                current_score = self.minimax_algorithm(self.max_depth, False, -float('inf'), float('inf'))
                self.update_marbles(-red, -blue)  
                if current_score > optimal_score:
                    optimal_score = current_score
                    best_action = (red, blue)

        red_taken, blue_taken = best_action
        print(f"AI removes {red_taken} red marbles and {blue_taken} blue marbles.")
        self.update_marbles(red_taken, blue_taken)

    def minimax_algorithm(self, depth, maximizing, alpha, beta):
        if self.game_is_over() or depth == 0:
            return self.evaluate_game()

        if maximizing:
            max_eval = -float('inf')
            for red in range(self.red_count + 1):
                for blue in range(self.blue_count + 1):
                    if red == 0 and blue == 0:
                        continue
                    self.update_marbles(red, blue)
                    eval_score = self.minimax_algorithm(depth - 1, False, alpha, beta)
                    self.update_marbles(-red, -blue)
                    max_eval = max(max_eval, eval_score)
                    alpha = max(alpha, eval_score)
                    if beta <= alpha:
                        break
            return max_eval
        else:
            min_eval = float('inf')
            for red in range(self.red_count + 1):
                for blue in range(self.blue_count + 1):
                    if red == 0 and blue == 0:
                        continue
                    self.update_marbles(red, blue)
                    eval_score = self.minimax_algorithm(depth - 1, True, alpha, beta)
                    self.update_marbles(-red, -blue)
                    min_eval = min(min_eval, eval_score)
                    beta = min(beta, eval_score)
                    if beta <= alpha:
                        break
            return min_eval

def start_game(red_count, blue_count, game_type, starting_player, max_depth):
    game_instance = NimVariationGame(red_count, blue_count, game_type, starting_player, max_depth)
    game_instance.display_game_status()

    while not game_instance.game_is_over():
        if game_instance.active_player == 'human':
            game_instance.player_turn()
            game_instance.active_player = 'computer'
            game_instance.human_score += 1
        else:
            game_instance.ai_turn()
            game_instance.active_player = 'human'
            game_instance.computer_score += 1

        game_instance.display_game_status()

    print("Game over!")
    print(f"Final Scores - Human: {game_instance.human_score}, Computer: {game_instance.computer_score}")
    final_result = game_instance.evaluate_game()
    if final_result == 1:
        print("Human wins!" if game_instance.game_type == 'standard' else "Computer wins!")
    else:
        print("Computer wins!" if game_instance.game_type == 'standard' else "Human wins!")

if __name__ == "__main__":
    red_count = int(input("Enter number of red marbles: "))
    blue_count = int(input("Enter number of blue marbles: "))
    game_type = input("Choose the game mode (standard/misere): ").strip().lower()
    starting_player = input("Who plays first (human/computer): ").strip().lower()
    max_depth = 3  

    start_game(red_count, blue_count, game_type, starting_player, max_depth)