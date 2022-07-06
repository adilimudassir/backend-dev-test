from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import ClientJobs

class ClientJobScheduler:
    def start():
        scheduler = BackgroundScheduler()
        scheduler.add_job(ClientJobs.fetch_clients, 'interval', minutes=60)
        scheduler.start()