import logging
file=logging.FileHandler("handle.log")
consol=logging.StreamHandler()
formatter=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file.setFormatter(formatter)
consol.setFormatter(formatter)
logging.basicConfig(handlers=[file,consol],level=logging.INFO)
logger=logging.getLogger(__name__)

logger.info("Progrma started .")

logger.warning("Sothing happened .")

logger.info("Program ended .")

