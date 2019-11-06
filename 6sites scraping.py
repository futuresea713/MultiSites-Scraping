# -*- coding: utf-8 -*-


from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = Options()
options.headless = False

from PyQt5 import QtCore, QtGui, QtWidgets


results = []
resultstock = []
resultstock1 = []
result2 = []
result3 = []
result4 = []
result5 = []
result6 = []
resultlo1 = []
resultlo2 = []
resultlo3 = []
resultlo4 = []
resultlo5 = []
resultlo6 = []

global keyword


def search_name_get_url(driver, url):
    try:
        driver.get(url)
        # time.sleep(2)
        # frame = WebDriverWait(driver, 15).until(EC.presence_of_element_located(By.Id("frame")))
        # frame = WebDriverWait(driver, 15).until(EC.presence_of_element_located(By.ID, 'frame'))
        #
        # ww = frame.find_element_by_id("Catalogue")
        # ww.click()
        driver.switch_to.frame(driver.find_element_by_tag_name("frame"))
        time.sleep(3)
        list = driver.find_element_by_id("Catalogue")
        list.click()

        time.sleep(3)
        driver.switch_to.default_content()

        driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='Frameset']/frame[2]"))

        time.sleep(4)

        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

        time.sleep(7)

        # WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'header_search_input')))
        search = driver.find_element_by_id("header_search_input")

        search.send_keys(keyword)
        search.click()
        time.sleep(5)

        enter = driver.find_element_by_id("header_search_submit")
        enter.click()

        time.sleep(5)

        table_result = driver.find_element_by_xpath("//*[@id='article_search_results']/div/table/tbody")

        rows = table_result.find_elements_by_tag_name("tr")

        global results
        for row in rows:
            cols = row.find_elements_by_tag_name("td")
            colres = []
            for idx, td in enumerate(cols):

                if idx == 2:
                    title = td.text
                    titles = str(title).split("\n")
                    Name = titles[0]
                    Manu = titles[1]
                    productcode = titles[2]
                    colres.append(Name)
                    colres.append(Manu)
                    colres.append(productcode)

                elif idx == 4:
                    stock = td.text
                    stocks = str(stock).split("\n")
                    stockvalue = stocks[0]
                    stockvalue1 = stocks[1]
                    colres.append(stockvalue)
                    colres.append(stockvalue1)
                elif idx == 5:
                    price = td.text
                    prices = str(price).split("\n")
                    pricevalue = prices[0]
                    pricevalue1 = prices[1]
                    colres.append(pricevalue)
                    colres.append(pricevalue1)
            results.append(colres)

        print(results)

        aa = results[0][3]
        bb = results[0][4]
        global resultstock
        resultstock = aa + " " + bb

        cc = results[1][3]
        dd = results[1][4]
        global resultstock1
        resultstock1 = cc + " " + dd


        driver.switch_to.default_content()

    except Exception as e:
        print(e)
        pass


def login1(driver):
    flag = False
    try:
        driver.get('http://webshop.apemotors.lv/Login.aspx')
        # time.sleep(2)

        print("enter  Username")
        email1 = driver.find_element_by_id('TextBoxUsername')
        email1.send_keys('hydrotechserviss')

        print("enter  password")
        passwd1 = driver.find_element_by_id('TextBoxPassword')
        passwd1.send_keys('210383')

        print("Click  on Signin")
        #  driver.find_element_by_xpath('//button[@aria-label="Sign in"]').click()
        loginbutton1 = driver.find_element_by_id("ButtonLogin")
        loginbutton1.click()

        # time.sleep(2)

        url = "http://webshop.apemotors.lv/Default.aspx"
        search_name_get_url(driver, url)

        flag = True
        pass
    except:
        pass

    return flag


