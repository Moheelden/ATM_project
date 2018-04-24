def ATM(mony,request):
	if request > mony :
		print ("Please insert another number , you don't have enough mony")
	else :
		if request <= 0 :
			print ("Please insert another number , your entry num not valid")
		else :
			while  request > 0:
				if request >= 100 :
					print ("give 100")
					request = request - 100
				elif  request >= 50:
					print ("give 50")
					request = request - 50
				elif request >= 10: 
					print ("give 10")
					request = request - 10
				elif request >=5 :
					print ("give 5")
					request = request - 5
				elif request < 5 :
					print ("give"+ str(request))
					return request


ATM (333,500)