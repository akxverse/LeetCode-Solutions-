class Solution(object):
    def capitalizeTitle(self, title):
        title= title.split()
        for i in range (len(title)):
            if len(title[i]) <=2:
                title[i]=title[i].lower()
            else:
                title[i]=title[i].capitalize()
        return ' '.join(title)
            