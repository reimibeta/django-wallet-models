class CurrentInstance:
    current_condition = None
    current_instance = None
    current_amount = None

    def __init__(
            self,
            current_condition=None,
            current_instance=None,
            current_amount=None
    ):
        self.current_condition = current_condition
        self.current_instance = current_instance
        self.current_amount = current_amount


class LastInstance:
    last_condition = None
    last_instance = None
    last_amount = None

    def __init__(
            self,
            last_condition=None,
            last_instance=None,
            last_amount=None
    ):
        self.last_condition = last_condition
        self.last_instance = last_instance
        self.last_amount = last_amount
