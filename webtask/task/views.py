from django.shortcuts import render
from django.contrib import messages
import requests


def index(request):		
	return render(request, "index.html")

def result(request):
	if request.POST.get('pupil'):		
		pupil = request.POST.get('pupil')
		pupil = pupil.replace(' ', '').split(',')		

	if request.POST.get('tutor'):		
		tutor = request.POST.get('tutor')
		tutor = tutor.replace(' ', '').split(',')

	if (len(pupil)%2 != 0) or (len(tutor)%2 != 0):
			messages.error(request, "Вы ввели нечётное кол-во интервалов")
			return render(request, "index.html")
	pupil_res = 0
	tutor_res = 0
	for i in range(len(pupil)):
		if not i%2==0:
			pupil_res += int(pupil[i])-int(pupil[i-1])

	for i in range(len(tutor)):
		if not i%2==0:
			tutor_res += int(tutor[i])-int(tutor[i-1])
	
	return render(request, "result.html", {'tutor_res': tutor_res, 'pupil_res': pupil_res  })
