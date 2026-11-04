# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** One person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan (review and confirm in the local AI project)

**Proposed prediction:** Player selects rock and computer selects paper. Expected result is `lose`, because paper covers rock. Confirm or replace this with your own prediction and explanation before treating the plan as agreed.

Implement only the rules in `determine_winner()` and keep the existing Flask server and interface. Return `tie` when moves match, `win` when the player's move beats the computer, and `lose` otherwise. A valid losing round is rock versus paper; it must show **Computer wins** rather than an error. The server must reject a missing move or unsupported value such as `lizard` with HTTP 400 and a helpful message. No scoring, persistence, framework changes, or AI API.

### Checks

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | Nine separate literal tests in `tests/test_game.py` match the table above, including losses and ties. |
| Integration — positive | A real Flask POST from rock against fixed computer scissors shows both moves, `win`, and **You win!**. Only `random.choice` is patched. |
| Integration — negative | Keep and rerun the starter's missing/unsupported-move tests; both must return HTTP 400 and a helpful message, without executing the rules. |
| E2E — positive | Real Chromium browser picks rock, gets fixed scissors and a win; a second click picks rock, gets fixed paper and a loss. The actual rule function and HTTP server remain active. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` (not `--fast`) for Black, Pylint, non-browser tests, and real-browser tests; inspect the diff. Do not weaken shared settings or assertions.

### Work record — replace placeholders with your actual evidence

- Issue: **ADD your own GitHub issue URL here**.
- Feature branch: `rps-001`.
- Pull request (merged): **ADD actual PR URL here**.
- Python checks run on final PR commit: **ADD actual GitHub Actions run URL here**.
- Implementation: [game.py](game.py).
- Unit and integration tests: [tests/test_game.py](tests/test_game.py).
- E2E browser test: [tests/e2e/test_round.py](tests/e2e/test_round.py).
- Existing HTTP 400 checks: Preserve and reference the relevant original starter test file(s) here after inspecting the clone.
- Full local checks (`.venv/bin/python check.py`): **NOT YET VERIFIED IN YOUR CLONE — replace with actual observed Black, Pylint, non-browser pytest, and Chromium results**.
- Example of a test and the mistake it would catch: `test_rock_paper_lose` asserts `determine_winner("rock", "paper") == "lose"`. It would catch a reversed comparison that incorrectly awards rock a win against paper. Review and explain it in your own words.
- Actual browser round: **After playing, record your move, the computer's move, on-screen result, and why that result follows RPS rules. Do not invent a round.**
- Replay and keyboard observation: **Record what actually happened after another click, and when using Tab/Enter (Safari may need Option+Tab).**
- AI assistance: ChatGPT helped prepare an implementation, automated tests, and an evidence template; the student reviewed and completed the local/GitHub verification.

Finish the actual issue, PR, checks, and browser observations before merging; do not present placeholders as completed evidence.
