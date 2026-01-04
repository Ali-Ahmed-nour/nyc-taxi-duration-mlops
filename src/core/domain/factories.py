from datetime import datetime

# Importing from specific modules as suggested by Pylance
from factory.base import Factory
from factory.declarations import Sequence, SubFactory

from src.core.domain import TaxiTrip, Location


class LocationFactory(Factory):
    """Factory for Location domain model."""

    class Meta:
        model = Location

    # Unique ID generation
    # Use string prefixes to avoid ambiguity between different ID types in logs (e.g., LOC-1 vs TRIP-1)
    # This also ensures flexibility for future non-numeric IDs (like UUIDs)
    location_id = Sequence(lambda n: f"LOC-{n}")


class TaxiTripFactory(Factory):
    """Factory for TaxiTrip domain model."""

    class Meta:
        model = TaxiTrip

    trip_id = Sequence(lambda n: f"TRIP-{n}")
    pickup_loc = SubFactory(LocationFactory)
    dropoff_loc = SubFactory(LocationFactory)

    # Default time values
    pickup_time = datetime(2026, 1, 1, 10, 0)
    dropoff_time = datetime(2026, 1, 1, 10, 30)