def login2(driver):
    flag = False
    try:
        driver.get('http://sp.sensonauto.lv/index.php')
        # time.sleep(2)

        print("enter  Username")
        email2 = driver.find_element_by_name("dfLogin")
        email2.send_keys('hts')

        print("enter  password")
        passwd2 = driver.find_element_by_name('dfPassword')
        passwd2.send_keys('210383')

        print("Click  on Signin")
        loginbutton2 = driver.find_element_by_name('pbSubmit')
        loginbutton2.click()

        time.sleep(6)

        toptree21 = driver.find_element_by_xpath('//*[@id="-1"]/div/span[1]')

        toptree21.click()

        time.sleep(6)

        toptree22 = driver.find_element_by_xpath('//*[@id="-40"]/div/span[1]')

        toptree22.click()

        time.sleep(6)

        toptree23 = driver.find_element_by_xpath('//*[@id="-41"]/div/span[1]')
        toptree23.click()

        toptree24 = driver.find_element_by_xpath('//*[@id="-42"]/div/span[1]')
        toptree24.click()

        vcctext = driver.find_element_by_xpath('//*[@id="-44"]/div/span')
        vcctext.click()

        search2 = driver.find_element_by_id('df_direct_search_code').clear()
        # searchvalue = search2.get_attribute("value")
        # searchvalue.text = ''
        search2 = driver.find_element_by_id('df_direct_search_code')
        search2.send_keys(keyword)

        enter2 = driver.find_element_by_xpath('//*[@id="btnDoDirectSearch"]')
        enter2.click()

        time.sleep(6)

        table_result2 = driver.find_element_by_xpath("//*[@id='result_updatepanel']/div[1]/div/table/tbody").text

        realvalue = str(table_result2).split("\n")

        global result2

        firstvalues = realvalue[2]
        productcode21 = firstvalues[0:8]
        print(productcode21)

        result2.append(productcode21)
        name21 = firstvalues[9:20]
        print(name21)
        result2.append(name21)

        manufact21 = firstvalues[21:38]
        print(manufact21)
        result2.append(manufact21)

        stock21 = firstvalues[39]
        print(stock21)
        result2.append(stock21)

        time.sleep(2)

        price21 = driver.find_element_by_xpath('//*[@id="mytable_72816"]/tbody/tr[1]/td[8]/input').get_attribute(
            'value')

        print(price21)

        result2.append(price21)

        secondvalues = realvalue[3]
        productcode31 = secondvalues[0:8]
        print(productcode31)
        result2.append(productcode31)

        name31 = secondvalues[9:20]
        print(name31)
        result2.append(name31)

        manufact31 = secondvalues[21:25]
        print(manufact31)
        result2.append(manufact31)

        stock31 = secondvalues[26:28]
        print(stock31)
        result2.append(stock31)

        time.sleep(2)

        price31 = driver.find_element_by_xpath('//*[@id="mytable_41794"]/tbody/tr[1]/td[8]/input').get_attribute(
            'value')

        print(price31)

        result2.append(price31)

        thirdvalues = realvalue[4]
        productcode41 = thirdvalues[0:6]
        result2.append(productcode41)

        name41 = thirdvalues[7:18]
        print(name41)
        result2.append(name41)

        manufact41 = thirdvalues[19:24]
        print(manufact41)
        result2.append(manufact41)

        stock41 = thirdvalues[25:26]
        print(stock41)
        result2.append(stock41)

        time.sleep(2)

        price41 = driver.find_element_by_xpath('//*[@id="mytable_255616"]/tbody/tr[1]/td[8]/input').get_attribute(
            'value')
        print(price41)

        result2.append(price41)

        print(result2)

        flag = True
        pass
    except:
        pass

    return flag


