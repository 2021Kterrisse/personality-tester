def question(question1, question2, question3, question4, question5):
    score = 0
    if question1 == "no":
      score = score + 1
    if question2 == "yes":
      score = score + 1
    if question3 == "no":
      score = score + 1
    if question4 == "no":
      score = score + 1
    if question5 == "yes":
      score = score + 1

    return "Your personality score is", score / 5 * 100,"% out of 100!"
