# RPS-001: Play a Round

## Purpose

Build a working Rock, Paper, Scissors game that determines the correct winner for one independent round. The player chooses rock, paper, or scissors, and the computer selects a move. The game displays both choices and the result.

Each new selection starts another round without storing scores or previous results.

## Prediction and Plan

**Prediction:** If I choose rock and the computer chooses scissors, I expect to win because rock beats scissors.

**Losing example:** If I choose rock and the computer chooses paper, I should lose because paper beats rock.

**Invalid input:** Missing or unsupported moves must return HTTP 400 with a helpful error message.

**Implementation plan:**

1. Implement `determine_winner(player, computer)` in `game.py`.
2. Return `win`, `lose`, or `tie` from the player's perspective.
3. Test all nine possible matchups.
4. Test valid and invalid HTTP requests.
5. Test a real browser round and replay.
6. Run Black, Pylint, pytest, and Chromium browser checks.
7. Review the changes and verify the game manually.

## Expected Results

| Player | Computer | Result |
|---|---|---|
| Rock | Rock | Tie |
| Rock | Paper | Lose |
| Rock | Scissors | Win |
| Paper | Rock | Win |
| Paper | Paper | Tie |
| Paper | Scissors | Lose |
| Scissors | Rock | Lose |
| Scissors | Paper | Win |
| Scissors | Scissors | Tie |

## Implementation

The winner logic is implemented in `determine_winner()` using the existing server and interface. Matching moves produce a tie. Otherwise, the function determines whether the player's move beats the computer's move.

The game allows the player to select another move immediately, starting an independent round.

## Testing and Verification

**Full local check command:**

`.venv/bin/python check.py`

**Actual results:**

- Black formatting: PASS
- Pylint code analysis: PASS
- Non-browser pytest: 23 passed
- Chromium browser pytest: 6 passed
- Total: 29 passed
- All configured checks passed.

The tests cover the nine outcomes, real HTTP request handling, invalid inputs, browser interaction, and replay.

**Test explanation:** The unit test for rock against scissors expects `win`. It would catch a mistake where the winner logic incorrectly returns `lose` or reverses the rules.

## Actual Browser Verification

**Observed round:**

- Player chose: Rock
- Computer chose: Scissors
- Displayed result: You win!
- Explanation: Rock beats scissors, so the result is correct.

The game displays both moves and the result. Selecting another move starts another round. Keyboard interaction can be tested using Tab to focus a move and Enter to activate it.

## GitHub Evidence

- **Issue:** https://github.com/Modrilexx/my-rps/issues/1
- **Feature branch:** `rps-001`
- **Pull request:** https://github.com/Modrilexx/my-rps/pull/2
- **Successful CI run:** https://github.com/Modrilexx/my-rps/actions/runs/41765952156
- **Implementation:** https://github.com/Modrilexx/my-rps/blob/rps-001/game.py
- **Unit and integration tests:** https://github.com/Modrilexx/my-rps/blob/rps-001/tests/test_game.py
- **Browser tests:** https://github.com/Modrilexx/my-rps/blob/rps-001/tests/e2e/test_round.py

## AI Assistance and Review

ChatGPT assisted with the implementation, automated tests, and preparation of the verification documentation. I reviewed the code changes, ran the full checks locally, and verified an actual game round in the browser.

The implementation retains the supplied interface and server without adding scoring, storage, accounts, or additional frameworks.
**GitHub issue:** https://github.com/Modrilexx/my-rps/issues/1

Successful Run: https://github.com/Modrilexx/my-rps/pull/2/