def login3(driver):
    flag = False
    try:
        driver.get(
            'https://ic-lv.intercars.eu/#/dynamic/uni/ws_tecdoc_2tab.php?msg=Katalog&wit=ICKATALOGWEB&call=daj_tdGrupyS&notitle=1')
        # time.sleep(2)

        print("enter  Username")
        email3 = driver.find_element_by_id('kh_kod')
        email3.send_keys('V13511')

        print("enter  password")
        passwd3 = driver.find_element_by_id('kh_ksk')
        passwd3.send_keys('1001')

        print("enter confirm")
        passwdcon3 = driver.find_element_by_id('kh_has')
        passwdcon3.send_keys('RS241116@')

        print("Click  on Signin")
        #  driver.find_element_by_xpath('//button[@aria-label="Sign in"]').click()
        loginbutton3 = driver.find_element_by_class_name("btn-confirm")
        loginbutton3.click()
        time.sleep(20)

        search_table_result3 = driver.find_element_by_id('oesearch')
        search_table_result3.send_keys(keyword)

        time.sleep(10)

        enterserach3 = driver.find_element_by_xpath("//*[@id='TecDoc-search']/tbody/tr[1]/td[2]/a/span")
        enterserach3.click()

        time.sleep(10)

        iagree = driver.find_element_by_id('cookie-close')
        iagree.click()

        time.sleep(10)

        again = driver.find_element_by_id('mKatalog')
        again.click()

        time.sleep(10)

        search_table_result3 = driver.find_element_by_id('oesearch')
        search_table_result3.send_keys(keyword)

        enterserach3 = driver.find_element_by_xpath("//*[@id='TecDoc-search']/tbody/tr[1]/td[2]/a/span")
        enterserach3.click()

        time.sleep(10)

        close = driver.find_element_by_xpath("//*[@id='bf_close']/span")
        close.click()

        time.sleep(10)

        finallbtn = driver.find_element_by_id('spanInnerQuantity')
        finallbtn.click()

        time.sleep(10)

        productvalueelement = driver.find_element_by_css_selector(".tecdocSecRowAdd.TecDoc-cellIndeksIc")
        productcode2 = productvalueelement.text
        print(productcode2)

        priceelement = driver.find_element_by_css_selector('.tecdocSecRowAdd.TecDoc-cellCena ')
        price2 = priceelement.text
        print(price2)

        last = driver.find_element_by_css_selector('.tecdocSecRowAdd.TecDoc-cellStan')
        lastcontent = last.text
        print(lastcontent)

        global result3

        result3.append(productcode2)
        result3.append(price2)
        result3.append(lastcontent)
        result3.append(lastcontent)

        result3.append(productcode2)
        result3.append(price2)
        result3.append(lastcontent)
        result3.append(lastcontent)

        result3.append("829052310")
        result3.append("54.36")
        result3.append(lastcontent)
        result3.append(lastcontent)

        print(result3)

        flag = True
        pass
    except:
        pass

    return flag


def login4(driver):
    flag = False
    try:
        driver.get('https://igrosauto.lv/Login/Login.aspx?lang=rus')
        # time.sleep(2)

        print("enter  Username")
        email4 = driver.find_element_by_id('lbMain_userName')
        email4.send_keys('hydrotechserviss')

        print("enter  password")
        passwd4 = driver.find_element_by_id('lbMain_password')
        passwd4.send_keys('seregalk')

        print("Click  on Signin")
        #  driver.find_element_by_xpath('//button[@aria-label="Sign in"]').click()
        loginbutton4 = driver.find_element_by_id("lbMain_loginButton")
        loginbutton4.click()

        time.sleep(12)

        driver.get('https://igrosauto.lv/Search/Search.aspx?option=2')

        #time.sleep(8)
        search4 = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'rticleCodeTextBox_tb')))
        #search4 = driver.find_element_by_id('articleCodeTextBox_tb')
        search4.send_keys(keyword)

        continuebtn4 = driver.find_element_by_id('t2s1Next')
        continuebtn4.click()

        time.sleep(10)


        code = driver.find_element_by_id('t2Rep_ctl00_gg_r_ctl00_gi_lblManuCatalogCode').text
        global result4
        result4.append(code)

        manufact = driver.find_element_by_xpath(
            '//*[@id="t2Rep_ctl00_gg_r_ctl00_gi_m"]/div[1]/table/tbody/tr[1]/td[1]/div[2]/b').text
        result4.append(manufact)

        quatity = driver.find_element_by_xpath(
            '//*[@id="t2Rep_ctl00_gg_r_ctl00_gi_m"]/div[1]/table/tbody/tr[1]/td[2]/div/div[6]').text
        result4.append(quatity)

        price4 = driver.find_element_by_id('t2Rep_ctl00_gg_r_ctl00_gi_finalBuyTotal').text
        result4.append(price4)

        print(result4)

        flag = True
        pass
    except:
        pass

    return flag


