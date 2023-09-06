class Questions:
    qestion_no: int = -1
    ques: str = ""
    option_a: str = ""
    option_b: str = ""
    option_c: str = ""
    option_d: str = ""
    right: int = -1

    def __init__(self, qestion_no, ques, option_a, option_b, option_c, option_d, right):
        self.right = right
        self.ques = ques
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.option_d = option_d
        self.qestion_no = qestion_no

    def get_right(self):
        if self.right == 1:
            return self.option_a
        elif self.right == 2:
            return self.option_b
        elif self.right == 3:
            return self.option_c
        elif self.right == 4:
            return self.option_d
        else:
            return "error!!"