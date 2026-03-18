
def calculate_seek(sequence):
    """Utility function to compute total seek movement"""
    return sum(abs(sequence[i+1] - sequence[i]) for i in range(len(sequence)-1))

def fcfs(requests, head):

    sequence = [head] + requests
    seek = calculate_seek(sequence)

    return seek, sequence


def sstf(requests, head):

    requests = requests.copy()
    sequence = [head]
    seek = 0

    while requests:

        closest = min(requests, key=lambda x: abs(x - head))

        seek += abs(closest - head)
        head = closest

        sequence.append(head)
        requests.remove(closest)

    return seek, sequence



def scan(requests, head, disk_size, direction):

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort()
    right.sort()

    sequence = [head]

    if direction == "up":

        right.append(disk_size - 1)
        sequence += right
        sequence += left[::-1]

    else:

        left.insert(0, 0)
        sequence += left[::-1]
        sequence += right

    seek = calculate_seek(sequence)

    return seek, sequence



def cscan(requests, head, disk_size):

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort()
    right.sort()

    sequence = [head]

    right.append(disk_size - 1)
    left.insert(0, 0)

    sequence += right
    sequence += left

    seek = calculate_seek(sequence)

    return seek, sequence



def look(requests, head, direction):

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort()
    right.sort()

    sequence = [head]

    if direction == "up":

        sequence += right
        sequence += left[::-1]

    else:

        sequence += left[::-1]
        sequence += right

    seek = calculate_seek(sequence)

    return seek, sequence




def clook(requests, head):

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort()
    right.sort()

    sequence = [head] + right + left

    seek = calculate_seek(sequence)

    return seek, sequence