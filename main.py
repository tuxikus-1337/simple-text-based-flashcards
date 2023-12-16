import os, sys

class Question:
    question_string = ""
    answer_string = ""

    def to_string(self):
        print("Q:", self.question_string)
        print("A:", self.answer_string)

class Parser:
    def parse_flashcards_file_string(self, input_string):
        read_question = False
        read_answer = False
        questions = []
        question = Question()

        current_char = ""
        prev_char = ""

        for i in range(0, len(input_string)):
            current_char = input_string[i]
            if i > 0:
                prev_char = input_string[i-1]

            if current_char == "\n" and prev_char == "\n":
                question.question_string = question.question_string[:-2]
                questions.append(question)
                question = Question()
                read_question = False
                read_answer = False

            if prev_char == "Q" and current_char == ":":
                read_question = True
                read_answer = False
                continue
            elif prev_char == "A" and current_char == ":":
                read_question = False
                read_answer = True
                continue

            if read_question:
                question.question_string += current_char
            elif read_answer:
                question.answer_string += current_char


        question.question_string = question.question_string[:-2]
        questions.append(question)

        return questions 

def get_file_from_arg():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return ""


def main():
    parser = Parser()

    file = get_file_from_arg()

    if file == "":
        print("No input file")
        return

    flashcards_file = open(file, "r")
    flashcards_file_content = flashcards_file.read()
    flashcards_file.close()

    questions = parser.parse_flashcards_file_string(flashcards_file_content)

    os.system("clear")

    for q in questions:
        print(q.question_string)
        user_input = input("Press ENTER to show the answer OR type quit + ENTER to quit the application : ")

        if user_input == "quit":
            return

        print(q.answer_string) 
        user_input = input("Press ENTER to get the next question OR type quit + ENTER to quit the application : ")

        if user_input == "quit":
            return

        os.system("clear")
    

if __name__ == "__main__":
    main()
