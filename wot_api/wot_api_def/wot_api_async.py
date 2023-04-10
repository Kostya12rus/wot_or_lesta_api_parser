import aiohttp, asyncio
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
    return str(data)


async def account_list_async(search: str, fields: str|list = None, language: str = None, limit: int = None, type_param: str = None) -> AccountListClass|dict[str, AccountListClass]|list[AccountListClass]:
    """
    Метод возвращает часть списка игроков, отфильтрованную по первым символам имени и отсортированную по алфавиту.
    Parameters:
        search (:obj:`str`): Строка поиска по имени игрока. Вид поиска и минимальная длина строки поиска зависят от параметра type_param. При использовании типа поиска exact можно перечислить несколько имён для поиска, разделив их запятыми. Mаксимальная длина: 24.
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
        limit (:obj:`int`): Количество возвращаемых записей (может вернуться меньше записей, но не больше 100). Если переданный лимит превышает 100, тогда автоматически выставляется лимит в None (по умолчанию).
        type_param (:obj:`str`): Тип поиска. По умолчанию: "startswith". Допустимые значения:
            "startswith" — Поиск по начальной части имени игрока без учёта регистра. Минимальная длина: 3 символа. Максимальная длина: 24 символа. (используется по умолчанию)
            "exact" — Поиск по строгому соответствию имени игрока без учёта регистра. Можно перечислить несколько имён для поиска (до 100 значений), разделив их запятыми.
    """
    params = {'search': get_str_in_list(search), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language), 'limit': get_str_in_list(limit), 'type': get_str_in_list(type_param)}
    request_post = await create_url_post("account/list", params)
    if not request_post or not request_post.get("data"):
        return AccountListClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [AccountListClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [AccountListClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: AccountListClass(data) for key, data in request_data.items()}
        return AccountListClass(request_data)

async def account_info_async(account_id: int|list, access_token: str = None, extra: str|list = None, fields: str|list = None, language: str = None) -> AccountInfoClass|dict[str, AccountInfoClass]|list[AccountInfoClass]:
    """
    Метод возвращает информацию об игроке.
    Parameters:
        account_id (:obj:`int` | :obj:`list`): Идентификатор аккаунта игрока. Максимальное ограничение: 100.
        access_token (:obj:`str`): Ключ доступа к личным данным аккаунта пользователя; можно получить при помощи метода авторизации; действителен в течение определённого времени
        extra (:obj:`str` | :obj:`list`): Список дополнительных полей, которые будут включены в ответ. Допустимые значения:
            "private.boosters" 
            "private.garage" 
            "private.grouped_contacts" 
            "private.personal_missions" 
            "private.rented" 
            "statistics.epic" 
            "statistics.fallout" 
            "statistics.globalmap_absolute" 
            "statistics.globalmap_champion" 
            "statistics.globalmap_middle" 
            "statistics.random" 
            "statistics.ranked_10x10" 
            "statistics.ranked_15x15" 
            "statistics.ranked_battles" 
            "statistics.ranked_battles_current" 
            "statistics.ranked_battles_previous" 
            "statistics.ranked_season_1" 
            "statistics.ranked_season_2" 
            "statistics.ranked_season_3"
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
    """
    if not extra:
        extra = ["private.boosters", "private.garage", "private.grouped_contacts", "private.personal_missions", "private.rented", "statistics.epic", "statistics.fallout", "statistics.globalmap_absolute", "statistics.globalmap_champion", "statistics.globalmap_middle", "statistics.random", "statistics.ranked_10x10", "statistics.ranked_15x15", "statistics.ranked_battles", "statistics.ranked_battles_current", "statistics.ranked_battles_previous", "statistics.ranked_season_1", "statistics.ranked_season_2", "statistics.ranked_season_3"]
    params = {'account_id': get_str_in_list(account_id), 'access_token': get_str_in_list(access_token), 'extra': get_str_in_list(extra), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language)}
    request_post = await create_url_post("account/info", params)
    if not request_post or not request_post.get("data"):
        return AccountInfoClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [AccountInfoClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [AccountInfoClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: AccountInfoClass(data) for key, data in request_data.items()}
        return AccountInfoClass(request_data)

async def account_tanks_async(account_id: int|list, access_token: str = None, fields: str|list = None, language: str = None, tank_id: int|list = None) -> AccountTanksClass|dict[str, AccountTanksClass]|list[AccountTanksClass]:
    """
    Метод возвращает информацию о технике игрока.
    Parameters:
        account_id (:obj:`int` | :obj:`list`): Идентификатор аккаунта игрока. Максимальное ограничение: 100.
        access_token (:obj:`str`): Ключ доступа к личным данным аккаунта пользователя; можно получить при помощи метода авторизации; действителен в течение определённого времени
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
        tank_id (:obj:`int` | :obj:`list`): Идентификатор техники игрока. Максимальное ограничение: 100.
    """
    params = {'account_id': get_str_in_list(account_id), 'access_token': get_str_in_list(access_token), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language), 'tank_id': get_str_in_list(tank_id)}
    request_post = await create_url_post("account/tanks", params)
    if not request_post or not request_post.get("data"):
        return AccountTanksClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [AccountTanksClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [AccountTanksClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: AccountTanksClass(data) for key, data in request_data.items()}
        return AccountTanksClass(request_data)

async def account_achievements_async(account_id: int|list, fields: str|list = None, language: str = None) -> AccountAchievementsClass|dict[str, AccountAchievementsClass]|list[AccountAchievementsClass]:
    """
    Метод возвращает информацию о достижениях игроков. Значения поля achievements зависят от свойств достижений:  от 1 до 4 для Знаков классности и Этапных достижений (type: "class"); максимальное значение серийных достижений (type: "series"); количество заработанных достижений из секций Герой битвы, Эпические достижения, Групповые достижения, Особые достижения и т.п. (type: "repeatable, single, custom"). 
    Parameters:
        account_id (:obj:`int` | :obj:`list`): Идентификатор аккаунта игрока. Максимальное ограничение: 100.
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
    """
    params = {'account_id': get_str_in_list(account_id), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language)}
    request_post = await create_url_post("account/achievements", params)
    if not request_post or not request_post.get("data"):
        return AccountAchievementsClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [AccountAchievementsClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [AccountAchievementsClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: AccountAchievementsClass(data) for key, data in request_data.items()}
        return AccountAchievementsClass(request_data)

async def auth_login_async(display: str = None, expires_at: int = None, nofollow: int = None, redirect_uri: str = None) -> AuthLoginClass|dict[str, AuthLoginClass]|list[AuthLoginClass]:
    """
    Метод осуществляет аутентификацию игрока при помощи Идентификатора Lesta ID (OpenID), который используется в играх Мир танков, Мир кораблей, Tanks Blitz. Игрок должен ввести email и пароль, использованные при создании аккаунта, или войти при помощи аккаунта социальной сети. Аутентификация не поддерживается для пользователя Game Center под iOS, если аккаунт не привязан к одной из социальных сетей или в профиле не указан email и пароль. Информация о статусе аутентификации будет отправлена на URL, указанный в параметре redirect_uri. Параметры redirect_uri при успешной аутентификации:  status: ok — аутентификация пройдена; access_token — ключ доступа, передаётся во все методы, требующие аутентификации; expires_at — срок действия access_token; account_id — Идентификатор пользователя; nickname — имя пользователя.  Параметры redirect_uri при ошибке аутентификации:  status: error — произошла ошибка аутентификации; code — код ошибки; message — информация об ошибке. 
    Parameters:
        display (:obj:`str`): Внешний вид формы мобильных приложений. Допустимые значения:
            "page" — Страница 
            "popup" — Всплывающее окно
        expires_at (:obj:`int`): Срок действия access_token в формате UNIX. Также можно указать дельту в секундах.Срок действия и дельта не должны превышать две недели, начиная с настоящего времени.
        nofollow (:obj:`int`): При передаче параметра nofollow=1 переадресация не происходит. URL возвращается в ответе. По умолчанию: 0. Минимальное значение: 0. Максимальное значение: 1.
        redirect_uri (:obj:`str`): URL на который будет переброшен пользователь после того как он пройдет аутентификацию.По умолчанию: api.tanki.su/wot//blank/
    """
    params = {'display': get_str_in_list(display), 'expires_at': get_str_in_list(expires_at), 'nofollow': get_str_in_list(nofollow), 'redirect_uri': get_str_in_list(redirect_uri)}
    request_post = await create_url_post("auth/login", params)
    if not request_post or not request_post.get("data"):
        return AuthLoginClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [AuthLoginClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [AuthLoginClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: AuthLoginClass(data) for key, data in request_data.items()}
        return AuthLoginClass(request_data)

async def auth_prolongate_async(access_token: str, expires_at: int = None) -> AuthProlongateClass|dict[str, AuthProlongateClass]|list[AuthProlongateClass]:
    """
    Метод генерирует новый access_token на основе действующего. Используется для тех случаев, когда пользователь всё ещё пользуется приложением, а срок действия access_token уже подходит к концу.
    Parameters:
        access_token (:obj:`str`): Ключ доступа к личным данным аккаунта пользователя; можно получить при помощи метода авторизации; действителен в течение определённого времени
        expires_at (:obj:`int`): Срок действия access_token в формате UNIX. Также можно указать дельту в секундах.Срок действия и дельта не должны превышать две недели, начиная с настоящего времени.
    """
    params = {'access_token': get_str_in_list(access_token), 'expires_at': get_str_in_list(expires_at)}
    request_post = await create_url_post("auth/prolongate", params)
    if not request_post or not request_post.get("data"):
        return AuthProlongateClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [AuthProlongateClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [AuthProlongateClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: AuthProlongateClass(data) for key, data in request_data.items()}
        return AuthProlongateClass(request_data)

async def auth_logout_async(access_token: str) -> AuthLogoutClass|dict[str, AuthLogoutClass]|list[AuthLogoutClass]:
    """
    Метод удаляет access_token пользователя. После вызова данного метода access_token перестаёт действовать.
    Parameters:
        access_token (:obj:`str`): Ключ доступа к личным данным аккаунта пользователя; можно получить при помощи метода авторизации; действителен в течение определённого времени
    """
    params = {'access_token': get_str_in_list(access_token)}
    request_post = await create_url_post("auth/logout", params)
    if not request_post or not request_post.get("data"):
        return AuthLogoutClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [AuthLogoutClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [AuthLogoutClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: AuthLogoutClass(data) for key, data in request_data.items()}
        return AuthLogoutClass(request_data)

async def stronghold_claninfo_async(clan_id: int|list, fields: str|list = None, language: str = None) -> StrongholdClaninfoClass|dict[str, StrongholdClaninfoClass]|list[StrongholdClaninfoClass]:
    """
    Метод возвращает общую информацию и боевую статистику кланов в режиме «Укрепрайон». Обратите внимание, что информация о количестве проведённых боёв, а также количестве побед и поражений клана обновляется один раз в сутки.
    Parameters:
        clan_id (:obj:`int` | :obj:`list`): Идентификатор клана. Чтобы получить его, используйте метод Кланы. Максимальное ограничение: 10.
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "ru" — Russian (используется по умолчанию)
            "be" — Belarusian 
            "uk" — Ukrainian 
            "kk" — Kazakh
    """
    params = {'clan_id': get_str_in_list(clan_id), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language)}
    request_post = await create_url_post("stronghold/claninfo", params)
    if not request_post or not request_post.get("data"):
        return StrongholdClaninfoClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [StrongholdClaninfoClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [StrongholdClaninfoClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: StrongholdClaninfoClass(data) for key, data in request_data.items()}
        return StrongholdClaninfoClass(request_data)

async def stronghold_clanreserves_async(access_token: str, fields: str|list = None, language: str = None) -> StrongholdClanreservesClass|dict[str, StrongholdClanreservesClass]|list[StrongholdClanreservesClass]:
    """
    Метод возвращает информацию о доступных резервах и их текущем статусе.
    Parameters:
        access_token (:obj:`str`): Ключ доступа к личным данным аккаунта пользователя; можно получить при помощи метода авторизации; действителен в течение определённого времени
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "ru" — Russian (используется по умолчанию)
            "be" — Belarusian 
            "uk" — Ukrainian 
            "kk" — Kazakh
    """
    params = {'access_token': get_str_in_list(access_token), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language)}
    request_post = await create_url_post("stronghold/clanreserves", params)
    if not request_post or not request_post.get("data"):
        return StrongholdClanreservesClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [StrongholdClanreservesClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [StrongholdClanreservesClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: StrongholdClanreservesClass(data) for key, data in request_data.items()}
        return StrongholdClanreservesClass(request_data)

async def stronghold_activateclanreserve_async(access_token: str, reserve_level: int, reserve_type: str, fields: str|list = None, language: str = None) -> StrongholdActivateclanreserveClass|dict[str, StrongholdActivateclanreserveClass]|list[StrongholdActivateclanreserveClass]:
    """
    Метод активирует доступный клановый резерв. Активировать резерв может только игрок клана, у которого есть необходимые права.
    Parameters:
        access_token (:obj:`str`): Ключ доступа к личным данным аккаунта пользователя; можно получить при помощи метода авторизации; действителен в течение определённого времени
        reserve_level (:obj:`int`): Уровень кланового резерва для активации
        reserve_type (:obj:`str`): 
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "ru" — Russian (используется по умолчанию)
            "be" — Belarusian 
            "uk" — Ukrainian 
            "kk" — Kazakh
    """
    params = {'access_token': get_str_in_list(access_token), 'reserve_level': get_str_in_list(reserve_level), 'reserve_type': get_str_in_list(reserve_type), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language)}
    request_post = await create_url_post("stronghold/activateclanreserve", params)
    if not request_post or not request_post.get("data"):
        return StrongholdActivateclanreserveClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [StrongholdActivateclanreserveClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [StrongholdActivateclanreserveClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: StrongholdActivateclanreserveClass(data) for key, data in request_data.items()}
        return StrongholdActivateclanreserveClass(request_data)

async def globalmap_fronts_async(fields: str|list = None, front_id: str|list = None, language: str = None, limit: int = None, page_no: int = None) -> GlobalmapFrontsClass|dict[str, GlobalmapFrontsClass]|list[GlobalmapFrontsClass]:
    """
    Метод возвращает информацию о Фронтах Глобальной карты.
    Parameters:
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        front_id (:obj:`str` | :obj:`list`): Список идентификаторов фронтов, указывающий, какие фронты необходимо возвращать. Максимальное ограничение: 100.
        language (:obj:`str`): Язык. По умолчанию: "ru". Допустимые значения:
            "ru" — Russian (используется по умолчанию)
        limit (:obj:`int`): Количество возвращаемых записей (может вернуться меньше записей, но не больше 100). Если переданный лимит превышает 100, тогда автоматически выставляется лимит в 100 (по умолчанию).
        page_no (:obj:`int`): Номер страницы. По умолчанию: 1. Минимальное значение: 1.
    """
    params = {'fields': get_str_in_list(fields), 'front_id': get_str_in_list(front_id), 'language': get_str_in_list(language), 'limit': get_str_in_list(limit), 'page_no': get_str_in_list(page_no)}
    request_post = await create_url_post("globalmap/fronts", params)
    if not request_post or not request_post.get("data"):
        return GlobalmapFrontsClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [GlobalmapFrontsClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [GlobalmapFrontsClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: GlobalmapFrontsClass(data) for key, data in request_data.items()}
        return GlobalmapFrontsClass(request_data)

async def globalmap_provinces_async(front_id: str, arena_id: str = None, daily_revenue_gte: int = None, daily_revenue_lte: int = None, fields: str|list = None, landing_type: str = None, language: str = None, limit: int = None, order_by: str = None, page_no: int = None, prime_hour: int = None, province_id: str|list = None) -> GlobalmapProvincesClass|dict[str, GlobalmapProvincesClass]|list[GlobalmapProvincesClass]:
    """
    Метод возвращает информацию о провинциях Глобальной карты.
    Parameters:
        front_id (:obj:`str`): Идентификатор фронта. Чтобы получить его, используйте метод Фронты.
        arena_id (:obj:`str`): 
        daily_revenue_gte (:obj:`int`): Поиск провинций с дневным доходом больше или равным значению
        daily_revenue_lte (:obj:`int`): Поиск провинций с дневным доходом меньше или равным значению
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        landing_type (:obj:`str`): Поиск провинций с типом высадки. Допустимые значения:
            "null" — аукционы отключены 
            "auction" — аукцион 
            "tournament" — высадочный турнир
        language (:obj:`str`): Язык. По умолчанию: "ru". Допустимые значения:
            "ru" — Russian (используется по умолчанию)
        limit (:obj:`int`): Количество возвращаемых записей (может вернуться меньше записей, но не больше 100). Если переданный лимит превышает 100, тогда автоматически выставляется лимит в 100 (по умолчанию).
        order_by (:obj:`str`): Сортировка. Допустимые значения:
            "province_id" — по названию провинции 
            "-province_id" — по названии провинции в обратном порядке 
            "daily_revenue" — по доходности провинции 
            "-daily_revenue" — по доходности провинции в обратном порядке 
            "prime_hour" — по Прайм-тайму 
            "-prime_hour" — по Прайм-тайму в обратном порядке
        page_no (:obj:`int`): Номер страницы. По умолчанию: 1. Минимальное значение: 1.
        prime_hour (:obj:`int`): Поиск провинций со значением часа начала Прайм-тайма. Доступные значения: от 0 до 23. Максимальное значение: 23.
        province_id (:obj:`str` | :obj:`list`): Фильтр по списку идентификаторов провинций. Максимальное ограничение: 100.
    """
    params = {'front_id': get_str_in_list(front_id), 'arena_id': get_str_in_list(arena_id), 'daily_revenue_gte': get_str_in_list(daily_revenue_gte), 'daily_revenue_lte': get_str_in_list(daily_revenue_lte), 'fields': get_str_in_list(fields), 'landing_type': get_str_in_list(landing_type), 'language': get_str_in_list(language), 'limit': get_str_in_list(limit), 'order_by': get_str_in_list(order_by), 'page_no': get_str_in_list(page_no), 'prime_hour': get_str_in_list(prime_hour), 'province_id': get_str_in_list(province_id)}
    request_post = await create_url_post("globalmap/provinces", params)
    if not request_post or not request_post.get("data"):
        return GlobalmapProvincesClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [GlobalmapProvincesClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [GlobalmapProvincesClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: GlobalmapProvincesClass(data) for key, data in request_data.items()}
        return GlobalmapProvincesClass(request_data)

async def globalmap_claninfo_async(clan_id: int|list, access_token: str = None, fields: str|list = None) -> GlobalmapClaninfoClass|dict[str, GlobalmapClaninfoClass]|list[GlobalmapClaninfoClass]:
    """
    Метод возвращает данные клана на Глобальной Карте.
    Parameters:
        clan_id (:obj:`int` | :obj:`list`): Идентификатор клана. Чтобы получить его, используйте метод Кланы. Максимальное ограничение: 10.
        access_token (:obj:`str`): Ключ доступа к личным данным аккаунта пользователя; можно получить при помощи метода авторизации; действителен в течение определённого времени
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
    """
    params = {'clan_id': get_str_in_list(clan_id), 'access_token': get_str_in_list(access_token), 'fields': get_str_in_list(fields)}
    request_post = await create_url_post("globalmap/claninfo", params)
    if not request_post or not request_post.get("data"):
        return GlobalmapClaninfoClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [GlobalmapClaninfoClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [GlobalmapClaninfoClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: GlobalmapClaninfoClass(data) for key, data in request_data.items()}
        return GlobalmapClaninfoClass(request_data)

async def globalmap_clanprovinces_async(clan_id: int|list, access_token: str = None, fields: str|list = None, language: str = None) -> GlobalmapClanprovincesClass|dict[str, GlobalmapClanprovincesClass]|list[GlobalmapClanprovincesClass]:
    """
    Метод возвращает списки провинций кланов.
    Parameters:
        clan_id (:obj:`int` | :obj:`list`): Список идентификаторов кланов. Чтобы получить идентификатор клана, используйте метод Кланы. Максимальное ограничение: 10.
        access_token (:obj:`str`): Ключ доступа к личным данным аккаунта пользователя; можно получить при помощи метода авторизации; действителен в течение определённого времени
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык. По умолчанию: "ru". Допустимые значения:
            "ru" — Russian (используется по умолчанию)
    """
    params = {'clan_id': get_str_in_list(clan_id), 'access_token': get_str_in_list(access_token), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language)}
    request_post = await create_url_post("globalmap/clanprovinces", params)
    if not request_post or not request_post.get("data"):
        return GlobalmapClanprovincesClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [GlobalmapClanprovincesClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [GlobalmapClanprovincesClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: GlobalmapClanprovincesClass(data) for key, data in request_data.items()}
        return GlobalmapClanprovincesClass(request_data)

async def globalmap_clanbattles_async(clan_id: int, fields: str|list = None, language: str = None, limit: int = None, page_no: int = None) -> GlobalmapClanbattlesClass|dict[str, GlobalmapClanbattlesClass]|list[GlobalmapClanbattlesClass]:
    """
    Метод возвращает список боёв клана на Глобальной карте.
    Parameters:
        clan_id (:obj:`int`): Идентификатор клана. Чтобы получить его, используйте метод Кланы.
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык. По умолчанию: "ru". Допустимые значения:
            "ru" — Russian (используется по умолчанию)
        limit (:obj:`int`): Количество возвращаемых записей (может вернуться меньше записей, но не больше 100). Если переданный лимит превышает 100, тогда автоматически выставляется лимит в 100 (по умолчанию).
        page_no (:obj:`int`): Номер страницы. По умолчанию: 1. Минимальное значение: 1.
    """
    params = {'clan_id': get_str_in_list(clan_id), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language), 'limit': get_str_in_list(limit), 'page_no': get_str_in_list(page_no)}
    request_post = await create_url_post("globalmap/clanbattles", params)
    if not request_post or not request_post.get("data"):
        return GlobalmapClanbattlesClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [GlobalmapClanbattlesClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [GlobalmapClanbattlesClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: GlobalmapClanbattlesClass(data) for key, data in request_data.items()}
        return GlobalmapClanbattlesClass(request_data)

async def globalmap_seasons_async(fields: str|list = None, language: str = None, limit: int = None, page_no: int = None, season_id: str = None, status: str = None) -> GlobalmapSeasonsClass|dict[str, GlobalmapSeasonsClass]|list[GlobalmapSeasonsClass]:
    """
    Метод возвращает информацию о сезонах.
    Parameters:
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык. По умолчанию: "ru". Допустимые значения:
            "ru" — Russian (используется по умолчанию)
        limit (:obj:`int`): Количество страниц. По умолчанию: 5. Минимальное значение: 1. Максимальное значение: 20.
        page_no (:obj:`int`): Номер страницы. По умолчанию: 1. Минимальное значение: 1.
        season_id (:obj:`str`): 
        status (:obj:`str`): Возвращает сезоны, отфильтрованные по статусу. Допустимые значения:
            "PLANNED" — Предстоящий сезон 
            "ACTIVE" — Текущий сезон 
            "FINISHED" — Сезон завершён
    """
    params = {'fields': get_str_in_list(fields), 'language': get_str_in_list(language), 'limit': get_str_in_list(limit), 'page_no': get_str_in_list(page_no), 'season_id': get_str_in_list(season_id), 'status': get_str_in_list(status)}
    request_post = await create_url_post("globalmap/seasons", params)
    if not request_post or not request_post.get("data"):
        return GlobalmapSeasonsClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [GlobalmapSeasonsClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [GlobalmapSeasonsClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: GlobalmapSeasonsClass(data) for key, data in request_data.items()}
        return GlobalmapSeasonsClass(request_data)

async def globalmap_seasonclaninfo_async(clan_id: int, season_id: str, vehicle_level: str|list, fields: str|list = None) -> GlobalmapSeasonclaninfoClass|dict[str, GlobalmapSeasonclaninfoClass]|list[GlobalmapSeasonclaninfoClass]:
    """
    Метод возвращает статистику клана для определённого сезона.
    Parameters:
        clan_id (:obj:`int`): Идентификатор клана. Чтобы получить его, используйте метод Кланы. Минимальное значение: 1.
        season_id (:obj:`str`): Идентификатор сезона. Чтобы получить его, используйте метод Сезоны.
        vehicle_level (:obj:`str` | :obj:`list`): Перечень уровней техники. Максимальное ограничение: 100. Допустимые значения:
            "6" — Техника 6 уровня 
            "8" — Техника 8 уровня 
            "10" — Техника 10 уровня
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
    """
    params = {'clan_id': get_str_in_list(clan_id), 'season_id': get_str_in_list(season_id), 'vehicle_level': get_str_in_list(vehicle_level), 'fields': get_str_in_list(fields)}
    request_post = await create_url_post("globalmap/seasonclaninfo", params)
    if not request_post or not request_post.get("data"):
        return GlobalmapSeasonclaninfoClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [GlobalmapSeasonclaninfoClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [GlobalmapSeasonclaninfoClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: GlobalmapSeasonclaninfoClass(data) for key, data in request_data.items()}
        return GlobalmapSeasonclaninfoClass(request_data)

async def globalmap_seasonaccountinfo_async(account_id: int, season_id: str, vehicle_level: str|list, fields: str|list = None) -> GlobalmapSeasonaccountinfoClass|dict[str, GlobalmapSeasonaccountinfoClass]|list[GlobalmapSeasonaccountinfoClass]:
    """
    Метод возвращает статистику игрока для определённого сезона.
    Parameters:
        account_id (:obj:`int`): Идентификатор аккаунта. Минимальное значение: 1.
        season_id (:obj:`str`): Идентификатор сезона. Чтобы получить его, используйте метод Сезоны.
        vehicle_level (:obj:`str` | :obj:`list`): Перечень уровней техники. Максимальное ограничение: 100. Допустимые значения:
            "6" — Техника 6 уровня 
            "8" — Техника 8 уровня 
            "10" — Техника 10 уровня
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
    """
    params = {'account_id': get_str_in_list(account_id), 'season_id': get_str_in_list(season_id), 'vehicle_level': get_str_in_list(vehicle_level), 'fields': get_str_in_list(fields)}
    request_post = await create_url_post("globalmap/seasonaccountinfo", params)
    if not request_post or not request_post.get("data"):
        return GlobalmapSeasonaccountinfoClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [GlobalmapSeasonaccountinfoClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [GlobalmapSeasonaccountinfoClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: GlobalmapSeasonaccountinfoClass(data) for key, data in request_data.items()}
        return GlobalmapSeasonaccountinfoClass(request_data)

async def globalmap_seasonrating_async(season_id: str, vehicle_level: str, fields: str|list = None, limit: int = None, page_no: int = None) -> GlobalmapSeasonratingClass|dict[str, GlobalmapSeasonratingClass]|list[GlobalmapSeasonratingClass]:
    """
    Метод возвращает клановый рейтинг сезона.
    Parameters:
        season_id (:obj:`str`): Идентификатор сезона. Чтобы получить его, используйте метод Сезоны.
        vehicle_level (:obj:`str`): Уровень техники. Допустимые значения:
            "6" — Техника 6 уровня 
            "8" — Техника 8 уровня 
            "10" — Техника 10 уровня
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        limit (:obj:`int`): Количество кланов. По умолчанию: 10. Минимальное значение: 1. Максимальное значение: 100.
        page_no (:obj:`int`): Номер страницы. По умолчанию: 1. Минимальное значение: 1.
    """
    params = {'season_id': get_str_in_list(season_id), 'vehicle_level': get_str_in_list(vehicle_level), 'fields': get_str_in_list(fields), 'limit': get_str_in_list(limit), 'page_no': get_str_in_list(page_no)}
    request_post = await create_url_post("globalmap/seasonrating", params)
    if not request_post or not request_post.get("data"):
        return GlobalmapSeasonratingClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [GlobalmapSeasonratingClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [GlobalmapSeasonratingClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: GlobalmapSeasonratingClass(data) for key, data in request_data.items()}
        return GlobalmapSeasonratingClass(request_data)

async def globalmap_seasonratingneighbors_async(clan_id: int, season_id: str, vehicle_level: str, fields: str|list = None, limit: int = None) -> GlobalmapSeasonratingneighborsClass|dict[str, GlobalmapSeasonratingneighborsClass]|list[GlobalmapSeasonratingneighborsClass]:
    """
    Метод возвращает список соседних позиций в клановом рейтинге сезона.
    Parameters:
        clan_id (:obj:`int`): Идентификатор клана. Чтобы получить его, используйте метод Кланы. Минимальное значение: 1.
        season_id (:obj:`str`): Идентификатор сезона. Чтобы получить его, используйте метод Сезоны.
        vehicle_level (:obj:`str`): Уровень техники. Допустимые значения:
            "6" — Техника 6 уровня 
            "8" — Техника 8 уровня 
            "10" — Техника 10 уровня
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        limit (:obj:`int`): Количество соседних позиций. По умолчанию: 10. Минимальное значение: 1. Максимальное значение: 99.
    """
    params = {'clan_id': get_str_in_list(clan_id), 'season_id': get_str_in_list(season_id), 'vehicle_level': get_str_in_list(vehicle_level), 'fields': get_str_in_list(fields), 'limit': get_str_in_list(limit)}
    request_post = await create_url_post("globalmap/seasonratingneighbors", params)
    if not request_post or not request_post.get("data"):
        return GlobalmapSeasonratingneighborsClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [GlobalmapSeasonratingneighborsClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [GlobalmapSeasonratingneighborsClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: GlobalmapSeasonratingneighborsClass(data) for key, data in request_data.items()}
        return GlobalmapSeasonratingneighborsClass(request_data)

async def globalmap_events_async(event_id: str = None, fields: str|list = None, language: str = None, limit: int = None, page_no: int = None, status: str = None) -> GlobalmapEventsClass|dict[str, GlobalmapEventsClass]|list[GlobalmapEventsClass]:
    """
    Метод возвращает информацию о событиях.
    Parameters:
        event_id (:obj:`str`): 
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык. По умолчанию: "ru". Допустимые значения:
            "ru" — Russian (используется по умолчанию)
        limit (:obj:`int`): Количество страниц. По умолчанию: 5. Минимальное значение: 1. Максимальное значение: 20.
        page_no (:obj:`int`): Номер страницы. По умолчанию: 1. Минимальное значение: 1.
        status (:obj:`str`): Возвращает события, отфильтрованные по статусу. Допустимые значения:
            "PLANNED" — Предстоящее событие 
            "ACTIVE" — Текущее событие 
            "FINISHED" — Событие завершено
    """
    params = {'event_id': get_str_in_list(event_id), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language), 'limit': get_str_in_list(limit), 'page_no': get_str_in_list(page_no), 'status': get_str_in_list(status)}
    request_post = await create_url_post("globalmap/events", params)
    if not request_post or not request_post.get("data"):
        return GlobalmapEventsClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [GlobalmapEventsClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [GlobalmapEventsClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: GlobalmapEventsClass(data) for key, data in request_data.items()}
        return GlobalmapEventsClass(request_data)

async def globalmap_eventclaninfo_async(clan_id: int, event_id: str, front_id: str|list, fields: str|list = None) -> GlobalmapEventclaninfoClass|dict[str, GlobalmapEventclaninfoClass]|list[GlobalmapEventclaninfoClass]:
    """
    Метод возвращает статистику клана для определённого события.
    Parameters:
        clan_id (:obj:`int`): Идентификатор клана. Чтобы получить его, используйте метод Кланы. Минимальное значение: 1.
        event_id (:obj:`str`): Идентификатор события. Чтобы получить его, используйте метод События.
        front_id (:obj:`str` | :obj:`list`): Идентификатор фронта. Чтобы получить его, используйте метод Фронты. Максимальное ограничение: 10.
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
    """
    params = {'clan_id': get_str_in_list(clan_id), 'event_id': get_str_in_list(event_id), 'front_id': get_str_in_list(front_id), 'fields': get_str_in_list(fields)}
    request_post = await create_url_post("globalmap/eventclaninfo", params)
    if not request_post or not request_post.get("data"):
        return GlobalmapEventclaninfoClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [GlobalmapEventclaninfoClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [GlobalmapEventclaninfoClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: GlobalmapEventclaninfoClass(data) for key, data in request_data.items()}
        return GlobalmapEventclaninfoClass(request_data)

async def globalmap_eventaccountinfo_async(account_id: int, event_id: str, front_id: str|list, clan_id: int = None, fields: str|list = None) -> GlobalmapEventaccountinfoClass|dict[str, GlobalmapEventaccountinfoClass]|list[GlobalmapEventaccountinfoClass]:
    """
    Метод возвращает статистику игрока для определённого события
    Parameters:
        account_id (:obj:`int`): Идентификатор аккаунта. Минимальное значение: 1.
        event_id (:obj:`str`): Идентификатор события. Чтобы получить его, используйте метод События.
        front_id (:obj:`str` | :obj:`list`): Идентификатор фронта. Чтобы получить его, используйте метод Фронты. Максимальное ограничение: 10.
        clan_id (:obj:`int`): Идентификатор клана. Чтобы получить его, используйте метод Кланы. Минимальное значение: 1.
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
    """
    params = {'account_id': get_str_in_list(account_id), 'event_id': get_str_in_list(event_id), 'front_id': get_str_in_list(front_id), 'clan_id': get_str_in_list(clan_id), 'fields': get_str_in_list(fields)}
    request_post = await create_url_post("globalmap/eventaccountinfo", params)
    if not request_post or not request_post.get("data"):
        return GlobalmapEventaccountinfoClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [GlobalmapEventaccountinfoClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [GlobalmapEventaccountinfoClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: GlobalmapEventaccountinfoClass(data) for key, data in request_data.items()}
        return GlobalmapEventaccountinfoClass(request_data)

async def globalmap_eventaccountratings_async(event_id: str, front_id: str, fields: str|list = None, in_rating: int = None, limit: int = None, page_no: int = None) -> GlobalmapEventaccountratingsClass|dict[str, GlobalmapEventaccountratingsClass]|list[GlobalmapEventaccountratingsClass]:
    """
    Метод возвращает рейтинг игрока в событии.
    Parameters:
        event_id (:obj:`str`): Идентификатор события. Чтобы получить его, используйте метод События.
        front_id (:obj:`str`): Идентификатор фронта. Чтобы получить его, используйте метод Фронты.
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        in_rating (:obj:`int`): Получить данные только для аккаунтов с рейтингом. По умолчанию: 0. Допустимые значения:
            "1" — Только с рейтингом 
            "0" — Все (используется по умолчанию)
        limit (:obj:`int`): Количество аккаунтов. По умолчанию: 20. Минимальное значение: 10. Максимальное значение: 100.
        page_no (:obj:`int`): Номер страницы. По умолчанию: 1. Минимальное значение: 1.
    """
    params = {'event_id': get_str_in_list(event_id), 'front_id': get_str_in_list(front_id), 'fields': get_str_in_list(fields), 'in_rating': get_str_in_list(in_rating), 'limit': get_str_in_list(limit), 'page_no': get_str_in_list(page_no)}
    request_post = await create_url_post("globalmap/eventaccountratings", params)
    if not request_post or not request_post.get("data"):
        return GlobalmapEventaccountratingsClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [GlobalmapEventaccountratingsClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [GlobalmapEventaccountratingsClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: GlobalmapEventaccountratingsClass(data) for key, data in request_data.items()}
        return GlobalmapEventaccountratingsClass(request_data)

async def globalmap_eventaccountratingneighbors_async(account_id: int, event_id: str, front_id: str, fields: str|list = None, limit: int = None, neighbours_count: int = None, page_no: int = None) -> GlobalmapEventaccountratingneighborsClass|dict[str, GlobalmapEventaccountratingneighborsClass]|list[GlobalmapEventaccountratingneighborsClass]:
    """
    Метод возвращает соседние позиции в рейтинге игроков события.
    Parameters:
        account_id (:obj:`int`): Идентификатор аккаунта. Минимальное значение: 1.
        event_id (:obj:`str`): Идентификатор события. Чтобы получить его, используйте метод События.
        front_id (:obj:`str`): Идентификатор фронта. Чтобы получить его, используйте метод Фронты.
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        limit (:obj:`int`): Количество кланов. По умолчанию: 20. Минимальное значение: 10. Максимальное значение: 100.
        neighbours_count (:obj:`int`): Сколько соседних позиций отобразить рядом с аккаунтом. По умолчанию: 3. Минимальное значение: 1. Максимальное значение: 99.
        page_no (:obj:`int`): Номер страницы. По умолчанию: 1. Минимальное значение: 1.
    """
    params = {'account_id': get_str_in_list(account_id), 'event_id': get_str_in_list(event_id), 'front_id': get_str_in_list(front_id), 'fields': get_str_in_list(fields), 'limit': get_str_in_list(limit), 'neighbours_count': get_str_in_list(neighbours_count), 'page_no': get_str_in_list(page_no)}
    request_post = await create_url_post("globalmap/eventaccountratingneighbors", params)
    if not request_post or not request_post.get("data"):
        return GlobalmapEventaccountratingneighborsClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [GlobalmapEventaccountratingneighborsClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [GlobalmapEventaccountratingneighborsClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: GlobalmapEventaccountratingneighborsClass(data) for key, data in request_data.items()}
        return GlobalmapEventaccountratingneighborsClass(request_data)

async def globalmap_eventrating_async(event_id: str, front_id: str, fields: str|list = None, limit: int = None, page_no: int = None) -> GlobalmapEventratingClass|dict[str, GlobalmapEventratingClass]|list[GlobalmapEventratingClass]:
    """
    Метод возвращает клановый рейтинг события
    Parameters:
        event_id (:obj:`str`): Идентификатор события. Чтобы получить его, используйте метод События.
        front_id (:obj:`str`): Идентификатор фронта. Чтобы получить его, используйте метод Фронты.
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        limit (:obj:`int`): Количество кланов. По умолчанию: 10. Минимальное значение: 1. Максимальное значение: 100.
        page_no (:obj:`int`): Номер страницы. По умолчанию: 1. Минимальное значение: 1.
    """
    params = {'event_id': get_str_in_list(event_id), 'front_id': get_str_in_list(front_id), 'fields': get_str_in_list(fields), 'limit': get_str_in_list(limit), 'page_no': get_str_in_list(page_no)}
    request_post = await create_url_post("globalmap/eventrating", params)
    if not request_post or not request_post.get("data"):
        return GlobalmapEventratingClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [GlobalmapEventratingClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [GlobalmapEventratingClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: GlobalmapEventratingClass(data) for key, data in request_data.items()}
        return GlobalmapEventratingClass(request_data)

async def globalmap_eventratingneighbors_async(clan_id: int, event_id: str, front_id: str, fields: str|list = None, limit: int = None) -> GlobalmapEventratingneighborsClass|dict[str, GlobalmapEventratingneighborsClass]|list[GlobalmapEventratingneighborsClass]:
    """
    Метод возвращает список соседних позиций в клановом рейтинге события
    Parameters:
        clan_id (:obj:`int`): Идентификатор клана. Чтобы получить его, используйте метод Кланы. Минимальное значение: 1.
        event_id (:obj:`str`): Идентификатор события. Чтобы получить его, используйте метод События.
        front_id (:obj:`str`): Идентификатор фронта. Чтобы получить его, используйте метод Фронты.
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        limit (:obj:`int`): Количество соседних позиций. По умолчанию: 10. Минимальное значение: 1. Максимальное значение: 99.
    """
    params = {'clan_id': get_str_in_list(clan_id), 'event_id': get_str_in_list(event_id), 'front_id': get_str_in_list(front_id), 'fields': get_str_in_list(fields), 'limit': get_str_in_list(limit)}
    request_post = await create_url_post("globalmap/eventratingneighbors", params)
    if not request_post or not request_post.get("data"):
        return GlobalmapEventratingneighborsClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [GlobalmapEventratingneighborsClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [GlobalmapEventratingneighborsClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: GlobalmapEventratingneighborsClass(data) for key, data in request_data.items()}
        return GlobalmapEventratingneighborsClass(request_data)

async def globalmap_info_async(fields: str|list = None) -> GlobalmapInfoClass|dict[str, GlobalmapInfoClass]|list[GlobalmapInfoClass]:
    """
    Метод возвращает общую информацию о Глобальной карте.
    Parameters:
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
    """
    params = {'fields': get_str_in_list(fields)}
    request_post = await create_url_post("globalmap/info", params)
    if not request_post or not request_post.get("data"):
        return GlobalmapInfoClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [GlobalmapInfoClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [GlobalmapInfoClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: GlobalmapInfoClass(data) for key, data in request_data.items()}
        return GlobalmapInfoClass(request_data)

async def encyclopedia_vehicles_async(fields: str|list = None, language: str = None, limit: int = None, nation: str|list = None, page_no: int = None, tank_id: int|list = None, tier: int|list = None, type_param: str|list = None) -> EncyclopediaVehiclesClass|dict[str, EncyclopediaVehiclesClass]|list[EncyclopediaVehiclesClass]:
    """
    Метод возвращает список доступной техники.
    Parameters:
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
        limit (:obj:`int`): Количество возвращаемых записей (может вернуться меньше записей, но не больше 100). Если переданный лимит превышает 100, тогда автоматически выставляется лимит в 100 (по умолчанию).
        nation (:obj:`str` | :obj:`list`): Нация. Максимальное ограничение: 100.
        page_no (:obj:`int`): 
        tank_id (:obj:`int` | :obj:`list`): Идентификатор техники. Максимальное ограничение: 100.
        tier (:obj:`int` | :obj:`list`): Уровень. Максимальное ограничение: 100.
        type_param (:obj:`str` | :obj:`list`): Тип техники. Максимальное ограничение: 100. Допустимые значения:
            "heavyTank" — Тяжёлый танк 
            "AT-SPG" — ПТ-САУ 
            "mediumTank" — Средний танк 
            "lightTank" — Легкий танк 
            "SPG" — САУ
    """
    params = {'fields': get_str_in_list(fields), 'language': get_str_in_list(language), 'limit': get_str_in_list(limit), 'nation': get_str_in_list(nation), 'page_no': get_str_in_list(page_no), 'tank_id': get_str_in_list(tank_id), 'tier': get_str_in_list(tier), 'type': get_str_in_list(type_param)}
    request_post = await create_url_post("encyclopedia/vehicles", params)
    if not request_post or not request_post.get("data"):
        return EncyclopediaVehiclesClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [EncyclopediaVehiclesClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [EncyclopediaVehiclesClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: EncyclopediaVehiclesClass(data) for key, data in request_data.items()}
        return EncyclopediaVehiclesClass(request_data)

async def encyclopedia_vehicleprofile_async(tank_id: int, engine_id: int = None, fields: str|list = None, gun_id: int = None, language: str = None, profile_id: str = None, radio_id: int = None, suspension_id: int = None, turret_id: int = None) -> EncyclopediaVehicleprofileClass|dict[str, EncyclopediaVehicleprofileClass]|list[EncyclopediaVehicleprofileClass]:
    """
    Метод возвращает характеристики конфигурации техники на основе указанных идентификаторов модулей.
    Parameters:
        tank_id (:obj:`int`): 
        engine_id (:obj:`int`): Идентификатор двигателя. Если модуль не указан, используется модуль базовой комплектации.
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        gun_id (:obj:`int`): Идентификатор орудия. Если модуль не указан, используется модуль базовой комплектации.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
        profile_id (:obj:`str`): Идентификатор комплектации. Если указан, параметры идентификаторов отдельных модулей не учитываются.
        radio_id (:obj:`int`): Идентификатор радиостанции. Если модуль не указан, используется модуль базовой комплектации.
        suspension_id (:obj:`int`): Идентификатор ходовой. Если модуль не указан, используется модуль базовой комплектации.
        turret_id (:obj:`int`): Идентификатор башни. Если модуль не указан, используется модуль базовой комплектации.
    """
    params = {'tank_id': get_str_in_list(tank_id), 'engine_id': get_str_in_list(engine_id), 'fields': get_str_in_list(fields), 'gun_id': get_str_in_list(gun_id), 'language': get_str_in_list(language), 'profile_id': get_str_in_list(profile_id), 'radio_id': get_str_in_list(radio_id), 'suspension_id': get_str_in_list(suspension_id), 'turret_id': get_str_in_list(turret_id)}
    request_post = await create_url_post("encyclopedia/vehicleprofile", params)
    if not request_post or not request_post.get("data"):
        return EncyclopediaVehicleprofileClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [EncyclopediaVehicleprofileClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [EncyclopediaVehicleprofileClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: EncyclopediaVehicleprofileClass(data) for key, data in request_data.items()}
        return EncyclopediaVehicleprofileClass(request_data)

async def encyclopedia_achievements_async(fields: str|list = None, language: str = None) -> EncyclopediaAchievementsClass|dict[str, EncyclopediaAchievementsClass]|list[EncyclopediaAchievementsClass]:
    """
    Метод возвращает информацию о достижениях.
    Parameters:
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
    """
    params = {'fields': get_str_in_list(fields), 'language': get_str_in_list(language)}
    request_post = await create_url_post("encyclopedia/achievements", params)
    if not request_post or not request_post.get("data"):
        return EncyclopediaAchievementsClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [EncyclopediaAchievementsClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [EncyclopediaAchievementsClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: EncyclopediaAchievementsClass(data) for key, data in request_data.items()}
        return EncyclopediaAchievementsClass(request_data)

async def encyclopedia_info_async(fields: str|list = None, language: str = None) -> EncyclopediaInfoClass|dict[str, EncyclopediaInfoClass]|list[EncyclopediaInfoClass]:
    """
    Метод возвращает информацию о Танкопедии.
    Parameters:
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
    """
    params = {'fields': get_str_in_list(fields), 'language': get_str_in_list(language)}
    request_post = await create_url_post("encyclopedia/info", params)
    if not request_post or not request_post.get("data"):
        return EncyclopediaInfoClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [EncyclopediaInfoClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [EncyclopediaInfoClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: EncyclopediaInfoClass(data) for key, data in request_data.items()}
        return EncyclopediaInfoClass(request_data)

async def encyclopedia_arenas_async(fields: str|list = None, language: str = None) -> EncyclopediaArenasClass|dict[str, EncyclopediaArenasClass]|list[EncyclopediaArenasClass]:
    """
    Метод возвращает информацию об игровых картах.
    Parameters:
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
    """
    params = {'fields': get_str_in_list(fields), 'language': get_str_in_list(language)}
    request_post = await create_url_post("encyclopedia/arenas", params)
    if not request_post or not request_post.get("data"):
        return EncyclopediaArenasClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [EncyclopediaArenasClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [EncyclopediaArenasClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: EncyclopediaArenasClass(data) for key, data in request_data.items()}
        return EncyclopediaArenasClass(request_data)

async def encyclopedia_provisions_async(fields: str|list = None, language: str = None, limit: int = None, page_no: int = None, provision_id: int|list = None, type_param: str|list = None) -> EncyclopediaProvisionsClass|dict[str, EncyclopediaProvisionsClass]|list[EncyclopediaProvisionsClass]:
    """
    Метод возвращает список доступного оборудования и снаряжения.
    Parameters:
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
        limit (:obj:`int`): Количество возвращаемых записей (может вернуться меньше записей, но не больше 100). Если переданный лимит превышает 100, тогда автоматически выставляется лимит в 100 (по умолчанию).
        page_no (:obj:`int`): 
        provision_id (:obj:`int` | :obj:`list`): Идентификатор оборудования или снаряжения. Максимальное ограничение: 100.
        type_param (:obj:`str` | :obj:`list`): Тип. По умолчанию: "equipment, optionalDevice". Максимальное ограничение: 100. Допустимые значения:
            "equipment" — Снаряжение 
            "optionalDevice" — Оборудование
    """
    params = {'fields': get_str_in_list(fields), 'language': get_str_in_list(language), 'limit': get_str_in_list(limit), 'page_no': get_str_in_list(page_no), 'provision_id': get_str_in_list(provision_id), 'type': get_str_in_list(type_param)}
    request_post = await create_url_post("encyclopedia/provisions", params)
    if not request_post or not request_post.get("data"):
        return EncyclopediaProvisionsClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [EncyclopediaProvisionsClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [EncyclopediaProvisionsClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: EncyclopediaProvisionsClass(data) for key, data in request_data.items()}
        return EncyclopediaProvisionsClass(request_data)

async def encyclopedia_personalmissions_async(campaign_id: int|list = None, fields: str|list = None, language: str = None, operation_id: int|list = None, set_id: int|list = None, tag: str|list = None) -> EncyclopediaPersonalmissionsClass|dict[str, EncyclopediaPersonalmissionsClass]|list[EncyclopediaPersonalmissionsClass]:
    """
    Метод возвращает информацию о Личных боевых задачах на основе указанных идентификаторов кампании, операции, ветки боевых задач и тегов.
    Parameters:
        campaign_id (:obj:`int` | :obj:`list`): Идентификатор кампании. Максимальное ограничение: 100.
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
        operation_id (:obj:`int` | :obj:`list`): Идентификатор операции. Максимальное ограничение: 100.
        set_id (:obj:`int` | :obj:`list`): Идентификатор ветки задач. Максимальное ограничение: 100.
        tag (:obj:`str` | :obj:`list`): Тег задачи. Максимальное ограничение: 100.
    """
    params = {'campaign_id': get_str_in_list(campaign_id), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language), 'operation_id': get_str_in_list(operation_id), 'set_id': get_str_in_list(set_id), 'tag': get_str_in_list(tag)}
    request_post = await create_url_post("encyclopedia/personalmissions", params)
    if not request_post or not request_post.get("data"):
        return EncyclopediaPersonalmissionsClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [EncyclopediaPersonalmissionsClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [EncyclopediaPersonalmissionsClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: EncyclopediaPersonalmissionsClass(data) for key, data in request_data.items()}
        return EncyclopediaPersonalmissionsClass(request_data)

async def encyclopedia_boosters_async(fields: str|list = None, language: str = None) -> EncyclopediaBoostersClass|dict[str, EncyclopediaBoostersClass]|list[EncyclopediaBoostersClass]:
    """
    Метод возвращает информацию о личных резервах.
    Parameters:
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
    """
    params = {'fields': get_str_in_list(fields), 'language': get_str_in_list(language)}
    request_post = await create_url_post("encyclopedia/boosters", params)
    if not request_post or not request_post.get("data"):
        return EncyclopediaBoostersClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [EncyclopediaBoostersClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [EncyclopediaBoostersClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: EncyclopediaBoostersClass(data) for key, data in request_data.items()}
        return EncyclopediaBoostersClass(request_data)

async def encyclopedia_vehicleprofiles_async(tank_id: int, fields: str|list = None, language: str = None, order_by: str = None) -> EncyclopediaVehicleprofilesClass|dict[str, EncyclopediaVehicleprofilesClass]|list[EncyclopediaVehicleprofilesClass]:
    """
    Метод возвращает характеристики комплектации техники.
    Parameters:
        tank_id (:obj:`int`): 
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
        order_by (:obj:`str`): Сортировка. Допустимые значения:
            "price_credit" — по стоимости в кредитах 
            "-price_credit" — по стоимости в кредитах, в обратном порядке
    """
    params = {'tank_id': get_str_in_list(tank_id), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language), 'order_by': get_str_in_list(order_by)}
    request_post = await create_url_post("encyclopedia/vehicleprofiles", params)
    if not request_post or not request_post.get("data"):
        return EncyclopediaVehicleprofilesClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [EncyclopediaVehicleprofilesClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [EncyclopediaVehicleprofilesClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: EncyclopediaVehicleprofilesClass(data) for key, data in request_data.items()}
        return EncyclopediaVehicleprofilesClass(request_data)

async def encyclopedia_modules_async(extra: str|list = None, fields: str|list = None, language: str = None, limit: int = None, module_id: int|list = None, nation: str|list = None, page_no: int = None, type_param: str|list = None) -> EncyclopediaModulesClass|dict[str, EncyclopediaModulesClass]|list[EncyclopediaModulesClass]:
    """
    Метод возвращает перечень доступных модулей, которые можно установить на технику, таких как двигатели, башни и т.д. Необходимо указать как минимум один входной параметр фильтра (идентификатор модуля, тип модуля).
    Parameters:
        extra (:obj:`str` | :obj:`list`): Список дополнительных полей, которые будут включены в ответ. Допустимые значения:
            "default_profile"
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
        limit (:obj:`int`): Количество возвращаемых записей (может вернуться меньше записей, но не больше 100). Если переданный лимит превышает 100, тогда автоматически выставляется лимит в 100 (по умолчанию).
        module_id (:obj:`int` | :obj:`list`): Идентификатор модуля. Максимальное ограничение: 100.
        nation (:obj:`str` | :obj:`list`): Нация. Максимальное ограничение: 100.
        page_no (:obj:`int`): 
        type_param (:obj:`str` | :obj:`list`): Тип модуля. Максимальное ограничение: 100. Допустимые значения:
            "vehicleRadio" — Радиостанции 
            "vehicleEngine" — Двигатели 
            "vehicleGun" — Орудия 
            "vehicleChassis" — Ходовые 
            "vehicleTurret" — Башни
    """
    if not extra:
        extra = ["default_profile"]
    params = {'extra': get_str_in_list(extra), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language), 'limit': get_str_in_list(limit), 'module_id': get_str_in_list(module_id), 'nation': get_str_in_list(nation), 'page_no': get_str_in_list(page_no), 'type': get_str_in_list(type_param)}
    request_post = await create_url_post("encyclopedia/modules", params)
    if not request_post or not request_post.get("data"):
        return EncyclopediaModulesClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [EncyclopediaModulesClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [EncyclopediaModulesClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: EncyclopediaModulesClass(data) for key, data in request_data.items()}
        return EncyclopediaModulesClass(request_data)

async def encyclopedia_badges_async(fields: str|list = None, language: str = None) -> EncyclopediaBadgesClass|dict[str, EncyclopediaBadgesClass]|list[EncyclopediaBadgesClass]:
    """
    Метод возвращает список доступных нашивок, которые игрок может заработать в Ранговых боях.
    Parameters:
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
    """
    params = {'fields': get_str_in_list(fields), 'language': get_str_in_list(language)}
    request_post = await create_url_post("encyclopedia/badges", params)
    if not request_post or not request_post.get("data"):
        return EncyclopediaBadgesClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [EncyclopediaBadgesClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [EncyclopediaBadgesClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: EncyclopediaBadgesClass(data) for key, data in request_data.items()}
        return EncyclopediaBadgesClass(request_data)

async def encyclopedia_crewroles_async(fields: str|list = None, language: str = None, role: str|list = None) -> EncyclopediaCrewrolesClass|dict[str, EncyclopediaCrewrolesClass]|list[EncyclopediaCrewrolesClass]:
    """
    Метод возвращает полное описание всех специальностей экипажа.
    Parameters:
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
        role (:obj:`str` | :obj:`list`): Идентификатор специальности экипажа. Максимальное ограничение: 100.
    """
    params = {'fields': get_str_in_list(fields), 'language': get_str_in_list(language), 'role': get_str_in_list(role)}
    request_post = await create_url_post("encyclopedia/crewroles", params)
    if not request_post or not request_post.get("data"):
        return EncyclopediaCrewrolesClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [EncyclopediaCrewrolesClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [EncyclopediaCrewrolesClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: EncyclopediaCrewrolesClass(data) for key, data in request_data.items()}
        return EncyclopediaCrewrolesClass(request_data)

async def encyclopedia_crewskills_async(fields: str|list = None, language: str = None, role: str = None, skill: str|list = None) -> EncyclopediaCrewskillsClass|dict[str, EncyclopediaCrewskillsClass]|list[EncyclopediaCrewskillsClass]:
    """
    Метод возвращает полное описание всех умений экипажа.
    Parameters:
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
        role (:obj:`str`): 
        skill (:obj:`str` | :obj:`list`): Идентификатор умения. Максимальное ограничение: 100.
    """
    params = {'fields': get_str_in_list(fields), 'language': get_str_in_list(language), 'role': get_str_in_list(role), 'skill': get_str_in_list(skill)}
    request_post = await create_url_post("encyclopedia/crewskills", params)
    if not request_post or not request_post.get("data"):
        return EncyclopediaCrewskillsClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [EncyclopediaCrewskillsClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [EncyclopediaCrewskillsClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: EncyclopediaCrewskillsClass(data) for key, data in request_data.items()}
        return EncyclopediaCrewskillsClass(request_data)

async def clanratings_dates_async(limit: int = None) -> ClanratingsDatesClass|dict[str, ClanratingsDatesClass]|list[ClanratingsDatesClass]:
    """
    Метод возвращает даты, за которые есть рейтинговые данные.
    Parameters:
        limit (:obj:`int`): Количество возвращаемых записей (может вернуться меньше записей, но не больше 365). Если переданный лимит превышает 365, тогда автоматически выставляется лимит в 7 (по умолчанию).
    """
    params = {'limit': get_str_in_list(limit)}
    request_post = await create_url_post("clanratings/dates", params)
    if not request_post or not request_post.get("data"):
        return ClanratingsDatesClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [ClanratingsDatesClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [ClanratingsDatesClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: ClanratingsDatesClass(data) for key, data in request_data.items()}
        return ClanratingsDatesClass(request_data)

async def clanratings_clans_async(clan_id: int|list, date: str = None, fields: str|list = None, language: str = None) -> ClanratingsClansClass|dict[str, ClanratingsClansClass]|list[ClanratingsClansClass]:
    """
    Метод возвращает рейтинги кланов по заданным идентификаторам.
    Parameters:
        clan_id (:obj:`int` | :obj:`list`): Идентификаторы кланов. Максимальное ограничение: 100.
        date (:obj:`str`): Дата расчёта рейтингов. Дата в формате UNIX timestamp или ISO 8601. Например, 1376542800 или 2013-08-15T00:00:00
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
    """
    params = {'clan_id': get_str_in_list(clan_id), 'date': get_str_in_list(date), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language)}
    request_post = await create_url_post("clanratings/clans", params)
    if not request_post or not request_post.get("data"):
        return ClanratingsClansClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [ClanratingsClansClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [ClanratingsClansClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: ClanratingsClansClass(data) for key, data in request_data.items()}
        return ClanratingsClansClass(request_data)

async def clanratings_neighbors_async(clan_id: int, rank_field: str, date: str = None, fields: str|list = None, language: str = None, limit: int = None) -> ClanratingsNeighborsClass|dict[str, ClanratingsNeighborsClass]|list[ClanratingsNeighborsClass]:
    """
    Метод возвращает список соседних позиций в заданном рейтинге кланов.
    Parameters:
        clan_id (:obj:`int`): 
        rank_field (:obj:`str`): 
        date (:obj:`str`): Дата расчёта рейтингов. Дата в формате UNIX timestamp или ISO 8601. Например, 1376542800 или 2013-08-15T00:00:00
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
        limit (:obj:`int`): Количество возвращаемых записей (может вернуться меньше записей, но не больше 50). Если переданный лимит превышает 50, тогда автоматически выставляется лимит в 5 (по умолчанию).
    """
    params = {'clan_id': get_str_in_list(clan_id), 'rank_field': get_str_in_list(rank_field), 'date': get_str_in_list(date), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language), 'limit': get_str_in_list(limit)}
    request_post = await create_url_post("clanratings/neighbors", params)
    if not request_post or not request_post.get("data"):
        return ClanratingsNeighborsClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [ClanratingsNeighborsClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [ClanratingsNeighborsClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: ClanratingsNeighborsClass(data) for key, data in request_data.items()}
        return ClanratingsNeighborsClass(request_data)

async def clanratings_top_async(rank_field: str, date: str = None, fields: str|list = None, language: str = None, limit: int = None, page_no: int = None) -> ClanratingsTopClass|dict[str, ClanratingsTopClass]|list[ClanratingsTopClass]:
    """
    Метод возвращает список лучших кланов по заданным параметрам.
    Parameters:
        rank_field (:obj:`str`): 
        date (:obj:`str`): Дата расчёта рейтингов. Дата в формате UNIX timestamp или ISO 8601. Например, 1376542800 или 2013-08-15T00:00:00
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
        limit (:obj:`int`): Количество возвращаемых записей (может вернуться меньше записей, но не больше 1000). Если переданный лимит превышает 1000, тогда автоматически выставляется лимит в 10 (по умолчанию).
        page_no (:obj:`int`): Номер страницы. По умолчанию: 1. Минимальное значение: 1.
    """
    params = {'rank_field': get_str_in_list(rank_field), 'date': get_str_in_list(date), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language), 'limit': get_str_in_list(limit), 'page_no': get_str_in_list(page_no)}
    request_post = await create_url_post("clanratings/top", params)
    if not request_post or not request_post.get("data"):
        return ClanratingsTopClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [ClanratingsTopClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [ClanratingsTopClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: ClanratingsTopClass(data) for key, data in request_data.items()}
        return ClanratingsTopClass(request_data)

async def tanks_stats_async(account_id: int, access_token: str = None, extra: str|list = None, fields: str|list = None, in_garage: str = None, language: str = None, tank_id: int|list = None) -> TanksStatsClass|dict[str, TanksStatsClass]|list[TanksStatsClass]:
    """
    Метод возвращает общую, ротную и клановую статистику по каждой единице техники каждого пользователя.
    Parameters:
        account_id (:obj:`int`): 
        access_token (:obj:`str`): Ключ доступа к личным данным аккаунта пользователя; можно получить при помощи метода авторизации; действителен в течение определённого времени
        extra (:obj:`str` | :obj:`list`): Список дополнительных полей, которые будут включены в ответ. Допустимые значения:
            "epic" 
            "fallout" 
            "random" 
            "ranked_10x10" 
            "ranked_battles"
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        in_garage (:obj:`str`): Фильтр по наличию техники в Ангаре. Если параметр не указан, возвращается вся техника. Параметр обрабатывается только при наличии действующего access_token для указанного account_id. Допустимые значения:
            "1" — Возвращать технику из Ангара. 
            "0" — Возвращать технику, которой уже нет в Ангаре.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
        tank_id (:obj:`int` | :obj:`list`): Идентификатор техники игрока. Максимальное ограничение: 100.
    """
    if not extra:
        extra = ["epic", "fallout", "random", "ranked_10x10", "ranked_battles"]
    params = {'account_id': get_str_in_list(account_id), 'access_token': get_str_in_list(access_token), 'extra': get_str_in_list(extra), 'fields': get_str_in_list(fields), 'in_garage': get_str_in_list(in_garage), 'language': get_str_in_list(language), 'tank_id': get_str_in_list(tank_id)}
    request_post = await create_url_post("tanks/stats", params)
    if not request_post or not request_post.get("data"):
        return TanksStatsClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [TanksStatsClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [TanksStatsClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: TanksStatsClass(data) for key, data in request_data.items()}
        return TanksStatsClass(request_data)

async def tanks_achievements_async(account_id: int, access_token: str = None, fields: str|list = None, in_garage: str = None, language: str = None, tank_id: int|list = None) -> TanksAchievementsClass|dict[str, TanksAchievementsClass]|list[TanksAchievementsClass]:
    """
    Метод возвращает список достижений по всей технике игрока. Значения поля achievements зависят от свойств достижений:  степень от 1 до 4 для знака классности и этапных достижений (type: "class") максимальное значение серийных достижений (type: "series") количество заработанных наград из секций: Герой битвы, Эпические достижения, Групповые достижения, Особые достижения и т.п. (type: "repeatable, single, custom"). 
    Parameters:
        account_id (:obj:`int`): 
        access_token (:obj:`str`): Ключ доступа к личным данным аккаунта пользователя; можно получить при помощи метода авторизации; действителен в течение определённого времени
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        in_garage (:obj:`str`): Фильтр по наличию техники в Ангаре. Если параметр не указан, возвращается вся техника. Параметр обрабатывается только при наличии действующего access_token для указанного account_id. Допустимые значения:
            "1" — Возвращать технику из Ангара. 
            "0" — Возвращать технику, которой уже нет в Ангаре.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
        tank_id (:obj:`int` | :obj:`list`): Идентификатор техники игрока. Максимальное ограничение: 100.
    """
    params = {'account_id': get_str_in_list(account_id), 'access_token': get_str_in_list(access_token), 'fields': get_str_in_list(fields), 'in_garage': get_str_in_list(in_garage), 'language': get_str_in_list(language), 'tank_id': get_str_in_list(tank_id)}
    request_post = await create_url_post("tanks/achievements", params)
    if not request_post or not request_post.get("data"):
        return TanksAchievementsClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [TanksAchievementsClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [TanksAchievementsClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: TanksAchievementsClass(data) for key, data in request_data.items()}
        return TanksAchievementsClass(request_data)

async def tanks_mastery_async(distribution: str, percentile: int|list, fields: str|list = None, language: str = None, tank_id: int|list = None) -> TanksMasteryClass|dict[str, TanksMasteryClass]|list[TanksMasteryClass]:
    """
    Метод возвращает перцентили распределения значений среднего урона или опыта по каждой единице техники
    Parameters:
        distribution (:obj:`str`): Тип данных. Допустимые значения:
            "damage" — Использовать распределение по урону 
            "xp" — Использовать распределение по опыту
        percentile (:obj:`int` | :obj:`list`): Список перцентилей, который должен быть включен в ответ. Максимальное ограничение: 10. Минимальное значение: 1. Максимальное значение: 100.
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
        tank_id (:obj:`int` | :obj:`list`): Идентификатор техники игрока. Максимальное ограничение: 100.
    """
    params = {'distribution': get_str_in_list(distribution), 'percentile': get_str_in_list(percentile), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language), 'tank_id': get_str_in_list(tank_id)}
    request_post = await create_url_post("tanks/mastery", params)
    if not request_post or not request_post.get("data"):
        return TanksMasteryClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [TanksMasteryClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [TanksMasteryClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: TanksMasteryClass(data) for key, data in request_data.items()}
        return TanksMasteryClass(request_data)

async def clans_list_async(fields: str|list = None, language: str = None, limit: int = None, page_no: int = None, search: str = None) -> ClansListClass|dict[str, ClansListClass]|list[ClansListClass]:
    """
    Метод проводит поиск по кланам и сортирует их в указанном порядке.
    Parameters:
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
        limit (:obj:`int`): Количество возвращаемых записей (может вернуться меньше записей, но не больше 100). Если переданный лимит превышает 100, тогда автоматически выставляется лимит в 100 (по умолчанию).
        page_no (:obj:`int`): Номер страницы. По умолчанию: 1. Минимальное значение: 1.
        search (:obj:`str`): Часть названия или тега клана, по которому осуществляется поиск. Не может быть меньше 2 символов
    """
    params = {'fields': get_str_in_list(fields), 'language': get_str_in_list(language), 'limit': get_str_in_list(limit), 'page_no': get_str_in_list(page_no), 'search': get_str_in_list(search)}
    request_post = await create_url_post("clans/list", params)
    if not request_post or not request_post.get("data"):
        return ClansListClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [ClansListClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [ClansListClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: ClansListClass(data) for key, data in request_data.items()}
        return ClansListClass(request_data)

async def clans_info_async(clan_id: int|list, access_token: str = None, extra: str|list = None, fields: str|list = None, language: str = None, members_key: str = None) -> ClansInfoClass|dict[str, ClansInfoClass]|list[ClansInfoClass]:
    """
    Метод возвращает полную информацию о клане.
    Parameters:
        clan_id (:obj:`int` | :obj:`list`): Идентификатор клана. Максимальное ограничение: 100.
        access_token (:obj:`str`): Ключ доступа к личным данным аккаунта пользователя; можно получить при помощи метода авторизации; действителен в течение определённого времени
        extra (:obj:`str` | :obj:`list`): Список дополнительных полей, которые будут включены в ответ. Допустимые значения:
            "private.online_members"
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
        members_key (:obj:`str`): Данный параметр изменяет тип поля members. Допустимые значения:
            "id" — Поле members в ответе будет содержать associative array c индексацией по account_id
    """
    if not extra:
        extra = ["private.online_members"]
    params = {'clan_id': get_str_in_list(clan_id), 'access_token': get_str_in_list(access_token), 'extra': get_str_in_list(extra), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language), 'members_key': get_str_in_list(members_key)}
    request_post = await create_url_post("clans/info", params)
    if not request_post or not request_post.get("data"):
        return ClansInfoClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [ClansInfoClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [ClansInfoClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: ClansInfoClass(data) for key, data in request_data.items()}
        return ClansInfoClass(request_data)

async def clans_accountinfo_async(account_id: int|list, fields: str|list = None, language: str = None) -> ClansAccountinfoClass|dict[str, ClansAccountinfoClass]|list[ClansAccountinfoClass]:
    """
    Метод возвращает информацию об игроке клана и краткую информацию о клане.
    Parameters:
        account_id (:obj:`int` | :obj:`list`): Идентификатор аккаунта. Максимальное ограничение: 100. Минимальное значение: 1.
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
    """
    params = {'account_id': get_str_in_list(account_id), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language)}
    request_post = await create_url_post("clans/accountinfo", params)
    if not request_post or not request_post.get("data"):
        return ClansAccountinfoClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [ClansAccountinfoClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [ClansAccountinfoClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: ClansAccountinfoClass(data) for key, data in request_data.items()}
        return ClansAccountinfoClass(request_data)

async def clans_glossary_async(fields: str|list = None, language: str = None) -> ClansGlossaryClass|dict[str, ClansGlossaryClass]|list[ClansGlossaryClass]:
    """
    Метод возвращает информацию о клановых сущностях.
    Parameters:
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
    """
    params = {'fields': get_str_in_list(fields), 'language': get_str_in_list(language)}
    request_post = await create_url_post("clans/glossary", params)
    if not request_post or not request_post.get("data"):
        return ClansGlossaryClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [ClansGlossaryClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [ClansGlossaryClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: ClansGlossaryClass(data) for key, data in request_data.items()}
        return ClansGlossaryClass(request_data)

async def clans_messageboard_async(access_token: str, fields: str|list = None) -> ClansMessageboardClass|dict[str, ClansMessageboardClass]|list[ClansMessageboardClass]:
    """
    Метод возвращает сообщения доски объявлений клана.Метод будет отключён. Используйте метод Доска объявлений (World of Tanks)
    Parameters:
        access_token (:obj:`str`): Ключ доступа к личным данным аккаунта пользователя; можно получить при помощи метода авторизации; действителен в течение определённого времени
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
    """
    params = {'access_token': get_str_in_list(access_token), 'fields': get_str_in_list(fields)}
    request_post = await create_url_post("clans/messageboard", params)
    if not request_post or not request_post.get("data"):
        return ClansMessageboardClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [ClansMessageboardClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [ClansMessageboardClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: ClansMessageboardClass(data) for key, data in request_data.items()}
        return ClansMessageboardClass(request_data)

async def clans_memberhistory_async(account_id: int, fields: str|list = None, language: str = None) -> ClansMemberhistoryClass|dict[str, ClansMemberhistoryClass]|list[ClansMemberhistoryClass]:
    """
    Метод возвращает информацию о клановой истории игрока. В ответе присутсвует информация о 10 последних пребываниях в кланах.Метод будет отключён. Используйте метод Клановая история игрока (World of Tanks)
    Parameters:
        account_id (:obj:`int`): Идентификатор аккаунта. Минимальное значение: 1.
        fields (:obj:`str` | :obj:`list`): Поля ответа. Поля разделяются запятыми. Вложенные поля разделяются точками. Для исключения поля используется знак «-» перед названием поля. Если параметр не указан, возвращаются все поля. Максимальное ограничение: 100.
        language (:obj:`str`): Язык локализации. По умолчанию: "ru". Допустимые значения:
            "en" — English 
            "ru" — Русский (используется по умолчанию)
            "pl" — Polski 
            "de" — Deutsch 
            "fr" — Français 
            "es" — Español 
            "zh-cn" — 简体中文 
            "zh-tw" — 繁體中文 
            "tr" — Türkçe 
            "cs" — Čeština 
            "th" — ไทย 
            "vi" — Tiếng Việt 
            "ko" — 한국어
    """
    params = {'account_id': get_str_in_list(account_id), 'fields': get_str_in_list(fields), 'language': get_str_in_list(language)}
    request_post = await create_url_post("clans/memberhistory", params)
    if not request_post or not request_post.get("data"):
        return ClansMemberhistoryClass(request_post.get("data"))
    else:
        request_data = request_post.get("data")
        if isinstance(request_data, list):
            return [ClansMemberhistoryClass(data) for data in request_data]
        if isinstance(request_data, dict):
            for key, data in request_data.items():
                if isinstance(data, list):
                    return {key: [ClansMemberhistoryClass(data_list or {}) for data_list in data or []] for key, data in request_data.items()}
                elif str(key).isnumeric():
                    return {key: ClansMemberhistoryClass(data) for key, data in request_data.items()}
        return ClansMemberhistoryClass(request_data)
