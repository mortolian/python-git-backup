class Logger:
    """
    Logger is for creating log files.
    """

    def write_to_log(self, logfile_path, append, log_string):
        append = 'a' if append else 'w'
        file = open(logfile_path, append)
        response = file.write(log_string)
        file.close()
        print(response)
        return response
