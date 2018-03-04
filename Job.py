class Job:
    def __init__(self, _url, _title, _type, _publish, _expire, _address, _description, args):
        self.url = _url
        self.title = _title
        self.type = _type
        self.publishment = _publish
        self.expire = _expire
        self.address = _address
        self.description = _description
        self.info = []
        for arg in args:
            self.info.append(arg)
