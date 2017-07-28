#!C:\Program Files (x86)\Python36-32\python.exe

import os
from win32com.client import Dispatch
import re
from xml.etree import ElementTree as et
import webbrowser
import time
import getpass
import zipfile
import json
import subprocess

# RESULTS_FILE_PATH = "C:\\" + os.environ['HOMEPATH'] + "\\Desktop\\result.txt"
RESULTS_FILE_PATH = os.getcwd() + "\\result.txt"
TEMP_DIR_PATH = '%s\\Temp\\' % os.environ['LOCALAPPDATA']
BM_DIR_PATH = '%s\\Yandex\\BrowserManager\\' % os.environ['LOCALAPPDATA'] + "\\BrowserManager.exe"
YAPIN_DIR_PATH = '%s\\Yandex\\YaPin\\' % os.environ['LOCALAPPDATA'] + "\\YandexWorking.exe"
APPLICATION_DIR_PATH = '%s\\Yandex\\YandexBrowser\\Application\\' % os.environ['LOCALAPPDATA']
UPDATE_URL_PATH = '%s\\..\\LocalLow\\Yandex\\Updater\\yabrowser\\appinfo.xml' % os.environ['LOCALAPPDATA']


class VersionEXE:
    @staticmethod
    def path_for_exe():
        """
        Возвращает list из путей до exe и название самого exe
        """
        result = []
        exe_files = ["sender.exe", "seederexe.exe", "lite_installer.exe", "downloader.exe"]
        path = TEMP_DIR_PATH
        tree = os.walk(path)
        for d, dirs, file in tree:
            for elem in exe_files:
                if elem in file:
                    if elem not in result:
                        result.append(d)
                        result.append(elem)
        return result

    def result_path_exe(self):
        """
        делит на 2 листа: в одном пути, а в другом названия exe файлов
        """
        results = []
        path = []
        exe = []
        n = 1
        r = 0
        for elem in self.path_for_exe():
            if n % 2 != 0:
                path.append(elem)
                n += 1
            else:
                exe.append(elem)
                n += 1
        for p in path:
            results.append(p + "\\" + exe[r])
            r += 1
        return results

    def report_exe_numbers(self):
        with open(RESULTS_FILE_PATH, "w") as f:
            for elem in self.result_path_exe():
                parser = Dispatch("Scripting.FileSystemObject")
                res = parser.GetFileVersion(elem)
                ui = elem + "-" + "[" + res + "]" + "\n"
                f.write(ui)

    @staticmethod
    def report_number_bm():
        try:
            path = BM_DIR_PATH
            with open(RESULTS_FILE_PATH, "a") as f:
                parser = Dispatch("Scripting.FileSystemObject")
                res = parser.GetFileVersion(path)
                ui = "BrowserManager" + "-" + "[" + res + "]" + "\n"
                f.write(ui)
        except:
            print("BrowserManager hasn't been installed")

    @staticmethod
    def report_number_pin():
        try:
            path = YAPIN_DIR_PATH
            with open(RESULTS_FILE_PATH, "a") as f:
                parser = Dispatch("Scripting.FileSystemObject")
                res = parser.GetFileVersion(path)
                ui = "Булавка" + "-" + "[" + res + "]" + "\n"
                f.write(ui)
        except:
            print("YaPin hasn't been installed")

    @staticmethod
    def number_exe_browser():
        """
        Возвращает папку с номером браузера
        """
        end_path = APPLICATION_DIR_PATH + "\\browser.exe"
        parser = Dispatch("Scripting.FileSystemObject")
        res = parser.GetFileVersion(end_path)
        return res

    def report_browser_exe(self):
        try:
            with open(RESULTS_FILE_PATH, "a") as f:
                ui = "Yandex" + "-" + "[" + self.number_exe_browser() + "]" + "\n"
                f.write(ui)
        except:
            print("YaBro hasn't been installed")

    def report_updater_exe(self):
        try:
            end_path = APPLICATION_DIR_PATH + "\\" + self.number_exe_browser() + "\\" + "dllyupdate.dll"
            with open(RESULTS_FILE_PATH, "a") as f:
                parser = Dispatch("Scripting.FileSystemObject")
                res = parser.GetFileVersion(end_path)
                ui = "Апдейтер" + "-" + "[" + res + "]" + "\n"
                f.write(ui)
        except FileNotFoundError:
            print("There is no dllyupdate.dll")

    def brand_id_version(self):
        """
        Возвращает строку с соотв. brand_id
        """
        brand_config_path = APPLICATION_DIR_PATH + self.number_exe_browser() + "\\" + "brand_config"
        with open(brand_config_path) as file:
            temp = file.read()
            res = str(re.search("\"brand_id\":\s\".*\"", temp))
        return res

    def report_brand_id(self):
        try:
            with open(RESULTS_FILE_PATH, "a") as f:
                ui = "brandID" + "-" + "[" + self.brand_id_version() + "]" + "\n"
                f.write(ui)
        except FileNotFoundError:
            print("There is no 'brand_config' file")

    def partner_id_version(self):
        """
        Возвращает строку с соотв. config_id
        """
        brand_config_path = APPLICATION_DIR_PATH + self.number_exe_browser() + "\\" + "partner_config"
        with open(brand_config_path) as file:
            temp = file.read()
            res = str(re.search("\"partner_id\":\s\".*\"", temp))
        return res

    def report_partner_id(self):
        try:
            with open(RESULTS_FILE_PATH, "a") as f:
                ui = "partner_id" + "-" + "[" + self.partner_id_version() + "]" + "\n"
                f.write(ui)
        except FileNotFoundError:
            print("There is no 'partner_config' file")

    @staticmethod
    def get_path_for_open_yabro():
        name = getpass.getuser()
        res = "C:/Users/" + name + "/AppData/Local/Yandex/YandexBrowser/Application/browser.exe %s"
        return res

    def waiting_for_the_file(self):
        browser = subprocess.Popen(self.get_path_for_open_yabro())
        time.sleep(40)
        browser.kill()

    def url_update(self):
        l = []
        xml_path = UPDATE_URL_PATH
        with open(xml_path) as file:
            file.read()
        for el in et.parse(xml_path).getroot().findall("VersionUrl"):
            l.append(el.text)
        return l[0]

    def report_url_update(self, stop="no"):
        if stop == "yes":
            try:
                with open(RESULTS_FILE_PATH, "a") as f:
                    ui = "URL обновления" + "-" + "[" + self.url_update() + "]" + "\n"
                    f.write(ui)
            except FileNotFoundError:
                print("Problems with file 'appinfo.xml'")
        else:
            with open(RESULTS_FILE_PATH, "a") as f:
                ui = "URL обновления" + "-" + "[" + self.url_update() + "]" + "\n"
                f.write(ui)


