from dataclasses import dataclass


@dataclass
class Station:
  def __init__(self, lat: float, lon: float):
    self.lat = lat
    self.lon = lon
