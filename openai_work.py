import openai
openai.api_key = "YOUR_API_KEY"

def process(first_prompt,content_prompt,last_prompt,language):
	tmp_dict = {}
	model_engine = "gpt-3.5-turbo-instruct"
	#prompt = "This is for a new prompt for an LMS.\n Give me a "+prompt + "\n Send it in "+str(language)+"."
	prompt = first_prompt +" on "+content_prompt+" and "+last_prompt+" "+ "\n Send it in "+str(language)+"."
	completion = openai. Completion.create(engine=model_engine,prompt=prompt,max_tokens=1024, n=1,stop=None,temperature=0.5,)
	response = completion.choices[0].text
	tmp_dict["result"] = response.replace("\n"," ")
	return tmp_dict

#print(process("Description","tennis","women","Tamil"))