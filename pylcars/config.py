"""Configuration constants for pylcars.

This module centralizes all magic numbers and configuration values used throughout
the pylcars library. All hardcoded values should be defined here for easy tuning
and consistency across the codebase.
"""

# Window defaults
DEFAULT_WINDOW_WIDTH: int = 800
DEFAULT_WINDOW_HEIGHT: int = 480

# Audio configuration
AUDIO_CHUNK_SIZE: int = 256

# Animation timing (milliseconds)
TICKLE_DURATION_MS: int = 300
SHUTDOWN_SEQUENCE_MS: int = 3000

# Fonts
# Note: LCARS font needs to be installed separately
# If not available, falls back to system fonts
DEFAULT_FONT_NAME: str = "LCARS"
DEFAULT_FONT_SIZE: int = 26
FALLBACK_FONT_NAME: str = "Courier"  # Fallback if LCARS unavailable
FALLBACK_FONT_SIZE: int = 18  # Smaller fallback size to match original look

# Demo menu defaults
DEMO_MENU_WIDTH: int = 800
DEMO_MENU_HEIGHT: int = 480
DEMO_MENU_BUTTON_WIDTH: int = 130
DEMO_MENU_BUTTON_HEIGHT: int = 40
DEMO_MENU_ROW_HEIGHT: int = 44
DEMO_MENU_BUTTON_SPACING: int = 4
DEMO_MENU_MARGIN_LEFT: int = 140
DEMO_MENU_MARGIN_TOP: int = 180
DEMO_MENU_FONT_SIZE: int = 80
DEMO_MENU_SVG_WIDTH: int = 200
DEMO_MENU_SVG_HEIGHT: int = 100
DEMO_MENU_SHUTDOWN_DIALOG_WIDTH: int = 640
DEMO_MENU_SHUTDOWN_DIALOG_HEIGHT: int = 300

# Demo sounds grid
DEMO_SOUNDS_GRID_COLS: int = 6
DEMO_SOUNDS_GRID_ROWS: int = 10
DEMO_SOUNDS_BUTTON_WIDTH: int = 120
DEMO_SOUNDS_BUTTON_HEIGHT: int = 40
DEMO_SOUNDS_BUTTON_SPACING: int = 10
