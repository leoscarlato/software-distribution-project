#!/usr/bin/env python3
from dev_aberto import hello
from datetime import datetime
import babel.dates as dates
import gettext

if __name__ == '__main__':
    gettext.bindtextdomain('cli', 'locale')
    gettext.textdomain('cli')
    _ = gettext.gettext

    date, name = hello()

    real_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    formatted_date = dates.format_date(real_date, locale='en_US')

    print(_('Último commit feito em:'), formatted_date, _('por'), name)