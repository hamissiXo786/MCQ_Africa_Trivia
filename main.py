import random


def questions():
    questions = {"1": "What is the largest country in Africa by area? \n a. Egypt \n b. Algeria \n  c. Nigeria \n d. "
                      "Sudan ",
                 "2": "Which African country is known as the 'Rainbow Nation'? \n a) Kenya \n b) South Africa \n c) Egypt \n  d) Tanzania",
                 "3": "Which African country is home to the Great Sphinx and the Pyramids of Giza? \n a) Morocco \n b) Egypt \n  c) Tunisia \n d) Libya \n ",
                 "4": "What is the name of the highest mountain in Africa? a) Mount Kilimanjaro \n  b) Mount Everest \n  c) Mount Fuji \n d) Mount Elbrus \n ",
                 "5": "Which African country is known for producing the most cocoa beans in the world? a) Ghana \n b) Ivory Coast \n c) Nigeria \n  d) Cameroon \n ",
                 "6": "Which African country was formerly known as Rhodesia? a) South Africa \n b) Zimbabwe \n  c) Zambia \n d) Botswana \n ",
                 "7": "What is the official language of Nigeria? a) English \n b) French \n c) Arabic \n d) Swahili \n",
                 "8": "Which African country is known for its famous Maasai Mara National Reserve? \n a) South Africa \n b) Tanzania \n c) Kenya \n d) Botswana \n",
                 "9": "What is the largest river in Africa? \n a) Nile River \n b) Congo River \n c) Zambezi River \n d) Niger River \n",
                 "10": "Which African country was the first to gain independence from European colonial rule? \n a) South Africa \n b) Ghana \n c) Kenya \n d) Nigeria"}

    return questions


def answers():
    answers = ["algeria", "south africa", "egypt", "mount kilimanjaro", "ivory coast", "zimbabwe", "english",
               "kenya","nile river", "ghana"]

    return answers


score = 0


def main():
    NUM_TRIES = 10
    q = 0

    while True:
        list_question = questions()
        score = 0
        play = input("would you like to play the game?? \n > ")
        if play == "no":
            break
        i = 1
        print("welcome to our african quiz game, you have 10 questions that you will be asked"
              "i hope you get everything correct, best of luck :)")

        while i <= NUM_TRIES:
            print(f"question {i}")
            Question = pickQuestion(list_question, i)
            print(Question)
            answer = input('> ')
            score, response = check_answer(answer, score, i)

            print(response)
            print(score)
            i += 1


def pickQuestion(list_q, question_number):
    question = ''
    question = list_q[str(question_number)]
    return question



def check_answer(the_answer, Score, question_number):
    question = questions()
    Answers = answers()
    response = ''
    if question_number != 11:

        if Answers[question_number - 1] == the_answer:
            Score += 1
            response = "you got it correct"
            return Score, response
        else:
            response = "you got it wrong"
            return Score, response


if __name__ == "__main__":
    main()
