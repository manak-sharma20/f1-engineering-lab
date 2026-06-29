class Track:
    valid_tracks={"street","permanent","hybrid"}
    def validate_length(self,length_km:float)->None:
        if length_km<3.0 or length_km>8.0:
            raise ValueError(f"Length must be between 3.0 and 8.0 km. Got: {length_km}")
    def validate_roughness(self,roughness:float)->None:
        if roughness<0.0 or roughness>1.0:
            raise ValueError(f"Roughness must be between 0.0 and 1.0. Got: {roughness}")
    def __init__(self, name:str, track_type:str,country:str,length_km:float,roughness:float,lap_record_s):
        
        if track_type not in self.valid_tracks:
            raise ValueError(f"Invalid track type: {track_type}. Valid types are: {self.valid_tracks}")
        self._track_type = track_type
        self._name=name
        self._country=country
        self._length_km=length_km
        self._roughness=roughness
        self._lap_record_s=lap_record_s
        
        

        self.validate_length(length_km)
        self.validate_roughness(roughness)
    @property
    def name(self):
        return self._name
    @property
    def track_type(self):
        return self._track_type
    @property
    def country(self):
        return self._country
    
    @property
    def length_km(self):
        return self._length_km
    @property
    def roughness(self):
        return self._roughness
    
    @property
    def lap_record_s(self):
        return self._lap_record_s
    def is_street_circuit(self)->bool:
        return self._track_type=="street"
    def description(self)->str:
        return f"{self._name} ({self._country}) - {self.track_type} circuit, {self._length_km:.2f} km, roughness: {self._roughness:.2f}, lap record: {self._lap_record_s:.2f}s"
    def __repr__(self) -> str:
        return f"Track({self._name}, {self.track_type}, {self._country}, {self._length_km:.2f} km, roughness: {self._roughness:.2f}, lap record: {self._lap_record_s:.2f}s)"


monaco = Track("Monaco", "street", "Monaco", 3.337, 0.2, 71.382)
print(monaco)
print(monaco.description())
print(monaco.is_street_circuit())