
import sys
sys.stdout.reconfigure(encoding='utf-8') 
import os
import json
from datetime import datetime
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.core.text import LabelBase
from kivy.utils import platform
from kivy.core.window import Window

try:
    LabelBase.register(name='Vazir',fn_regular='fonts/Vazirmatn-Regular.ttf')
    FONT_NAME = 'Vazir'
except:
    FONT_NAME = 'Roboto'

class PersianLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = FONT_NAME
        self.halign = 'right'
        self.text_size = (self.width, None)
        self.bind(width=self.update_text_size)
    
    def update_text_size(self, *args):
        self.text_size = (self.width, None)

class MainApp(App):
    def build(self):
        self.title = "یادآور قرص - فارسی"
        
        if platform != 'android':
            Window.size = (400, 700)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # عنوان
        title = PersianLabel(
            text='💊 یادآور مصرف قرص',
            font_size='28sp',
            size_hint=(1, 0.2)
        )
        layout.add_widget(title)
        
        # دکمه‌ها
        buttons = [
            ('📝 افزودن قرص جدید', self.add_pill),
            ('📋 لیست قرص‌ها', self.show_pills),
            ('⚙️ تنظیمات', self.settings),
            ('🚪 خروج', self.exit_app)
        ]
        
        for text, callback in buttons:
            btn = Button(
                text=text,
                font_name=FONT_NAME,
                size_hint=(1, 0.15),
                background_color=(0.2, 0.6, 0.8, 1),
                background_normal=''
            )
            btn.bind(on_press=callback)
            layout.add_widget(btn)
        
        return layout
    
    def add_pill(self, instance):
        content = BoxLayout(orientation='vertical', padding=20, spacing=15)
        content.add_widget(PersianLabel(text='قرص جدید اضافه شد!'))
        
        popup = Popup(
            title='موفقیت',
            content=content,
            size_hint=(0.8, 0.4)
        )
        popup.open()
    
    def show_pills(self, instance):
        content = BoxLayout(orientation='vertical', padding=20, spacing=15)
        content.add_widget(PersianLabel(text='لیست قرص‌ها نمایش داده می‌شود'))
        
        popup = Popup(
            title='لیست قرص‌ها',
            content=content,
            size_hint=(0.8, 0.4)
        )
        popup.open()
    
    def settings(self, instance):
        content = BoxLayout(orientation='vertical', padding=20, spacing=15)
        content.add_widget(PersianLabel(text='تنظیمات برنامه'))
        
        popup = Popup(
            title='تنظیمات',
            content=content,
            size_hint=(0.8, 0.4)
        )
        popup.open()
    
    def exit_app(self, instance):
        App.get_running_app().stop()

if __name__ == '__main__':
    MainApp().run()
