# Prompts for the user
adjective_prompt = "Please type an adjective: "
noun_prompt = "Please type a noun: "
verb_prompt = "Please type a verb: "

# Taking input from the user
adjective_input = input(adjective_prompt)
noun_input = input(noun_prompt)
verb_input = input(verb_prompt)

# Constructing the sentence
sentence = "Learning Python is amazing, I built a program that makes a " + adjective_input + " " + noun_input + " " + verb_input + "!"

# Output the final sentence
print(sentence)
