"""Helper class/library to smoothly work with time zone aware datetime objects that easily convert between timezones."""
import datetime
import pytz
import tzlocal

from adatetime import adatetime as adt

# Example usage:
print('\n# Example usage:')
try:
    # Current time in local timezone
    print('\n# Current time in local timezone')
    now_local = adt()
    print(now_local)
    print(f"UTC: {now_local.utc}")
    print(f"Local: {now_local.local}")

    # Specific time in a specific timezone
    print('\n# Specific time in a specific timezone')
    dt = datetime.datetime(2024, 10, 28, 12, 30, 0)
    ny_time = adt(dt, "America/New_York")
    print(ny_time)
    print(f"UTC: {ny_time.utc}")
    print(f"New York: {ny_time.local}")

    # Timezone object directly
    print('\n# Timezone object directly')
    london_tz = pytz.timezone("Europe/London")
    london_time = adt(dt, london_tz)
    print(london_time)
    print(f"UTC: {london_time.utc}")
    print(f"London: {london_time.local}")

    # Convert to a different timezone
    print('\n# Convert to a different timezone')
    la_time = ny_time.to_datetime("America/Los_Angeles")
    print(f"Los Angeles time from NY time: {la_time}")

    berlin_time = ny_time.to_datetime(pytz.timezone("Europe/Berlin"))
    print(f"Berlin time from NY time: {berlin_time}")

    # Print
    print('\n# Print')
    print(adt(dt, "Europe/Stockholm"))

except ValueError as e:
    print(f"Error: {e}")
except TypeError as e:
    print(f"Error: {e}")
