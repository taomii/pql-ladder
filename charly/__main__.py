import configparser
import logging
from charly.web.webapp import launch
from charly.modules.util import Context
from charly.modules.task import task
from apscheduler.schedulers.background import BackgroundScheduler

logger = logging.getLogger(__name__)
logger.debug("Starting Charly ")

config = configparser.ConfigParser()
config.read("../config.ini")

ctx = Context(
        logger=logger,
        config=config,
    )

if "config" in config and "interval" in config["config"]:
    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(task, 'interval', [ctx], seconds=int(config["config"]["interval"]))
    logger.debug("Starting TaskScheduler")
    scheduler.start()

    logger.debug("Launching WebApp ")
    launch(config)






