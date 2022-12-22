from mlib.stations import Stations, Station
import pytest


class TestStations:
  stations = Stations()
  stations\
      .add_station(Station(1, 10))\
      .add_station(Station(5, 7))\
      .add_station(Station(14, 15))
  s1, s2, s3 = stations._list

  def test_distance(self):
    assert self.stations.distance_between(
        self.s1, self.s2) == 5

  def test_triangle_area(self):
    assert self.stations.triangle_area(
        self.s1, self.s2, self.s3) == pytest.approx(29.5, 0.1)

  def test_min_area(self):
    self.stations._list.clear()
    self.stations.load('stations.json')
    assert self.stations.find_minimal_triangle_by_area() == pytest.approx(9.38, 0.01)
