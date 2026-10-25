# main.py - приложение "Проба Руфье"
# Собрано из кода учеников. Строки с пометкой "ДОПИСАНО" / "ИСПРАВЛЕНО" - то, чего не хватало.

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from instructions import txt_instruction, txt_test1, txt_test3, txt_sits
from ruffier import test

# Глобальные переменные: экраны записывают сюда данные пользователя
age = 7
name = ""
p1, p2, p3 = 0, 0, 0


# ДОПИСАНО: безопасное превращение текста в число.
# Если в поле буквы или пусто, программа не упадёт, а возьмёт значение default.
def to_int(text, default=0):
    try:
        return int(text)
    except ValueError:
        return default


# =====================================================
# ОБРАЗЕЦ. Экран первого замера пульса.
# =====================================================
class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 1. Текст-инструкция сверху
        instr = Label(text=txt_test1)

        # 2. Строка "подпись + поле ввода"
        line = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result = Label(text='Введите результат:', halign='right')
        self.in_result = TextInput(text='0', multiline=False)  # self. - чтобы достать в next()
        line.add_widget(lbl_result)
        line.add_widget(self.in_result)

        # 3. Кнопка. on_press = что выполнить при нажатии
        self.btn = Button(text='Продолжить', size_hint=(0.3, 0.2),
                          pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next

        # 4. Складываем всё в вертикальную колонку и добавляем на экран
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def next(self):
        global p1                          # говорим: меняем глобальную переменную
        p1 = to_int(self.in_result.text)   # текст из поля -> число (to_int вместо int)
        self.manager.current = 'sits'      # переходим на экран с именем 'sits'


# =====================================================
# ЗАДАНИЕ 1. Экран имени и возраста
# =====================================================
class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        InstLabel = Label(text=txt_instruction)

        # ДОПИСАНО: строки "подпись + поле" для имени и возраста
        # (в коде учеников были пустые контейнеры Podpis и TextInp без полей)
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(Label(text='Введите имя:', halign='right'))
        self.in_name = TextInput(multiline=False)
        line1.add_widget(self.in_name)

        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2.add_widget(Label(text='Введите возраст:', halign='right'))
        self.in_age = TextInput(text='7', multiline=False)
        line2.add_widget(self.in_age)

        self.btn = Button(text='Начать', size_hint=(0.3, 0.2),
                          pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next

        # ИСПРАВЛЕНО: порядок - сначала текст, потом поля, кнопка в самом низу
        outer = BoxLayout(orientation='vertical', padding=12, spacing=12)
        outer.add_widget(InstLabel)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)             # ДОПИСАНО: без этой строки экран пустой

    def next(self):
        global name, age
        name = self.in_name.text
        age = to_int(self.in_age.text, 7)
        self.manager.current = 'pulse1'


# =====================================================
# ЗАДАНИЕ 2. Экран с приседаниями
# =====================================================
class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Label_txt = Label(text=txt_sits, color='red')
        self.btn = Button(text='Продолжить', size_hint=(0.3, 0.2),
                          pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(Label_txt)
        outer.add_widget(self.btn)
        self.add_widget(outer)             # ДОПИСАНО: без этой строки экран пустой

    def next(self):
        self.manager.current = 'pulse2'    # ДОПИСАНО: был pass, кнопка ничего не делала


# =====================================================
# ЗАДАНИЕ 3. Экран второго и третьего замеров
# =====================================================
class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # ДОПИСАНО: весь экран (у учеников был пустой)
        instr = Label(text=txt_test3)

        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(Label(text='Результат:', halign='right'))
        self.in_result1 = TextInput(text='0', multiline=False)
        line1.add_widget(self.in_result1)

        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2.add_widget(Label(text='Результат после отдыха:', halign='right'))
        self.in_result2 = TextInput(text='0', multiline=False)
        line2.add_widget(self.in_result2)

        self.btn = Button(text='Завершить', size_hint=(0.3, 0.2),
                          pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def next(self):
        # ИСПРАВЛЕНО: у учеников переход вёл на 'pulse2' (сам на себя), нужен 'result'
        global p2, p3
        p2 = to_int(self.in_result1.text)
        p3 = to_int(self.in_result2.text)
        self.manager.current = 'result'


# =====================================================
# ЗАДАНИЕ 4. Экран результата
# =====================================================
class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.instr = Label(text='')        # ИСПРАВЛЕНО: был тестовый "Hello world"
        InstrLabel = BoxLayout(orientation='vertical', padding=17, spacing=17)
        InstrLabel.add_widget(self.instr)
        self.add_widget(InstrLabel)        # ДОПИСАНО: без этой строки экран пустой

    def on_enter(self):
        self.instr.text = name + '\n' + test(p1, p2, p3, age)


# =====================================================
# ЗАДАНИЕ 5. Приложение: соединяем все экраны
# =====================================================
class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        # ДОПИСАНО: у учеников здесь был TODO, экраны не добавлялись
        sm.add_widget(InstrScr(name='instr'))
        sm.add_widget(PulseScr(name='pulse1'))
        sm.add_widget(CheckSits(name='sits'))
        sm.add_widget(PulseScr2(name='pulse2'))
        sm.add_widget(Result(name='result'))
        return sm


app = HeartCheck()
app.run()
