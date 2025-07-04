from collections import defaultdict, deque


with open('5/d5_input.txt','r') as input:
    pairs = defaultdict(list)
    data = []

    fl = input.readline()
    x = fl.split("|")

    for line in input:
        line = line.strip()
        if "|" in line:
            split_line = line.split('|')
            pairs[split_line[1].strip()].append(split_line[0].strip())
        else:
            data_split = [item.strip() for item in line.split(",") if item.strip()]
            if data_split:
                data.append(data_split)


def is_valid(page_list, pairs):
    pos = {page: idx for idx, page in enumerate(page_list)}
    for y in page_list:
        for x in pairs[y]:
            if x in pos and pos[x] > pos[y]:
                return False
    return True

def build_graph(page_list, pairs):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    pages = set(page_list)
    for y in page_list:
        for x in pairs[y]:
            if x in pages:
                graph[x].append(y)
                indegree[y] += 1
                indegree.setdefault(x, 0)
    return graph, indegree

def topo_sort(page_list, graph, indegree):
    queue = deque([p for p in page_list if indegree[p] == 0])
    result = []
    seen = set()
    while queue:
        node = queue.popleft()
        if node not in seen:
            result.append(node)
            seen.add(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
    for p in page_list:
        if p not in result:
            result.append(p)
    return result

#dictionary key, value. value must come before key in order 
total = 0
for page_list in data:
    if not is_valid(page_list, pairs):
        graph, indegree = build_graph(page_list, pairs)
        sorted_list = topo_sort(page_list, graph, indegree)
        mid = len(sorted_list) // 2
        total += int(sorted_list[mid])

print(total)