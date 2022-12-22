import sys
import json
from .station import Station


class StationsException(Exception):
  ...


class Stations:
  def __init__(self):
    self._list: list[Station] = []

  def add_station(self, station: Station):
    self._list.append(station)
    return self

  def load(self, path: str):
    for st in json.load(open(path, 'r')):
      try:
        self.add_station(Station(st["location"]["lat"], st["location"]["lon"]))
      except:
        ...

  def distance_between(self, a: Station, b: Station):
    return ((a.lat - b.lat) ** 2 + (a.lon - b.lon) ** 2) ** 0.5

  def triangle_area(self, a: Station, b: Station, c: Station) -> float:
    d1 = self.distance_between(a, b)
    d2 = self.distance_between(b, c)
    d3 = self.distance_between(a, c)
    p = (d1 + d2 + d3) / 2

    return (p * (p - d1) * (p - d2) * (p - d3)) ** 0.5

  def find_minimal_triangle_by_area(self) -> float:
    min_area = sys.maxsize

    for i in range(len(self._list)):
      for j in range(len(self._list)):
        for k in range(len(self._list)):
          if i != j and j != k and i != k:
            area = self.triangle_area(
                self._list[i], self._list[j], self._list[k])
            if area < min_area:
              min_area = area

    return min_area


st = Stations()
print(st.find_minimal_triangle_by_area())
