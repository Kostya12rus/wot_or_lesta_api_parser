class BattlesCountAvgClass:
    def __init__(self, battles_count_avg_data: dict):
        if not battles_count_avg_data: battles_count_avg_data = {}
        self._battles_count_avg: dict = battles_count_avg_data
        self.rank: int = battles_count_avg_data.get('rank', 0)
        self.rank_delta: int = battles_count_avg_data.get('rank_delta', 0)
        self.value: float = battles_count_avg_data.get('value', 0.0)

class BattlesCountAvgDailyClass:
    def __init__(self, battles_count_avg_daily_data: dict):
        if not battles_count_avg_daily_data: battles_count_avg_daily_data = {}
        self._battles_count_avg_daily: dict = battles_count_avg_daily_data
        self.rank: int = battles_count_avg_daily_data.get('rank', 0)
        self.rank_delta: int = battles_count_avg_daily_data.get('rank_delta', 0)
        self.value: float = battles_count_avg_daily_data.get('value', 0.0)

class EfficiencyClass:
    def __init__(self, efficiency_data: dict):
        if not efficiency_data: efficiency_data = {}
        self._efficiency: dict = efficiency_data
        self.rank: int = efficiency_data.get('rank', 0)
        self.rank_delta: int = efficiency_data.get('rank_delta', 0)
        self.value: int = efficiency_data.get('value', 0)

class FbEloRatingClass:
    def __init__(self, fb_elo_rating_data: dict):
        if not fb_elo_rating_data: fb_elo_rating_data = {}
        self._fb_elo_rating: dict = fb_elo_rating_data
        self.rank: int = fb_elo_rating_data.get('rank', 0)
        self.rank_delta: int = fb_elo_rating_data.get('rank_delta', 0)
        self.value: float = fb_elo_rating_data.get('value', 0.0)

class FbEloRating10Class:
    def __init__(self, fb_elo_rating_10_data: dict):
        if not fb_elo_rating_10_data: fb_elo_rating_10_data = {}
        self._fb_elo_rating_10: dict = fb_elo_rating_10_data
        self.rank: int = fb_elo_rating_10_data.get('rank', 0)
        self.rank_delta: int = fb_elo_rating_10_data.get('rank_delta', 0)
        self.value: int = fb_elo_rating_10_data.get('value', 0)

class FbEloRating6Class:
    def __init__(self, fb_elo_rating_6_data: dict):
        if not fb_elo_rating_6_data: fb_elo_rating_6_data = {}
        self._fb_elo_rating_6: dict = fb_elo_rating_6_data
        self.rank: int = fb_elo_rating_6_data.get('rank', 0)
        self.rank_delta: int = fb_elo_rating_6_data.get('rank_delta', 0)
        self.value: int = fb_elo_rating_6_data.get('value', 0)

class FbEloRating8Class:
    def __init__(self, fb_elo_rating_8_data: dict):
        if not fb_elo_rating_8_data: fb_elo_rating_8_data = {}
        self._fb_elo_rating_8: dict = fb_elo_rating_8_data
        self.rank: int = fb_elo_rating_8_data.get('rank', 0)
        self.rank_delta: int = fb_elo_rating_8_data.get('rank_delta', 0)
        self.value: int = fb_elo_rating_8_data.get('value', 0)

class GlobalRatingAvgClass:
    def __init__(self, global_rating_avg_data: dict):
        if not global_rating_avg_data: global_rating_avg_data = {}
        self._global_rating_avg: dict = global_rating_avg_data
        self.rank: int = global_rating_avg_data.get('rank', 0)
        self.rank_delta: int = global_rating_avg_data.get('rank_delta', 0)
        self.value: float = global_rating_avg_data.get('value', 0.0)

class GlobalRatingWeightedAvgClass:
    def __init__(self, global_rating_weighted_avg_data: dict):
        if not global_rating_weighted_avg_data: global_rating_weighted_avg_data = {}
        self._global_rating_weighted_avg: dict = global_rating_weighted_avg_data
        self.rank: int = global_rating_weighted_avg_data.get('rank', 0)
        self.rank_delta: int = global_rating_weighted_avg_data.get('rank_delta', 0)
        self.value: float = global_rating_weighted_avg_data.get('value', 0.0)

