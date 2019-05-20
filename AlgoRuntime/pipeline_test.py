import unittest
import time
import importlib
import logging
import io
import pipeline as pipeline

class PipelineTest(unittest.TestCase):
    
    def test_execute_runs_steps(self):
        self.has_run = False

        result = pipeline.Pipeline({
            "Step1": lambda ctx: self.mark_as_executed()
        }).execute()

        self.assertEqual(self.has_run, True)
    
    def test_times_execution_and_adds_it_to_result(self):
        result = pipeline.Pipeline({
            "Step1": lambda ctx: self.mark_as_executed()
        }).execute()

        self.assertEqual(result["timings"][0], "Completed: 'Step1''. Took 0.0ms")
    
    
    def test_times_execution_and_adds_it_to_result_for_actual_work(self):
        result = pipeline.Pipeline({
            "Step1": lambda ctx: time.sleep(1)
        }).execute()

        self.assertTrue(result["timings"][0].startswith("Completed: 'Step1''. Took 1"))
    
    def test_logs_output(self):
        logs = io.StringIO()
        logging_spy = logging.StreamHandler()
        logging_spy.setStream(logs)
        logging.getLogger().addHandler(logging_spy)

        result = pipeline.Pipeline({
            "Step1": lambda ctx: time.sleep(0)
        }).execute()

        logs.seek(0)
        log_contents = logs.readlines()

        self.assertIn("blah", log_contents)

    def mark_as_executed(self):
        self.has_run = True

if __name__ == '__main__':
    unittest.main()