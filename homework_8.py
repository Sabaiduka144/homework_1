import datetime

ACTION_LOG = []

def log_action(message, *, timestamp=None):
    """Prints and stores a timestamped log entry."""
    if timestamp is None:
        timestamp = datetime.datetime.now()
    line = f"{timestamp.isoformat()} — {message}"
    ACTION_LOG.append(line)
    print(line)

class WeatherSnapshot:
    def __init__(self, temperature, humidity, observed_at):
        self.temperature = temperature
        self.humidity = humidity
        self.observed_at = observed_at

    def __repr__(self):
        ts = self.observed_at.isoformat(timespec='minutes')
        return f"WeatherSnapshot({ts}, {self.temperature}°C, {self.humidity}%)"

    def cool_down(self, delta=1):
        """Return a NEW snapshot with lower temperature."""
        return WeatherSnapshot(
            self.temperature - delta,
            self.humidity,
            self.observed_at
        )

class SmartIrrigator:
    def __init__(self, name, water_reserve, daily_limit):
        self.name = name
        self.water_reserve = water_reserve
        self.capacity = water_reserve
        self.daily_limit = daily_limit
        self.used_today = 0

    @property
    def needs_refill(self):
        return self.water_reserve < 0.2 * self.capacity

    def refill(self, amount):
        self.water_reserve += amount
        log_action(f"Refilled {amount}L into {self.name}")

    def sprinkle(self, volume):
        if self.used_today + volume > self.daily_limit:
            raise ValueError(f"{self.name} exceeded daily limit!")

        if volume > self.water_reserve:
            raise ValueError(f"{self.name} does not have enough water!")

        self.water_reserve -= volume
        self.used_today += volume

        log_action(f"Sprinkled {volume}L from {self.name}")

    def status(self):
        return (
            f"{self.name}: {self.water_reserve}L left, "
            f"used today={self.used_today}L, "
            f"limit={self.daily_limit}L"
        )


class SmartMister(SmartIrrigator):
    def __init__(self, name, water_reserve, daily_limit, humidity_boost=5):
        super().__init__(name, water_reserve, daily_limit)
        self.humidity_boost = humidity_boost

    def status(self):
        base = super().status()
        return base + f" (mister boost +{self.humidity_boost}%)"

class Greenhouse:
    def __init__(self):
        self.devices = {}

    def register_device(self, device):
        self.devices[device.name] = device
        log_action(f"Registered device {device.name}")
        return device

    def get_device(self, name):
        return self.devices.get(name)

    def total_water_remaining(self):
        return sum(d.water_reserve for d in self.devices.values())

    def busiest_device(self):
        if not self.devices:
            return None
        return max(self.devices.values(), key=lambda d: d.used_today)


if __name__ == "__main__":

    print("\n=== TASK 1: WeatherSnapshot ===")
    now = datetime.datetime(2025, 2, 14, 8, 0)

    snapshots = [
        WeatherSnapshot(18, 62, now),
        WeatherSnapshot(21, 55, now + datetime.timedelta(hours=1)),
        WeatherSnapshot(17, 70, now + datetime.timedelta(hours=2)),
        WeatherSnapshot(20, 68, now + datetime.timedelta(hours=3)),
    ]

    for snap in snapshots:
        print(snap, " -> cooled:", snap.cool_down())

    print("\n=== TASK 2 + 3: SmartIrrigator & Greenhouse ===")

    gh = Greenhouse()

    device1 = gh.register_device(SmartIrrigator("HerbGarden", 30, 10))
    device2 = gh.register_device(SmartIrrigator("VeggieBed", 50, 20))
    device3 = gh.register_device(SmartMister("MushroomZone", 40, 15, humidity_boost=12))

    device1.sprinkle(3)
    device2.sprinkle(5)
    device1.sprinkle(4)
    device3.sprinkle(6)
    device2.sprinkle(10)

    print("\n-- Device Status --")
    for dev in gh.devices.values():
        print(dev.status(), "| Needs refill:", dev.needs_refill)

    print("\nTotal remaining water:", gh.total_water_remaining())

    busiest = gh.busiest_device()
    if busiest:
        print("Busiest device:", busiest.name)

    expected = sum(d.water_reserve for d in gh.devices.values())
    assert gh.total_water_remaining() == expected

    print("\n=== ACTION LOG ===")
    for line in ACTION_LOG:
        print(line)
