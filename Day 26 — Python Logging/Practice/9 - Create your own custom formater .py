import logging

file=logging.FileHandler("file.log")

console=logging.StreamHandler()

formatter=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

file.setFormatter(formatter)

console.setFormatter(formatter)

logging.basicConfig(handlers=[file,console],level=logging.INFO)

logging.info("Program started .")

logging.info(" Print something .")

logging.info("Program ended .")