# utils/state_manager.py
from utils.definitions import GameState

class StateManager:
    def __init__(self):
        self.current_state = GameState.EXPLORING  # Default state

    def get_current_state(self):
        return self.current_state

    def set_current_state(self, new_state):
        self.current_state = new_state
