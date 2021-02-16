from datetime import datetime
from typing import Any


class Formatter:
    @staticmethod
    def str_to_date(date: Any) -> datetime:
        return datetime.fromisoformat(Formatter.replace_utf_format(date))

    @staticmethod
    def replace_utf_format(date: Any) -> str:
        return date.replace("Z", "+00:00")
