from charly.web.webapp import launch
from charly.modules.util import Context
from charly.modules.task import task
from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(task, 'interval', [ctx], seconds=int(config["config"]["interval"]))
logger.debug("Starting TaskScheduler")
scheduler.start()

logger.debug("Launching WebApp ")
launch(config)






