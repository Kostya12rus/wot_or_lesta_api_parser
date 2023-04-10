import pathlib, os, json, re
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import ChromiumOptions
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

capabilities = DesiredCapabilities.CHROME
capabilities["loggingPrefs"] = {"performance": "ALL"}
capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
options = ChromiumOptions()
options.add_argument("headless")

driver = webdriver.Chrome(desired_capabilities=capabilities, executable_path=ChromeDriverManager().install(), options=options)
driver.get("https://developers.lesta.ru/reference/all/wot/account/list/?r_realm=ru")

print("Начинаю поиск страниц Lesta API")
def get_all_site():
    driver.get("https://developers.lesta.ru/reference/all/wot/account/list/?r_realm=ru")
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[1]/div[2]/div[1]/div[1]")))
    site_all = {}
    soup = BeautifulSoup(driver.page_source, features = "html.parser")
    context_menu_sub = soup.find('div', {'data-reactid': '.0.0.0.1.0:$0'})
    if context_menu_sub:
        context_menu = context_menu_sub.find_all('li', {'class': 'context-menu-sub2_item'})
        if context_menu:
            for li in context_menu:
                url_link_a = li.find('a', {'class': 'context-menu-sub2_link'})
                url_link_href = url_link_a.get('href')
                url_link_rsplit = str(url_link_href).rsplit('/')
                url_link_short = '_'.join([url_link_rsplit[4], url_link_rsplit[5]])
                if url_link_short not in site_all:
                    site_all[url_link_short] = {}
                site_all[url_link_short]['url'] = f"https://developers.lesta.ru{url_link_href}?r_realm=ru"
    return site_all
all_url = get_all_site()
print("Поиск страниц Lesta API завершен, найдено:", len(all_url))

print("Начинаю загрузку данных страниц сайта Lesta API")
def load_page_source(url_link: str):
    driver.get(url_link)
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[1]/div[2]/div[1]/div[1]")))
    page_source = BeautifulSoup(driver.page_source, features="html.parser")
    alert_text = page_source.find('div', {'class': 'alert_text'})
    if alert_text: return
    return page_source
for url_link_short, url_data in all_url.items():
    url_data['page_source'] = load_page_source(url_data['url'])
    print(f"Загрузили данные для {url_link_short}")
    # break
driver.quit()
print("Загрузку страниц Lesta API завершена, найдено")


dir_def = pathlib.Path(os.getcwd()) / 'wot_api'
if not dir_def.is_dir(): dir_def.mkdir()
dir_class_init = dir_def / '__init__.py'
with open(dir_class_init, 'w') as init_file:
    init_file.write(f'from .wot_api_class import *\n')
    init_file.write(f'from .wot_api_def import *\n')

print("Начинаю создание class`ов для Lesta API")
def get_class_dist(page_source: BeautifulSoup) -> dict:
    tbody = page_source.find('tbody', {'data-reactid': '.0.0.1.1.0.1.0.0'})
    if not tbody: exit("не найден tbody")
    all_tr = tbody.find_all('tr')
    def get_type_param(type_data_get: str|None) -> str:
        if not type_data_get: return 'dict', {}
        elif type_data_get == 'associative array': return 'dict', {}
        elif type_data_get == 'list of integers': return 'list', []
        elif type_data_get == 'list of strings': return 'list', []
        elif type_data_get == 'list of timestamps': return 'list', []
        elif type_data_get == 'object': return 'list', []
        elif type_data_get == 'numeric': return 'int', 0
        elif type_data_get == 'timestamp': return 'int', 0
        elif type_data_get == 'float': return 'float', 0.0
        elif type_data_get == 'boolean': return 'bool', False
        elif type_data_get == 'string': return 'str', "''"
        else:
            print(type_data_get, "<-----------------------------")
            return type_data_get
    params = {}

    for tr in all_tr:
        code_secret = tr.get('data-reactid')
        name: str = tr.find('td', {'data-reactid': f'{code_secret}.0'})
        if name:
            name = name.text
        type_data: str = tr.find('td', {'data-reactid': f'{code_secret}.1'})
        if type_data:
            type_data = type_data.text
        info: str = tr.find('td', {'data-reactid': f'{code_secret}.2'})
        if info:
            info = info.text
        if not name and not type_data and not info: continue
        type_data, real_type = get_type_param(type_data)

        table_add = params
        if name.find('.') >= 0:
            table_name = name.rsplit('.')
            for name in table_name:
                if type(table_add) != dict:
                    table_add = {}
                if name not in table_add:
                    table_add[name] = real_type
                table_add = table_add[name]
            table_add = real_type
            continue
        table_add[name] = real_type
    return params
