import random
import pandas as pd
import re

def generate_single_intent(n):

	m = {
		"name": ["Andrew", "Lisa", "Tom", "Berk", "Maria", "Semih"],
		"relative_name": ["Andrew", "Lisa", "Tom", "Berk", "Maria", "Semih"],
		"relation": ["wife", "husband", "son", "daughter", "mother", "father", "boyfriend", "girlfriend"],
		"sport": ["tennis", "golfing", "soccer", "basketball", "ballroom dancing", "baseball"]
	}
	# add intent
	add = ["I met {name} today", "{name} has a {relation} named {relative_name}", "{relative_name} is the {relation} of {name}"]

	# remind intent
	remind_a = ["remind me to", "I need to", "I should"]
	remind_action = ["email {name} tomorrow at 9am", "pick up my dry cleaning on Friday", "call {name} next week"]
	remind_e = ["remind me", "remind that", "remember"]
	remind_event = ["it's {name}'s birthday on March 27th", "my wedding anniversary"]

	# search intent
	what = ["what"]
	what_question = ["sports does {name} like", "is {name}'s {relation}'s name"]
	who = ["who"]
	who_question = ["likes {sport}", "has a {relation}", "lives in New York and had Covid"]


	data = []
	for i in range(n):
		data.append(get_intent_mention([random.choice(remind_a) + " " + random.choice(remind_action), "reminder"], m))
		data.append(get_intent_mention([random.choice(remind_e) + " " + random.choice(remind_event), "reminder"], m))
		data.append(get_intent_mention([random.choice(what) + " " + random.choice(what_question), "search"], m))
		data.append(get_intent_mention([random.choice(who) + " " + random.choice(who_question), "search"], m))
		data.append(get_intent_mention([random.choice(add), "add"], m))

	df = pd.DataFrame(data, columns = ["utterance", "intent", "mentions"]) 
	return df
	
def get_intent_mention(l, m):
	regexp = re.compile(r'\{.*?\}')
	intent = l.pop()
	utterance = ""
	mentions = {}
	for clause in l:
		while(regexp.search(clause)):
			# find the first matching mention
			pattern = re.search(regexp, clause).group()
			replacement = random.choice(m[pattern[1:-1]])
			mentions[replacement] = pattern
			clause = re.sub(pattern, replacement, clause, 1)
		utterance += clause + " "
	return [utterance, intent, mentions]

print(generate_single_intent(10))