class GmEloRatingClass:
    def __init__(self, gm_elo_rating_data: dict):
        if not gm_elo_rating_data: gm_elo_rating_data = {}
        self._gm_elo_rating: dict = gm_elo_rating_data
        self.rank: int = gm_elo_rating_data.get('rank', 0)
        self.rank_delta: int = gm_elo_rating_data.get('rank_delta', 0)
        self.value: float = gm_elo_rating_data.get('value', 0.0)

class GmEloRating10Class:
    def __init__(self, gm_elo_rating_10_data: dict):
        if not gm_elo_rating_10_data: gm_elo_rating_10_data = {}
        self._gm_elo_rating_10: dict = gm_elo_rating_10_data
        self.rank: int = gm_elo_rating_10_data.get('rank', 0)
        self.rank_delta: int = gm_elo_rating_10_data.get('rank_delta', 0)
        self.value: int = gm_elo_rating_10_data.get('value', 0)

class GmEloRating6Class:
    def __init__(self, gm_elo_rating_6_data: dict):
        if not gm_elo_rating_6_data: gm_elo_rating_6_data = {}
        self._gm_elo_rating_6: dict = gm_elo_rating_6_data
        self.rank: int = gm_elo_rating_6_data.get('rank', 0)
        self.rank_delta: int = gm_elo_rating_6_data.get('rank_delta', 0)
        self.value: int = gm_elo_rating_6_data.get('value', 0)

class GmEloRating8Class:
    def __init__(self, gm_elo_rating_8_data: dict):
        if not gm_elo_rating_8_data: gm_elo_rating_8_data = {}
        self._gm_elo_rating_8: dict = gm_elo_rating_8_data
        self.rank: int = gm_elo_rating_8_data.get('rank', 0)
        self.rank_delta: int = gm_elo_rating_8_data.get('rank_delta', 0)
        self.value: int = gm_elo_rating_8_data.get('value', 0)

class RatingFortClass:
    def __init__(self, rating_fort_data: dict):
        if not rating_fort_data: rating_fort_data = {}
        self._rating_fort: dict = rating_fort_data
        self.rank: int = rating_fort_data.get('rank', 0)
        self.rank_delta: int = rating_fort_data.get('rank_delta', 0)
        self.value: float = rating_fort_data.get('value', 0.0)

class V10LAvgClass:
    def __init__(self, v10l_avg_data: dict):
        if not v10l_avg_data: v10l_avg_data = {}
        self._v10l_avg: dict = v10l_avg_data
        self.rank: int = v10l_avg_data.get('rank', 0)
        self.rank_delta: int = v10l_avg_data.get('rank_delta', 0)
        self.value: float = v10l_avg_data.get('value', 0.0)

class WinsRatioAvgClass:
    def __init__(self, wins_ratio_avg_data: dict):
        if not wins_ratio_avg_data: wins_ratio_avg_data = {}
        self._wins_ratio_avg: dict = wins_ratio_avg_data
        self.rank: int = wins_ratio_avg_data.get('rank', 0)
        self.rank_delta: int = wins_ratio_avg_data.get('rank_delta', 0)
        self.value: float = wins_ratio_avg_data.get('value', 0.0)

