#EVERYTHING PRESENTED HERE IS MADE BY CHATGPT!!!
import random

# Define the card class
class Card:
    def __init__(self, name, damage, heal):
        self.name = name
        self.damage = damage
        self.heal = heal

# Create a list of 120 cards
deck = [
    Card("Attack", damage=5, heal=0),
    Card("Attack", damage=5, heal=0),
    Card("Attack", damage=5, heal=0),
    Card("Attack", damage=5, heal=0),
    Card("Attack", damage=5, heal=0),
    Card("Attack", damage=5, heal=0),
    Card("Healing Potion", damage=0, heal=10),
    # Add more cards with different abilities
]

# Initialize player and enemy health
player_health = 100
doge_health = 100  # Initialize 'doge_health' with a value
stage = 1

# Initialize the player's hand with 5 randomly generated cards
player_cards = random.sample(deck, 5)

# Draw and use cards in a battle
def play_turn(player_health, enemy_health, player_cards, max_hand_size):
    # Draw a card for each turn and add it to the player's hand
    if len(player_cards) < max_hand_size:
        player_cards.append(random.choice(deck))
    
    # Player's turn: Choose how many cards to use
    print("Your available cards:")
    for i, card in enumerate(player_cards):
        print(f"{i + 1}. {card.name}")
    
    while True:
        try:
            num_cards_to_play = int(input(f"Select how many cards to play (1-{min(max_hand_size, len(player_cards))}): "))
            if 1 <= num_cards_to_play <= min(max_hand_size, len(player_cards)):
                break
            else:
                print("Invalid choice. Please select a valid number of cards.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    cards_played = []
    for _ in range(num_cards_to_play):
        while True:
            try:
                choice = int(input(f"Select a card to use (1-{len(player_cards)}): "))
                if 0 <= choice < len(player_cards):
                    if player_cards[choice] not in cards_played:
                        break
                    else:
                        print("You've already played that card. Please choose a different card.")
                else:
                    print("Invalid choice. Please select a valid card.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        selected_card = player_cards.pop(choice)
        cards_played.append(selected_card)
        
        # Apply the selected card's effects
        player_damage = selected_card.damage
        player_heal = selected_card.heal

        if stage == 1:
            enemy_health -= player_damage
            doge_damage = 0
        else:
            doge_damage = player_damage
            enemy_health = 0

        player_health -= player_damage
        player_health += player_heal

        # Ensure health doesn't go below 0
        player_health = max(0, player_health)
        doge_health = max(0, doge_health)

    # Display the turn summary
    print(f"Player used the following cards:")
    for card in cards_played:
        print(f"   {card.name}")
    print(f"   Damage to Player: {player_damage}")
    print(f"   Healing for Player: {player_heal}")
    print(f"   Damage to Doge: {doge_damage}")
    print(f"Player Health: {player_health}")
    print(f"Doge Health: {doge_health}")

# Simulate the battle
player_cards = []

while player_health > 0 and (stage == 1 and doge_health > 0) or (stage == 2 and enemy_health > 0):
    if stage == 1 and doge_health == 0:
        stage = 2
        enemy_health = 200  # Replace with stats for the stage 2 enemy
        print("\nStage 2: A new enemy appears!")

    if stage == 1:
        print("\nStage 1: Battle with Doge")
    else:
        print("\nStage 2: Battle with a new enemy")

    play_turn(player_health, enemy_health if stage == 2 else doge_health, player_cards, max_hand_size=5)

# Determine the winner
if player_health == 0:
    print("Player loses.")
elif stage == 1 and doge_health == 0:
    print("Stage 1 completed. Player advances to Stage 2.")
elif stage == 2 and enemy_health == 0:
    print("Stage 2 completed. Player wins!")