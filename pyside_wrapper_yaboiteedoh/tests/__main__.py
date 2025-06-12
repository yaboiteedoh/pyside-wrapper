from pyside_wrapper_yaboiteedoh.components import (
    TApp
)
from pyside_wrapper_yaboiteedoh.widgets import (
    TLabeledInput
)

class App(TApp):
    def __init__(self):
        super().__init__(title='Testing')

        frame = TLabeledInput('TESTING')
        frame.greedy.connect(self.surrender)
        frame.greedy.emit()

        self.exec()

if __name__ == '__main__':
    App()
