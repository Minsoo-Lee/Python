def offer(data, n):
    data.append(n)

def poll(data):
    if len(data) > 0:
        return data.pop(0)
    return False