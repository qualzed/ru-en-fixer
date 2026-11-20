import pyperclip, keyboard, time, pyautogui
from src import serializer

alphabet = {
     ("q", "й"),
     ("w", "ц"),
     ("e", "у"),
     ("r", "к"),
     ("t", "е"),
     ("y", "н"),
     ("u", "г"),
     ("i", "ш"),
     ("o", "щ"),
     ("p", "з"),
     ("[", "х"),
     ("]", "ъ"),
     ("\\", "\\"), # funny
     ("a", "ф"),
     ("s", "ы"),
     ("d", "в"),
     ("f", "а"),
     ("g", "п"),
     ("h", "р"),
     ("j", "о"),
     ("k", "л"),
     ("l", "д"),
     (";", "ж"),
     ("'", "э"),
     ("z", "я"),
     ("x", "ч"),
     ("c", "с"),
     ("v", "м"),
     ("b", "и"),
     ("n", "т"),
     ("m", "ь"),
     (",", "б"),
     (".", "ю"),
     ("/", "."),
     ("`", "ё"),
     ("?", ","),

     # Symbols only
     ("@", "\""),
     ("#", "№"),
     ("$", ";"),
     ("^", ":")
     # ("&", "?"),
}

def awaitHotkeys():
     print(f"Утилита работает. Используйте: {serializer.hotkeys} для исправления. Не забудьте выделить текст!")
     def on_hotkey():
          time.sleep(0.5)
          pyautogui.hotkey("ctrl", "c")
          fixText(text=pyperclip.paste())

     keyboard.add_hotkey(serializer.hotkeys, on_hotkey)
     keyboard.wait()

def detectDominantLanguage(text: str) -> str:
     count: list = [0, 0] # english and russian

     for english, russian in alphabet:
          for i in text:
               if i in english:
                    count[0] += 1
               elif i in russian:
                    count[1] += 1

     if count[0] > count[1]:
          return "english"
     else:
          return "russian"

def fixText(text: str):
     if text == "\0":
          return

     language = detectDominantLanguage(text=text)

     for english, russian in alphabet:
          if language == "english":
               if english in text:
                    text = text.replace(english, russian)
               elif english.upper() in text:
                    text = text.replace(english.upper(), russian.upper())
          else:
               if russian in text:
                    text = text.replace(russian, english)
               elif russian.upper() in text:
                    text = text.replace(russian.upper(), english.upper())
     pyperclip.copy(text=text)
     pyautogui.hotkey("ctrl", "v")
     pyperclip.copy("\0")

if __name__ == "__main__":
     try:
          serializer.readJSON()
          awaitHotkeys()
     except Exception as e:
          print(f"Ошибка при запуске: {e}")