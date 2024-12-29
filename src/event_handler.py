from src.core.game_state import GameState
from src.utils.screenshot import ScreenshotManager

import pygame


class EventHandler:
    """
    Class to handle all the events in the game

    Args:
        game_state (GameState): The current game state

    Attributes:
        game_state (GameState): The current game state
        screenshot_manager (ScreenshotManager): The screenshot manager
                to take screenshots

    """

    def __init__(self, game_state: GameState) -> None:
        self.game_state = game_state
        self.screenshot_manager = ScreenshotManager()

    def handle_events(self) -> bool:
        """
        Handle all the events in the game

        Returns:
            bool: True if the game should continue, False if the game should end
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        return True