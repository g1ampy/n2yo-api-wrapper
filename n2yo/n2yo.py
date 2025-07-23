import logging, requests
from dacite import from_dict

from .models.search import TleData, SatellitePositionsData, VisualPassesData, RadioPassesData, SatellitesAboveData
from .exceptions import N2YOInvalidKeyException


# Set up logging - datetime format, level, and format
# Default to INFO level

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


class n2yo:
    def __init__(self, api_key: str)-> None: 

        self.apiKey = api_key
        self.params = {'apiKey': self.apiKey}

        self.base_url = f"https://api.n2yo.com"
        self.api_url = f"{self.base_url}/rest/v1/satellite/"
        
        logger.info("n2yo client initialization completed successfully")

    def get_tle(self,
            id: int) -> TleData:

        """
        Retrieve the Two Line Elements (TLE) for a satellite identified by NORAD id.

        
        **API Endpoint**  
            `/tle/{id}`

        **Parameters:**
            `id` (int): NORAD satellite ID (**required**)

        **Returns:**
            TleData: A structured object containing satellite data.

        **Response Fields:**
            `satid` (int): NORAD ID used in the request
            `satname` (str): Satellite name
            `transactionscount` (int): API transaction count in the past 60 minutes
            `tle` (str): Full Two Line Element set for the satellite
        """

        response = requests.get(url=f'{self.api_url}tle/{id}/', params=self.params)
        data = response.json()

        if data.get("error") == "Invalid API Key!":
            raise N2YOInvalidKeyException("The API key is invalid or missing.")
    
        result = from_dict(data_class=TleData, data=data)
        return result

    def get_satellite_positions(self,
                            id: int,
                            observer_lat: float,
                            observer_lng: float,
                            observer_alt: float,
                            seconds: float) -> SatellitePositionsData:
        
        """
        Retrieve the future positions of any satellite as footprints (latitude, longitude) to display orbits on maps. Also return the satellite's azimuth and elevation with respect to the observer location. Each element in the response array is one second of calculation. First element is calculated for current UTC time.


        **API Endpoint**  
            `/positions/{id}/{observer_lat}/{observer_lng}/{observer_alt}/{seconds}`

        **Parameters:**
            `id` (int): NORAD satellite ID
            `observer_lat` (float): Observer's latitude (decimal degrees)
            `observer_lng` (float): Observer's longitude (decimal degrees)
            `observer_alt` (float): Altitude above sea level (meters)
            `seconds` (int): Number of future seconds to calculate (max 300)

        **Returns:**
            SatellitePositionsData: A structured object containing satellite positions data.

        **Response Fields:**
            `satid` (int): NORAD ID used in request
            `satname` (str): Satellite name
            `transactionscount` (int): API usage in the past 60 minutes
            `satlatitude` (float): Satellite latitude projection on Earth's surface
            `satlongitude` (float): Satellite longitude projection on Earth's surface
            `azimuth` (float): Azimuth angle from observer to satellite (degrees)
            `elevation` (float): Elevation angle from observer to satellite (degrees)
            `ra` (float): Right ascension in celestial coordinates (degrees)
            `dec` (float): Declination in celestial coordinates (degrees)
            `timestamp` (int): UNIX timestamp for this position (UTC)
        """

        response = requests.get(url=f'{self.api_url}positions/{id}/{observer_lat}/{observer_lng}/{observer_alt}/{seconds}/', params=self.params)
        data = response.json()
        
        if data.get("error") == "Invalid API Key!":
            raise N2YOInvalidKeyException("The API key is invalid or missing.")
        
        result = from_dict(data_class=SatellitePositionsData, data=data)
        return result
    
    def get_visual_passes(self,
                    id: int,
                    observer_lat: float,
                    observer_lng: float,
                    observer_alt: float,
                    days: int,
                    min_visibility: int) -> VisualPassesData:
        
        """
        Get predicted visual passes for any satellite relative to a location on Earth. A 'visual pass' is a pass that should be optically visible on the entire (or partial) duration of crossing the sky. For that to happen, the satellite must be above the horizon, illumintaed by Sun (not in Earth shadow), and the sky dark enough to allow visual satellite observation.

        
        **API Endpoint**  
            `/visualpasses/{id}/{observer_lat}/{observer_lng}/{observer_alt}/{days}/{min_visibility}`

        **Parameters:**
            `id` (int): NORAD satellite ID
            `observer_lat` (float): Observer's latitude (decimal degrees)
            `observer_lng` (float): Observer's longitude (decimal degrees)
            `observer_alt` (float): Observer's altitude (meters)
            `days` (int): Number of days to search (max 10)
            `min_visibility` (int): Minimum number of seconds satellite must be visible to include the pass

        **Returns:**
            VisualPassesData: A structured object containing visual passes data.
            
        **Response Fields:**
            `satid` (int): Same NORAD ID provided in input
            `satname` (str): Name of the satellite
            `transactionscount` (int): Number of API calls in the last 60 minutes
            `passescount` (int): Number of passes returned
            `startAz` (float): Azimuth at start of pass (degrees)
            `startAzCompass` (str): Cardinal direction of start azimuth (e.g., N, NE, E, SE, ...)
            `startEl` (float): Elevation at start of pass (degrees)
            `startUTC` (int): UNIX timestamp for start of pass (UTC)
            `maxAz` (float): Azimuth at max elevation point
            `maxAzCompass` (str): Cardinal direction of max azimuth
            `maxEl` (float): Maximum elevation during pass (degrees)
            `maxUTC` (int): UNIX timestamp for max elevation point (UTC)
            `endAz` (float): Azimuth at end of pass
            `endAzCompass` (str): Cardinal direction of end azimuth
            `endEl` (float): Elevation at end of pass (degrees)
            `endUTC` (int): UNIX timestamp for end of pass (UTC)
            `mag` (float): Maximum visual magnitude (smaller = brighter; 100000 = unknown)
            `duration` (int): Total visible duration of the pass (in seconds)
        """

        response = requests.get(url=f'{self.api_url}visualpasses/{id}/{observer_lat}/{observer_lng}/{observer_alt}/{days}/{min_visibility}/', params=self.params)
        data = response.json()

        if data.get("error") == "Invalid API Key!":
            raise N2YOInvalidKeyException("The API key is invalid or missing.")
    
        result = from_dict(data_class=VisualPassesData, data=data)
        return result
    
    def get_radio_passes(self,
                    id: int,
                    observer_lat: float,
                    observer_lng: float,
                    observer_alt: float,
                    days: int,
                    min_elevation: int) -> RadioPassesData:
       
        """
        The 'radio passes' are similar to 'visual passes', the only difference being the requirement for the objects to be optically visible for observers. This function is useful mainly for predicting satellite passes to be used for radio communications. The quality of the pass depends essentially on the highest elevation value during the pass, which is one of the input parameters.

        
        **API Endpoint**  
            `/radiopasses/{id}/{observer_lat}/{observer_lng}/{observer_alt}/{days}/{min_elevation}`

        **Parameters:**
            `id` (int): NORAD ID of the satellite
            `observer_lat` (float): Observer's latitude in decimal degrees
            `observer_lng` (float): Observer's longitude in decimal degrees
            `observer_alt` (float): Observer's altitude in meters
            `days` (int): Number of days to search for passes
            `min_elevation` (int): Minimum elevation angle (in degrees) to consider the pass valid

        **Returns:**
            RadioPassesData: A structured object containing radio passes data.

        **Response Fields:**
            `satid` (int): Same NORAD ID provided in input
            `satname` (str): Name of the satellite
            `transactionscount` (int): Number of API transactions in the last hour
            `passescount` (int): Number of passes returned
            `startAz` (float): Azimuth at start of pass (degrees)
            `startAzCompass` (str): Cardinal direction of start azimuth (e.g., N, NE, E)
            `startUTC` (int): UNIX timestamp of pass start (UTC)
            `maxAz` (float): Azimuth at max elevation point
            `maxAzCompass` (str): Cardinal direction of max azimuth
            `maxEl` (float): Maximum elevation during pass (degrees)
            `maxUTC` (int): UNIX timestamp of max elevation point (UTC)
            `endAz` (float): Azimuth at end of pass
            `endAzCompass` (str): Cardinal direction of end azimuth
            `endUTC` (int): UNIX timestamp of pass end (UTC)
        """

        response = requests.get(url=f'{self.api_url}radiopasses/{id}/{observer_lat}/{observer_lng}/{observer_alt}/{days}/{min_elevation}/', params=self.params)
        data = response.json()

        if data.get("error") == "Invalid API Key!":
            raise N2YOInvalidKeyException("The API key is invalid or missing.")
        
        result = from_dict(data_class=RadioPassesData, data=data)
        return result
    
    def get_above(
            self, 
            observer_lat: float, 
            observer_lng: float,
            observer_alt: float,
            search_radius: int,
            category_id: int) -> SatellitesAboveData:
        
        """
        The 'above' function will return all objects within a given search radius above observer's location. The radius (θ), expressed in degrees, is measured relative to the point in the sky directly above an observer (azimuth).

        
        **API Endpoint**
            /above/{observer_lat}/{observer_lng}/{observer_alt}/{search_radius}/{category_id}

        **Parameters:**
            observer_lat (float): Latitude in decimal degrees.
            observer_lng (float): Longitude in decimal degrees.
            observer_alt (float): Altitude above sea level (in meters).
            search_radius (int): Search radius in degrees (0–90).
            category_id (int): Satellite category ID (use 0 for all categories).

        **Returns:**
            SatellitesAboveData: A structured object containing satellite pass data.

        **Response Fields:**
            category (str): Category name (e.g., "ANY" if ID = 0)
            transactionscount (int): API calls in the last 60 minutes
            satcount (int): Number of satellites returned
            startAz (float): Start azimuth in degrees
            satid (int): NORAD satellite ID
            intDesignator (str): International designator
            satname (str): Satellite name
            launchDate (str): Format YYYY-MM-DD
            satlat (float): Satellite latitude
            satlng (float): Satellite longitude
            satalt (float): Satellite altitude (km)
        """         

        response = requests.get(url=f'{self.api_url}above/{observer_lat}/{observer_lng}/{observer_alt}/{search_radius}/{category_id}/', params=self.params)
        data = response.json()

        if data.get("error") == "Invalid API Key!":
            raise N2YOInvalidKeyException("The API key is invalid or missing.")
        
        result = from_dict(data_class=SatellitesAboveData, data=data)

        return result