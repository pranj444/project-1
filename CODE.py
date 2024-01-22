from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from datetime import datetime

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        current_date = datetime.now()
        day, month, year = current_date.day, current_date.month, current_date.year
        intermediate_result = day * year + month
        final_result = intermediate_result * 365

        intermediate_result_label = Label(text=f'Intermediate Result: {intermediate_result}', font_size=18)
        final_result_label = Label(text=f'Final Result: {final_result}', font_size=18)

        layout.add_widget(intermediate_result_label)
        layout.add_widget(final_result_label)

        return layout

if __name__ == '__main__':
    MyApp().run()
