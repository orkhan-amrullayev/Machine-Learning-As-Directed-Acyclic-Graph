class TaskProcess(d6tflow.tasks.TaskPqPandas): # define output format

    def requires(self):
        return TaskGetData() # define dependency

    def run(self):
        data = self.input().load() # load input data
        data = do_stuff(data) # process data
        self.save(data) # save output data
