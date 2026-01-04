# tests/test_trip_model.py
import pytest
from datetime import datetime, timedelta
from src.core.domain.model import TaxiTrip, Location


@pytest.fixture
def loc():
    return Location("A")


# 1. Normal Trip (Happy Path)
def test_normal_trip_is_valid(loc):
    start = datetime(2026, 1, 1, 10, 0)
    end = start + timedelta(minutes=15)  # 15 mins
    trip = TaxiTrip("T1", loc, loc, start, end)
    assert trip.is_valid_for_model() is True


# 2. Lower Boundary (Exactly 1 minute)
def test_one_minute_is_valid(loc):
    start = datetime(2026, 1, 1, 10, 0)
    end = start + timedelta(minutes=1)
    trip = TaxiTrip("T2", loc, loc, start, end)
    assert trip.is_valid_for_model() is True


# 3. Upper Boundary (Exactly 60 minutes)
def test_sixty_minutes_is_valid(loc):
    start = datetime(2026, 1, 1, 10, 0)
    end = start + timedelta(minutes=60)
    trip = TaxiTrip("T3", loc, loc, start, end)
    assert trip.is_valid_for_model() is True


# 4. Out of Bounds (More than 60 minutes)
def test_sixty_one_minutes_is_invalid(loc):
    start = datetime(2026, 1, 1, 10, 0)
    end = start + timedelta(minutes=61)
    trip = TaxiTrip("T4", loc, loc, start, end)
    assert trip.is_valid_for_model() is False


# 5. Logical Error (Negative duration)
def test_negative_duration_is_invalid(loc):
    start = datetime(2026, 1, 1, 10, 15)
    end = datetime(2026, 1, 1, 10, 0)
    trip = TaxiTrip("T5", loc, loc, start, end)
    assert trip.is_valid_for_model() is False
