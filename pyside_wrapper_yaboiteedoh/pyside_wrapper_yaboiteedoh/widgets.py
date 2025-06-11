from PySide6.QtWidgets import (
    QRadioButton
)

from .components import TFrame


class RadioMenu(TFrame):
    def __init__(
        self,
        label,
        *args,
        options=[],
        default='',
        size_policy='',
        **kwargs
    ):
        super().__init__(
            *args,
            label=label,
            size_policy=size_policy,
            **kwargs
        )

        self.options = options
        if default:
            self.value = default


    @property
    def options(self):
        return [option.text() for option in self.children]


    @options.setter
    def options(self, options: list[str]):
        selection = self.value
        self.clear_widgets()
        self.populate(
            QRadioButton,
            [{'text': option} for option in options]
        )
        self.value = selection


    @property
    def value(self):
        for option in self.children:
            if option.isChecked():
                return option.text()


    @value.setter
    def value(self, value):
        if value in self.options:
            for option in self.children:
                if option.text() == value:
                    option.setChecked()

