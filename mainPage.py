def flatten(nestedList):
    # Write your code here
    stack = [nestedList]
    flatten_list = []

    while stack:
        top = stack.pop()
        print(top)
        if isinstance(top, list):
            for elem in reversed(top):
                stack.append(elem)
                print("+++", elem)
        else:
            flatten_list.append(top)

    return flatten_list


print(flatten([[1,1],2,[1,2]]))
