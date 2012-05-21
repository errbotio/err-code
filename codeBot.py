__author__ = 'gbin'

from botplugin import BotPlugin
from jabberbot import botcmd
from less_serious_plugins.codepad import CodePad

class CodeBot(BotPlugin):
    
    @botcmd
    def python(self, mess, args):
        """ Execute the python expression """
        return CodePad(args).eval()

    @botcmd
    def c(self, mess, args):
        """ Execute the c expression """
        return CodePad(args, lang='C').eval()

    @botcmd
    def cpp(self, mess, args):
        """ Execute the c expression """
        return CodePad(args, lang='C++').eval()
