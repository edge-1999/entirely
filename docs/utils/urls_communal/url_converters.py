class MenuId:
    regex = r'\d{1,5}'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value
