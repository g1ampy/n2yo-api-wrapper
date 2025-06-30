from dataclasses import dataclass
from typing import List, Optional


@dataclass
class SatelliteInfo:
    category: Optional[str] # Category name (ANY if category id requested was 0)
    satid: Optional[int] # NORAD id used in input
    satcount : Optional[int] # Count of satellites returned
    satname: Optional[str] # Satellite name
    transactionscount: int # Count of transactions performed with this API key in last 60 minutes
    passescount: Optional[int] # Count of passes returned

@dataclass
class SatellitePosition:
    satlatitude: float # Satellite footprint latitude (decimal degrees format)
    satlongitude: float # Satellite footprint longitude (decimal degrees format)
    azimuth: float # Satellite azimuth with respect to observer's location (degrees)
    elevation: float # Satellite elevation with respect to observer's location (degrees)
    ra: float # Satellite right ascension (degrees)
    dec: float # Satellite declination (degrees)
    timestamp: int # Unix time for this position (seconds). You should convert this UTC value to observer's time zone

@dataclass
class VisualPass:
    startAz: float # Satellite azimuth for the start of this pass (relative to the observer, in degrees)
    startAzCompass: str # Satellite azimuth for the start of this pass (relative to the observer). Possible values: N, NE, E, SE, S, SW, W, NW
    startEl: float # Satellite elevation for the start of this pass (relative to the observer, in degrees)
    startUTC: int # Unix time for the start of this pass. You should convert this UTC value to observer's time zone
    maxAz: float # Satellite azimuth for the max elevation of this pass (relative to the observer, in degrees)
    maxAzCompass: str # Satellite azimuth for the max elevation of this pass (relative to the observer). Possible values: N, NE, E, SE, S, SW, W, NW
    maxEl: float # Satellite max elevation for this pass (relative to the observer, in degrees)
    maxUTC: int # Unix time for the max elevation of this pass. You should convert this UTC value to observer's time zone
    endAz: float # Satellite azimuth for the end of this pass (relative to the observer, in degrees)
    endAzCompass: str # Satellite azimuth for the end of this pass (relative to the observer). Possible values: N, NE, E, SE, S, SW, W, NW
    endEl: float #Satellite elevation for the end of this pass (relative to the observer, in degrees)
    endUTC: int # Unix time for the end of this pass. You should convert this UTC value to observer's time zone
    mag: float # Max visual magnitude of the pass, same scale as star brightness. If magnitude cannot be determined, the value is 100000
    duration: int # Total visible duration of this pass (in seconds)

@dataclass
class RadioPass:
    startAz: float # Satellite azimuth for the start of this pass (relative to the observer, in degrees)
    startAzCompass: str # Satellite azimuth for the start of this pass (relative to the observer). Possible values: N, NE, E, SE, S, SW, W, NW
    startUTC: int # Unix time for the start of this pass. You should convert this UTC value to observer's time zone
    maxAz: float # Satellite azimuth for the max elevation of this pass (relative to the observer, in degrees)
    maxAzCompass: str # Satellite azimuth for the max elevation of this pass (relative to the observer). Possible values: N, NE, E, SE, S, SW, W, NW
    maxEl: float # Satellite max elevation for this pass (relative to the observer, in degrees)
    maxUTC: int # Unix time for the max elevation of this pass. You should convert this UTC value to observer's time zone
    endAz: float # Satellite azimuth for the end of this pass (relative to the observer, in degrees)
    endAzCompass: str # Satellite azimuth for the end of this pass (relative to the observer). Possible values: N, NE, E, SE, S, SW, W, NW
    endUTC: int # Unix time for the end of this pass. You should convert this UTC value to observer's time zone

@dataclass
class SatelliteAbove:
    satid: int # Satellite NORAD id
    intDesignator: str # Satellite international designator
    satname: str # Satellite name
    launchDate: str # Satellite launch date (YYYY-MM-DD)
    satlat: float # Satellite footprint latitude (decimal degrees format)
    satlng: float # Satellite footprint longitude (decimal degrees format)
    satalt: float # Satellite altitude (km)

@dataclass
class TleData:
    info: SatelliteInfo
    tle: str # TLE on single line string. Split the line in two by \r\n to get original two lines

@dataclass
class SatellitePositionsData:
    info: SatelliteInfo
    positions: List[SatellitePosition]

@dataclass
class VisualPassesData:
    info: SatelliteInfo
    passes: List[VisualPass]

@dataclass
class RadioPassesData:
    info: SatelliteInfo
    passes: List[RadioPass]

@dataclass
class SatellitesAboveData:
    info: SatelliteInfo
    above: List[SatelliteAbove]