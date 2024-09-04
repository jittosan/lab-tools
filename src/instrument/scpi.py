from .base import BaseInstrument

class SCPIInstrument(BaseInstrument):
    def __init__(self):
        super().__init__()
        self._instrument = None

    def __str__(self) -> str:
        try:
            label = str(self.instrument)
        except ValueError:
            label = '--'
        return "[SCPI] " + label
    
    def ident(self) -> str:
        return self.query("*IDN?")

    def write(self, command: str):
        self.instrument.write(command)
        
    def query(self, command: str) -> str:
        return self.instrument.query(command)
    
    def read(self) -> str:
        return self.instrument.read()
    
    def read_raw(self) -> bytes:
        return self.instrument.read_raw()
    
    def read_values(self) -> list:
        return self.instrument.read_values()
    
    def read_binary_values(self, datatype: str, is_big_endian: bool, termination: str, encoding: str) -> list:
        return self.instrument.read_binary_values(datatype, is_big_endian, termination, encoding)
    
    def read_ascii_values(self, converter: str, separator: str, container: str) -> list:
        return self.instrument.read_ascii_values(converter, separator, container)
    
    def read_complex(self, datatype: str, is_big_endian: bool, termination: str, encoding: str) -> list:
        return self.instrument.read_complex(datatype, is_big_endian, termination, encoding)
    
    def read_float(self, datatype: str, is_big_endian: bool, termination: str, encoding: str) -> float:
        return self.instrument.read_float(datatype, is_big_endian, termination, encoding)
    
    def read_int(self, datatype: str, is_big_endian: bool, termination: str, encoding: str) -> int:
        return self.instrument.read_int(datatype, is_big_endian, termination, encoding)
    
    def read_long(self, datatype: str, is_big_endian: bool, termination: str, encoding: str) -> int:
        return self.instrument.read_long(datatype, is_big_endian, termination, encoding)
    
    def read_short(self, datatype: str, is_big_endian: bool, termination: str, encoding: str) -> int:
        return self.instrument.read_short(datatype, is_big_endian, termination, encoding)
    
    def read_string(self, datatype: str, is_big_endian: bool, termination: str, encoding: str) -> str:
        return self.instrument.read_string(datatype, is_big_endian, termination, encoding)