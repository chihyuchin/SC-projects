"""
File: Bloomberg Terminal
Name: Geoffrey
----------------------
Bloomberg Terminal is a software most financial firms subscribe to obtain market data and do trades,
It is a monopoly platform when it comes to fixed-income trading, literally all bond-related trades are done on it
It's owner Mike Bloomberg ran for the Democratic presidential candidates and miserably lose
But it's all right as Bloomberg, being one of the most profitable market data providers,
has been making shit-ton of money for decades, especially during the pandemic

It is so sad but so true that markets participants, whether the buy-side or sell-side,
heavily rely on it and cannot live without it.

I'm so addicted to BBG terminal that I even use python to draw it's login page
I added the graphic name "Bloomberg Terminal" to show what it really looks like in the file for your reference.

"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow


window = GWindow(width=800, height=580, title='Bloomberg')

def main():
    """
    TODO:
    """
    background = GRect(800, 580)
    background.filled = True
    window.add(background)

    # forgot password font
    click = GLabel('Forgot Login Name or Password?')
    click.font = '-16'
    click.filled = True
    click.color = 'deepskyblue'
    window.add(click, 40, 350)

    # contact us sign
    click = GLabel(' Contact Us')
    click.font = '-15'
    click.filled = True
    click.color = 'deepskyblue'
    window.add(click, 60, 400)

    # phone
    phone = GRect(8, 14)
    phone.filled = True
    phone.fill_color = 'lightgrey'
    phone.color = 'lightgrey'
    window.add(phone, 42, 385)

    # phone screen
    screen = GRect(6, 8)
    screen.filled = True
    window.add(screen, 43, 386)

    # phone button
    button = GOval(2, 2)
    button.color = True
    window.add(button, 45, 397)

    # create account sign
    click = GLabel(' Create a New Login')
    click.font = '-15'
    click.filled = True
    click.color = 'deepskyblue'
    window.add(click, 60, 425)

    # head
    head = GOval(7, 7)
    head.filled = True
    head.fill_color = 'lightgrey'
    head.color = 'lightgrey'
    window.add(head, 42, 408)

    # neck
    neck = GRect(1, 6)
    neck.filled = True
    neck.fill_color = 'lightgrey'
    neck.color = 'lightgrey'
    window.add(neck, 45, 411)

    # body
    body = GOval(11, 5)
    body.filled = True
    body.fill_color = 'lightgrey'
    body.color = 'lightgrey'
    window.add(body, 40, 418)

    # body2
    body2 = GRect(11, 1)
    body2.filled = True
    body2.fill_color = 'lightgrey'
    body2.color = 'lightgrey'
    window.add(body2, 40, 422)

    # login box
    lg_box = GRect(90, 20)
    lg_box.filled = True
    lg_box.fill_color = 'dimgray'
    lg_box.color = True
    window.add(lg_box, 45, 250)

    # login font
    lg = GLabel('Login')
    lg.font = '-17'
    lg.filled = True
    lg.color = 'floralwhite'
    window.add(lg, 68, 270)

    # BBG title
    label = GLabel('Bloomberg')
    label.font = '-33'
    label.filled = True
    label.color = 'floralwhite'
    window.add(label, 40, 110)

    # account label
    account = GLabel('Login Name')
    account.font = '-15'
    account.filled = True
    account.color = 'floralwhite'
    window.add(account, 40, 150)

    # account box
    ac_box = GRect(150, 20)
    ac_box.filled = True
    ac_box.fill_color = 'darkorange'
    ac_box.color = 'darkorange'
    window.add(ac_box, 40, 155)

    # password label
    password = GLabel('Password')
    password.font = '-15'
    password.filled = True
    password.color = 'floralwhite'
    window.add(password, 40, 200)

    # password box
    ps_box = GRect(150, 20)
    ps_box.filled = True
    ps_box.fill_color = 'darkorange'
    ps_box.color = 'darkorange'
    window.add(ps_box, 40, 205)

    right1 = GLabel('Select Language for Analytics and')
    right1.font = '-15'
    right1.filled = True
    right1.color = 'floralwhite'
    window.add(right1, 390, 180)

    right2 = GLabel('Communication Functions: ')
    right2.font = '-15'
    right2.filled = True
    right2.color = 'floralwhite'
    window.add(right2, 390, 200)

    eng = GLabel('✓ English ')
    eng.font = '-16'
    eng.filled = True
    eng.color = 'floralwhite'
    window.add(eng, 397, 240)

    jap = GLabel('日本語 ')
    jap.font = '-18'
    jap.filled = True
    jap.color = 'darkorange'
    window.add(jap, 418, 265)

    frn = GLabel('Français ')
    frn.font = '-16'
    frn.filled = True
    frn.color = 'darkorange'
    window.add(frn, 415, 290)

    det = GLabel('Deutsch ')
    det.font = '-15'
    det.filled = True
    det.color = 'darkorange'
    window.add(det, 415, 315)

    esp = GLabel('Español ')
    esp.font = '-16'
    esp.filled = True
    esp.color = 'darkorange'
    window.add(esp, 520, 240)

    por = GLabel('Português ')
    por.font = '-16'
    por.filled = True
    por.color = 'darkorange'
    window.add(por, 520, 265)

    ita = GLabel('Italinao ')
    ita.font = '-16'
    ita.filled = True
    ita.color = 'darkorange'
    window.add(ita, 520, 290)

    man = GLabel('繁體中文 ')
    man.font = '-18'
    man.filled = True
    man.color = 'darkorange'
    window.add(man, 520, 315)

    kor = GLabel('한국어 ')
    kor.font = '-16'
    kor.filled = True
    kor.color = 'darkorange'
    window.add(kor, 630, 240)

    chn = GLabel('简体中文 ')
    chn.font = '-18'
    chn.filled = True
    chn.color = 'darkorange'
    window.add(chn, 630, 265)

    rus = GLabel('Pyccкий ')
    rus.font = '-16'
    rus.filled = True
    rus.color = 'darkorange'
    window.add(rus, 630, 290)

    right3 = GLabel('To customize your News language experience')
    right3.font = '-15'
    right3.filled = True
    right3.color = 'lightgrey'
    window.add(right3, 390, 350)

    right4 = GLabel('type LANG <GO> after login. ')
    right4.font = '-15'
    right4.filled = True
    right4.color = 'lightgrey'
    window.add(right4, 390, 370)

    down1 = GLabel('S/N 175387-0 | SID 3760936-1 | Version 08 Aug 20 | Netid N193')
    down1.font = '-13'
    down1.filled = True
    down1.color = 'grey'
    window.add(down1, 40, 470)

    down2 = GLabel('The BLOOMBERG PROFESSIONAL serviec and data products are owned and distributed by '
                   'BLOOMBERG Finance L.P.and its subsidiaries(BFLP) except')
    down2.font = '-10'
    down2.filled = True
    down2.color = 'lightgrey'
    window.add(down2, 30, 500)

    down3 = GLabel('in Argentina, Bermuda, China, India, Japan, Korea (where Bloomberg L.P. and its subsidiaries (BLP)'
                   'distribute these products). BLP provides BFLP with')
    down3.font = '-10'
    down3.filled = True
    down3.color = 'lightgrey'
    window.add(down3, 30, 516)

    down4 = GLabel('global marketing and operational support and service for these products. BFLP and BLP believe the '
                   'information herein came from reliable sources.')
    down4.font = '-10'
    down4.filled = True
    down4.color = 'lightgrey'
    window.add(down4, 30, 532)

    down5 = GLabel('but do not guarantee its accuracy. No information or opinion herein constitutes a solicitation of'
                   'the purchase or sale of securities or commodities.')
    down5.font = '-10'
    down5.filled = True
    down5.color = 'lightgrey'
    window.add(down5, 30, 548)


if __name__ == '__main__':
    main()
