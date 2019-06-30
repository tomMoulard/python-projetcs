#!/usr/bin/env python3
import random
import sys

usage = """usage: {0} mcq.txt""".format(sys.argv[0])
prompt = """> """

class bcolors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class Answer():
    def __init__(self, string):
        self.string = string[1:]
        self.true = string[0] == '*'
    def __str__(self):
        return self.string
    def is_true(self):
        return self.true
    def answer(self):
        return f"{bcolors.GREEN if self.true else ''}{self.string}{bcolors.ENDC}"

class Question():
    def __init__(self, s):
        self.full_question = s
        splited = s.split('\n')
        self.question = splited[0]
        self.answers = []
        for answer in splited[1:]:
            self.answers.append(Answer(answer))
        random.shuffle(self.answers)
    def ask(self):
        print(bcolors.BOLD, self.question, bcolors.ENDC, sep="")
        for i in range(len(self.answers)):
            print(f"{i}) {self.answers[i]}")
        self.answer = False
        while not self.answer:
            self.answer = input(prompt)
        self.corret = True
        self.answerss = [int(x) for x in self.answer.split(',')]
        for i in range(len(self.answers)):
            if (i in self.answerss and not self.answers[i].is_true()) \
                or (not i in self.answerss and self.answers[i].is_true()):
                self.corret = False
                break;
        if not self.corret:
            for i in range(len(self.answers)):
                print(f"{i}) {self.answers[i].answer()}")
            return 0
        return 1

class MCQ():
    def __init__(self, file_content, maximum=None):
        self.file_content = file_content
        self.questions = []
        for q in file_content.split("\n\n"):
            self.questions.append(Question(q))
        random.shuffle(self.questions)
        self.questions = self.questions[:maximum]
        self.score = 0
    def play(self):
        for pos in range(len(self.questions)):
            self.score += self.questions[pos].ask()
            print(f"\nScore: {self.score} / {pos + 1}\n")
        return (self.score, len(self.questions))

def main(file):
    with open(file, "r+") as f:
        file_content = f.read()
        mcq = MCQ(file_content)
        score = mcq.play()
        print(f"Score: {score[0]} / {score[1]}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(usage)
        raise SystemExit(1)
    main(sys.argv[1])