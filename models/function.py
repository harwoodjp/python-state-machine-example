class Function:
    def __init__(self, fn: callable):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs)
