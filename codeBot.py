from errbot import BotPlugin, botcmd
from codepad import CodePad


class CodeBot(BotPlugin):

    @botcmd
    def python(self, _, args):
        """ Execute the python expression """
        return CodePad(args).eval()

    @botcmd
    def c(self, _, args):
        """ Execute the c expression """
        return CodePad(args, lang='C').eval()

    @botcmd
    def cpp(self, _, args):
        """ Execute the c expression """
        return CodePad(args, lang='C++').eval()
