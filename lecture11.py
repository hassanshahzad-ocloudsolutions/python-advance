#logging
#security levels

'''5 Security Levels
Debuging, Info(general information), Warning(something bad is going to be happened), Error(System breaks), Critical(when essential part of system breaks down)
'''

import logging


logging.basicConfig(level=logging.INFO) #will now also display the info logs

logging.info("You have got 20 mails in your inbox") #not visible only critical and warning logs will be displayed but we can change the configurations
logging.critical("Too much RAM is being consumed")

logger = logging.getLogger("Hassan") #noe root changed to hassan
logger.info("Hassan logger")
logger.log(logging.ERROR, "An Error Occurred")

#File Handler( our logs will be sent to a file)

handler = logging.FileHandler('mylog.log')
handler.setLevel(logging.INFO)
logger.addHandler(handler)
logger.info("This is Important Message")



