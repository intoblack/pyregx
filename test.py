

from pyregx.pyregx import PPattern


if __name__ == "__main__":

    p = PPattern()
    print p.IP != '123.145.23.45'
    del p.IP
    print p.mail.find_iter('xxx1212@126.com')
    print p.html_tag.find_iter("<html xx=11>")
    print p.date  == '2013/12/05'
    print 'xx'.replace('x', 'y')