from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.image import Image
# initialize the app
class MainApp(App):
    def build(self):
        # creating a button
        button = Button(text = 'Hey yall', size_hint=(1, .5),
        )
        button.bind(on_press = self.on_press_button)
        return button
    def on_press_button(self, instance):
        print('You pressed the button!')

        img = Image(source='https://images.pexels.com/photos/4173624/pexels-photo-4173624.jpeg?cs=srgb&dl=pexels-elijah-o%27donnell-4173624.jpg&fm=jpg',size_hint=(1, .5), pos_hint={'center_x':.5, 'center_y':.5})

        return img 
# kivy app windown runs as long as 
if __name__ == '__main__':
    MainApp().run()
