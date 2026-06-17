class Engine:
    VALID_MODES={"race","qualifying","saving"}
    def __init__(self,manufacturer:str,power_bhp:str,fuel_mode:str="race"):
        if not (800<=power_bhp<=1200):
            raise ValueError(f"power_bhp must be 800-1200.Got : {power_bhp} ")
        if fuel_mode not in self.VALID_MODES:
            raise ValueError(f"Invalid mode : {fuel_mode},expected: {self.VALID_MODES}")
        self._manufacturer=manufacturer
        self._power_bhp=power_bhp
        self._fuel_mode=fuel_mode
        self._mileage_km=0.0
    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def power_bhp(self):
        return self._power_bhp
    
    @property
    def fuel_mode(self):
        return self._fuel_mode

    def get_power_output(self) -> float :
        multipliers={"qualifying":1.0,"race":0.92,"saving":0.78}
        return self._power_bhp * multipliers[self._fuel_mode]
    def set_fuel_mode(self,mode:str)-> None:
        if mode not in self.VALID_MODES:
            raise ValueError(f"Invalid mode:{mode}")
        self._fuel_mode=mode
    def add_mileage(self,km:float)-> None :
        if km<=0:
            raise ValueError(f"km must be positive.Got : {km} ")
        self._mileage_km+=km
    def needs_replacement(self)-> bool:
        return self._mileage_km>2000
    def __repr__(self) -> str:
        return f"Engine({self._manufacturer}, {self._power_bhp}bhp, {self._fuel_mode} mode, {self._mileage_km:.0f}km)"




class Tyre:
    VALID_COMPOUND={"soft","medium","hard","intermediate","wet"}
    def __init__(self,compound:str):
        if compound not in self.VALID_COMPOUND:
            raise ValueError(f"Compound not recognised.Got: {compound}")
        starting_grip={"soft": 1.00, "medium": 0.88, "hard": 0.78,
        "intermediate": 0.85, "wet": 0.80}

        self._compound=compound
        self._grip_level=starting_grip[compound]
        
        self._lap_used=0
    @property
    def compound(self):
        return self._compound
    @property
    def grip_level(self):
        return self._grip_level
    @property
    def lap_used(self):
        return self._lap_used
    
    wear_rates={"soft": 2.0, "medium": 1.4, "hard": 1.0,
        "intermediate": 1.2, "wet": 1.1}


    def add_lap(self,track_roughness:float)->None:
        if track_roughness>1.0 or track_roughness<0.0:
            raise ValueError(f"Invalid track_roughness.Got : {track_roughness}")
        wear=0.01*track_roughness*self.wear_rates[self._compound]
        self._grip_level=max(0.0,self._grip_level-wear)
        self._lap_used+=1
    def is_critical(self)->bool:
        return self._grip_level<0.3
    def should_pit(self)->bool:
        return self._grip_level<0.5
    def __repr__(self) -> str:
        return f"Tyre({self._compound}, grip={self._grip_level:.2f}, {self._lap_used} laps)"
