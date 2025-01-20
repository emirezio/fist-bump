import logging

class HeaderFilter(logging.Filter):
    def __init__(self, header):
        super().__init__()
        self.header = header

    def filter(self, record):
        record.name = self.header
        return True


class Config:
    def __init__(self, log_file="app.log", log_level=logging.DEBUG, log_header=""):
        self.log_file = log_file
        self.log_level = log_level
        self.log_header = log_header
        self.configure_logging()

    def configure_logging(self):
        logging.basicConfig(
            level=self.log_level,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            filename=self.log_file,
            filemode="a"
        )
        self.logger = logging.getLogger(self.log_header or "DefaultLogger")

        if self.log_header:
            header_filter = HeaderFilter(self.log_header)
            self.logger.addFilter(header_filter)

        self.logger.info("Log Configuration is done.")
