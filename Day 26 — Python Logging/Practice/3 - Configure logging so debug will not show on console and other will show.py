import logging

# logging.basicConfig(level=logging.INFO)

# logging.info("Info about something .")

# logging.warning("Give warning for some operation")

# logging.error("Error must be handle or error occur ")

# logging.critical("Critical problem occur .")

# # This will not show on console if its in start are last
# logging.debug("Program debuging start ")
logging.basicConfig(filename="infoa.log",level=logging.INFO , format="%(asctime)s - %(levelname)s - %(message)s")
logging.StreamHandler("__name__")
try:
    number = int("abc")
except:
    logging.exception("Something went wrong")
