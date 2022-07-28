"""Main module to extract, transform and load data
"""
import logging
import extract
import transform
import load

# set logging config
logging.basicConfig(
    filename='debug.log',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO,
    )

MIN_CONTROL_NUMBER = 1
MAX_CONTROL_NUMBER = 20000
SIZE = 1000

def main():
    logging.info(" ------- Started ETL ----------")

    logging.info(" ------ [EXTRACT] Started ----- ")
    extract.main()
    logging.info(" ------ [EXTRACT] Finished ----- ")

    logging.info(" ------ [Transform] Started ----- ")
    transform.main()
    logging.info(" ------ [Transform] Finished ----- ")

    logging.info(" ------ [LOAD] Started ----- ")
    load.main()
    logging.info(" ------ [LOAD] Finished ----- ")

    logging.info(" ------- Finished ETL ----------")

if __name__ == '__main__':
    main()