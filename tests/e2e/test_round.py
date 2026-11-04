"""Real Chromium browser exercise: play and immediately replay a round."""

import pytest
from playwright.sync_api import expect

import app as web


@pytest.mark.e2e
def test_browser_round_and_replay(live_server, page, monkeypatch):
    """A player can win, then play another independent losing round."""
    # Only fix the computer's move; keep the actual rules and HTTP server.
    monkeypatch.setattr(web.random, "choice", lambda _moves: "scissors")
    page.goto(live_server)
    expect(page.get_by_role("heading", name="Your next move?")).to_be_visible()

    page.get_by_role("button", name="Rock").click()
    expect(page.locator(".choices")).to_contain_text("Rock")
    expect(page.locator(".choices")).to_contain_text("Scissors")
    expect(page.locator(".result")).to_have_attribute("data-outcome", "win")
    expect(page.get_by_role("heading", name="You win!")).to_be_visible()

    # Another click submits a new round, rather than reusing the old result.
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")
    page.get_by_role("button", name="Rock").click()
    expect(page.locator(".choices")).to_contain_text("Rock")
    expect(page.locator(".choices")).to_contain_text("Paper")
    expect(page.locator(".result")).to_have_attribute("data-outcome", "lose")
    expect(page.get_by_role("heading", name="Computer wins")).to_be_visible()
