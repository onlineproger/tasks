def appearance(intervals):
	pupil = intervals.get('pupil')	
	tutor = intervals.get('tutor')
	pupil_res = 0
	tutor_res = 0
	for i in range(len(pupil)):
		if not i%2==0:
			pupil_res += pupil[i]-pupil[i-1]

	for i in range(len(tutor)):
		if not i%2==0:
			tutor_res += tutor[i]-tutor[i-1]
	return 'Учитель присутстовал на уроке {} секунд.\nУченик присутстовал на уроке {} секунд.'.format(tutor_res, pupil_res)	

dct = { 
  'lesson': [1594663200, 1594666800], 
  'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472], 
  'tutor': [1594663290, 1594663430, 1594663443, 1594666473] 
}

print(appearance(dct))
