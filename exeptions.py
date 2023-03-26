class NotSpaceRequired(Exception):
    message = "Не достаточно свободного места"


class NotRequiredPosution(Exception):
    message = "Нет запрошенной позиции"


class NotRequiredCountAvailable(Exception):
    message = "Нет запрошенного количества"


class ToManyPositions(Exception):
    message = "Слишком много уникальных позиций"

class RequestError(Exception):
    message = "Ошибка формата запроса"

class NotPointForRequest(Exception):
    message = "Нет магазина или склада указанного в запросе"