def create_class(name_get:str, data: dict) -> list[str, list]:
    list_classes = []
    name_class_get = name_get.replace("_", " ").title().replace(" ", "")
    name_class_in_class = f"{name_class_get}Class"
    string_class = ""
    string_class += f"class {name_class_in_class}:\n"
    string_class += f"    def __init__(self, {name_get}_data: dict):\n"
    string_class += f"        if not {name_get}_data: {name_get}_data = "+"{}\n"
    string_class += f"        self._{name_get}: dict = {name_get}_data\n"
    for param_name, param_type in data.items():
        if type(param_type) == dict and param_type:
            name_class_in_class_add, list_classes_new = create_class(param_name, param_type)
            list_classes += list_classes_new
            param_data = [f"key == '{key}'" for key in param_type]
            # string_class += f"        self.{param_name}: {name_class_in_class_add} = {name_class_in_class_add}({name_get}_data.get('{param_name}', "+"{}))\n"
            string_class += f"\n        {param_name}_temp: dict = self._{name_get}.get('{param_name}')\n"
            string_class += f"        {param_name}_class = None\n"
            string_class += f"        if isinstance({param_name}_temp, dict):\n"
            string_class += f"            for key in {param_name}_temp:\n"
            string_class += f"                if str(key).isnumeric():\n"
            string_class += f"                    {param_name}_class = "+"{"+f"key: {name_class_in_class_add}(data) for key, data in {param_name}_temp.items()"+"}\n"
            string_class += f"                    break\n"
            string_class += f"                if {' or '.join(param_data)}:\n"
            string_class += f"                    {param_name}_class = {name_class_in_class_add}({param_name}_temp)\n"
            string_class += f"                    break\n"
            string_class += f"        elif isinstance({param_name}_temp, list):\n"
            string_class += f"            {param_name}_class = [{name_class_in_class_add}(data) for data in {param_name}_temp]\n"
            string_class += f"        if not {param_name}_class:\n"
            string_class += f"            {param_name}_class: {name_class_in_class_add} = {name_class_in_class_add}({param_name}_temp)\n"
            string_class += f"        self.{param_name}: {name_class_in_class_add} | list[{name_class_in_class_add}] | dict[str, {name_class_in_class_add}] = {param_name}_class\n"
            string_class += f"        del {param_name}_temp, {param_name}_class\n\n"
            continue
        string_class += f"        self.{param_name}: {type(param_type).__name__} = {name_get}_data.get('{param_name}', {param_type})\n"
    string_class += "\n"
    list_classes.append(string_class)
    return name_class_in_class, list_classes
dir_class = pathlib.Path(os.getcwd()) / 'wot_api' / 'wot_api_class'
if not dir_class.is_dir(): dir_class.mkdir()
dir_class_init = dir_class / '__init__.py'
with open(dir_class_init, 'w', encoding='UTF-8') as init_file:
    for url_link_short, url_data in all_url.items():
        page_source = url_data.get('page_source')
        if not page_source: continue
        print(f"Начинаю поиск данных: {url_link_short}")
        all_params = get_class_dist(page_source)
        print(f"Нашел данные для создания class {url_link_short}, {len(all_params)} параметров")

        print("Начинаю создание класса для:", url_link_short)
        name_class, all_class = create_class(url_link_short, all_params)
        url_data['name_class'] = name_class
        print(f"Создание класса {name_class} завершенно, внутри {len(all_class)} классов")

        dir_class_file = dir_class / f'{url_link_short}.py'
        print("Начинаю запись в файл:", dir_class_file.as_posix())
        with open(dir_class_file, 'w') as classes_file:
            classes_file.writelines(all_class)
        print("Запись в файл завершена")

        print("Записываю новый import в: __init__.py")
        init_file.write(f'from .{url_link_short} import *\n')
        print("Создание нового класса завершено")
print("Создание class для Lesta API завершено")


