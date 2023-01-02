import requests
import json
import random

def playGameQuestion(question, i, winPoints) : 
    print("Q# ", i+1, ": ", question["results"][i]["question"]) 
    options_answers = question["results"][i]["incorrect_answers"]
    options_answers.append(question["results"][i]["correct_answer"])
    random.shuffle(options_answers)

    printOptions(options_answers)
    isUserEarnPoints = isCorrectAndswer(question, options_answers)
    if (isUserEarnPoints):
        print("Correct! + ", winPoints, "points")
        return winPoints
    else:
        print("Bad andswer :C")
        return 0

    # for j in range(len(options_answers)):
    #     print (j+1, ") ", options_answers[j])
    
    # user_answer = int (input ("Choice the number for the answer: "))
    # correct_asnwer = question["results"][i]["correct_answer"]
    # given_answer = options_answers[user_answer-1]
    # if (given_answer == correct_asnwer):
    #     print("Correct! + ", winPoints, "points")
    #     return winPoints
    # else:
    #     print("Bad andswer :C")
    #     return 0

def printOptions (options_answers):
    for j in range(len(options_answers)):
        print (j+1, ") ", options_answers[j])

def isCorrectAndswer(question, options_answers):
    user_answer = int (input ("Choice the number for the answer: "))
    correct_asnwer = question["results"][i]["correct_answer"]
    given_answer = options_answers[user_answer-1]
    if (given_answer == correct_asnwer):
        # print("Correct! + ", winPoints, "points")
        return True
    else:
        return False
    

continue_play_game = True
points_to_earn = 100
player_points = 0
   

while continue_play_game == True:
    url = "https://opentdb.com/api.php?amount=5&category=18&difficulty=easy&type=multiple"
    response = requests.get(url)
    question = json.loads(response.text)
    for i in range(0,len(question["results"])):
        points_earned_this_thime = playGameQuestion(question, i, points_to_earn)
        player_points = player_points + points_earned_this_thime
        # print("Q# ", i+1, ": ", question["results"][i]["question"]) 
        # options_answers = question["results"][i]["incorrect_answers"]
        # options_answers.append(question["results"][i]["correct_answer"])
        # random.shuffle(options_answers)

        # for j in range(len(options_answers)):
        #     print (j+1, ") ", options_answers[j])
        
        # user_answer = int (input ("Choice the number for the answer: "))
        # correct_asnwer = question["results"][i]["correct_answer"]
        # given_answer = options_answers[user_answer-1]
        # if (given_answer == correct_asnwer):
        #     print("Correct! + ", points_to_earn, "points")
        #     player_points = player_points + points_to_earn
        # else:
        #     print("Bad andswer :C")
    
    print ("Points earned at now: ", player_points)
    continue_aswer = input("Do you want to continue playing? (Y/N): ")
    while continue_aswer != 'N' and continue_aswer != 'Y':
        continue_aswer = input("Incorrect answere, do you want to continue playing? (Y/N): ")
       
    if (continue_aswer == "N"):
        print("**********Total points earned: ", player_points, "**********")
        break
    if (continue_aswer == "Y"):
        continue
