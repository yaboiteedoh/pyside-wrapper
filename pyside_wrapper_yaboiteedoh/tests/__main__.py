from pyside_wrapper_yaboiteedoh.components import (
    TApp,
    TCheckBox
)
from pyside_wrapper_yaboiteedoh.widgets import (
    TFlexFrame
)

class App(TApp):
    def __init__(self):
        super().__init__(title='Testing')

        frame = TFlexFrame(frame_style=['box', 'plain', 3, 3])
        label = frame.add_widget(
            TCheckBox(
                'TESTING'
            )
        )
        spacer = frame.add_widget(TFlexFrame(), stretch=1)

        frame.greedy.connect(self.surrender)
        frame.greedy.emit()
        frame.value = 'YUGE'

        self.exec()

if __name__ == '__main__':
    App()