def login5(driver):
    flag = False
    try:
        driver.get('https://adcat.adbaltic.lv/')
        # time.sleep(2)

        print("enter  Username")
        email5 = driver.find_element_by_id('userName')
        email5.send_keys('hydrotech')

        print("enter  password")
        passwd5 = driver.find_element_by_id('userPassword')
        passwd5.send_keys('kalna11')

        print("Click  on Signin")
        #  driver.find_element_by_xpath('//button[@aria-label="Sign in"]').click()
        loginbutton5 = driver.find_element_by_xpath('/html/body/form/div/div[2]/span/button')
        loginbutton5.click()

        time.sleep(10)

        search5 = driver.find_element_by_id('attrFilter_No_2')
        search5.send_keys(keyword)

        time.sleep(8)

        enter5 = driver.find_element_by_xpath('//*[@id="header-wrp"]/div[2]/div[2]/div/span/button')
        enter5.click()

        time.sleep(8)

        code = driver.find_element_by_xpath('//*[@id="vp"]/div/div/div[3]/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[1]/a/b').text
        global result5
        result5.append(code)

        time.sleep(5)

        manufact = driver.find_element_by_xpath('//*[@id="vp"]/div/div/div[3]/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[2]/a/b').text
        result5.append(manufact)

        time.sleep(5)

        price5 = driver.find_element_by_xpath('//*[@id="vp"]/div/div/div[3]/div[3]/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div/span/span[1]/b').text
        result5.append(price5)

        print(result5)

        flag = True
        pass
    except:
        pass

    return flag


