"""Defines the data objects to be used by the view_model.py file"""

class TrackingData:
    """Model class representing the data from Open Notify -- ISS API"""

    def __init__(self, longitude: float, latitude: float, timestamp: str, vessel_name: str):
        self.longitude = longitude
        self.latitude = latitude
        self.timestamp = timestamp
        self.vessel_name = vessel_name

    @property
    def longitude(self) -> float:
        """Getter Method for longitude field"""
        return self._longitude

    @longitude.setter
    def longitude(self, value: float) -> None:
        self._longitude = value

    @property
    def latitude(self) -> float:
        """Getter Method for latitude field"""
        return self._latitude

    @latitude.setter
    def latitude(self, value: float) -> None:
        self._latitude = value

    @property
    def timestamp(self) -> str:
        """Getter Method for timestamp field"""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: str) -> None:
        self._timestamp = value

    @property
    def vessel_name(self) -> str:
        """Getter Method for vessel_name field"""
        return self._vessel_name

    @vessel_name.setter
    def vessel_name(self, value: str) -> None:
        self._vessel_name = value
