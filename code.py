import re

from errbot import BotPlugin, botcmd
import requests
from bs4 import BeautifulSoup


def scrape_codepad(code, lang='Python', private=True, run=True):
    data = {'code': code,
            'lang': lang,
            'private': str(private),
            'run': str(run),
            'submit': 'Submit'}
    r = requests.post('http://codepad.org/', data=data)
    if not r.ok:
        return "Failed to contact codepad: %s" % r.content

    soup = BeautifulSoup(r.content, 'lxml')
    output = soup.find('a', attrs={'name': 'output'})
    if not output:
        return "Failed to parse the result page."

    result = output.findNext('div').table.tr.td.findNext('td').div.pre.text
    return '```\n%s\n```' % result.strip('\n ')


class CodeBot(BotPlugin):

    @botcmd
    def python(self, _, args):
        """ Execute the python expression.
            ie. !python print(range(10))
        """
        return scrape_codepad(args)

    @botcmd
    def c(self, _, args):
        """ Execute the c expression """
        return scrape_codepad(args, lang='C')

    @botcmd
    def cpp(self, _, args):
        """ Execute the cpp expression """
        return scrape_codepad(args, lang='C++')

    @botcmd
    def php(self, _, args):
        """ Execute the PHP expression """
        return scrape_codepad(args, lang='PHP')

    @botcmd
    def perl(self, _, args):
        """ Execute the Perl expression """
        return scrape_codepad(args, lang='Perl')

    @botcmd
    def tcl(self, _, args):
        """ Execute the TCL expression """
        return scrape_codepad(args, lang='Tcl')

    @botcmd
    def lua(self, _, args):
        """ Execute the LUA expression """
        return scrape_codepad(args, lang='Lua')
