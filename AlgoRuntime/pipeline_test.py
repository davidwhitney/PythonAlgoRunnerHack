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
        with self.assertLogs('', level='INFO') as cm:
            pipeline.Pipeline({
                "Step1": lambda ctx: time.sleep(1)
            }).execute()

            # "INFO:root:Completed: 'Step1'. Took 1"

            
            self.assertTrue(any(logline.startswith("INFO:root:Completed: 'Step1'. Took 1") for logline in cm.output) )
    
    def test_logs_output(self):
        with self.assertLogs('', level='INFO') as cm:
            pipeline.Pipeline({
                "Step1": lambda ctx: time.sleep(0)
            }).execute()
            
            self.assertEqual(cm.output, ["INFO:root:Completed: 'Step1'. Took 0.0ms"])

    def mark_as_executed(self):
        self.has_run = True

if __name__ == '__main__':
    unittest.main()