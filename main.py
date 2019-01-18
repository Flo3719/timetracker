import sys, time, json, os

startWorkingTime = 0




def homescreen():
	menu = input(
		"""
		What do you want to do? 
		0: Start Working
		1: Overview
		2: New project
		3. Delete project
		q: Quit
		""")
	if menu == "0":
		startWorking()
	elif menu == "1":
		Overview()
	elif menu == "2":
		newProject(firstProject = False)
	elif menu == "3":
		deleteProject()	
	elif menu == "q":
		os.system("clear")
		quit()	
	else:
		InputError()


def startWorking():
	os.system('clear')
	ShowProjects()
	updateProjectsList()

	global startWorkingTime
	global projects
	startWorkingTime = time.time()

	StopNow = input("\nTo stop working type the ID of the project you're working on. (x to cancel)")
	try:
		if((StopNow != "x") & (int(StopNow) >= 0) & (int(StopNow) <= len(projects))):
			stopWorking(StopNow)
			stopNow = 0
		elif stopNow == "x":
			stopNow = 0
			os.system("clear")
			ShowProjects()
			print("\nYou canceled your worksession.")
			homescreen()
	except: 
		stopNow = 0
		InputError()
	



def stopWorking(projectID):
	
	ShowProjects()
	global startWorkingTime

	TimeSpent = time.time() - startWorkingTime

	projects[int(projectID)]["Minutes spent"] += TimeSpent/60

	TimeSpent = 0

	os.system('clear')

	ShowProjects()
	updateJSON()
	# BACK TO HOMESCREEN
	homescreen()

def newProject(firstProject):
	os.system('clear')
	global projects
	
	ShowProjects()
	projectname = input("\nHow do you want to name your new project?")

	try:
		if firstProject == True:
			projects = [{
				"Name":projectname,
				"Minutes spent":0,}]
			updateJSON()
		else:	
			projects.append({
				"Name":projectname,
				"Minutes spent":0,
				})
	except:
		InputError()		

	os.system('clear')
	ShowProjects()
	print("\nYour new project",projectname,"has been created.")
	
	updateJSON()
	# BACK TO HOMESCREEN
	homescreen()

def deleteProject():
	os.system('clear')
	ShowProjects()
	DeleteWhich = input("\nWhich project do you want do delete? (ID)")
	try:
		del projects[int(DeleteWhich)]
	except:
		InputError()		
	
	updateJSON()

	os.system('clear')
	ShowProjects()
	print("\nThe project has been deleted.")
	homescreen()

def updateJSON():
	with open("projects.json", "w") as write_file:
   		json.dump(projects, write_file)

def updateProjectsList():
	with open("projects.json", "r") as read_file:
		projects = json.load(read_file)

def ShowProjects():
	updateProjectsList()
	for i in enumerate(projects):
		print(i)

def Overview():
	os.system("clear")
	ShowProjects()
	homescreen()

def InputError():
	os.system("clear")
	ShowProjects()
	print("\nYour Input was not valid. Action canceled.")	
	homescreen()

# PROGRAM START
try:
	with open("projects.json", "r") as read_file:
		projects = json.load(read_file)
except:
	newProject(firstProject = True)


os.system("clear")
updateProjectsList()
homescreen()

