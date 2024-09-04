class BaseInstrument():
    def __init__(self):
        self._instrument = None
        self._feedback = None
        
    @property
    def instrument(self):
        return self._instrument
    
    @instrument.setter
    def instrument(self, instrument):
        self._instrument = instrument
        
    @property
    def active(self):
        return self._instrument is not None
    
    def __str__(self) -> str:
        try:
            label = str(self.instrument)
        except ValueError:
            label = '--'
        return "[INST] " + label
    
    def feedback(self, message: str):
        pass