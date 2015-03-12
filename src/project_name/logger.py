# Support new str.format syntax in log messages
#
# Based on http://stackoverflow.com/a/25433007 and
# http://stackoverflow.com/a/26003573 and logging cookbook
# https://docs.python.org/3/howto/logging-cookbook.html#use-of-alternative-formatting-styles
#
# It's worth noting that this implementation has problems if key words
# used for brace substitution include level, msg, args, exc_info,
# extra or stack_info. These are argument names used by the log method
# of Logger. If you need to one of these names then modify process to
# exclude these names or just remove log_kwargs from the _log call. On
# a further note, this implementation also silently ignores misspelled
# keywords meant for the Logger (eg. ectra).
#


import logging


class NewStyleLogMessage(object):
    def __init__(self, message, *args, **kwargs):
        self.message = message
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        args = (i() if callable(i) else i for i in self.args)
        kwargs = dict((k, v() if callable(v) else v)
                      for k, v in self.kwargs.items())

        return self.message.format(*args, **kwargs)

N = NewStyleLogMessage


class StyleAdapter(logging.LoggerAdapter):
    def __init__(self, logger, extra=None):
        super(StyleAdapter, self).__init__(logger, extra or {})

    def log(self, level, msg, *args, **kwargs):
        if self.isEnabledFor(level):
            msg, log_kwargs = self.process(msg, kwargs)
            self.logger._log(level, N(msg, *args, **kwargs), (),
                             **log_kwargs)


logger = StyleAdapter(logging.getLogger("project"))
#   Emits "Lazily formatted log entry: 123 foo" in log
# logger.debug('Lazily formatted entry: {0} {keyword}', 123, keyword='foo')
