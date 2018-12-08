class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        stack = [nestedList]
        flatten_list = []

        while stack:
            top = stack.pop()
            if isinstance(top, list):
                for elem in reversed(top):
                    stack.append(elem)
            else:
                flatten_list.append(top)

        return flatten_list