# -*- coding: utf-8 -*-
import subprocess
import sys


class Configuration(object):
    def __init__(self, wkhtmltopdf='', meta_tag_prefix='pdfkit-'):
        self.meta_tag_prefix = meta_tag_prefix

        self.wkhtmltopdf = wkhtmltopdf
        '''
        if not self.wkhtmltopdf:
            if sys.platform == 'win32':
                self.wkhtmltopdf = subprocess.Popen(
                    ['where', 'wkhtmltopdf'], stdout=subprocess.PIPE).communicate()[0].strip()
            else:
                self.wkhtmltopdf = subprocess.Popen(
                    ['which', 'wkhtmltopdf'], stdout=subprocess.PIPE).communicate()[0].strip()

        try:
            with open(self.wkhtmltopdf) as f:
                pass
        except IOError:
            raise IOError('No wkhtmltopdf executable found: "%s"\n'
                          'If this file exists please check that this process can '
                          'read it. Otherwise please install wkhtmltopdf - '
                          'https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf' % self.wkhtmltopdf)
        '''
        #
        # (davidpower)  I don't know other but win32 platform's `where` command only search from current
        #               dir and system $PATH environment variable (user's $PATH doesn't work), so
        #               to make things easier, instead of query exec path from `where`/`which`,
        #               I chose testing with `--version` flag.
        #
        if not self.wkhtmltopdf:
            self.wkhtmltopdf = 'wkhtmltopdf'

        stdout, stderr = subprocess.Popen(
                        [self.wkhtmltopdf, '--version'],
                        shell= True,
                        stdout= subprocess.PIPE,
                        stderr= subprocess.PIPE,
                        stdin= subprocess.PIPE).communicate()
        if stderr:
            raise IOError('No wkhtmltopdf executable found: \n%s' % self.wkhtmltopdf)
