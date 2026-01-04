# tests/test_trip_model.py (using Factory)
from src.core.domain import TaxiTripFactory
from datetime import datetime, timedelta


# 4. Out of Bounds (More than 60 minutes) - Clean Version
def test_sixty_one_minutes_is_invalid_with_factory():
    start = datetime(2026, 1, 1, 10, 0)
    # بنغير بس اللي محتاجينه، والفاكتوري بيكمل الباقي (IDs, Locations)
    trip = TaxiTripFactory(
        pickup_time=start, dropoff_time=start + timedelta(minutes=61)
    )
    assert trip.is_valid_for_model() is False
