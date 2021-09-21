# -*- coding: utf-8 -*-
import datetime, pytz
from django.conf import settings as django_settings
from django.utils.translation import ugettext_lazy as _, string_concat
from django.utils import timezone

from magi.default_settings import (
    DEFAULT_ACTIVITY_TAGS,
    DEFAULT_ENABLED_NAVBAR_LISTS,
    DEFAULT_ENABLED_PAGES,
    DEFAULT_NAVBAR_ORDERING,
    DEFAULT_JAVASCRIPT_TRANSLATED_TERMS,
    DEFAULT_GLOBAL_OUTSIDE_PERMISSIONS,
    DEFAULT_LANGUAGES_CANT_SPEAK_ENGLISH,
    DEFAULT_EXTRA_PREFERENCES,
    DEFAULT_HOME_ACTIVITY_TABS,
    DEFAULT_SEASONS,
    DEFAULT_GROUPS,
)
from magi.utils import tourldash
from bang.utils import (
    bangGlobalContext,
    randomArtForCharacter,
    getBackgrounds,
    getHomepageArts,
)
from bang import models

############################################################
# License, game and site settings

SITE_NAME = 'Bandori Party'
SITE_EMOJIS = [u'★', u'🎸', u'🤘']
SITE_IMAGE = 'share/bandori_party.png'
SITE_LOGO = 'logo/bandori_party.png'

GAME_NAME = string_concat(_('BanG Dream!'), ' ', _('Girls Band Party'))
GAME_URL = 'https://bang-dream.bushimo.jp/'

COLOR = '#E40046'
SECONDARY_COLOR = '#F2B141'

LAUNCH_DATE = datetime.datetime(2017, 04, 9, 12, 0, 0, tzinfo=pytz.UTC)

############################################################
# Images

CORNER_POPUP_IMAGE = 'chibi_kanae.png'
ABOUT_PHOTO = 'deby.jpg'
EMPTY_IMAGE = 'stars_with_white.png'
SITE_NAV_LOGO = 'star.png'
SITE_LOGO_WHEN_LOGGED_IN = 'BandoriPartyLogoHorizontal.png'

############################################################
# Settings per languages

SITE_NAME_PER_LANGUAGE = {
    'ja': u'バンドリパーティー',
    'zh-hans': u'Bandori 派对',
    'zh-hant': u'Bandori 派對',
    'kr' : u'밴드리파티',
    'ru': u'бандори парти',
}

SITE_LOGO_PER_LANGUAGE = {
    'ja': 'logo/bandori_party_japanese.png',
    'zh-hans': 'logo/bandori_party_chinese.png',
    'zh-hant': 'logo/bandori_party_taiwanese.png',
    'kr': 'logo/bandori_party_korean.png',
    'ru': 'logo/bandori_party_russian.png',
}

SITE_IMAGE_PER_LANGUAGE = {
    'en': 'share/bandori_party_english.png',
    'ja': 'share/bandori_party_japanese.png',
    'zh-hans': 'share/bandori_party_chinese.png',
    'zh-hant': 'share/bandori_party_taiwanese.png',
    'kr': 'share/bandori_party_korean.png',
    'ru': 'share/bandori_party_russian.png',
}

############################################################
# Contact & Social

CONTACT_EMAIL = 'contact@bandori.party'
CONTACT_REDDIT = 'AmbiBambiii'
CONTACT_FACEBOOK = 'BandoriParty'
CONTACT_DISCORD = 'https://discord.gg/njKRrAg'

FEEDBACK_FORM = 'https://docs.google.com/forms/d/1lfd3x4TX6R1IYrZqhwPN_GqghCQpBLwNkkwro7uBAxI/viewform'
GITHUB_REPOSITORY = ('SchoolIdolTomodachi', 'BanGDream')

TWITTER_HANDLE = 'BandoriParty'
HASHTAGS = [u'バンドリ', u'ガルパ']

############################################################
# Homepage

DONATORS_GOAL = 950

HOMEPAGE_BACKGROUND = 'bg_pattern.png'
HOMEPAGE_ART_GRADIENT = True

HOMEPAGE_ARTS = [{
    'url': 'default_art.png',
}]

