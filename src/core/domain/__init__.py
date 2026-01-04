from .model import TaxiTrip, Location
from .factories import TaxiTripFactory

# This defines what is accessible when someone imports from 'src.core.domain'
__all__ = ["TaxiTrip", "Location", "TaxiTripFactory"]
