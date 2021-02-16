from datetime import datetime
from typing import Any


class Formatter:
    @staticmethod
    def str_to_date(date: str) -> datetime:
        return datetime.fromisoformat(Formatter.replace_utf_format(date))

    @staticmethod
    def date_to_str(date: datetime) -> str:
        return str(date.date())

    @staticmethod
    def replace_utf_format(date: str) -> str:
        return date.replace("Z", "+00:00")
