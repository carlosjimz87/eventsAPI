from datetime import datetime


class Formatter:
    @staticmethod
    def str_to_date(date: str) -> datetime:
        if "z" in date.lower():
            date = date.lower().replace("z", "+00:00")
        if "+0000" in date.lower():
            date = date.replace("+0000", "+00:00")
        return datetime.fromisoformat(date)

