class RecentCounter:
    TIME_BUFFER = 3000

    def __init__(self):
        self.ping_times = []

    def ping(self, t: int) -> int:
        self.ping_times.append(t)

        i = 0
        while i < len(self.ping_times) and (
            self.ping_times[i] < (t - self.TIME_BUFFER)
        ):
            i += 1

        self.ping_times = self.ping_times[i:]

        return len(self.ping_times)
