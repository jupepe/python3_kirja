# Periytyminen

class Language:
    def __init__(self, **kwargs):
        if "name" in kwargs:
            self._name = kwargs["name"]
        else:
            self._name = None
        if "version" in kwargs:
            self._version = kwargs["version"]
        else:
            self._version = None

    def version(self, version=None):
        if version is not None:
            self._version = version
        return self._version

    def name(self, name=None):
        if name is not None:
            self._name = name
        return self._name

    def __str__(self):
        return f"{self._name}, {self._version}"


class WebLanguage(Language):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if "markup" in kwargs:
            self._markup = kwargs["markup"]
        else:
            self._markup = None
        if "documentation" in kwargs:
            self._documentation = kwargs["documentation"]
        else:
            self._documentation = None

    def markup(self, markup=None):
        if markup is not None:
            self._markup = markup
        return self._markup

    def documentation(self, documentation=None):
        if documentation is not None:
            self._documentation = documentation
        return self._documentation

    def __str__(self):
        return f"{super().__str__()}, {self._markup}, {self._documentation}"


java = WebLanguage(name="Java", version="14", markup="HTML5", documentation="Javadoc")
print(java)
java.markup("Markdown")
print(java)

java._documentation = "HTML"
print(java)

python = WebLanguage(name="Python", version="3.10", markup="md")
print(python)

print(WebLanguage())
