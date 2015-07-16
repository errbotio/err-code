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

    @botcmd
    def php(self, _, args):
        """ Execute the PHP expression """
        return CodePad(args, lang='PHP').eval()

    @botcmd
    def perl(self, _, args):
        """ Execute the Perl expression """
        return CodePad(args, lang='Perl').eval()

    @botcmd
    def tcl(self, _, args):
        """ Execute the TCL expression """
        return CodePad(args, lang='Tcl').eval()

    @botcmd
    def lua(self, _, args):
        """ Execute the LUA expression """
        return CodePad(args, lang='Lua').eval()
