#Function to return reactions in post or comment
def getReactions(element):
    reactions=[]
    reactions.append(element['like']['summary']['total_count'])
    reactions.append(element['love']['summary']['total_count'])
    reactions.append(element['wow']['summary']['total_count'])
    reactions.append(element['haha']['summary']['total_count'])
    reactions.append(element['sad']['summary']['total_count'])
    reactions.append(element['angry']['summary']['total_count'])
    reactions.append(element['thankful']['summary']['total_count'])
    reactions.append(element['pride']['summary']['total_count'])

    return reactions