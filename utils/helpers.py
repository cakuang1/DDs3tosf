import datetime


def timetostring(): 
   return datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

