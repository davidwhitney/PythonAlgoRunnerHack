import logging
import time

class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def execute(self):
        context = {
            "timings": []
        }

        for key, step in self.steps.items():
            logging.info(f"Step: '{key}'.'")
            start = time.time()

            step(context)
            
            end = time.time()
            time_message = f"Completed: '{key}''. Took {end - start}ms"
            context["timings"].append(time_message)
            logging.info(time_message)


        return context