"""
Firefox methods!!!!!!!
"""
FF_PROFILES = "C:\\" + os.environ['HOMEPATH'] + "\\AppData\Roaming\Mozilla\Firefox\Profiles\\"
class FirefoxExt:
    def ff_ext_version(self):
        """
        Возвращает имя папки дефолтного пользователя для FF
        """
        def_user_list = []
        def_user_reg = ".*.default"
        part_path = FF_PROFILES
        dirs = os.listdir(part_path)
        for elem in dirs:
            if re.match(def_user_reg, elem) != None:
                def_user_list.append(elem)
            else:
                print("there is no 'default_user'")
        return def_user_list[0]

    def path_for_ff_ext(self):
        neccessary_extensions = ["vb", "sovetnik"]
        result = []
        path_for_file = FF_PROFILES + self.ff_ext_version() + "\\prefs.js"
        with open(path_for_file, encoding="UTF-8") as file:
            pr = file.read()
            pr.find("extensions.enabledAddons", )
            res = re.findall("extensions.enabledAddons.*\)", pr)
            po = re.split(",", str(res))
            for elem in po:
                for i in neccessary_extensions:
                    if i in elem:
                        result.append(elem)
        print(result)
        # return end_ff_ext_path

df = FirefoxExt()
df.ff_ext_version()
df.path_for_ff_ext()

        # ext_version(self):
    #     """
    #     Возвращает имя папки дефолтного пользователя для FF
    #     """
    #     def_user_list = []
    #     def_user_reg = ".*.default"
    #     part_path = FF_PROFILES
    #     dirs = os.listdir(part_path)
    #     for elem in dirs:
    #         if re.match(def_user_reg, elem) != None:
    #             def_user_list.append(elem)
    #         else:
    #             print("there is no 'default_user'")
    #     return def_user_list[0]
    #
    # def path_for_ff_ext(self):
    #     part_path = FF_PROFILES + self.ff_ext_version() + "\\extensions\\"
    #     dirs = os.listdir(part_path)
    #     c = len(dirs)
    #     n = 0
    #     for elem in dirs:
    #         if elem == "staged":
    #             end_ff_ext_path = part_path + "staged\\"
    #             break
    #         else:
    #             n += 1
    #             if n == c:
    #                 end_ff_ext_path = part_path
    #     return end_ff_ext_path
    #
    # def list_with_ff_ext(self):
    #     sovetnik = "sovetnik@metabar.ru.xpi"
    #     vb = "vb@yandex.ru.xpi"
    #     temp_list_ext = os.listdir(self.path_for_ff_ext())
    #     list_ext = []
    #     for elem in temp_list_ext:
    #         if elem == sovetnik or elem == vb:
    #             list_ext.append(elem)
    #     return list_ext
    #
    # def final_path_for_ff_ext(self):
    #     final_path = []
    #     for elem in self.list_with_ff_ext():
    #         final_path.append(self.path_for_ff_ext() + elem)
    #     return final_path
    #
    # def creating_install_rdf(self):
    #     """
    #     извлекаются 'install.rdf' файлы и создаются соотв файл с данными для каждого расширения
    #     """
    #     try:
    #         n = 1
    #         for end_path in self.final_path_for_ff_ext():
    #             z = zipfile.ZipFile(end_path, 'r')
    #             z.extract('install.rdf')
    #             if n == 1:
    #                 with zipfile.ZipFile('first.txt', 'w') as my:
    #                     my.write('install.rdf')
    #                     n += 1
    #             elif n == 2:
    #                 with zipfile.ZipFile('second.txt', 'w') as my:
    #                     my.write('install.rdf')
    #                     n += 1
    #             else:
    #                 with zipfile.ZipFile('other.txt', 'a') as my:
    #                     my.write('install.rdf')
    #                     n += 1
    #     except:
    #         print("something wrong")
    #
    # def report_first_ff_ext(self):
    #     try:
    #         files_path = os.getcwd() + "\\first.txt"
    #         name_pars = "<em:id>.*</em:id>"
    #         version_pars = "<em:version>.*</em:version>"
    #         with open(files_path, encoding="ANSI") as file:
    #             temp = file.read()
    #             name = str(re.search(name_pars, temp))
    #             version = str(re.search(version_pars, temp))
    #             result = name + "-" + "[" + version + "]" + "\n"
    #             with open(RESULTS_FILE_PATH, "a") as f:
    #                 f.write(result)
    #     except FileNotFoundError:
    #         print("There is no first_file something wrong")
    #
    # def report_second_ff_ext(self):
    #     try:
    #         files_path = os.getcwd() + "\\second.txt"
    #         name_pars = "<em:id>.*</em:id>"
    #         version_pars = "<em:version>.*</em:version>"
    #         with open(files_path, encoding="ANSI") as file:
    #             temp = file.read()
    #             name = str(re.search(name_pars, temp))
    #             version = str(re.search(version_pars, temp))
    #             result = name + "-" + "[" + version + "]" + "\n"
    #             with open(RESULTS_FILE_PATH, "a") as f:
    #                 f.write(result)
    #     except FileNotFoundError:
    #         print("There is no second_file something wrong")


