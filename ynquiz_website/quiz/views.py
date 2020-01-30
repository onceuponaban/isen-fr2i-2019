from django.http import HttpResponse
from django.shortcuts import render
from quiz.models import Answer
from quiz.models import Question
from random import seed
from random import randint 
from django.http import HttpResponseRedirect
from quiz.forms import QuizForm
from django.http import JsonResponse

def home(request):
    return render(request, 'quiz/home.html', locals())

def play(request):

    #If we handle the page after POST (ie: after we validate the answer)
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = QuizForm(request.POST)
        #We take the question ID from the JavaScript getAnswer() function
        questionID = request.POST['questionID']
        #We take the answer ID from the JavaScript getAnswer() function
        answerID = request.POST['answerID']
        #We take all the answer from the question
        answers = Answer.objects.filter(question__id=questionID)
        #We take the object of the good answer
        goodAnswerObject = Answer.objects.filter(question__id=1, is_correct=True)
        #We take the ID of the good answer
        goodAnswerID = goodAnswerObject[0].id
        
        #If the answer selected by the user is right...
        if True == answers[int(answerID)].is_correct : 
        #We set the boolean to True
            goodAnswerBool = True
        #We set the boolean to False
        else:
            goodAnswerBool = False
        
        print("GOOD ANSWER ID")
        print(goodAnswerID)
        data = {
            'goodAnswerBool': goodAnswerBool,
            'goodAnswerID': goodAnswerID,
        }
        theReturn = JsonResponse(data)
        
    # If this is a GET (or any other method) create the default form.
    else:
        questionID = 1
        answers = Answer.objects.filter(question__id=questionID)
        question = Question.objects.filter(id=questionID)
        keys = []
        answersArray = []
        anAnswer = []
        seed()
        form = QuizForm(request.POST or None)
        #We randomise all the answers
        for i in range(0,3) : 
            while True:
                key = randint(0,2)
                if ((key in keys) == False) :
                    keys.append(key)
                    anAnswer.append(key)
                    anAnswer.append(answers[key].answer_text)
                    answersArray.append(tuple(anAnswer))
                    anAnswer = []
                    #We handle the ID of the correct answer
                    if(answers[key].is_correct == True):
                        goodAnswer = key
                    break
        #We put the randomised answers in the form
        form.fields['choice_field'].choices = answersArray
        #We put the good answer ID in the form 
        form.answerID = goodAnswer
        print("OUIOUIOUI")
        print(answersArray)
        #Set up of the data set send at the HTML page when it's loading
        context = {
            'form' : form,
            'question': question[0],
            'questionID': questionID,
            'answerArray': answersArray,
        }
        theReturn = render(request, 'quiz/play.html', context )
    return theReturn

def ranking(request):
    return render(request, 'quiz/ranking.html', locals())

def signin(request):
    return render(request, 'quiz/signin.html', locals())

def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']
        moui = form.cleaned_data['oui']

        # Nous pourrions ici envoyer l'e-mail grâce aux données 
        # que nous venons de récupérer
        envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'quiz/contact.html', locals())