print("Начинаю создание папки и файлов в wot_api_def")
def create_files_defs():
    dir_def = pathlib.Path(os.getcwd()) / 'wot_api' / 'wot_api_def'
    if not dir_def.is_dir(): dir_def.mkdir()
    dir_def_init = dir_def / '__init__.py'
    with open(dir_def_init, 'w', encoding='UTF-8') as init_file:
        init_file.write(f'from .wot_api_async import *\n')
        init_file.write(f'from .wot_api import *\n')

    dir_def_file = dir_def / 'wot_api_async.py'
    async_text = """import aiohttp, asyncio
import logging
from .config import application_id
from ..wot_api_class import *

BASE_URL = 'https://api.tanki.su/wot'


async def create_url_post(url, params) -> dict|None:
    if not "application_id" in params: params['application_id'] = application_id
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.post(f'{BASE_URL}/{url}/', params=params, timeout=10) as response:
                    if response.ok:
                        return await response.json(encoding='UTF-8')
            except:
                await asyncio.sleep(1)


def get_str_in_list(data):
    if data is None:
        return ''
    if type(data) is list or type(data) is dict:
        return ','.join(map(str, data))
    return str(data)\n\n"""
    with open(dir_def_file, 'w', encoding='UTF-8') as file_async_def:
        file_async_def.write(async_text)

    dir_def_file = dir_def / 'wot_api.py'
    not_async_text = """import requests, time
from .config import application_id
from ..wot_api_class import *

BASE_URL = 'https://api.tanki.su/wot'

def create_url_post(url, params) -> dict|None:
    if not "application_id" in params: params['application_id'] = application_id
    while True:
        response = requests.post(f'{BASE_URL}/{url}/', data=params)
        if response.ok: 
            return response.json()
        time.sleep(1)


def get_str_in_list(data):
    if data is None:
        return ''
    if type(data) is list or type(data) is dict:
        return ','.join(map(str, data))
    return str(data)\n\n"""
    with open(dir_def_file, 'w', encoding='UTF-8') as file_def:
        file_def.write(not_async_text)

    dir_config_file = dir_def / 'config.py'
    if not dir_config_file.is_file():
        config_text = """application_id = '***'"""
        with open(dir_config_file, 'w', encoding='UTF-8') as file_def:
            file_def.write(config_text)
create_files_defs()

def get_def_params(page_source: BeautifulSoup):
    params_list = []
    alert_text = page_source.find('div', {'class': 'alert_text'})
    if alert_text: return
    parameters_block = page_source.find('div', {'id': 'parameters_block'})
    if not parameters_block: return
    tbody = parameters_block.find_all('tr')
    if not tbody: return

    element_desc = ''
    element_desc_data = page_source.find('div', {'data-reactid': '.0.0.1.0.4.2'})
    if element_desc_data:
        element_desc = element_desc_data.text
        data = element_desc.rsplit('\n')
        if '' in data:
            data.remove('')

    for tr in tbody:
        param_dict = {}
        td = tr.find('td', {'width': '95'})
        if not td: continue

        spans = td.find_all('span')
        if spans:
            cont = False
            for span in spans:
                text = span.text
                if str(text).find('application_id') > -1: cont = True
                if str(text).find('*') > -1:
                    param_dict['required'] = True
                    continue
                param_dict['name'] = text
            if cont:
                continue

        input_data = tr.find('input', {'class': 'input'})
        if input_data:
            param_dict['type_param'] = []
            placeholder = input_data.get('placeholder')
            types = str(placeholder).rsplit(', ')
            for t in types:
                if t == 'numeric':
                    param_dict['type_param'].append('int')
                elif t == 'list':
                    param_dict['type_param'].append('list')
                else:
                    param_dict['type_param'].append('str')

        parameter_descr = tr.find('div', {'class': 'js-param-descr-switcher param-descr-switcher'})
        if parameter_descr:
            parameter_text: str = parameter_descr.text
            parameter_text = parameter_text.replace('...', '').replace('  ', ' ')
            parameter_text = parameter_text.strip()
            param_dict['descr'] = parameter_text

            if 'name' in param_dict and param_dict['name'] == 'extra':
                param_dict['extra'] = []
                parameter_descr_li = tr.find_all('li')
                if parameter_descr_li:
                    for li in parameter_descr_li:
                        li_text = re.findall('".*"', li.text)[0].replace('"', '')
                        param_dict['extra'].append(li_text)
        params_list.append(param_dict)
    return params_list, element_desc
def get_input_params(def_params: list):
    if not def_params: return ''
    params_input = []
    for def_param in def_params:
        name_param = def_param.get('name')
        required_param = def_param.get('required')
        type_param_param = def_param.get('type_param')
        params_input.append(f'{name_param}: {"|".join(type_param_param)}{" = None" if not required_param else ""}')
    return ', '.join(params_input)