HOMEPAGE_ART_SIDE = 'left'
HOMEPAGE_ART_POSITION = {
    'position': 'center right',
    'size': '150%',
    'y': '30%',
    'x': '100%',
}

USERS_BIRTHDAYS_BANNER = 'happy_birthday.png'

GET_BACKGROUNDS = getBackgrounds
GET_HOMEPAGE_ARTS = getHomepageArts
RANDOM_ART_FOR_CHARACTER = randomArtForCharacter

HOME_ACTIVITY_TABS = DEFAULT_HOME_ACTIVITY_TABS.copy()
if 'staffpicks' in HOME_ACTIVITY_TABS:
    del(HOME_ACTIVITY_TABS['staffpicks'])
HOME_ACTIVITY_TABS['top_this_week'] = {
    'title': _('TOP'),
    'icon': 'trophy',
    'form_fields': {
        'ordering': '_cache_total_likes,id',
    },
}

############################################################
# First steps

FIRST_COLLECTION = 'collectiblecard'
GET_STARTED_VIDEO = 'TqL9nSNouhw'

############################################################
# Activities

ACTIVITY_TAGS = [
    # BanG Dream!
    ('anime', lambda: u'{} / {} / {}'.format(
        _('Anime'),
        _('Manga'),
        _('Movie'),
    )),
    ('members', _('Characters')),
    # Girls Band Party
    ('cards', _('Cards')),
    ('scout', _('Scouting')),
    ('event', _('Events')),
    ('live', _('Songs')),
    # Generic
    ('birthday', _('Birthday')),

    # Restricted
    ('communityevent', {
        'translation': _('Community event'),
        'has_permission_to_add': lambda r: r.user.hasPermission('post_community_event_activities'),
    }),

    # Events
    ('RASpreciaton', {
        'translation': 'RASpreciaton 🎧',
        'start_date': datetime.datetime(2021, 6, 15, 0, 0, 0, tzinfo=timezone.utc),
        'end_date': datetime.datetime(2021, 7, 1, 0, 0, 0, tzinfo=timezone.utc),
    }),
    ('PRIDEReady2021', {
        'translation': u'PRIDE Ready! 2021 🏳️‍🌈🏳️‍⚧️',
        'start_date': datetime.datetime(2021, 6, 3, 17, tzinfo=timezone.utc),
        'end_date': datetime.datetime(2021, 6, 10, 17, tzinfo=timezone.utc),
    }),
    ('DaysofBanGDream', {
        'translation': 'DaysofBanGDream!',
        'start_date': datetime.datetime(2021, 3, 10, 0, 0, 0, tzinfo=timezone.utc),
        'end_date': datetime.datetime(2021, 4, 11, 10, 0, 0, tzinfo=timezone.utc),
    }),
    ('StockingStuffingParty', {
        'translation': 'StockingStuffingParty',
        'start_date': datetime.datetime(2020, 12, 12, 0, 0, 0, tzinfo=timezone.utc),
        'end_date': datetime.datetime(2020, 12, 25, 0, 0, 0, tzinfo=timezone.utc),
    }),
    ('BBSChallenge', {
        'translation': 'BBSChallenge',
        'start_date': datetime.datetime(2020, 03, 25, 10, 00, tzinfo=timezone.utc),
        'end_date': datetime.datetime(2020, 04, 19, 10, 00, tzinfo=timezone.utc),
    }),
    ('FanLettersForMyValentine', {
        'translation': 'FanLettersForMyValentine',
        'start_date': datetime.datetime(2020, 02, 10, 10, 00, tzinfo=timezone.utc),
        'end_date': datetime.datetime(2020, 03, 01, 10, 00, tzinfo=timezone.utc),
    }),
    ('petiteidolstudiosummer', {
        'translation': 'PetiteIdolStudioSummer',
        'start_date': datetime.datetime(2018, 8, 1, 13, tzinfo=timezone.utc),
        'end_date': datetime.datetime(2018, 8, 31, 13, tzinfo=timezone.utc),
    }),
    ('changemymindchallenge', {
        'translation': _('Change My Mind Challenge'),
        'start_date': datetime.datetime(2018, 5, 20, tzinfo=timezone.utc),
        'end_date': datetime.datetime(2018, 6, 3, tzinfo=timezone.utc),
    }),
    ('thankyouyurushii', {
        'translation': _('Thank you Yurishii'),
        'start_date': datetime.datetime(2018, 5, 13, tzinfo=timezone.utc),
        'end_date': datetime.datetime(2018, 5, 20, tzinfo=timezone.utc),
    }),
    ('thankyouakesaka', {
        'translation': _('Thank you Ake-san'),
        'start_date': datetime.datetime(2018, 9, 18, tzinfo=timezone.utc),
        'end_date': datetime.datetime(2018, 9, 25, tzinfo=timezone.utc),
    }),
    ('cosparty18', {
        'translation': _('CosParty 2018'),
        'start_date': datetime.datetime(2018, 10, 10, 0, tzinfo=timezone.utc),
        'end_date': datetime.datetime(2018, 11, 15, tzinfo=timezone.utc),
    }),
    ('bandorisnap', {
        'translation': 'Bandori SnaP!',
        'start_date': datetime.datetime(2019, 10, 2, 13, tzinfo=timezone.utc),
        'end_date': datetime.datetime(2019, 11, 10, tzinfo=timezone.utc),
    }),
] + DEFAULT_ACTIVITY_TAGS