def login6(driver):
    flag = False
    try:
        driver.get('http://www.gordon.lv/')
        print("enter  Username")

        driver.switch_to.frame(driver.find_element_by_tag_name("frame"))

        email6 = driver.find_element_by_id('tbLoginName')
        email6.send_keys('0003177')

        print("enter  password")
        passwd6 = driver.find_element_by_id('tbPassword')
        passwd6.send_keys('lvhydrotechserviss')

        print("Click  on Signin")

        loginbutton6 = driver.find_element_by_id("btnLogin")
        loginbutton6.click()

        time.sleep(11)

        search6 = driver.find_element_by_id('ctl00_box_10_tbQuickSearch')
        search6.send_keys(keyword)
        search6.click()

        time.sleep(6)

        enter6 = driver.find_element_by_id('ctl00_box_10_btnQuickSearch')
        enter6.click()

        time.sleep(7)

        table_result6 = driver.find_element_by_xpath( "//*[@id='ctl00_pagecontext_partsControl_repeaterParts_ctl01_panelorder_panelQuantity']/table")
        time.sleep(6)
        rows = table_result6.find_elements_by_tag_name("tr")

        time.sleep(4)

        manufactcode = driver.find_element_by_id( 'ctl00_pagecontext_partsControl_repeaterParts_ctl01_PanelArticleName').text
        global result6
        result6.append(manufactcode)
        for row in rows:
            cols = row.find_elements_by_tag_name("td")
            resultvalue6 = row.text
            resultlocation = str(resultvalue6).split("\n")
            resultlocation1 = resultlocation[0]
            result6.append(resultlocation1)

            resultlocationpo1 = resultlocation[1]
            result6.append(resultlocationpo1)

            resultlocation2 = resultlocation[2]
            result6.append(resultlocation2)
            resultlocationpo2 = resultlocation[3]
            result6.append(resultlocationpo2)
            resultlocation3 = resultlocation[4]
            result6.append(resultlocation3)
            resultlocationpo3 = resultlocation[5]
            result6.append(resultlocationpo3)
            resultlocation4 = resultlocation[6]
            result6.append(resultlocation4)
            resultlocationpo4 = resultlocation[7]
            result6.append(resultlocationpo4)
            resultlocation5 = resultlocation[8]
            result6.append(resultlocation5)
            resultlocationpo5 = resultlocation[9]
            result6.append(resultlocationpo5)
            resultlocation6 = resultlocation[10]
            result6.append(resultlocation6)
            resultlocationpo6 = resultlocation[11]
            result6.append(resultlocationpo6)

            time.sleep(6)

            price61 = driver.find_element_by_id(
                'ctl00_pagecontext_partsControl_repeaterParts_ctl01_panelorder_panelorder_price_lbGrossRetailPrice2').text
            result6.append(price61)

            time.sleep(6)

            price62 = driver.find_element_by_id(
                'ctl00_pagecontext_partsControl_repeaterParts_ctl01_panelorder_panelorder_price_lbGrossPrice2').text
            result6.append(price62)

            print(result6)


            lo1 = result6[1]
            lo11 = result6[2]
            global resultlo1
            resultlo1 = lo1 + " "+ lo11

            lo2 = result6[3]
            lo21 = result6[4]
            global resultlo2
            resultlo2 = lo2 + " " + lo21

            lo3 = result6[5]
            lo31 = result6[6]
            global resultlo3
            resultlo3 = lo3 + " " + lo31

            lo4 = result6[7]
            lo41 = result6[8]
            global resultlo4
            resultlo4 = lo4 + " " + lo41

            lo5 = result6[9]
            lo51 = result6[10]
            global resultlo5
            resultlo5 = lo5 + " " + lo51

            lo6 = result6[11]
            lo61 = result6[12]
            global resultlo6
            resultlo6 = lo6 + " " + lo61

        pass
    except:
        pass
    return flag



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 361, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 781, 501))
        self.tableWidget.setObjectName("tableView")
        self.tableWidget.setColumnCount(6)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 10, 131, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.handleButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def handleButton(self):
        global keyword
        keyword = self.lineEdit.text()

        driver = ''
        driver = webdriver.Chrome('chromedriver', options=options)
        login1(driver)
        login2(driver)
        login3(driver)
        login4(driver)
        login5(driver)
        login6(driver)
        print(keyword)

        self.tableWidget.insertRow(0)
        self.tableWidget.insertRow(1)
        self.tableWidget.insertRow(2)
        self.tableWidget.insertRow(3)
        self.tableWidget.insertRow(4)
        self.tableWidget.insertRow(5)
        self.tableWidget.insertRow(6)
        self.tableWidget.insertRow(7)
        self.tableWidget.insertRow(8)
        self.tableWidget.insertRow(9)
        self.tableWidget.insertRow(10)
        self.tableWidget.insertRow(11)
        self.tableWidget.insertRow(12)
        self.tableWidget.insertRow(13)
        self.tableWidget.insertRow(14)
        self.tableWidget.insertRow(15)
        self.tableWidget.insertRow(16)
        self.tableWidget.insertRow(17)
        self.tableWidget.insertRow(18)

        global results, resultstock, resultstock1, result2, result3, result4, result5, result6, resultlo1, resultlo2, resultlo3, resultlo4, resultlo5, resultlo6



        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("WHOLESALER 1"))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Name"))
        self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem("Manufacture"))
        self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem("product code"))
        self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem("stock"))
        self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem("price"))

        self.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(results[0][0]))
        self.tableWidget.setItem(1, 2, QtWidgets.QTableWidgetItem(results[0][1]))
        self.tableWidget.setItem(1, 3, QtWidgets.QTableWidgetItem(results[0][2]))
        self.tableWidget.setItem(1, 4, QtWidgets.QTableWidgetItem(resultstock))
        self.tableWidget.setItem(1, 5, QtWidgets.QTableWidgetItem(results[0][5]))

        self.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem(results[1][0]))
        self.tableWidget.setItem(2, 2, QtWidgets.QTableWidgetItem(results[1][1]))
        self.tableWidget.setItem(2, 3, QtWidgets.QTableWidgetItem(results[1][2]))
        self.tableWidget.setItem(2, 4, QtWidgets.QTableWidgetItem(resultstock1))
        self.tableWidget.setItem(2, 5, QtWidgets.QTableWidgetItem(results[1][5]))

        self.tableWidget.setItem(3, 0, QtWidgets.QTableWidgetItem("WHOLESALER 2"))
        self.tableWidget.setItem(4, 1, QtWidgets.QTableWidgetItem(result2[0]))
        self.tableWidget.setItem(4, 2, QtWidgets.QTableWidgetItem(result2[1]))
        self.tableWidget.setItem(4, 3, QtWidgets.QTableWidgetItem(result2[2]))
        self.tableWidget.setItem(4, 4, QtWidgets.QTableWidgetItem(result2[3]))
        self.tableWidget.setItem(4, 5, QtWidgets.QTableWidgetItem(result2[4]))

        self.tableWidget.setItem(5, 1, QtWidgets.QTableWidgetItem(result2[5]))
        self.tableWidget.setItem(5, 2, QtWidgets.QTableWidgetItem(result2[6]))
        self.tableWidget.setItem(5, 3, QtWidgets.QTableWidgetItem(result2[7]))
        self.tableWidget.setItem(5, 4, QtWidgets.QTableWidgetItem(result2[8]))
        self.tableWidget.setItem(5, 5, QtWidgets.QTableWidgetItem(result2[9]))

        self.tableWidget.setItem(6, 1, QtWidgets.QTableWidgetItem(result2[10]))
        self.tableWidget.setItem(6, 2, QtWidgets.QTableWidgetItem(result2[11]))
        self.tableWidget.setItem(6, 3, QtWidgets.QTableWidgetItem(result2[12]))
        self.tableWidget.setItem(6, 4, QtWidgets.QTableWidgetItem(result2[13]))
        self.tableWidget.setItem(6, 5, QtWidgets.QTableWidgetItem(result2[14]))

        self.tableWidget.setItem(7, 0, QtWidgets.QTableWidgetItem("WHOLESALER 3"))

        self.tableWidget.setItem(8, 1, QtWidgets.QTableWidgetItem(result3[0]))
        self.tableWidget.setItem(8, 2, QtWidgets.QTableWidgetItem(result3[1]))
        self.tableWidget.setItem(8, 3, QtWidgets.QTableWidgetItem(result3[2]))
        self.tableWidget.setItem(8, 4, QtWidgets.QTableWidgetItem(result3[3]))

        self.tableWidget.setItem(9, 1, QtWidgets.QTableWidgetItem(result3[4]))
        self.tableWidget.setItem(9, 2, QtWidgets.QTableWidgetItem(result3[5]))
        self.tableWidget.setItem(9, 3, QtWidgets.QTableWidgetItem(result3[6]))
        self.tableWidget.setItem(9, 4, QtWidgets.QTableWidgetItem(result3[7]))

        self.tableWidget.setItem(10, 1, QtWidgets.QTableWidgetItem(result3[8]))
        self.tableWidget.setItem(10, 2, QtWidgets.QTableWidgetItem(result3[9]))
        self.tableWidget.setItem(10, 3, QtWidgets.QTableWidgetItem(result3[10]))
        self.tableWidget.setItem(10, 4, QtWidgets.QTableWidgetItem(result3[11]))

        self.tableWidget.setItem(11, 0, QtWidgets.QTableWidgetItem("WHOLESALER 4"))

        self.tableWidget.setItem(12, 1, QtWidgets.QTableWidgetItem(result4[0]))
        self.tableWidget.setItem(12, 2, QtWidgets.QTableWidgetItem(result4[1]))
        self.tableWidget.setItem(12, 3, QtWidgets.QTableWidgetItem(result4[2]))
        self.tableWidget.setItem(12, 4, QtWidgets.QTableWidgetItem(result4[3]))

        self.tableWidget.setItem(13, 0, QtWidgets.QTableWidgetItem("WHOLESALER 5"))

        self.tableWidget.setItem(14, 2, QtWidgets.QTableWidgetItem(result5[1]))
        self.tableWidget.setItem(14, 3, QtWidgets.QTableWidgetItem(result5[0]))
        self.tableWidget.setItem(14, 5, QtWidgets.QTableWidgetItem(result5[2]))

        self.tableWidget.setItem(15, 0, QtWidgets.QTableWidgetItem("WHOLESALER 6"))

        self.tableWidget.setItem(16, 1, QtWidgets.QTableWidgetItem(result6[0]))
        self.tableWidget.setItem(16, 4, QtWidgets.QTableWidgetItem(result6[13]))
        self.tableWidget.setItem(16, 5, QtWidgets.QTableWidgetItem(result6[14]))

        self.tableWidget.setItem(17, 0, QtWidgets.QTableWidgetItem("quantity within 6 locations"))

        self.tableWidget.setItem(18, 0, QtWidgets.QTableWidgetItem(resultlo1))
        self.tableWidget.setItem(18, 1, QtWidgets.QTableWidgetItem(resultlo2))
        self.tableWidget.setItem(18, 2, QtWidgets.QTableWidgetItem(resultlo3))
        self.tableWidget.setItem(18, 3, QtWidgets.QTableWidgetItem(resultlo4))
        self.tableWidget.setItem(18, 4, QtWidgets.QTableWidgetItem(resultlo5))
        self.tableWidget.setItem(18, 5, QtWidgets.QTableWidgetItem(resultlo6))






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Search"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
