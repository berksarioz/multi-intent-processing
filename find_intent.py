import random
import pandas as pd

def generate_single_intent(n):

	names = ["Andrew", "Lisa", "Tom", "Berk", "Maria", "Semih"]
	relations = ["wife", "husband", "son", "daughter", "mother", "father", "boyfriend", "girlfriend"]
	sports = ["tennis", "golfing", "soccer", "basketball", "ballroom dancing", "baseball"]


	data = []
	for i in range(n):
		name = random.choice(names)
		name2 = random.choice(names)
		relation = random.choice(relations)
		sport = random.choice(sports)

		# add intent
		add = [f"I met {name} today", f"{name} has a {relation} named {name2}"]

		# remind intent
		remind_a = ["remind me to", "I need to", "I should"]
		remind_action = [f"email {name} tomorrow at 9am", "pick up my dry cleaning on Friday", f"call {name} next week"]
		remind_e = ["remind me", "remind that", "remember"]
		remind_event = [f"it's {name}'s birthday on March 27th", "my wedding anniversary"]

		# search intent
		what = ["what"]
		what_question = [f"sports does {name} like", f"is {name}'s {relation}'s name"]
		who = ["who"]
		who_question = [f"likes {sport}", f"has a {relation}", "lives in New York and had Covid"]

		data.append([random.choice(add), "add"])
		data.append([random.choice(remind_a) + " " + random.choice(remind_action), "reminder"])
		data.append([random.choice(remind_e) + " " + random.choice(remind_event), "reminder"])
		data.append([random.choice(what) + " " + random.choice(what_question), "search"])
		data.append([random.choice(who) + " " + random.choice(who_question), "search"])
	df = pd.DataFrame(data, columns = ["utterance", "intent"]) 
	return df
	

print(generate_single_intent(10))