############################################################
# User preferences and profiles

CUSTOM_PREFERENCES_FORM = True

EXTRA_PREFERENCES = DEFAULT_EXTRA_PREFERENCES + [
    ('i_favorite_band', lambda: _('Favorite {thing}').format(thing=_('Band').lower())),
]

FAVORITE_CHARACTERS_MODEL = models.Member

USER_COLORS = [
    ('power', _('Power'), 'Power', '#FF2D54'),
    ('cool', _('Cool'), 'Cool', '#4057E3'),
    ('pure', _('Pure'), 'Pure', '#44C527'),
    ('happy', _('Happy'), 'Happy', '#FF8400'),
]

ACCOUNT_TAB_ORDERING = ['about', 'collectiblecard', 'eventparticipation', 'playedsong', 'item', 'areaitem']

############################################################
# Technical settings

SITE_URL = 'https://bandori.party/'
SITE_STATIC_URL = '//i.bandori.party/'

GET_GLOBAL_CONTEXT = bangGlobalContext
ACCOUNT_MODEL = models.Account

DISQUS_SHORTNAME = 'bangdream'
GOOGLE_ANALYTICS = 'UA-96550529-1'

JAVASCRIPT_TRANSLATED_TERMS = DEFAULT_JAVASCRIPT_TRANSLATED_TERMS + [
    u'Coming soon',
    u'Open {thing}',
]

############################################################
# Customize pages

ENABLED_PAGES = DEFAULT_ENABLED_PAGES

ENABLED_PAGES['wiki'][0]['enabled'] = True
ENABLED_PAGES['wiki'][1]['enabled'] = True
ENABLED_PAGES['wiki'][0]['divider_before'] = True
ENABLED_PAGES['wiki'][0]['navbar_link_list'] = 'girlsbandparty'

ENABLED_PAGES['map']['share_image'] = 'screenshots/map.png'
ENABLED_PAGES['map']['navbar_link_list'] = 'community'

ENABLED_PAGES['settings']['custom'] = True

ENABLED_PAGES['discord'] = {
    'title': 'Discord',
    'icon': 'chat',
    'navbar_link_list': 'community',
    'redirect': 'https://discord.gg/njKRrAg',
    'new_tab': True,
    'check_permissions': lambda c: c['request'].LANGUAGE_CODE not in DEFAULT_LANGUAGES_CANT_SPEAK_ENGLISH,
}

ENABLED_PAGES['twitter'] = {
    'title': 'Twitter',
    'icon': 'twitter',
    'navbar_link_list': 'community',
    'redirect': 'https://twitter.com/bandoriparty',
    'new_tab': True,
    'check_permissions': lambda c: c['request'].LANGUAGE_CODE not in DEFAULT_LANGUAGES_CANT_SPEAK_ENGLISH,
}

