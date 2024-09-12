from .seat_status import SeatStatus
from .seat_type import SeatType


class Seat:
    def __init__(self, seat_id: str, row: int, column: int, seat_type: SeatType, price: float, status: SeatStatus):
        self._id = seat_id
        self._row = row
        self._column = column
        self._type = seat_type
        self._price = price
        self._status = status

    @property
    def id(self):
        return self._id

    @property
    def row(self):
        return self._row

    @property
    def column(self):
        return self._column

    @property
    def price(self):
        return self._price

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status: SeatStatus):
        self._status = status
