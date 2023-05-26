# https://stepik.org/lesson/590035/step/24?thread=solutions&unit=584967

from collections import defaultdict

def best_sender(messages, senders):
    result = defaultdict(int)

    for person, message in zip(senders, messages):
        result[person] += len(message.split())
    
    return max(result, key=lambda x: (result[x], x))