def get_def_desc(def_desc: str, def_params: list):
    return_text = '    """\n'
    if def_desc:
        def_desc = def_desc.replace("\n", " ")
        return_text += f'    {def_desc}\n'
    if def_params:
        return_text += f'    Parameters:\n'
    for def_param in def_params:
        name_param = def_param.get('name')
        type_param = def_param.get('type_param')
        type_param_list = [f":obj:`{data}`" for data in type_param]
        type_param_str = ' | '.join(type_param_list)
        descr = def_param.get('descr')
        descr_list = descr.rsplit('\n')
        if '' in descr_list: descr_list.remove('')
        descr_str = "\n            ".join(descr_list)
        return_text += f'        {name_param} ({type_param_str}): {descr_str}\n'
    return_text += '    """'
    return return_text
def get_set_params(def_params: list):
    set_param_list = []
    for def_param in def_params:
        name_param = def_param.get('name')
        set_param_list.append(f"'{name_param}': get_str_in_list({name_param})")
    return 'params = {' + f'{", ".join(set_param_list)}' + "}"
def get_extra(def_params: list):
    for param in def_params:
        name = param.get('name')
        if not name or name != 'extra': continue
        extra = param.get('extra')
        return extra

def create_def_text(api_data: dict, api_name: str):
    text_return = '\n'
    text_return += f'async def {api_name}_async({get_input_params(api_data.get("def_params"))}) -> {api_data.get("name_class")}|dict[str, {api_data.get("name_class")}]|list[{api_data.get("name_class")}]:\n'
    'AuthLogoutClass|dict[str, AuthLogoutClass]|list[AuthLogoutClass]:'
    text_return += f'{get_def_desc(api_data.get("def_desc"), api_data.get("def_params"))}\n'
    extra = get_extra(api_data.get("def_params"))
    if extra:
        text_return += f'    if not extra:\n'
        text_return += f'        extra = {json.dumps(extra)}\n'
    text_return += f'    {get_set_params(api_data.get("def_params"))}\n'
    text_return += f'    request_post = await create_url_post("{api_name.replace("_", "/")}", params)\n'
    text_return += f'    if not request_post or not request_post.get("data"):\n'
    text_return += f'        return {api_data.get("name_class")}(request_post.get("data"))\n'
    text_return += f'    else:\n'
    text_return += f'        request_data = request_post.get("data")\n'
    text_return += f'        if isinstance(request_data, list):\n'
    text_return += f'            return [{api_data.get("name_class")}(data) for data in request_data]\n'
    text_return += f'        if isinstance(request_data, dict):\n'
    text_return += f'            for key, data in request_data.items():\n'
    text_return += f'                if isinstance(data, list):\n'
    text_return += f'                    return '+'{'+f'key: [{api_data.get("name_class")}(data_list or '+'{}'+f') for data_list in data or []] for key, data in request_data.items()'+'}'+'\n'
    text_return += f'                elif str(key).isnumeric():\n'
    text_return += f'                    return '+'{'+f'key: {api_data.get("name_class")}(data) for key, data in request_data.items()'+'}'+'\n'
    text_return += f'        return {api_data.get("name_class")}(request_data)\n'
    return text_return

dir_def = pathlib.Path(os.getcwd()) / 'wot_api' / 'wot_api_def'
for url_link_short, url_data in all_url.items():
    page_source = url_data.get('page_source')
    if not page_source: continue
    def_params_all = get_def_params(page_source)
    if not def_params_all: continue
    def_params, def_desc = def_params_all
    if not def_params: continue
    url_data['def_params'] = def_params
    url_data['def_desc'] = def_desc
    text_async = create_def_text(url_data, url_link_short)
    if not text_async: continue
    text_async = text_async.replace(" type:", " type_param:").replace(" type ", " type_param ").\
        replace("(type)", "(type_param)").replace(" type.", " type_param.")

    dir_async_def_file = dir_def / 'wot_api_async.py'
    with open(dir_async_def_file, 'a', encoding='UTF-8') as file_async_def:
        file_async_def.write(text_async)
    dir_def_file = dir_def / 'wot_api.py'
    with open(dir_def_file, 'a', encoding='UTF-8') as file_def:
        file_def.write(text_async.replace('_async', "").replace('async ', "").replace('await ', ""))
print("создание папки и файлов в wot_api_def завершено")


