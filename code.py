import re

from errbot import BotPlugin, botcmd
import requests
from bs4 import BeautifulSoup


class CodeBot(BotPlugin):

    def scrape_codepad(self, code=None, lang='Python', private=True, run=True):
        data = {'code': code,
                'lang': lang,
                'private': str(private),
                'run': str(run),
                'submit': 'Submit'}
        r = requests.post('http://codepad.org/', data=data)
        if not r.ok:
            return "Failed to contact codepad: %s" % r.content

        results = []
        soup = BeautifulSoup(r.content, 'lxml')
        all_as = soup.findAll('a', attrs={'name': re.compile(r'^output-line-\d+$')})
        for a in all_as:
            res = a.parent.parent.parent.nextSibling.nextSibling.div.pre.string
            if not res:
                results = ['Error, check the error here : %s' % r.url]
                break
            results.append(res)

        return ''.join(results).strip('\n ').replace('&quot;', '"')

    @botcmd
    def python(self, _, args):
        """ Execute the python expression """
        return self.scrape_codepad(args)

    @botcmd
    def c(self, _, args):
        """ Execute the c expression """
        return self.scrape_codepad(args, lang='C')

    @botcmd
    def cpp(self, _, args):
        """ Execute the c expression """
        return self.scrape_codepad(args, lang='C++')

    @botcmd
    def php(self, _, args):
        """ Execute the PHP expression """
        return self.scrape_codepad(args, lang='PHP')

    @botcmd
    def perl(self, _, args):
        """ Execute the Perl expression """
        return self.scrape_codepad(args, lang='Perl')

    @botcmd
    def tcl(self, _, args):
        """ Execute the TCL expression """
        return self.scrape_codepad(args, lang='Tcl')

    @botcmd
    def lua(self, _, args):
        """ Execute the LUA expression """
        return self.scrape_codepad(args, lang='Lua')
