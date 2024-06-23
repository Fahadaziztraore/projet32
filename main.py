from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivy.config import Config
from kivy.core.window import Window
from kivymd.uix.textfield import MDTextField

KV="""

ScreenManager:
    First:

<First>:

    MDLabel:
        text:'    FAHADA'
        pos_hint:{'center_x':0.5,'center_y':0.9}
        font_size: '40sp'

    MDTextField:
        hint_text:'enter password'
        helper_text:'entrer au moins 8 caractere'
        font_size:'15sp'
        
        pos_hint:{'center_x':0.50,'center_y':0.6}
        
    
    MDLabel:
        text:'Password'
        pos_hint:{'center_x':0.85,'center_y':0.5}
        font_size: '20sp'

        
    MDRectangleFlatButton:
        text:'click me'
        pos_hint:{'center_x':0.5,'center_y':0.2}



        
"""

class First(Screen):
    pass


class Myapp(MDApp):
    def build(self):
        Window.size = (300,600)
        return Builder.load_string(KV)
    

if __name__=="__main__":
    Myapp().run()