ENABLED_PAGES['instagram'] = {
    'title': 'Instagram',
    'icon': 'pictures',
    'navbar_link_list': 'community',
    'redirect': 'https://instagram.com/BandoriParty',
    'new_tab': True,
    'check_permissions': lambda c: c['request'].LANGUAGE_CODE not in DEFAULT_LANGUAGES_CANT_SPEAK_ENGLISH,
}

ENABLED_PAGES['donate'] = {
    'title': _('Donate'),
    'icon': 'heart',
    'navbar_link_list': 'more',
    'redirect': '/donate/',
}

ENABLED_PAGES['teambuilder'] = {
    'title': _('Team builder'),
    'icon': 'settings',
    'navbar_link': False,
    'authentication_required': True,
    'as_sidebar': True,
    'show_title': True,
    #'navbar_link_list': 'girlsbandparty',
}

ENABLED_PAGES['gallery'] = {
    'title': _('Gallery'),
    'icon': 'pictures',
    'navbar_link_list': 'girlsbandparty',
    'page_description': lambda: u'{} - {}'.format(_('Gallery of {license} images').format(
        license=unicode(GAME_NAME)), u', '.join(
            [unicode(_d['translation']) for _d in models.Asset.TYPES.values()])),
}

ENABLED_PAGES['officialart'] = {
    'title': lambda _c: _('{things} list').format(things=_('Official art')),
    'icon': 'pictures',
    'navbar_link_list': 'bangdream',
    'redirect': '/assets/officialart/',
    'divider_before': True,
}

ENABLED_PAGES['comics'] = {
    'title': lambda _c: _('{things} list').format(things=_('Comics')),
    'icon': 'album',
    'navbar_link_list': 'bangdream',
    'redirect': '/assets/comic/',
}

ENABLED_PAGES['add_rerun'] = {
    'title': u'Add {} rerun dates'.format(u'/'.join(models.Rerun.ITEMS)),
    'staff_required': True,
    'permissions_required': ['manage_main_items'],
    'icon': 'date',
    'navbar_link_list': 'staff',
    'redirect': '/rerun/add/',
}

ENABLED_PAGES['generate_giveaway_discord_messages'] = {
    'title': 'Giveaway Discord messages',
    'navbar_link_list': 'staff',
    'icon': 'developer',
    'permissions_required': ['generate_giveaway_discord_messages'],
    'show_title': True,
}

############################################################
# Customize nav bar

ENABLED_NAVBAR_LISTS = DEFAULT_ENABLED_NAVBAR_LISTS
ENABLED_NAVBAR_LISTS['bangdream'] = {
    'title': _('BanG Dream!'),
    'image': 'BanGDream',
    'order': ['member_list', 'song_list', 'officialart', 'comics'],
}
ENABLED_NAVBAR_LISTS['girlsbandparty'] = {
    'title': _('Girls Band Party'),
    'image': 'GirlsBandParty',
    'order': [
        'card_list', 'cards_quickadd', 'costume_list',
        'event_list', 'gacha_list',
        'item_list', 'area_list',
        'wiki', 'gallery', 'teambuilder',
    ],
}
ENABLED_NAVBAR_LISTS['community'] = {
    'title': _('Community'),
    'icon': 'users',
    'order': ['activity_list', 'account_list', 'map', 'donate_list', 'discord', 'twitter', 'instagram'],
}
ENABLED_NAVBAR_LISTS['more']['order'] = ENABLED_NAVBAR_LISTS['more']['order'] + ['donate']

NAVBAR_ORDERING = ['card_list', 'member_list', 'song_list', 'events', 'community'] + DEFAULT_NAVBAR_ORDERING

############################################################
# Seasons

SEASONS = DEFAULT_SEASONS.copy()

# Christmas

SEASONS['christmas'].update({
    'accent_color': SECONDARY_COLOR,
    'site_logo': 'logo/bandori_party_christmas.png',
    'site_nav_logo': 'star_christmas.png',
    'to_random_homepage_art': 'getRandomChristmasArt',
    'to_random_homepage_background': 'getRandomChristmasBackground',
})

# April fools

SEASONS['aprilfools'].update({
    'color': '#b297ce',
    'secondary_color': '#95e7e1',
    'accent_color': SECONDARY_COLOR,
})

