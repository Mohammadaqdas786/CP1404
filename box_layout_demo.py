from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutDemo( BoxLayout ):
    def handle_greet(self):
        # Update the label with the greeting
        self.ids.output_label.text = f"Hello {self.ids.input_name.text}"

    def handle_clear(self):
        # Clear the text input and label
        self.ids.input_name.text = ''
        self.ids.output_label.text = ''


class MyApp( App ):
    def build(self):
        return BoxLayoutDemo()


if __name__ == '__main__':
    MyApp().run()
