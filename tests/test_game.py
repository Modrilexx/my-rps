"""Literal unit checks for all nine RPS results and a real Flask request."""

import pytest

import app as web
from game import determine_winner


@pytest.mark.unit
def test_rock_rock_tie():
    """Matching rocks must tie."""
    assert determine_winner("rock", "rock") == "tie"


@pytest.mark.unit
def test_rock_paper_lose():
    """Paper defeats the player's rock."""
    assert determine_winner("rock", "paper") == "lose"


@pytest.mark.unit
def test_rock_scissors_win():
    """Rock defeats scissors."""
    assert determine_winner("rock", "scissors") == "win"


@pytest.mark.unit
def test_paper_rock_win():
    """Paper defeats rock."""
    assert determine_winner("paper", "rock") == "win"


@pytest.mark.unit
def test_paper_paper_tie():
    """Matching papers must tie."""
    assert determine_winner("paper", "paper") == "tie"


@pytest.mark.unit
def test_paper_scissors_lose():
    """Scissors defeats the player's paper."""
    assert determine_winner("paper", "scissors") == "lose"


@pytest.mark.unit
def test_scissors_rock_lose():
    """Rock defeats the player's scissors."""
    assert determine_winner("scissors", "rock") == "lose"


@pytest.mark.unit
def test_scissors_paper_win():
    """Scissors defeats paper."""
    assert determine_winner("scissors", "paper") == "win"


@pytest.mark.unit
def test_scissors_scissors_tie():
    """Matching scissors must tie."""
    assert determine_winner("scissors", "scissors") == "tie"


@pytest.mark.integration
def test_real_post_uses_rules_and_renders_result(monkeypatch):
    """A submitted move uses the real rule and renders both choices."""
    # Fix computer randomness only. Do not patch determine_winner().
    monkeypatch.setattr(web.random, "choice", lambda _moves: "scissors")
    response = web.app.test_client().post("/", data={"move": "rock"})

    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'data-outcome="win"' in html
    assert "You chose" in html
    assert "Computer chose" in html
    assert "Rock" in html
    assert "Scissors" in html
    assert "You win!" in html
