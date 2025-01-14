"""Helper class/library to smoothly work with time zone aware datetime objects that easily convert between timezones."""
import datetime
import pytz
import tzlocal
import pandas as pd

class adatetime:
    """An aware datetime object that helps you manage timezones."""

    def __init__(self, dt=None, tz=None):
        """
        Creates an aware datetime object.

        Args:
            dt: A naive datetime object. If None, the current time is used.
            tz: A pytz timezone object or a timezone name string. If None,
                the system's local timezone is used.
        """

        if dt is None:
            dt = datetime.datetime.utcnow()  # Start with UTC naive

        if tz is None:
            try:
                self.tz = tzlocal.get_localzone()
            except pytz.UnknownTimeZoneError:
                print("Could not determine local timezone. Defaulting to UTC.")
                self.tz = pytz.utc
        elif isinstance(tz, str):
            try:
                self.tz = pytz.timezone(tz)
            except pytz.UnknownTimeZoneError as exc:
                raise ValueError(f"Invalid timezone: {tz}") from exc
        elif isinstance(tz, pytz.BaseTzInfo):
            self.tz = tz
        else:
            raise TypeError("tz must be a string or a pytz timezone object")

        self._utc_dt = pytz.utc.localize(dt)
        self._local_dt = self._utc_dt.astimezone(self.tz)

    @property
    def utc(self):
        """Returns the datetime in UTC."""
        return self._utc_dt

    @property
    def local(self):
        """Returns the datetime in the specified timezone."""
        return self._local_dt

    def __repr__(self):
      return f"adatetime(utc={self.utc.isoformat()}, local={self.local.isoformat()}, timezone={self.tz})"

    def to_datetime(self, tz=None):
        """Returns a datetime object in a specific timezone. Defaults to local if tz is None"""
        if tz is None:
            return self.local
        elif isinstance(tz, str):
            try:
                target_tz = pytz.timezone(tz)
            except pytz.UnknownTimeZoneError:
                raise ValueError(f"Invalid timezone: {tz}")
            return self.utc.astimezone(target_tz)
        elif isinstance(tz, pytz.BaseTzInfo):
            return self.utc.astimezone(tz)
        else:
             raise TypeError("tz must be a string or a pytz timezone object")

    def __str__(self):
        """Returns a formatted string representation of the adatetime object."""
        local_str = self.local.strftime('%Y-%m-%d %H:%M:%S %Z%z')
        utc_str = self.utc.strftime('%Y-%m-%d %H:%M:%S')
        return f"{local_str} ({self.tz}) [{utc_str} UTC]"
