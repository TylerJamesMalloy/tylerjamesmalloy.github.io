from pyibl import Agent

def identity_similarity(x,y):
    if(x==y): 
        return 1
    else: 
        return 0 

def always_zero(x,y):
    return 0 

agent = Agent(name="Contextual Bandit", attributes=["shape","color"], mismatch_penalty=1, decay=0, temperature=1, noise=0)
agent.similarity(attributes="color", function=identity_similarity)
agent.similarity(attributes="shape", function=always_zero)

agent.populate([{"shape":"circle","color":"blue"}], 1)
agent.populate([{"shape":"square","color":"red"}], 0)
choice, details = agent.choose([{"shape":"square","color":"blue"}], details=True)

print(details[0]['blended_value'])

"""agent = Agent(name="Contextual Bandit", attributes=["shape","color"], mismatch_penalty=1, decay=0, temperature=1, noise=0)
agent.similarity(["shape", "color"], identity_similarity)
agent.populate([{"shape":"circle","color":"blue"}}, 1)
agent.populate([{"shape":"square","color":"red"}}, 0)
choice, details = agent.choose([{"shape":"square","color":"blue"}], details=True)

print(details[0]['blended_value'])"""