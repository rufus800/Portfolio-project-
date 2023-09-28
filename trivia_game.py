import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QButtonGroup, QRadioButton

# Sample trivia questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "answer": "Paris",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Mars",
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Lion", "Tiger", "Giraffe", "Blue Whale"],
        "answer": "Blue Whale",
    },
]

class TriviaGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Trivia Game')
        self.setGeometry(100, 100, 400, 300)

        self.score = 0
        self.current_question_index = 0

        self.layout = QVBoxLayout()

        self.question_label = QLabel('')
        self.layout.addWidget(self.question_label)

        self.option_buttons_layout = QVBoxLayout()
        self.option_buttons = QButtonGroup()
        self.layout.addLayout(self.option_buttons_layout)

        for _ in range(4):
            option_button = QRadioButton('')
            self.option_buttons.addButton(option_button)
            self.option_buttons_layout.addWidget(option_button)

        self.next_button = QPushButton('Next Question')
        self.next_button.clicked.connect(self.next_question)
        self.layout.addWidget(self.next_button)
        self.next_button.setEnabled(False)

        self.prev_button = QPushButton('Previous Question')
        self.prev_button.clicked.connect(self.prev_question)
        self.layout.addWidget(self.prev_button)
        self.prev_button.setEnabled(False)

        self.setLayout(self.layout)

        self.load_question()

    def load_question(self):
        if 0 <= self.current_question_index < len(questions):
            current_question = questions[self.current_question_index]
            self.question_label.setText(current_question['question'])

            options = current_question['options']
            for i, option_button in enumerate(self.option_buttons.buttons()):
                option_button.setText(options[i])

    def next_question(self):
        if 0 <= self.current_question_index < len(questions):
            selected_option = self.option_buttons.checkedButton()
            current_question = questions[self.current_question_index]

            if selected_option is not None and selected_option.text() == current_question['answer']:
                self.score += 5  # Each correct answer is 5 points

        self.current_question_index += 1
        self.option_buttons.setExclusive(False)
        self.option_buttons.setExclusive(True)

        if self.current_question_index < len(questions):
            self.load_question()
            self.prev_button.setEnabled(True)
        else:
            self.show_summary()

    def prev_question(self):
        if 0 <= self.current_question_index < len(questions):
            selected_option = self.option_buttons.checkedButton()
            current_question = questions[self.current_question_index]

            if selected_option is not None and selected_option.text() == current_question['answer']:
                self.score += 5  # Each correct answer is 5 points

        self.current_question_index -= 1
        self.option_buttons.setExclusive(False)
        self.option_buttons.setExclusive(True)

        if self.current_question_index >= 0:
            self.load_question()
            self.next_button.setEnabled(True)

    def show_summary(self):
        self.close()
        summary_page = SummaryPage(self.score)
        summary_page.show()

class SummaryPage(QWidget):
    def __init__(self, score):
        super().__init__()
        self.score = score
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Trivia Game - Summary')
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        summary_label = QLabel(f'Total Correct Questions: {self.score // 5}')
        self.layout.addWidget(summary_label)

        score_label = QLabel(f'Score: {self.score}')
        self.layout.addWidget(score_label)

        self.setLayout(self.layout)

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Trivia Game - Home')
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.title_label = QLabel('Welcome to Trivia Game')
        self.layout.addWidget(self.title_label)

        self.start_button = QPushButton('Start Game')
        self.start_button.clicked.connect(self.start_game)
        self.layout.addWidget(self.start_button)

        self.setLayout(self.layout)

    def start_game(self):
        self.trivia_game = TriviaGame()
        self.trivia_game.show()
        self.close()

def main():
    app = QApplication(sys.argv)
    home_page = HomePage()
    home_page.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
