import logging
logging.basicConfig(level = logging.DEBUG, filename = "logs.log", filemode = "a",format="%(asctime)s %(message)s" )

try:
    print(10/0)
except Exception:
    logging.exception(Exception)