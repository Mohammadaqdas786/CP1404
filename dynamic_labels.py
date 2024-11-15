from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabelsApp( BoxLayout ):
    def __init__(self, **kwargs):
        super( DynamicLabelsApp, self ).__init__( **kwargs )

        # List of names to display
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

        # Create and add a Label for each name in the list
        for name in self.names:
            label = Label( text=name, size_hint_y=None, height=40 )  # Set height for each label
            self.add_widget( label )


class MyApp( App ):
    def build(self):
        return DynamicLabelsApp()


if __name__ == '__main__':
    MyApp().run()