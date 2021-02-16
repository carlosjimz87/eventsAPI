from datetime import datetime, timedelta
from typing import Union, Dict, List, Optional

from models.errors import MissingDateParameter
from utils.formatter import Formatter


class Validator:

    @staticmethod
    def is_online(event: Dict) -> bool:
        try:
            return event["sell_mode"] == "online"
        except KeyError:
            print("Event has no sell_mode attribute.")

    @staticmethod
    def is_valid_date(date: Union[str, datetime]) -> datetime:

        if date is None:
            raise MissingDateParameter("Date parameter is necessary.")

        if isinstance(date, str):
            return Formatter.str_to_date(date)

        elif isinstance(date, datetime):
            return date

        else:
            raise ValueError("Invalid date parameter")

    @staticmethod
    def range_of_dates(starts_at: datetime, ends_at: Optional[datetime] = None, days: Optional[int] = 10) -> List[datetime]:
        # for internal use we allow a 10 days range creation
        ends_at = starts_at + timedelta(days=days-1) if not ends_at else ends_at

        delta = Validator.delta(ends_at, starts_at)
        return [(ends_at - timedelta(days=i)) for i in range(delta.days + 1)]

    @staticmethod
    def delta(ends_at: datetime, starts_at: datetime) -> timedelta:
        return abs(ends_at - starts_at)
