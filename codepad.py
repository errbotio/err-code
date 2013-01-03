import requests
from bs4 import BeautifulSoup


class CodePad(object):
    def __init__(self, code=None, lang="Python", private=True, run=True):
        self.code = code
        self.lang = lang
        self.private = "True" if private else "False"
        self.run = "True" if run else "False"
        self.data = {'code': self.code, 'lang': self.lang,
                     'private': self.private, 'run': self.run,
                     'submit': 'Submit'}

    def eval(self):
        r = requests.post("http://codepad.org/", data=self.data)
        result = ''
        if r.ok:
            soup = BeautifulSoup(r.content)
            asses = soup.findAll('a')
            for a in asses:
                name = a.get('name')
                if name and name.startswith('output-line'):
                    res = a.parent.parent.parent.nextSibling.nextSibling.div.pre.string
                    if res:
                        result += res
                    else:
                        result += "Error, check the error here : " + r.url
        return result.strip('\n ').replace('&quot;', '"')
