from enum import Enum

import pygame

# WINDOW -----------------------------------------------------------------------
WIDTH = 640
HEIGHT = 480

# FOX -------------------------------------------------------------------------
BASE_SPEED = 6
MAX_SPEED = 20
FOX_HITBOX_DIFF = 15

# CLOUD -----------------------------------------------------------------------
# PLAYER1
CLOUD_PLAYER1_X = 5
CLOUD_PLAYER1_ROTATION = 270

# PLAYER2
CLOUD_PLAYER2_X = WIDTH - 48
CLOUD_PLAYER2_ROTATION = 90

CLOUD_Y = HEIGHT // 2
CLOUD_HITBOX_WIDTH_DIFF = 26
CLOUD_HITBOX_HEIGHT_DIFF = 0

# BONUS STAR ------------------------------------------------------------------
# We set something like IDs for the events
BONUS_SPAWN_EVENT = (
    pygame.USEREVENT + 1
)  # (32769) - a special event type with number 32768
BONUS_DE_SPAWN_EVENT = pygame.USEREVENT + 2  # (32770)
BONUS_SPAWN_INTERVAL = 20 * 1000  # 20 * 1000 milliseconds
BONUS_LIFETIME = 5 * 1000  # 5 * 1000 milliseconds
BONUS_POINTS = 2
BONUS_HITBOX_DIFF = 5

# COLORS -----------------------------------------------------------------------
STAR_PARTICLES_COLOR = (249, 182, 154)  # for particles
WARM_GREY = (155, 155, 155)
WHITE = (255, 255, 255)


# GAME STATES ------------------------------------------------------------------
class GameStates(Enum):
    START = "start"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER_LEADERBOARD = "game over leaderboard"


# START SCREEN -----------------------------------------------------------------
# START BUTTON
START_BUTTON_TEXT = "START"
START_BUTTON_FONT_SIZE = 30
START_BUTTON_FONT = "courier new"
START_BUTTON_TEXT_COLOR = WARM_GREY
START_BUTTON_POS = (WIDTH // 2 - 100, HEIGHT // 2 + 100)

# MULTIPLAYER TOGGLE BUTTON
MULTIPLAYER_TOGGLE_BUTTON_TEXT_ON = "MULTIPLAYER"
MULTIPLAYER_TOGGLE_BUTTON_TEXT_OFF = "SINGLE PLAYER"
MULTIPLAYER_TOGGLE_BUTTON_FONT_SIZE = 24
MULTIPLAYER_TOGGLE_BUTTON_FONT = START_BUTTON_FONT
MULTIPLAYER_TOGGLE_BUTTON_TEXT_COLOR = WARM_GREY
MULTIPLAYER_TOGGLE_BUTTON_POS = (WIDTH // 2 - 100, HEIGHT // 2 + 150)

# SOUND TOGGLE BUTTON
SOUND_TOGGLE_BUTTON_TEXT_ON = "SOUND: ON"
SOUND_TOGGLE_BUTTON_TEXT_OFF = "SOUND: OFF"
SOUND_TOGGLE_BUTTON_FONT_SIZE = 24
SOUND_TOGGLE_BUTTON_FONT = START_BUTTON_FONT
SOUND_TOGGLE_BUTTON_TEXT_COLOR = WARM_GREY
SOUND_TOGGLE_BUTTON_POS = (WIDTH // 2 + 100, HEIGHT // 2 + 100)

# MUSIC TOGGLE BUTTON
MUSIC_TOGGLE_BUTTON_TEXT_ON = "MUSIC: ON"
MUSIC_TOGGLE_BUTTON_TEXT_OFF = "MUSIC: OFF"
MUSIC_TOGGLE_BUTTON_FONT_SIZE = 24
MUSIC_TOGGLE_BUTTON_FONT = START_BUTTON_FONT
MUSIC_TOGGLE_BUTTON_TEXT_COLOR = WARM_GREY
MUSIC_TOGGLE_BUTTON_POS = (WIDTH // 2 + 100, HEIGHT // 2 + 150)

# CONTROLS INFO
CONTROLS_INFO_FONT_SIZE = 14
CONTROLS_INFO_TEXT = (
    "Player 1: W/S || Player 2: UP/DOWN || Pause/Resume: SPACE || Exit/Settings: ESC"
)
CONTROLS_INFO_FONT = "arial"
CONTROLS_INFO_TEXT_COLOR = STAR_PARTICLES_COLOR
CONTROLS_INFO_POS = (WIDTH // 2, HEIGHT - 50)


# PLAYING SCREEN ---------------------------------------------------------------
# SCORE BOARD
SCORE_FONT_SIZE = 20
SCORE_FONT = "courier new"
SCORE_TEXT = "SCORE:"
SCORE_TEXT_COLOR = STAR_PARTICLES_COLOR
SCORE_POS_PLAYER1 = (WIDTH // 2 - 150, 20)
SCORE_POS_PLAYER2 = (WIDTH // 2 + 20, 20)

# LEVEL BOARD
LEVEL_TEXT = "LEVEL:"
LEVEL_FONT_SIZE = 20
LEVEL_FONT = "courier new"
LEVEL_TEXT_COLOR = STAR_PARTICLES_COLOR
LEVEL_POS = (WIDTH // 2 - 47, 60)

# PAUSE SCREEN -----------------------------------------------------------------
# PAUSE TEXT
PAUSE_TEXT = "PAUSED"
PAUSE_FONT_SIZE = 50
PAUSE_FONT = "courier new"
PAUSE_TEXT_COLOR = STAR_PARTICLES_COLOR
PAUSE_TEXT_POS = (WIDTH // 2, HEIGHT // 4 - 30)

# PAUSE SUBTEXT
PAUSE_SUBTEXT = "Press SPACE to resume or ESC to quit the game"
PAUSE_SUBTEXT_FONT_SIZE = 20
PAUSE_SUBTEXT_FONT = "arial"
PAUSE_SUBTEXT_COLOR = STAR_PARTICLES_COLOR
PAUSE_SUBTEXT_POS = (WIDTH // 2, HEIGHT // 4 + 20)

# BUTTON POSITIONS
PAUSE_SOUND_TOGGLE_BUTTON_POS = (WIDTH // 2, HEIGHT // 2)
PAUSE_MUSIC_TOGGLE_BUTTON_POS = (WIDTH // 2, HEIGHT // 2 + 50)
