from twill.browser import TwillBrowser
from BeautifulSoup import BeautifulSoup
import ClientForm

from urllib import unquote

import sys

class ListManipulator(object):
    def __init__(self, uri, adminpw):

        self.uri = uri
        if self.uri.startswith('http://'):
            self.uri = self.uri.replace('http://', 'https://', 1)
        
        if not self.uri.startswith('https://'):
            self.uri = 'https://' + self.uri

        if not self.uri.endswith('/'):
            self.uri += '/'

        self.br = TwillBrowser()
        self.br._browser.addheaders.append(('User-agent', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.7 Safari/533.2'))

        self.br.go(self.uri)
        code = self.br.get_code()
        if code != 200:
            raise Exception, "(Code: %i)  Failed to access %s."%(code,self.uri)

        # Now login...
        form = self.br.get_all_forms()[0]
        form['adminpw'] = adminpw
        self.br.clicked(form, form.find_control('admlogin'))
        self.br.submit()
        code = self.br.get_code()

        if code != 200:
            raise Exception, "(Code: %i)  Failed to login @ %s."%(code,self.uri)
        
        
    def has_subscriber(self, addr):
        if not isinstance(addr, str):
            raise ValueError, '`addr` must be a string (type "str")'
        
        loc = "%s%s" % ( self.uri, 'members/list')
        self.br.go(loc)
        code = self.br.get_code()
        if code != 200:
            raise Exception, "(Code: %i)  Failed to access %s." % (code, loc)

        form = self.br.get_all_forms()[0]
        form['findmember'] = addr
        self.br.clicked(form, form.find_control('findmember_btn'))
        self.br.submit()
        code = self.br.get_code()
        if code != 200:
            raise Exception, "(Code: %i)  Failed to search %s." % (code,loc)
        form = self.br.get_all_forms()[0]
        try:
            field = form.find_control('user')
            found = unquote(field.attrs['value'])
            return found == addr
        except ClientForm.ControlNotFoundError:
            return False

    def subscribe(self, addrs):
        if not isinstance(addrs, list):
            raise ValueError, '`addrs` must be a list of email addresses'

        loc = "%s%s" % ( self.uri, 'members/add')
        self.br.go(loc)
        code = self.br.get_code()
        if code != 200:
            raise Exception, "(Code: %i)  Failed to access %s." % (code, loc)

        form = self.br.get_all_forms()[0]
        form['subscribees'] = '\n'.join(addrs)
        self.br.clicked(form, form.find_control('setmemberopts_btn'))
        self.br.submit()
        code = self.br.get_code()
        if code != 200:
            raise Exception, "(Code: %i)  Failed to add @ %s." % (code,loc)

    def unsubscribe(self, addrs):
        if not isinstance(addrs, list):
            raise ValueError, '`addrs` must be a list of email addresses'

        loc = "%s%s" % ( self.uri, 'members/remove')
        self.br.go(loc)
        code = self.br.get_code()
        if code != 200:
            raise Exception, "(Code: %i)  Failed to access %s." % (code, loc)

        form = self.br.get_all_forms()[0]
        form['unsubscribees'] = '\n'.join(addrs)
        self.br.clicked(form, form.find_control('setmemberopts_btn'))
        self.br.submit()
        code = self.br.get_code()
        if code != 200:
            raise Exception, "(Code: %i)  Failed to add @ %s." % (code,loc)



        




