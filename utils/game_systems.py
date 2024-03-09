class TimeSystem:
    def __init__(self):
        self.day = 1
        self.hour = 6  # Start at 6 AM
        self.is_daytime = True

    def advance_time(self, hours=1):
        self.hour += hours
        if self.hour >= 24:
            self.hour -= 24
            self.day += 1

        # Update day/night status based on the hour
        if 6 <= self.hour < 21:
            self.is_daytime = True
        else:
            self.is_daytime = False

    def time_status(self):
        if self.is_daytime:
            return f"Day {self.day}, {self.hour}:00 - Daytime"
        else:
            return f"Day {self.day}, {self.hour}:00 - Nighttime"

time_system = TimeSystem()
