"""Rock, Paper, Scissors rules for one independent round (RPS-001)."""


def determine_winner(player: str, computer: str) -> str:
    """Return 'win', 'lose', or 'tie' from the player's perspective.

    The supplied Flask server accepts only rock, paper, and scissors.
    A tie occurs when both players choose the same move; otherwise the
    winning player/computer pairs below decide the outcome.
    """
    if player == computer:
        return "tie"

    player_wins = {
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper"),
    }
    return "win" if (player, computer) in player_wins else "lose"
