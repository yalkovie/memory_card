from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGroupBox, QRadioButton, QHBoxLayout, QButtonGroup
from random import shuffle

class Question():
    def  __init__(self, qwesten, right_answer, wrong_1, wrong_2, wrong_3):
        self.qwesten = qwesten
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3

qwesten_list = []
qwesten_list.append(Question('Годы правления Екатерины I','1712 - 1721 ','1710 - 1720','1715 - 1718','1713 - 1724'))
qwesten_list.append(Question('Кто убил великого поэта Пушкина?','Жорж Дантес','Евгений Онегин','Владимир Даль','Михаил Лермонтов'))


app = QApplication([])
main_win = QWidget()
main_win.resize(600, 500)
main_win.setWindowTitle('Memory Card')
qwesten = QLabel('Когда изобрели шариковую ручку?')
batton = QPushButton('Ответить')

layout_core = QVBoxLayout()

line1 = QHBoxLayout()
line1.addWidget(qwesten, alignment = Qt.AlignCenter)

line3 = QHBoxLayout()
line3.addWidget(batton, alignment = Qt.AlignCenter)

RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('1879')
rbtn_2 = QRadioButton('1888')
rbtn_3 = QRadioButton('1922')
rbtn_4 = QRadioButton('1854')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1, alignment = Qt.AlignCenter)
layout_ans2.addWidget(rbtn_2, alignment = Qt.AlignCenter)
layout_ans3.addWidget(rbtn_3, alignment = Qt.AlignCenter)
layout_ans3.addWidget(rbtn_4, alignment = Qt.AlignCenter)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

line2 = QHBoxLayout()
line2.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)

AnsGroupBox = QGroupBox("Результат теста")

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('Правильный ответ')

AnsGroupBox.hide()

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
line2.addWidget(AnsGroupBox, alignment = Qt.AlignCenter) 

line3.addStretch(1)
line3.addWidget(batton, stretch=2) # кнопка должна быть большой
line3.addStretch(1)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    batton.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    batton.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong_1)
    answer[2].setText(q.wrong_2)
    answer[3].setText(q.wrong_3)
    qwesten.setText(q.qwesten)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        main_win.scored += 1
        show_correct('Правильно!')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неправильно!')

def chek_OK():
    if batton.text() == 'Ответить':
        check_answer()
    else:
        next_qwesten()

def next_qwesten():
    main_win.total += 1
    main_win.cur_qwesten += 1
    if len(qwesten_list) <= main_win.cur_qwesten:
        main_win.cur_qwesten = 0
    q = qwesten_list[main_win.cur_qwesten]
    ask(q)

layout_core.addLayout(line1)
layout_core.addLayout(line2)
layout_core.addLayout(line3)

main_win.cur_qwesten = -1

q = Question('Когда изобрили кубик рубика?', '1970', '1975', '1986', '1978')#1970

ask(q)

main_win.total = 1
main_win.scored = 0

batton.clicked.connect(chek_OK)

main_win.setLayout(layout_core)

a = main_win.scored / main_win.total * 100 #рейтинг
print(a)

main_win.show()
app.exec_()