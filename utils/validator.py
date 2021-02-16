from datetime import datetime
from typing import  Union

from models.errors import MissingDateParameter
from utils.formatter import Formatter


class Validator:
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
