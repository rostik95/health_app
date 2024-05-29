from wtforms import FloatField


class MyFloatField(FloatField):
    def process_formdata(self, valuelist):
        if valuelist:
            try:
                self.data = float(valuelist[0].replace(",", "."))
            except ValueError:
                self.data = None
                raise ValueError(self.gettext("Not a valid float value"))