SEASONS['aprilfools']['js_variables']['aprilfools_configuration'].update({
    'startImage': 'https://i.imgur.com/cVPYABX.png',
    'startBubbleText': 'Kanae? Who\'s  that? We don\'t know who you\'re talking about 😈<br><br><p>We are</p><img src="https://i.imgur.com/tO7ih1A.png" alt="RAISE A SUILEN" class="img-responsive" /><p> and we\'re taking over this community today.</p>',
    'bubbleColor': '#b297ce',
    'startText': '<quote class="fontx1-5">Looks like Kanae is in trouble 😰<br><br>If you want to save Bandori Party, you\'ll have  to find all the <img src="https://i.imgur.com/iqrWQGK.png" alt="cat headphones" /> of RAISE A SUILEN hidden around the website.<br><br>If you manage to finish before the end of April 1st, you\'ll earn a badge! 🏅</quote>',
    'startButton': 'Find all the <img src="https://i.imgur.com/rNwhPvb.png" alt="cat headphones" />',
    'items': [
        u'https://i.imgur.com/iqrWQGK.png',
        u'https://i.imgur.com/SCtXgEI.png',
        u'https://i.imgur.com/GOC3gHT.png',
    ],
    'endBubbleText': u'Thank you so much!<br>You saved me!',
    'endText': 'You gave all the <img src="https://i.imgur.com/iqrWQGK.png" alt="cat hearphones"> you collected to RAISE A SUILEN, so they freed Kanae 🎉<br><br><div class="alert alert-warning">Don\'t know who Kanae is?<br><a href="/about/">→ Read more about her!</a></div>',
    'endImage': 'https://i.bandori.party/static/img/chibi_kanae.png',
    'itemSize': '35px',
})

SEASONS['aprilfools']['js_variables']['aprilfools_configuration']['hiddenAfterDivs'] += [
    ['[data-item="asset"] h3', 'You can download official images and other assets on BanPa~'],
    ['body.current-gallery figure', 'Check out our gallery of images!'],
    ['[data-item="gacha"] div', 'Have you checked gachas?'],
    ['[data-item="event"] div', 'Have you checked events?'],
    ['[data-item="song"] div', 'Have you checked the songs?'],
    ['[data-item="item"] div', 'Have you checked the items?'],
    ['[data-item="areaitem"] div', 'Have you checked the area items?'],
    ['[data-item="area"] h5', 'The gallery includes areas! Nice~'],
    ['[for="id_i_attribute"]', 'Look for cards by attribute!'],
    ['[for="id_gacha_type"]', 'Try to filter for gacha cards!'],
    ['.card-wrapper', 'Have you checked the cards?'],
    ['.col-xs-2[data-item="card"] .icon-card', 'Try to quick add cards!'],
    ['.area_see_all', 'The gallery includes areas! Yay~'],
    ['[for="id_status"]', 'You can filter events by version!'],
    ['[for="id_i_boost_stat"]', 'Try to filter events "Challenge Live"!'],
]
SEASONS['aprilfools']['extra']['badge_image'] = 'https://i.bandori.party/u/badges/15April-Fools-2019-Knight-E7MPPt.png'

# Pride month

SEASONS['pride'].update({
    'site_logo': 'bandori_party_pride.png',
    'site_logo_when_logged_in': 'bandori_party_pride_horizontal.png',
    'site_nav_logo': 'pride_star.png',
    'to_random_homepage_art': 'getRandomPrideArt',
    'to_random_homepage_background': 'getRandomPrideBackground',
})

############################################################
# Groups

GROUPS = DEFAULT_GROUPS

# Add permissions

for _name, _details in GROUPS:
    if _name in ['manager', 'discord', 'entertainer']:
        if 'permissions' not in _details:
            _details['permissions'] = []
        _details['permissions'].append('generate_giveaway_discord_messages')

# Add Graphic designer - Manager role

_HDESIGN = dict(GROUPS)['design'].copy()
_HDESIGN.update({
    'translation': string_concat(_('Graphic designer'), ' - ', _('Manager')),
    'requires_staff': True,
    'permissions': [
        'access_site_before_launch',
        'beta_test_features',
        'upload_custom_2x',
        'upload_custom_thumbnails',
    ],
})
GROUPS.append(('hdesign', _HDESIGN))
