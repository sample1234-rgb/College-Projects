'''from googletrans import Translator,LANGCODES
lang ={'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy',
        'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs',
       'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn',
       'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da',
       'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl',
       'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka',
       'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha',
       'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu',
       'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it',
       'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km',
       'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la',
       'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg',
       'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr',
       'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or',
       'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi',
 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
f_name = "First Name:"
trans = Translator()
translator = trans.translate(text=f_name,dest='zh-tw')
'''
import tkinter as tk
import random

class Desktop:

    array = [(50,50,70,70),(100,50,120,70),(150,50,170,70),(150,100,170,120),
            (150,150,170,170),(100,150,120,170),(50,150,70,170),(50,100,70,120)]

    def __init__(self, master):
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.canvas.create_rectangle(100, 250, 300, 350)

        # to keep all IDs and its start position
        self.ovals = {}

        for item in self.array:
            # create oval and get its ID
            item_id = self.canvas.create_oval(item, fill='brown', tags='id')
            # remember ID and its start position
            self.ovals[item_id] = item

        self.canvas.tag_bind('id', '<B1-Motion>', self.move)
        self.canvas.tag_bind('id', '<ButtonRelease-1>', self.stop_move)

    def move(self, event):
        # get selected item
        selected = event.widget.find_withtag("current")[0]

        # move selected item
        self.canvas.coords(selected, event.x-10, event.y-10, event.x+10,event.y+10)

    def stop_move(self, event):
        # get selected item
        selected = event.widget.find_withtag("current")[0]

        # delete or release selected item
        if 100 < event.x < 300 and 250 < event.y < 350:
            self.canvas.delete(selected)
            del self.ovals[selected]
        else:
            self.canvas.coords(selected, self.ovals[selected])

root = tk.Tk()
d = Desktop(root)
root.mainloop()