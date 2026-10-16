class Solution(object):
    def interpret(self, command):
        goal= command.replace("()","o")
        goal= goal.replace("(al)","al")
        return goal
        