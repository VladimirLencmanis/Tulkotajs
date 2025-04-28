import tkinter as tk
from tkinter import messagebox
from googletrans import Translator
from PIL import Image, ImageTk
import asyncio  # Добавляем импорт asyncio наверху
from deep_translator import GoogleTranslator


class TranslatorApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Tulkotājs")

    self.frame_index = 0
    self.translator = Translator()

    # Загружаем картинку один раз
    logo_image = Image.open("logo.jpg").resize(
        (100, 100))  # Убедись, что файл называется logo.jpg
    self.logo = ImageTk.PhotoImage(logo_image)

    self.frames = [
        self.create_frame0(),
        self.create_frame1(),
        self.create_frame2()
    ]
    self.show_frame(0)

  def create_frame0(self):
    frame = tk.Frame(self.root)

    # Показываем логотип
    tk.Label(frame, image=self.logo).pack(pady=10)

    # Название
    tk.Label(frame, text="Tulkotājs",
             font=("Helvetica", 16, "bold")).pack(pady=10)

    # Кнопка "вправо"
    next_button = tk.Button(frame,
                            text="➔",
                            width=4,
                            command=lambda: self.show_frame(1))
    next_button.place(relx=0.9, rely=0.9, anchor="center")
    next_button.place(relx=0.9, rely=0.9, anchor="center")

    return frame

  def create_frame1(self):
    frame = tk.Frame(self.root)

    tk.Label(frame, text="Tulkotājs",
             font=("Helvetica", 16, "bold")).pack(pady=10)

    content_frame = tk.Frame(frame)
    content_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Левая часть — ввод текста
    left_frame = tk.Frame(content_frame)
    left_frame.pack(side="left", fill="both", expand=True)

    tk.Label(left_frame, text="Ievadiet latviešu tekstu!").pack(anchor="w",
                                                                pady=(0, 5))
    self.input_text = tk.Text(left_frame, width=40, height=6)
    self.input_text.pack(anchor="nw")  # <-- текст вверх слева

    # Правая часть — кнопка
    right_frame = tk.Frame(content_frame)
    right_frame.pack(side="right", fill="y", padx=(10, 0))

    translate_button = tk.Button(right_frame,
                                 text="Tulkot !",
                                 width=15,
                                 command=self.translate_text)
    translate_button.pack(pady=(50, 5))

    return frame

  def create_frame2(self):
    frame = tk.Frame(self.root)

    tk.Label(frame, text="Tulkotājs",
             font=("Helvetica", 16, "bold")).pack(pady=10)

    content_frame = tk.Frame(frame)
    content_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Левая часть — текст
    left_frame = tk.Frame(content_frame)
    left_frame.pack(side="left", fill="both", expand=True)

    tk.Label(left_frame, text="Tulkots teksts angļu valodā").pack(pady=(0, 5))
    self.output_text = tk.Text(left_frame, width=40, height=6)
    self.output_text.pack(anchor="n")  # <-- ставим текст к верху

    # Правая часть — кнопки
    right_frame = tk.Frame(content_frame)
    right_frame.pack(side="right", fill="y", padx=(10, 0))

    tk.Button(right_frame,
              text="Turpināt",
              width=15,
              command=lambda: self.show_frame(1)).pack(pady=(50, 5))
    tk.Button(right_frame, text="Pabeigt", width=15,
              command=self.root.quit).pack()

    return frame

  def show_frame(self, index):
    for frame in self.frames:
      frame.pack_forget()
    self.frames[index].pack(fill="both", expand=True)
    self.frame_index = index

  def translate_text(self):
    text = self.input_text.get("1.0", "end").strip()
    if text:
      try:
        translated = GoogleTranslator(source='latvian',
                                      target='english').translate(text)
        self.output_text.delete("1.0", "end")
        self.output_text.insert("end", translated)
        self.show_frame(2)
      except Exception as e:
        messagebox.showerror("Error", str(e))
    else:
      messagebox.showwarning("Warning", "Lūdzu, ievadiet tekstu!")


if __name__ == "__main__":
  root = tk.Tk()
  app = TranslatorApp(root)
  root.geometry("400x200")  # Сделал окно чуть выше, чтобы влезал логотип
  root.mainloop()