class ClanratingsClansClass:
    def __init__(self, clanratings_clans_data: dict):
        if not clanratings_clans_data: clanratings_clans_data = {}
        self._clanratings_clans: dict = clanratings_clans_data
        self.clan_id: int = clanratings_clans_data.get('clan_id', 0)
        self.clan_name: str = clanratings_clans_data.get('clan_name', '')
        self.clan_tag: str = clanratings_clans_data.get('clan_tag', '')
        self.exclude_reasons: dict = clanratings_clans_data.get('exclude_reasons', {})

        battles_count_avg_temp: dict = self._clanratings_clans.get('battles_count_avg')
        battles_count_avg_class = None
        if isinstance(battles_count_avg_temp, dict):
            for key in battles_count_avg_temp:
                if str(key).isnumeric():
                    battles_count_avg_class = {key: BattlesCountAvgClass(data) for key, data in battles_count_avg_temp.items()}
                    break
                if key == 'rank' or key == 'rank_delta' or key == 'value':
                    battles_count_avg_class = BattlesCountAvgClass(battles_count_avg_temp)
                    break
        elif isinstance(battles_count_avg_temp, list):
            battles_count_avg_class = [BattlesCountAvgClass(data) for data in battles_count_avg_temp]
        if not battles_count_avg_class:
            battles_count_avg_class: BattlesCountAvgClass = BattlesCountAvgClass(battles_count_avg_temp)
        self.battles_count_avg: BattlesCountAvgClass | list[BattlesCountAvgClass] | dict[str, BattlesCountAvgClass] = battles_count_avg_class
        del battles_count_avg_temp, battles_count_avg_class


        battles_count_avg_daily_temp: dict = self._clanratings_clans.get('battles_count_avg_daily')
        battles_count_avg_daily_class = None
        if isinstance(battles_count_avg_daily_temp, dict):
            for key in battles_count_avg_daily_temp:
                if str(key).isnumeric():
                    battles_count_avg_daily_class = {key: BattlesCountAvgDailyClass(data) for key, data in battles_count_avg_daily_temp.items()}
                    break
                if key == 'rank' or key == 'rank_delta' or key == 'value':
                    battles_count_avg_daily_class = BattlesCountAvgDailyClass(battles_count_avg_daily_temp)
                    break
        elif isinstance(battles_count_avg_daily_temp, list):
            battles_count_avg_daily_class = [BattlesCountAvgDailyClass(data) for data in battles_count_avg_daily_temp]
        if not battles_count_avg_daily_class:
            battles_count_avg_daily_class: BattlesCountAvgDailyClass = BattlesCountAvgDailyClass(battles_count_avg_daily_temp)
        self.battles_count_avg_daily: BattlesCountAvgDailyClass | list[BattlesCountAvgDailyClass] | dict[str, BattlesCountAvgDailyClass] = battles_count_avg_daily_class
        del battles_count_avg_daily_temp, battles_count_avg_daily_class


        efficiency_temp: dict = self._clanratings_clans.get('efficiency')
        efficiency_class = None
        if isinstance(efficiency_temp, dict):
            for key in efficiency_temp:
                if str(key).isnumeric():
                    efficiency_class = {key: EfficiencyClass(data) for key, data in efficiency_temp.items()}
                    break
                if key == 'rank' or key == 'rank_delta' or key == 'value':
                    efficiency_class = EfficiencyClass(efficiency_temp)
                    break
        elif isinstance(efficiency_temp, list):
            efficiency_class = [EfficiencyClass(data) for data in efficiency_temp]
        if not efficiency_class:
            efficiency_class: EfficiencyClass = EfficiencyClass(efficiency_temp)
        self.efficiency: EfficiencyClass | list[EfficiencyClass] | dict[str, EfficiencyClass] = efficiency_class
        del efficiency_temp, efficiency_class


        fb_elo_rating_temp: dict = self._clanratings_clans.get('fb_elo_rating')
        fb_elo_rating_class = None
        if isinstance(fb_elo_rating_temp, dict):
            for key in fb_elo_rating_temp:
                if str(key).isnumeric():
                    fb_elo_rating_class = {key: FbEloRatingClass(data) for key, data in fb_elo_rating_temp.items()}
                    break
                if key == 'rank' or key == 'rank_delta' or key == 'value':
                    fb_elo_rating_class = FbEloRatingClass(fb_elo_rating_temp)
                    break
        elif isinstance(fb_elo_rating_temp, list):
            fb_elo_rating_class = [FbEloRatingClass(data) for data in fb_elo_rating_temp]
        if not fb_elo_rating_class:
            fb_elo_rating_class: FbEloRatingClass = FbEloRatingClass(fb_elo_rating_temp)
        self.fb_elo_rating: FbEloRatingClass | list[FbEloRatingClass] | dict[str, FbEloRatingClass] = fb_elo_rating_class
        del fb_elo_rating_temp, fb_elo_rating_class


        fb_elo_rating_10_temp: dict = self._clanratings_clans.get('fb_elo_rating_10')
        fb_elo_rating_10_class = None
        if isinstance(fb_elo_rating_10_temp, dict):
            for key in fb_elo_rating_10_temp:
                if str(key).isnumeric():
                    fb_elo_rating_10_class = {key: FbEloRating10Class(data) for key, data in fb_elo_rating_10_temp.items()}
                    break
                if key == 'rank' or key == 'rank_delta' or key == 'value':
                    fb_elo_rating_10_class = FbEloRating10Class(fb_elo_rating_10_temp)
                    break
        elif isinstance(fb_elo_rating_10_temp, list):
            fb_elo_rating_10_class = [FbEloRating10Class(data) for data in fb_elo_rating_10_temp]
        if not fb_elo_rating_10_class:
            fb_elo_rating_10_class: FbEloRating10Class = FbEloRating10Class(fb_elo_rating_10_temp)
        self.fb_elo_rating_10: FbEloRating10Class | list[FbEloRating10Class] | dict[str, FbEloRating10Class] = fb_elo_rating_10_class
        del fb_elo_rating_10_temp, fb_elo_rating_10_class


        fb_elo_rating_6_temp: dict = self._clanratings_clans.get('fb_elo_rating_6')
        fb_elo_rating_6_class = None
        if isinstance(fb_elo_rating_6_temp, dict):
            for key in fb_elo_rating_6_temp:
                if str(key).isnumeric():
                    fb_elo_rating_6_class = {key: FbEloRating6Class(data) for key, data in fb_elo_rating_6_temp.items()}
                    break
                if key == 'rank' or key == 'rank_delta' or key == 'value':
                    fb_elo_rating_6_class = FbEloRating6Class(fb_elo_rating_6_temp)
                    break
        elif isinstance(fb_elo_rating_6_temp, list):
            fb_elo_rating_6_class = [FbEloRating6Class(data) for data in fb_elo_rating_6_temp]
        if not fb_elo_rating_6_class:
            fb_elo_rating_6_class: FbEloRating6Class = FbEloRating6Class(fb_elo_rating_6_temp)
        self.fb_elo_rating_6: FbEloRating6Class | list[FbEloRating6Class] | dict[str, FbEloRating6Class] = fb_elo_rating_6_class
        del fb_elo_rating_6_temp, fb_elo_rating_6_class


        fb_elo_rating_8_temp: dict = self._clanratings_clans.get('fb_elo_rating_8')
        fb_elo_rating_8_class = None
        if isinstance(fb_elo_rating_8_temp, dict):
            for key in fb_elo_rating_8_temp:
                if str(key).isnumeric():
                    fb_elo_rating_8_class = {key: FbEloRating8Class(data) for key, data in fb_elo_rating_8_temp.items()}
                    break
                if key == 'rank' or key == 'rank_delta' or key == 'value':
                    fb_elo_rating_8_class = FbEloRating8Class(fb_elo_rating_8_temp)
                    break
        elif isinstance(fb_elo_rating_8_temp, list):
            fb_elo_rating_8_class = [FbEloRating8Class(data) for data in fb_elo_rating_8_temp]
        if not fb_elo_rating_8_class:
            fb_elo_rating_8_class: FbEloRating8Class = FbEloRating8Class(fb_elo_rating_8_temp)
        self.fb_elo_rating_8: FbEloRating8Class | list[FbEloRating8Class] | dict[str, FbEloRating8Class] = fb_elo_rating_8_class
        del fb_elo_rating_8_temp, fb_elo_rating_8_class


        global_rating_avg_temp: dict = self._clanratings_clans.get('global_rating_avg')
        global_rating_avg_class = None
        if isinstance(global_rating_avg_temp, dict):
            for key in global_rating_avg_temp:
                if str(key).isnumeric():
                    global_rating_avg_class = {key: GlobalRatingAvgClass(data) for key, data in global_rating_avg_temp.items()}
                    break
                if key == 'rank' or key == 'rank_delta' or key == 'value':
                    global_rating_avg_class = GlobalRatingAvgClass(global_rating_avg_temp)
                    break
        elif isinstance(global_rating_avg_temp, list):
            global_rating_avg_class = [GlobalRatingAvgClass(data) for data in global_rating_avg_temp]
        if not global_rating_avg_class:
            global_rating_avg_class: GlobalRatingAvgClass = GlobalRatingAvgClass(global_rating_avg_temp)
        self.global_rating_avg: GlobalRatingAvgClass | list[GlobalRatingAvgClass] | dict[str, GlobalRatingAvgClass] = global_rating_avg_class
        del global_rating_avg_temp, global_rating_avg_class


        global_rating_weighted_avg_temp: dict = self._clanratings_clans.get('global_rating_weighted_avg')
        global_rating_weighted_avg_class = None
        if isinstance(global_rating_weighted_avg_temp, dict):
            for key in global_rating_weighted_avg_temp:
                if str(key).isnumeric():
                    global_rating_weighted_avg_class = {key: GlobalRatingWeightedAvgClass(data) for key, data in global_rating_weighted_avg_temp.items()}
                    break
                if key == 'rank' or key == 'rank_delta' or key == 'value':
                    global_rating_weighted_avg_class = GlobalRatingWeightedAvgClass(global_rating_weighted_avg_temp)
                    break
        elif isinstance(global_rating_weighted_avg_temp, list):
            global_rating_weighted_avg_class = [GlobalRatingWeightedAvgClass(data) for data in global_rating_weighted_avg_temp]
        if not global_rating_weighted_avg_class:
            global_rating_weighted_avg_class: GlobalRatingWeightedAvgClass = GlobalRatingWeightedAvgClass(global_rating_weighted_avg_temp)
        self.global_rating_weighted_avg: GlobalRatingWeightedAvgClass | list[GlobalRatingWeightedAvgClass] | dict[str, GlobalRatingWeightedAvgClass] = global_rating_weighted_avg_class
        del global_rating_weighted_avg_temp, global_rating_weighted_avg_class


        gm_elo_rating_temp: dict = self._clanratings_clans.get('gm_elo_rating')
        gm_elo_rating_class = None
        if isinstance(gm_elo_rating_temp, dict):
            for key in gm_elo_rating_temp:
                if str(key).isnumeric():
                    gm_elo_rating_class = {key: GmEloRatingClass(data) for key, data in gm_elo_rating_temp.items()}
                    break
                if key == 'rank' or key == 'rank_delta' or key == 'value':
                    gm_elo_rating_class = GmEloRatingClass(gm_elo_rating_temp)
                    break
        elif isinstance(gm_elo_rating_temp, list):
            gm_elo_rating_class = [GmEloRatingClass(data) for data in gm_elo_rating_temp]
        if not gm_elo_rating_class:
            gm_elo_rating_class: GmEloRatingClass = GmEloRatingClass(gm_elo_rating_temp)
        self.gm_elo_rating: GmEloRatingClass | list[GmEloRatingClass] | dict[str, GmEloRatingClass] = gm_elo_rating_class
        del gm_elo_rating_temp, gm_elo_rating_class


        gm_elo_rating_10_temp: dict = self._clanratings_clans.get('gm_elo_rating_10')
        gm_elo_rating_10_class = None
        if isinstance(gm_elo_rating_10_temp, dict):
            for key in gm_elo_rating_10_temp:
                if str(key).isnumeric():
                    gm_elo_rating_10_class = {key: GmEloRating10Class(data) for key, data in gm_elo_rating_10_temp.items()}
                    break
                if key == 'rank' or key == 'rank_delta' or key == 'value':
                    gm_elo_rating_10_class = GmEloRating10Class(gm_elo_rating_10_temp)
                    break
        elif isinstance(gm_elo_rating_10_temp, list):
            gm_elo_rating_10_class = [GmEloRating10Class(data) for data in gm_elo_rating_10_temp]
        if not gm_elo_rating_10_class:
            gm_elo_rating_10_class: GmEloRating10Class = GmEloRating10Class(gm_elo_rating_10_temp)
        self.gm_elo_rating_10: GmEloRating10Class | list[GmEloRating10Class] | dict[str, GmEloRating10Class] = gm_elo_rating_10_class
        del gm_elo_rating_10_temp, gm_elo_rating_10_class


        gm_elo_rating_6_temp: dict = self._clanratings_clans.get('gm_elo_rating_6')
        gm_elo_rating_6_class = None
        if isinstance(gm_elo_rating_6_temp, dict):
            for key in gm_elo_rating_6_temp:
                if str(key).isnumeric():
                    gm_elo_rating_6_class = {key: GmEloRating6Class(data) for key, data in gm_elo_rating_6_temp.items()}
                    break
                if key == 'rank' or key == 'rank_delta' or key == 'value':
                    gm_elo_rating_6_class = GmEloRating6Class(gm_elo_rating_6_temp)
                    break
        elif isinstance(gm_elo_rating_6_temp, list):
            gm_elo_rating_6_class = [GmEloRating6Class(data) for data in gm_elo_rating_6_temp]
        if not gm_elo_rating_6_class:
            gm_elo_rating_6_class: GmEloRating6Class = GmEloRating6Class(gm_elo_rating_6_temp)
        self.gm_elo_rating_6: GmEloRating6Class | list[GmEloRating6Class] | dict[str, GmEloRating6Class] = gm_elo_rating_6_class
        del gm_elo_rating_6_temp, gm_elo_rating_6_class


        gm_elo_rating_8_temp: dict = self._clanratings_clans.get('gm_elo_rating_8')
        gm_elo_rating_8_class = None
        if isinstance(gm_elo_rating_8_temp, dict):
            for key in gm_elo_rating_8_temp:
                if str(key).isnumeric():
                    gm_elo_rating_8_class = {key: GmEloRating8Class(data) for key, data in gm_elo_rating_8_temp.items()}
                    break
                if key == 'rank' or key == 'rank_delta' or key == 'value':
                    gm_elo_rating_8_class = GmEloRating8Class(gm_elo_rating_8_temp)
                    break
        elif isinstance(gm_elo_rating_8_temp, list):
            gm_elo_rating_8_class = [GmEloRating8Class(data) for data in gm_elo_rating_8_temp]
        if not gm_elo_rating_8_class:
            gm_elo_rating_8_class: GmEloRating8Class = GmEloRating8Class(gm_elo_rating_8_temp)
        self.gm_elo_rating_8: GmEloRating8Class | list[GmEloRating8Class] | dict[str, GmEloRating8Class] = gm_elo_rating_8_class
        del gm_elo_rating_8_temp, gm_elo_rating_8_class


        rating_fort_temp: dict = self._clanratings_clans.get('rating_fort')
        rating_fort_class = None
        if isinstance(rating_fort_temp, dict):
            for key in rating_fort_temp:
                if str(key).isnumeric():
                    rating_fort_class = {key: RatingFortClass(data) for key, data in rating_fort_temp.items()}
                    break
                if key == 'rank' or key == 'rank_delta' or key == 'value':
                    rating_fort_class = RatingFortClass(rating_fort_temp)
                    break
        elif isinstance(rating_fort_temp, list):
            rating_fort_class = [RatingFortClass(data) for data in rating_fort_temp]
        if not rating_fort_class:
            rating_fort_class: RatingFortClass = RatingFortClass(rating_fort_temp)
        self.rating_fort: RatingFortClass | list[RatingFortClass] | dict[str, RatingFortClass] = rating_fort_class
        del rating_fort_temp, rating_fort_class


        v10l_avg_temp: dict = self._clanratings_clans.get('v10l_avg')
        v10l_avg_class = None
        if isinstance(v10l_avg_temp, dict):
            for key in v10l_avg_temp:
                if str(key).isnumeric():
                    v10l_avg_class = {key: V10LAvgClass(data) for key, data in v10l_avg_temp.items()}
                    break
                if key == 'rank' or key == 'rank_delta' or key == 'value':
                    v10l_avg_class = V10LAvgClass(v10l_avg_temp)
                    break
        elif isinstance(v10l_avg_temp, list):
            v10l_avg_class = [V10LAvgClass(data) for data in v10l_avg_temp]
        if not v10l_avg_class:
            v10l_avg_class: V10LAvgClass = V10LAvgClass(v10l_avg_temp)
        self.v10l_avg: V10LAvgClass | list[V10LAvgClass] | dict[str, V10LAvgClass] = v10l_avg_class
        del v10l_avg_temp, v10l_avg_class


        wins_ratio_avg_temp: dict = self._clanratings_clans.get('wins_ratio_avg')
        wins_ratio_avg_class = None
        if isinstance(wins_ratio_avg_temp, dict):
            for key in wins_ratio_avg_temp:
                if str(key).isnumeric():
                    wins_ratio_avg_class = {key: WinsRatioAvgClass(data) for key, data in wins_ratio_avg_temp.items()}
                    break
                if key == 'rank' or key == 'rank_delta' or key == 'value':
                    wins_ratio_avg_class = WinsRatioAvgClass(wins_ratio_avg_temp)
                    break
        elif isinstance(wins_ratio_avg_temp, list):
            wins_ratio_avg_class = [WinsRatioAvgClass(data) for data in wins_ratio_avg_temp]
        if not wins_ratio_avg_class:
            wins_ratio_avg_class: WinsRatioAvgClass = WinsRatioAvgClass(wins_ratio_avg_temp)
        self.wins_ratio_avg: WinsRatioAvgClass | list[WinsRatioAvgClass] | dict[str, WinsRatioAvgClass] = wins_ratio_avg_class
        del wins_ratio_avg_temp, wins_ratio_avg_class


