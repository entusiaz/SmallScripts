# imports
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

# Create a scheduler
sched = BackgroundScheduler(daemon=True)

# Define main application logic 
counter = 0
def sensor():
	global counter
	sched.print_jobs()
	print('Cont: ', count)
	counter += 1

# Add a job using an anonymous function
# sched.add_job(lambda : sched.print_jobs(), 'interval', seconds=5)

# Add a job with an actual function
sched.add_job(sensor, 'cron', second='*')

# Start scheduler
sched.start()


# Flask runner
app = Flask(__name__)

if __name__ == "__main__":
	app.run('0.0.0.0', port=3000)

