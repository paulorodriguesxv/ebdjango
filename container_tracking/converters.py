class ContainerNumberConverter:
    regex = '[A-Z]{4}\d{7}'

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return "%s" % value