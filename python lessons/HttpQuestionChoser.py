import json
import random
import requests
# Import the requests modue to handle requests from http's adress.
import html
# Import the html module for HTML entity decoding.

def fetch_random_question():
    apiurl = 'https://opentdb.com/api.php?amount=1'

    try:
        r = requests.get(apiurl)
        #r stands for response
        r.raise_for_status()
        #Raise an exception for 4xx/5xx status codes.
        data = r.json()
        if data["response_code"] == 0:
            q = html.unescape(data["results"][0]["question"])
            #Result from question(q) in API.
            ca = html.unescape(data["results"][0]["correct_answer"])
            #Result from correct answer(ca) in API.
            incorrect_answers = [html.unescape(answer) for answer in data["results"][0]["incorrect_answers"]]
            # Decode HTML entities in the question, correct and incorrect answer.
            answers = incorrect_answers + [ca]
            random.shuffle(answers)
            return q, answers, ca
        else:
            print("Error: Unable to fetch question. Response code:", data["response_code"])
            return None, None, None
    except requests.exceptions.RequestException as e:
        print("Error fetching question:", e)
        return None, None, None

def main():
    score_correct = 0
    score_incorrect = 0
    
    while True: # Loop until user chooses to stop
        q, answers, ca = fetch_random_question()
        if q and answers and ca:
            print("Question:", q)

            # Display correct answer
            print("Correct Answer:", ca)

            # Display answers
            for i, answer in enumerate(answers, start=1):
                print(f"{i}. {answer}")

            # Get user's answer
            while True:
                user_answer = input("Type the number of the correct answer: ")
                try:
                    user_answer = int(user_answer)
                    if 1 <= user_answer <= len(answers):
                        break
                    else:
                        print("Invalid answer. Please enter a number between 1 and", len(answers))
                except ValueError:
                    print("Invalid answer. Please enter a number.")

        user_answer = answers[user_answer - 1]

        # Check user's answer
        if user_answer == ca:
            print("\nCongratulations! You answered correctly!")
            score_correct += 1
        else:
            print("\nSorry, that's incorrect. The correct answer is:", ca)
            score_incorrect += 1

        print("\nYour score:")
        print("Correct answers:", score_correct)
        print("Incorrect answers:", score_incorrect)

        # Ask if the user wants to play again
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice != 'yes':
            break
    print("\nThanks  for playing!")

if __name__ == "__main__":
    main()
'''
import requests
import json
import pprint
import random
import html

score_correct = 0
score_incorrect = 0

url = "https://opentdb.com/api.php?amount=1"
endGame = ""

while endGame != "quit":
    r = requests.get(url)
    if(r.status_code != 200):
        endGame = input("Sorry, there was a problem retrieving the question. Press enter to try again or type 'quit' to quit.")
    else:
        valid_answer = False
        answer_number = 1
        data = json.loads(r.text)
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)
        #pprint.pprint(data)
        #input("Press enter to get a new question.")

        print(html.unescape(question) + "\n")

        for answer in answers:
            print(str(answer_number) + "- " + html.unescape(answer))
            answer_number += 1

        while valid_answer == False:
            user_answer = input("\nType the number of the correct answer: ")
            try:
                user_answer = int(user_answer)
                if user_answer > len(answers) or user_answer <= 0:
                    print("Invalid Answer")
                else:
                    valid_answer = True 
            except:
                print("Invalid answer. Use only numbers")

        user_answer = answers[int(user_answer)-1]

        if user_answer == correct_answer:
            print("\nCongratulations! You answered correctly! The correct answer was: " + html.unescape(correct_answer))
            score_correct += 1
        else:
            print("Keep Going, " + html.unescape(user_answer) + " is incorrect. But the correct answer is: " + html.unescape(correct_answer))
            score_incorrect += 1

        print("\n##########################")
        print("Your score is:")
        print("Correct answers: " + str(score_correct))
        print("Incorrect answers: " + str(score_incorrect))
        print("##########################")
        
        endGame = input("\nPress enter to play again or type 'quit' to quit the game.").lower()

print("\nThanks for playing")
'''
'''
import json
import random
import requests
# Import the requests modue to handle requests from http's adress.
import html
# Import the html module for HTML entity decoding.

def fetch_random_question():
    apiurl = 'https://opentdb.com/api.php?amount=1'

    try:
        r = requests.get(apiurl)
        #r stands for response
        r.raise_for_status()
        #Raise an exception for 4xx/5xx status codes.
        data = r.json()
        if data["response_code"] == 0:
            q = data["results"][0]["question"]
            #Result from question(q) in API.
            ca = data["results"][0]["correct_answer"]
            #Result from correct answer(ca) in API.
            q = html.unescape(q)
            # Decode HTML entities in the question
            return q, ca
        else:
            print("Error: Unable to fetch question. Response code:", data["response_code"])
            return None, None
    except requests.exceptions.RequestException as e:
        print("Error fetching question:", e)
        return None, None
def main():
    while True: # Loop until user chooses to stop
        q, ca = fetch_random_question()
        if q and ca:
            print("Question:", q)
            user_answer = input("Your answer (with a word, or with true or false): ").strip()
            if user_answer.lower() == ca.lower():
                print("Correct!")
            else:
                print("Incorrect. The correct answer is:", ca)
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice != "yes":
            break

if __name__ == "__main__":
    main()
'''
'''
import requests

def fetch_random_question():
    api_url = "https://opentdb.com/api.php?amount=1"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        data = response.json()
        if data["response_code"] == 0:  # Check if response is successful
            # Extract the question
            question = data["results"][0]["question"]
            return question
        else:
            print("Error: Unable to fetch question. Response code:", data["response_code"])
            return None
    except requests.exceptions.RequestException as e:
        print("Error fetching question:", e)
        return None

# Example usage:
question = fetch_random_question()
if question:
    print("Random Question:", question)
'''
'''
import json
import random
import requests

# -*- coding: utf-8 -*-
r = requests.get('https://opentdb.com/api.php?amount=1')
#python how to print the first 50 characters of an http request

data = r.json()
#q = json.loads(r.text)

#q ['results'][0]['question']

q = data['results'][0]['question']

for i in range(1):
        print (q)

#https://www.datacamp.com/tutorial/making-http-requests-in-python
'''
'''
import json
import random
import requests

r = requests.get('https://opentdb.com/api.php?amount=10')

question = json.loads(r.text)
#json.dumps

payload = {"results", [0], "question"}

q = random.choices(payload)

response_json = question.json(q)

#for i in range(10):
print(response_json)
'''
