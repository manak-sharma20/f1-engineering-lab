class Driver:

    def _validate_rating(self, name: str, value: float) -> None:
        if value < 0 or value > 1:
            raise ValueError(f"{name} must be 0.0–1.0. Got: {value}")

    def __init__(self, name: str, nationality: str, skill_rating: float,
                 aggression: float, wet_weather_skill: float,
                 license_number: str = "UNKNOWN"):

        self._validate_rating("skill_rating", skill_rating)
        self._validate_rating("aggression", aggression)
        self._validate_rating("wet_weather_skill", wet_weather_skill)

        self._name = name
        self._nationality = nationality
        self._skill_rating = skill_rating
        self._aggression = aggression
        self._wet_weather_skill = wet_weather_skill
        self._license_number = license_number

    @property
    def name(self):
        return self._name

    @property
    def nationality(self):
        return self._nationality

    @property
    def skill_rating(self):
        return self._skill_rating

    @property
    def aggression(self):
        return self._aggression

    @property
    def wet_weather_skill(self):
        return self._wet_weather_skill

    def lap_time_delta(self, is_wet: bool) -> float:
        if is_wet:
            return (0.5 - self.wet_weather_skill) * 2.5
        return (0.5 - self.skill_rating) * 2.0

    def __repr__(self) -> str:
        return f"Driver({self._name}, skill={self._skill_rating}, aggression={self._aggression})"


if __name__ == "__main__":
    verstappen = Driver("Max Verstappen", "Dutch", 0.98, 0.85, 0.92)
    print(verstappen.lap_time_delta(is_wet=False))  # -0.96
    print(verstappen.lap_time_delta(is_wet=True))   # -1.05
    print(verstappen)