class GoogleChrome:
    CHROME_PREF_FILE = "C:" + os.environ['HOMEPATH'] + r"\AppData\Local\Google\Chrome\User Data\Default\Preferences"
    CHROME_SECURE_PREF_FILE = "C:" + os.environ['HOMEPATH'] + r"\AppData\Local\Google\Chrome\User Data\Default\Secure Preferences"
    ext_data = "\\extensions_data.txt"
    # ext_secure_data = "\\extensions_secure_data.txt"
    Search_Yandex = ["lgdnilodcpljomelbbnpgdogdbmclbni", "jdfonankhfnhihdcpaagpabbaoclnjfp",
                     "ablpcikjmhamjanpibkccdmpoekjigja", "bejnpnkhfgfkcpgikiinojlmdcjimobi",
                     "necfmkplpminfjagblfabggomdpaakan"]
    Start_Page_Yandex = ["hpcghcdjnehpkdecaflpedhklimnejia", "gbjeiekahklbgbfccohipinhgaadijad",
                        "pjfkgjlnocfakoheoapicnknoglipapd", "cpegcopcfajiiibidlaelhjjblpefbjk",
                        "dkekdlkmdpipihonapoleopfekmapadh"]
    Sovetnik = ["fdjdjkkjoiomafnihnobkinnfjnnlhdg", "ppiaojpbclpegkkkmikabinlpbahhbha"]
    New_Tab = ["hdpgllbnilfcbckbdchjcfgopijgllcm", "pchfckkccldkbclgdepkaonamkignanh"]
    LIST_WITH_EXTENSIONS = [Search_Yandex, Start_Page_Yandex, Sovetnik, New_Tab]

    def get_chrome_pref_json(self, data_file=CHROME_SECURE_PREF_FILE):
        try:
            with open(data_file, encoding='UTF-8') as f:
                js = json.load(f)
                with open(os.getcwd() + self.ext_data, mode="w") as res:
                    json.dump(js, res)
        except FileNotFoundError:
            print("There is no {}".format(data_file))

    def ext_chrome(self):
        folders_for_extensions = self.LIST_WITH_EXTENSIONS
        count_success = 0
        with open(os.getcwd() + self.ext_data, encoding="UTF-8") as f:
            js = json.load(f)
            for elem in folders_for_extensions:
                for folder in elem:
                    try:
                        name = js["extensions"]["settings"][folder]["manifest"]["name"]
                    except KeyError:
                        continue
                    count_success += 1
                    version = js["extensions"]["settings"][folder]["manifest"]["version"]
                    with open(RESULTS_FILE_PATH, "a") as file:
                        result = name + "-" + "[" + version + "]" + "\n"
                        file.write(result)
            if count_success != len(folders_for_extensions):
                print("there is(are) only {} of {} extension(s)".format(count_success, len(self.LIST_WITH_EXTENSIONS)))
        return count_success


# _versionexe = VersionEXE()
# _GH = GoogleChrome()
#
# _versionexe.report_exe_numbers()
# _versionexe.creating_install_rdf()
# _versionexe.report_first_ff_ext()
# _versionexe.report_second_ff_ext()
# _GH.get_chrome_pref_json()
# res = _GH.ext_chrome()
# if res != len(_GH.LIST_WITH_EXTENSIONS):
#     _GH.get_chrome_pref_json(_GH.CHROME_PREF_FILE)
#     _GH.ext_chrome()
# _versionexe.report_number_bm()
# _versionexe.report_number_pin()
# _versionexe.report_browser_exe()
# _versionexe.report_partner_id()
# _versionexe.report_brand_id()
# _versionexe.report_updater_exe()
# try:
#     _versionexe.report_url_update()
# except FileNotFoundError:
#     _versionexe.waiting_for_the_file()
#     _versionexe.report_url_update("yes")
