* `django.log`: Contains logs by Django framework like executed SQL statements
* `project.log`: Contains logs from the `project` logger. For example:

		# At the top of your file/module
		import logging
		logger = logging.getLogger("project")

		# Anywhere else in the file
		logger.info('Started processing foo')
