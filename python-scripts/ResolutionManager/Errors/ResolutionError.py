

class ResolutionError(Exception):

    def __init__(self, og_error, resolution, method):
        self.og_error = og_error
        self.resolution = resolution
        self.method = method

    def __str__(self):
        return f"\n======\n{self.og_error}\n{self.resolution}\n======\n"
