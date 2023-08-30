from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
import random

# Create your views here.

def randomNum():
    global correctGuess
    correctGuess = random.randint(0,100)
randomNum()

previousGuesses = []

def checkguess(guess):
    guess = int(guess)
    if guess > correctGuess:
        return "Guess was too large"
    elif guess < correctGuess:
        return "Guess was too small"
    elif guess == correctGuess:
        return "Correct guess!"

class indexView(View):
    def get(self, request):
        msg = request.session.get('msg', False)
        if (msg) : del(request.session['msg']) 
        return render(request, 'GuessApp/index.html', {'message': msg,
                                                       'guesses': reversed(previousGuesses)})

    def post(self, request):
        if request.POST.get("again"):
            randomNum()
            previousGuesses.clear()
            return redirect(request.path)

        guess = request.POST.get("guess")
        msg = checkguess(guess)
        request.session['msg'] = msg
        previousGuesses.append(guess)
        return redirect(request.path)