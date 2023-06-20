# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import division, print_function, unicode_literals

import math

from .lang_EU import Num2Word_EU

GENERIC_DOLLARS = ('dòlar', 'dòlars')
GENERIC_CENTS = ('cent', 'cents')
CURRENCIES_UNA = ('SLL', 'SEK', 'NOK', 'CZK', 'DKK', 'ISK',
                  'SKK', 'GBP', 'CYP', 'EGP', 'FKP', 'GIP',
                  'LBP', 'SDG', 'SHP', 'SSP', 'SYP', 'INR',
                  'IDR', 'LKR', 'MUR', 'NPR', 'PKR', 'SCR',
                  'ESP', 'TRY', 'ITL')
CENTS_UNA = ('EGP', 'JOD', 'LBP', 'SDG', 'SSP', 'SYP')


class Num2Word_CA(Num2Word_EU):
    CURRENCY_FORMS = {
        'EUR': (('euro', 'euros'), ('céntim', 'céntims')),
        'ESP': (('pesseta', 'pessetes'), ('céntim', 'céntims')),
        'USD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'PEN': (('sol', 'sols'), ('céntim', 'céntims')),
        'CRC': (('colón', 'colons'), GENERIC_CENTS),
        'AUD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'CAD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'GBP': (('lliura', 'lliures'), ('penic', 'penics')),
        'RUB': (('ruble', 'rubles'), ('kopeika', 'kopeikas')),
        'SEK': (('corona', 'corones'), ('öre', 'öre')),
        'NOK': (('corona', 'corones'), ('øre', 'øre')),
        'PLN': (('zloty', 'zlots'), ('grosz', 'groszys')),
        'MXN': (('peso', 'pesos'), GENERIC_CENTS),
        'RON': (('leu', 'lei'), ('ban', 'bani')),
        'INR': (('rupia', 'rupies'), ('paisa', 'paisas')),
        'HUF': (('florín', 'florins'), ('fillér', 'fillérs')),
        'FRF': (('franc', 'francs'), ('céntim', 'céntims')),
        'CNY': (('iuan', 'iuans'), ('fen', 'jiaos')),
        'CZK': (('corona', 'corones'), ('hàler', 'hàlers')),
        'NIO': (('córdoba', 'córdobas'), GENERIC_CENTS),
        'VES': (('bolívar', 'bolívares'), ('céntim', 'céntims')),
        'BRL': (('real', 'reals'), GENERIC_CENTS),
        'CHF': (('franc', 'francs'), ('céntim', 'céntims')),
        'JPY': (('ien', 'iens'), ('sen', 'sens')),
        'KRW': (('won', 'wons'), ('jeon', 'jeons')),
        'KPW': (('won', 'wons'), ('chon', 'chons')),
        'TRY': (('lira', 'lires'), ('kuruş', 'kuruşs')),
        'ZAR': (('rand', 'rands'), ('céntim', 'céntims')),
        'KZT': (('tenge', 'tenges'), ('tïïn', 'tïïns')),
        'UAH': (('hrívn', 'hrívnies'), ('kopíi', 'kopíiks')),
        'THB': (('bat', 'bats'), ('satang', 'satangs')),
        'AED': (('dirham', 'dirhams'), ('fils', 'fils')),
        'AFN': (('afgani', 'afganis'), ('pul', 'puls')),
        'ALL': (('lek', 'lekë'), ('qindar', 'qindar')),
        'AMD': (('dram', 'drams'), ('lum', 'lum')),
        'ANG': (('florín', 'florins'), GENERIC_CENTS),
        'AOA': (('kwanza', 'kwanzas'), ('céntim', 'céntims')),
        'AOA': (('kwanza', 'kwanzas'), ('céntimo', 'céntimos')),
        'ARS': (('peso', 'pesos'), GENERIC_CENTS),
        'AWG': (('florí', 'florins'), GENERIC_CENTS),
        'AZN': (('manat', 'manats'), ('qəpik', 'qəpik')),
        'BBD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'BDT': (('taka', 'takas'), ('paisa', 'paisas')),
        'BGN': (('lev', 'leva'), ('stotinka', 'stotinki')),
        'BHD': (('dinar', 'dinars'), ('fils', 'fils')),
        'BIF': (('franc', 'francs'), ('céntim', 'céntims')),
        'BMD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'BND': (GENERIC_DOLLARS, GENERIC_CENTS),
        'BOB': (('bolivià', 'bolivians'), GENERIC_CENTS),
        'BSD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'BTN': (('ngultrum', 'ngultrum'), ('chetrum', 'chetrum')),
        'BWP': (('pula', 'pules'), ('thebe', 'thebes')),
        'BYN': (('ruble', 'rubles'), ('kópek', 'kópeks')),
        'BYR': (('ruble', 'rubles'), ('kópek', 'kópeks')),
        'BZD': (GENERIC_DOLLARS, ('céntim', 'céntims')),
        'CDF': (('franc congolès', 'francs congolesos'), ('céntim', 'céntims')),
        'CLP': (('peso', 'pesos'), GENERIC_CENTS),
        'COP': (('peso', 'pesos'), GENERIC_CENTS),
        'CUP': (('peso', 'pesos'), GENERIC_CENTS),
        'CVE': (('escut', 'escuts'), GENERIC_CENTS),
        'CYP': (('lliura', 'lliures'), ('céntim', 'céntims')),
        'DJF': (('franc de Djibouti', 'francs de Djibouti'), ('céntim', 'céntims')),
        'DKK': (('corona danesa', 'corones daneses'), ('øre', 'øre')),
        'DOP': (('peso', 'pesos'), GENERIC_CENTS),
        'DZD': (('dinar', 'dinars'), ('céntim', 'céntims')),
        'ECS': (('sucre', 'sucres'), GENERIC_CENTS),
        'EGP': (('lliura egípcia', 'lliures egípcies'), ('piastra', 'piastras')),
        'ERN': (('nakfa', 'nakfas'), ('céntim', 'céntims')),
        'ETB': (('birr', 'birrs'), ('céntim', 'céntims')),
        'FJD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'FKP': (('lliura de les illes Malvines', 'lliures de les illes Malvines'), ('penic', 'penics')),
        'GEL': (('lari', 'laris'), ('tetri', 'tetris')),
        'GHS': (('cedi', 'cedis'), ('pesewa', 'pesewas')),
        'GIP': (('lliura de Gibraltar', 'lliures de Gibraltar'), ('penic', 'penics')),
        'GMD': (('dalasi', 'dalasis'), ('butut', 'bututs')),
        'GNF': (('franc guineà', 'francs guineans'), ('céntim', 'céntims')),
        'GTQ': (('quetzal', 'quetzales'), GENERIC_CENTS),
        'GYD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'HKD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'HNL': (('lempira', 'lempires'), GENERIC_CENTS),
        'HRK': (('kuna', 'kunes'), ('lipa', 'lipes')),
        'HTG': (('gourde', 'gourdes'), ('céntim', 'céntims')),
        'IDR': (('rupia indonèsia', 'rupies indonesianes'), ('céntim', 'céntims')),
        'ILS': (('xéquel', 'xéquels'), ('agorà', 'agoròt')),
        'IQD': (('dinar iraquià', 'dinars iraquians'), ('fils', 'fils')),
        'IRR': (('rial iranià', 'rials iranians'), ('dinar', 'dinars')),
        'ISK': (('corona islandesa', 'corones islandeses'), ('eyrir', 'aurar')),
        'ITL': (('lira italiana', 'lires italianes'), ('céntim', 'céntims')),
        'JMD': (GENERIC_DOLLARS, ('céntim', 'céntims')),
        'JOD': (('dinar jordà', 'dinars jordans'), ('piastra', 'piastras')),
        'KES': (('xelín kenyà', 'xelins kenyans'), ('céntim', 'céntims')),
        'KGS': (('som', 'soms'), ('tyiyn', 'tyiyns')),
        'KHR': (('riel cambodjà', 'rieles cambodjans'), ('céntim', 'céntims')),
        'KMF': (('franc de les Comores', 'francs de les Comores'), ('céntim', 'céntims')),
        'KWD': (('dinar kuwaitià', 'dinars kuwaitians'), ('fils', 'fils')),
        'KYD': (GENERIC_DOLLARS, ('céntim', 'céntims')),
        'LAK': (('kip laosià', 'kips laosians'), ('att', 'att')),
        'LBP': (('lliura libanesa', 'lliures libaneses'), ('piastra', 'piastras')),
        'LKR': (('rupia de Sri Lanka', 'rupies de Sri Lanka'), ('céntim', 'céntims')),
        'LRD': (GENERIC_DOLLARS, ('céntim', 'céntims')),
        'LSL': (('loti', 'lotis'), ('céntim', 'céntims')),
        'LTL': (('litas lituana', 'litas lituanesos'), ('céntim', 'céntims')),
        'LVL': (('lat', 'lats'), ('céntimo', 'céntimos')),
        'LYD': (('dinar libi', 'dinars libis'), ('dírham', 'dírhams')),
        'MAD': (('dírham marroquí', 'dírhams marroquins'), ('céntim', 'céntims')),
        'MDL': (('leu moldau', 'lei moldaus'), ('ban', 'bani')),
        'MGA': (('ariary malgaix', 'ariaris malgaixos'), ('iraimbilanja', 'iraimbilanja')),
        'MKD': (('denar macedoni', 'denars macedonis'), ('deni', 'denis')),
        'MMK': (('kiat de Myanmar', 'kiats de Myanmar'), ('pya', 'pyas')),
        'MNT': (('tugrik mongol', 'tugriks mongols'), ('möngö', 'möngö')),
        'MOP': (('pataca de Macau', 'pataques de Macau'), ('avo', 'avos')),
        'MRO': (('ouguiya maurità', 'ouguiyas mauritànes'), ('khoums', 'khoums')),
        'MRU': (('ouguiya maurità', 'ouguiyas mauritànes'), ('khoums', 'khoums')),
        'MUR': (('rupia mauriciana', 'rupies mauricianes'), ('céntim', 'céntims')),
        'MVR': (('rufiyaa de les Maldives', 'rufiyaas de les Maldives'), ('laari', 'laari')),
        'MWK': (('kwacha malawià', 'kwachas malawians'), ('tambala', 'tambalas')),
        'MYR': (('ringgit de Malàisia', 'ringgits de Malàisia'), ('céntim', 'céntims')),
        'MZN': (('metical moçambiquès', 'meticals moçambiquesos'), GENERIC_CENTS),
        'NAD': (GENERIC_DOLLARS, ('céntim', 'céntims')),
        'NGN': (('naira nigerià', 'nairas nigerians'), ('kobo', 'kobo')),
        'NPR': (('rupia nepalesa', 'rupies nepaleses'), ('paisa', 'paisas')),
        'NZD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'OMR': (('rial omanita', 'rials omanites'), ('baisa', 'baisa')),
        'PAB': (('balboa panameny', 'balboes panamenys'), ('centèsim', 'centèsims')),
        'PGK': (('kina de Papua Nova Guinea', 'kines de Papua Nova Guinea'), ('toea', 'toea')),
        'PHP': (('peso filipí', 'pesos filipins'), GENERIC_CENTS),
        'PKR': (('rupia pakistanesa', 'rupies pakistaneses'), ('paisa', 'paisas')),
        'PLZ': (('zlòti polonès', 'zlòtis polonesos'), ('grosz', 'groszys')),
        'PYG': (('guaraní paraguaià', 'guaranís paraguaians'), ('céntim', 'céntims')),
        'QAR': (('rial', 'riales'), ('dírham', 'dírhams')),
        'QTQ': (('quetzal de Guatemala', 'quetzals de Guatemala'), GENERIC_CENTS),
        'RSD': (('dinar serbi', 'dinars serbis'), ('para', 'paras')),
        'RUR': (('rublo rus', 'rublos russos'), ('kopek', 'kopeks')),
        'RWF': (('franc ruandès', 'francs rwandesos'), ('céntim', 'céntims')),
        'SAR': (('rial saudita', 'rials saudites'), ('halala', 'halalas')),
        'SBD': (GENERIC_DOLLARS, ('céntim', 'céntims')),
        'SCR': (('rupia de les Seychelles', 'rupies de les Seychelles'), ('céntim', 'céntims')),
        'SDG': (('lliura sudanesa', 'lliures sudaneses'), ('piastra', 'piastras')),
        'SGD': (GENERIC_DOLLARS, ('céntim', 'céntims')),
        'SHP': (('lliura de Santa Helena', 'lliures de Santa Helena'), ('penic', 'penics')),
        'SKK': (('corona eslovaca', 'corones eslovaques'), ('halier', 'haliers')),
        'SLL': (('leone de Sierra Leone', 'leones de Sierra Leone'), ('céntim', 'céntims')),
        'SRD': (GENERIC_DOLLARS, ('céntim', 'céntims')),
        'SSP': (('lliura sud-sudanesa', 'lliures sud-sudaneses'), ('piastra', 'piastras')),
        'STD': (('dobra de São Tomé i Príncipe', 'dobres de São Tomé i Príncipe'), ('céntim', 'céntims')),
        'SVC': (('colón salvadoreny', 'colons salvadorencs'), GENERIC_CENTS),
        'SYP': (('lliura síria', 'lliures síries'), ('piastra', 'piastras')),
        'SZL': (('lilangeni swazi', 'emalangenis swazis'), ('céntim', 'céntims')),
        'TJS': (('somoni tadjik', 'somonis tadjiks'), ('diram', 'dirams')),
        'TMT': (('manat turcman', 'manats turcmans'), ('tenge', 'tenges')),
        'TND': (('dinar tunisià', 'dinars tunisians'), ('milèsim', 'milèsims')),
        'TOP': (('paanga tongà', 'paangas tongans'), ('céntim', 'céntims')),
        'TTD': (GENERIC_DOLLARS, ('céntim', 'céntims')),
        'TWD': (('nou dòlar de Taiwan', 'nous dòlars de Taiwan'), ('céntim', 'céntims')),
        'TZS': (('xelini tanzà', 'xelins tanzans'), ('céntim', 'céntims')),
        'UAG': (('hryvnia ucraïnesa', 'hryvnias ucraïneses'), ('kopiyka', 'kopiykas')),
        'UGX': (('chelín', 'chelines'), ('céntimo', 'céntimos')),
        'UYU': (('peso uruguaià', 'pesos uruguaians'), ('centèsim', 'centèsims')),
        'UZS': (('sum uzbek', 'sums uzbeks'), ('tiyin', 'tiyins')),
        'VEF': (('bolívar fort veneçolà', 'bolívars forts veneçolans'),
                ('centèsim', 'centèsims')),
        'VND': (('dong vietnamita', 'dongs vietnamites'), ('xu', 'xus')),
        'VUV': (('vatu de Vanuatu', 'vatus de Vanuatu'), ('cap', 'cap')),
        'WST': (('tala samoà', 'tales samoans'), ('centèsim', 'centèsims')),
        'XAF': (('franc CFA BEAC', 'francs CFA BEAC'), ('centèsim', 'centèsims')),
        'XCD': (GENERIC_DOLLARS, ('centèsim', 'centèsims')),
        'XOF': (('franc CFA BCEAO', 'francs CFA BCEAO'), ('centèsim', 'centèsims')),
        'XPF': (('franc CFP', 'francs CFP'), ('centèsim', 'centèsims')),
        'YER': (('rial iemenita', 'rials iemenites'), ('fils', 'fils')),
        'YUM': (('dinar iugoslau', 'dinars iugoslaus'), ('para', 'paras')),
        'ZMW': (('kwacha zambià', 'kwachas zambians'), ('ngwee', 'ngwees')),
        'ZRZ': (('zaire zairià', 'zaires zairians'), ('likuta', 'makuta')),
        'ZWL': (GENERIC_DOLLARS, ('centèsim', 'centèsims')),
        'ZWL': (GENERIC_DOLLARS, ('centèsim', 'centèsims')),
    }

    # //CHECK: Is this sufficient??
    GIGA_SUFFIX = None
    MEGA_SUFFIX = "illó"

    def setup(self):
        lows = ["cuatr", "tr", "b", "m"]
        self.high_numwords = self.gen_high_numwords([], [], lows)
        self.negword = "menys "
        self.pointword = "punt"
        self.errmsg_nonnum = "type(%s) no és [long, int, float]"
        self.errmsg_floatord = "El float %s no pot ser tractat com un ordinal."
        self.errmsg_negord = "El nombre negatiu %s no pot ser tractat com un ordinal."
        self.errmsg_toobig = (
            "abs(%s) ha de ser inferior a %s."
            )
        self.gender_stem = "o"
        self.exclude_title = ["i", "menys", "punt"]
        self.mid_numwords = [(1000, "mil"), (100, "cent"), (90, "noranta"),
                             (80, "vuitanta"), (70, "setanta"), (60, "seixanta"),
                             (50, "cinquanta"), (40, "quaranta"),
                             (30, "trenta")]
        self.low_numwords = ["vint-i-nou", "vint-i-huit", "vint-i-set",
                             "vint-i-sis", "vint-i-cinc", "vint-i-quatre",
                             "vint-i-tres", "vint-i-dos", "vint-i-un",
                             "vint", "dinou", "divuit", "disset",
                             "setze", "quinze", "catorze", "tretze", "dotze",
                             "onze", "deu", "nou", "vuit", "set", "sis",
                             "cinc", "quatre", "tres", "dos", "u", "zero"]
        self.ords = {1: "primer",
                    2: "segon",
                    3: "tercer",
                    4: "quart",
                    5: "cinquè",
                    6: "sisè",
                    7: "setè",
                    8: "vuitè",
                    9: "novè",
                    10: "dècim",
                    20: "vintè",
                    30: "trentè",
                    40: "quarantè",
                    50: "cinquantè",
                    60: "seixantè",
                    70: "setantè",
                    80: "vuitantè",
                    90: "norantè",
                    100: "centèsim",
                    200: "ducentèsim",
                    300: "tricentèsim",
                    400: "cuadrigentèsim",
                    500: "quingentèsim",
                    600: "sexcentèsim",
                    700: "septigentèsim",
                    800: "octigentèsim",
                    900: "noningentèsim",
                    1e3: "milèsim",
                    1e6: "milionèsim",
                    1e9: "billonèsim",
                    1e12: "trillonèsim",
                    1e15: "cuadrillonèsim"}

    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next
        if cnum == 1:
            if nnum < 1000000:
                return next
            ctext = "un"
        elif cnum == 100 and not nnum % 1000 == 0:
            ctext += "t" + self.gender_stem

        if nnum < cnum:
            if cnum < 100:
                return "%s i %s" % (ctext, ntext), cnum + nnum
            return "%s %s" % (ctext, ntext), cnum + nnum
        elif (not nnum % 1000000) and cnum > 1:
            ntext = ntext[:-3] + "lones"

        if nnum == 100:
            if cnum == 5:
                ctext = "quinzen"
                ntext = ""
            elif cnum == 7:
                ctext = "setzè"
            elif cnum == 9:
                ctext = "noven"
            ntext += "t" + self.gender_stem + "s"
        else:
            ntext = " " + ntext

        return (ctext + ntext, cnum * nnum)
    
    def to_ordinal(self, value):
        self.verify_ordinal(value)
        if value == 0:
            text = ""
        elif value <= 10:
            text = "%s%s" % (self.ords[value], self.gender_stem)
        elif value <= 12:
            text = (
                "%s%s%s" % (self.ords[10], self.gender_stem,
                            self.to_ordinal(value - 10))
                    )
        elif value <= 100:
            dec = (value // 10) * 10
            text = (
                "%s%s %s" % (self.ords[dec], self.gender_stem,
                            self.to_ordinal(value - dec))
                    )
        elif value <= 1e3:
            cen = (value // 100) * 100
            text = (
                "%s%s %s" % (self.ords[cen], self.gender_stem,
                            self.to_ordinal(value - cen))
                    )
        elif value < 1e18:
            # Arrodoneix cap avall al múltiple més proper de 1e(3n)
            # dec conté els següents valors:
            # [ 1e3,  1e6): 1e3
            # [ 1e6,  1e9): 1e6
            # [ 1e9, 1e12): 1e9
            # [1e12, 1e15): 1e12
            # [1e15, 1e18): 1e15
            dec = 1000 ** int(math.log(int(value), 1000))

            # Separa les parts abans i després de la paraula 'dec'
            # per exemple, (12, 345) = divmod(12_345, 1_000)
            high_part, low_part = divmod(value, dec)

            cardinal = self.to_cardinal(high_part) if high_part != 1 else ""
            text = (
                "%s%s%s %s" % (cardinal, self.ords[dec], self.gender_stem,
                            self.to_ordinal(low_part))
                    )
        else:
            text = self.to_cardinal(value)
        return text.strip()

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%s%s" % (value, "º" if self.gender_stem == 'o' else "ª")

    def to_currency(self, val, currency='EUR', cents=True, separator=' amb',
                    adjective=False):
        result = super(Num2Word_CA, self).to_currency(
            val, currency=currency, cents=cents, separator=separator,
            adjective=adjective)
        # Gestionar l'excepció: En català és "un euro" i no "un euro",
        # excepte en aquestes monedes, on és "una": lleona, corona,
        # lliura, lira, rupia, lempira, pesseta.
        # El mateix passa amb "vint-i-una", "trenta-i-una"...
        # A més, això s'ha de gestionar per separat per "dòlars" i
        # "centims".
        # Tots els "centims" són masculins excepte: piastre.
        # Font: https://www.rae.es/dpd/una (secció 2.2)

        # Separar la part de "dòlars" de la part de "centims"
        list_result = result.split(separator + " ")

        # PART DE "DÒLARS" (list_result[0])

        # Monedes femenines ("una lliura", "tres-centes lliures"...)
        if currency in CURRENCIES_UNA:

            # "una lliura", "vint-i-una lliures", "trenta-i-una lliures"...
            list_result[0] = list_result[0].replace("un", "una")

            # "dos-centes lliures", "tres-centes lliures"...
            list_result[0] = list_result[0].replace("centos", "centes")

        # Masc.: Ortografia correcta per al cas específic de "vint-i-un":
        list_result[0] = list_result[0].replace("vint-i-un", "vint-i-un")

        # Monedes masculines: cas general ("un euro", "trenta-i-un euros"...)
        list_result[0] = list_result[0].replace("un", "un")

        # PART DE "CENTIMS" (list_result[1])

        # "Centims" femenins ("una piastre", "vint-i-una piastres"...)
        if currency in CENTS_UNA:

            # "una piastre", "vint-i-una piastres", "trenta-i-una piastres"...
            list_result[1] = list_result[1].replace("un", "una")

        # Masc.: Ortografia correcta per al cas específic de "vint-i-un":
        list_result[1] = list_result[1].replace("vint-i-un", "vint-i-un")

        # "Centims" masculins: cas general ("un centim", "trenta-i-un
        # centims"...)
        list_result[1] = list_result[1].replace("un", "un")

        # Reunir la part de "dòlars" amb la part de "centims"
        result = (separator + " ").join(list_result)

        return result
