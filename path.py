class Login:
    textbox_username_id = "username"
    textbox_password_id = "password"
    button_login_xpath = "/html/body/div/div/div[2]/div/div/div/div/div[2]/form/div[3]/button"

class Dashboard:
    dashbutton = '/html/body/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/h5'
    back = "/html/body/div/nav/div/div/ul[1]/li[1]/a"
    pressalert = "/html/body/div/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/ul/li[1]/div"
    backbutton = "/html/body/div/div/div[2]/div/div/div/div[1]/div/div[2]/button/div/span"

class Map:
    menubarmap = "/html/body/div[1]/nav/div/div/ul[1]/li[2]/a"
    search = '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/input'
    clickbutton = "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/form/div/div[2]/div/label/input"
    clickbutton1 = "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/form/div/div[1]/div/label/input"

class Report:
    expand = "/html/body/div[1]/nav/div/div/ul[1]/div[1]/li/a"
    clickoption = "/html/body/div[1]/nav/div/div/ul[1]/div[1]/li/div/ul/li[3]/a"
    search1 = '/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/label/input'
    clicksearch = "/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/i"
    backbutton = "/html/body/div/div/div[2]/div/div/div/div[1]/div/div[2]/button/div/span"
    edit = "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[3]/i"
    remark = '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/textarea'
    clickcancel = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/div/div[2]/div[1]/div/i"
    frame = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/div"
    year = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/div/div[2]/div[2]/div/table/thead/tr[1]/th[2]"
    month = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/div/div[2]/div[2]/div/table[2]/tbody/tr[2]/td[1]"
    day = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[1]"
    save = "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[3]/i[2]"
    seedetails = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[1]/div/div/span[3]/button"
    inspection_status = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div/div/div[2]/div/div[1]/i"
    remark1 = '/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div/div/div[2]/div/div[2]/div[2]/textarea'
    editclick = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div/div/div[2]/div/div[3]/i"
    clickbox = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div/div/div[2]/div/div[2]/div[2]/label/input"
    remark2 = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div/div/div[2]/div/div[3]/div[2]/textarea"
    submit = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div/div/div[2]/div/div[5]/button/span[2]"
    editrevisit = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/i"
    require = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/div[2]/label/input"
    frame1 = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/div[4]/div[1]"
    year1 = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/div[4]/div[1]/div[2]/div[2]/div/table/thead/tr[1]/th[2]"
    month1 = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/div[4]/div[1]/div[2]/div[2]/div/table[2]/tbody/tr[2]/td[1]"
    day1 = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[1]"
    submit1 = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[4]/button/span[2]"
    choice = '/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/table/tbody/tr[6]'
