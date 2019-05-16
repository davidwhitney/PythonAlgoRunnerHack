class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def execute(self):
        context = {}
        
        for step in self.steps:
            step(context)
        
        return context