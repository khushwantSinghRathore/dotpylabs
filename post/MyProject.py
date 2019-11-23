class post:

    title = None
    post = None


    def __init__(self,title,post):
        self.post = post
        self.title = title

    def get_post(self):
        return self.title+' '+self.post

    def io(self):
        var = "this is it"
        return var

    def __str__(self):
        return self.title