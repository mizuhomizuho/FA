import datetime

class Tools:

    @staticmethod
    def now_utc():
        return datetime.datetime.fromtimestamp(datetime.datetime.now(datetime.UTC).timestamp())