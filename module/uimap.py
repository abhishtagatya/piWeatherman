# This is where all the colors are mapped in the GUI

# CLEAR
CLEAR_DAY = '#F6D347'
CLEAR_DAY_ACCENT = '#FBAE3C'
CLEAR_NIGHT = '#020A21'
CLEAR_NIGHT_ACCENT = '#00060D'

# SEMI CLOUDY
SEMI_CLOUDY_DAY = '#73B0F0'
SEMI_CLOUDY_DAY_ACCENT = '#67C7D7'
SEMI_CLOUDY_NIGHT = '#465C7C'
SEMI_CLOUDY_NIGHT_ACCENT = '#3E5865'

# CLOUDY
CLOUDY_DAY = '#6CA4E8'
CLOUDY_DAY_ACCENT = '#5AA9D4'
CLOUDY_NIGHT = '#253569'
CLOUDY_NIGHT_ACCENT = '#1E2B58'

# BROKEN CLOUDS
BROKEN_CLOUDY_DAY = '#4D85B9'
BROKEN_CLOUDY_DAY_ACCENT = '#8BBDFD'
BROKEN_CLOUDY_NIGHT = '#121A33'
BROKEN_CLOUDY_NIGHT_ACCENT = '#0A131F'

# RAIN
RAIN_DAY = '#4E6881'
RAIN_DAY_ACCENT = '#2F3F4E'
RAIN_NIGHT = '#283542'
RAIN_NIGHT_ACCENT = '#171F26'

# THUNDERSTORM
THUNDERSTORM_DAY = '#2D3656'
THUNDERSTORM_DAY_ACCENT = '#1E243A'
THUNDERSTORM_NIGHT = '#232A42'
THUNDERSTORM_NIGHT_ACCENT = '#141826'

# SNOW
SNOW_DAY = '#A3B1BC'
SNOW_DAY_ACCENT = '#8B97A0'
SNOW_NIGHT = '#42484C'
SNOW_NIGHT_ACCENT = '#2A2E30'

# MIST
MIST_DAY = '#E1E1D6'
MIST_DAY_ACCENT = '#C5C5BB'
MIST_NIGHT = '#565656'
MIST_NIGHT_ACCENT = '#3A3A3A'

# OTHERS
WHITE = '#FFF'
BLACK = '#000'

ui_map = {
    'foreground' : WHITE,
    'clear sky' : {
        'day' : {
            'background' : CLEAR_DAY,
            'accent' : CLEAR_DAY_ACCENT,
            'image' : 'assets/image/sun.png'
        },
        'night' : {
            'background' : CLEAR_NIGHT,
            'accent' : CLEAR_NIGHT_ACCENT,
            'image' : 'assets/image/moon.png'
        }
    },
    'few clouds' : {
        'day' : {
            'background' : SEMI_CLOUDY_DAY,
            'accent' : SEMI_CLOUDY_DAY_ACCENT,
            'image' : 'assets/image/semicloudday.png'
        },
        'night' : {
            'background' : SEMI_CLOUDY_NIGHT,
            'accent' : SEMI_CLOUDY_NIGHT_ACCENT,
            'image' : 'assets/image/semicloudnight.png'
        }
    },
    'scattered clouds' : {
        'day' : {
            'background' : CLOUDY_DAY,
            'accent' : CLOUDY_DAY_ACCENT,
            'image' : 'assets/image/cloud.png'
        },
        'night' : {
            'background' : CLOUDY_NIGHT,
            'accent' : CLOUDY_NIGHT_ACCENT,
            'image' : 'assets/image/cloud.png'
        }
    },
    'broken clouds' : {
        'day' : {
            'background' : BROKEN_CLOUDY_DAY,
            'accent' : BROKEN_CLOUDY_DAY_ACCENT,
            'image' : 'assets/image/brokencloud.png'
        },
        'night' : {
            'background' : BROKEN_CLOUDY_NIGHT,
            'accent' : BROKEN_CLOUDY_NIGHT_ACCENT,
            'image' : 'assets/image/brokencloud.png'
        }
    },
    'shower rain' : {
        'day' : {
            'background' : RAIN_DAY,
            'accent_color' : RAIN_DAY_ACCENT,
            'image' : 'assets/image/rain.png'
        },
        'night' : {
            'background' : RAIN_NIGHT,
            'accent' : RAIN_NIGHT_ACCENT,
            'image' : 'assets/image/rain.png'
        }
    },
    'rain' : {
        'day' : {
            'background' : CLOUDY_DAY,
            'accent' : CLOUDY_DAY_ACCENT,
            'image' : 'assets/image/rain.png'
        },
        'night' : {
            'background' : CLOUDY_NIGHT,
            'accent' : CLOUDY_NIGHT_ACCENT,
            'image' : 'assets/image/rain.png'
        }
    },
    'thunderstorm' : {
        'day' : {
            'background' : THUNDERSTORM_DAY,
            'accent' : THUNDERSTORM_DAY_ACCENT,
            'image' : 'assets/image/rain.png'
        },
        'night' : {
            'background' : THUNDERSTORM_NIGHT,
            'accent' : THUNDERSTORM_NIGHT_ACCENT,
            'image' : 'assets/image/rain.png'
        }
    },
    'snow' : {
        'day' : {
            'background' : SNOW_DAY,
            'accent' : SNOW_DAY_ACCENT,
            'image' : 'assets/image/rain.png'
        },
        'night' : {
            'background' : SNOW_NIGHT,
            'accent' : SNOW_NIGHT_ACCENT,
            'image' : 'assets/image/rain.png'
        }
    },
    'mist' : {
        'day' : {
            'background' : MIST_DAY,
            'accent' : MIST_DAY_ACCENT,
            'image' : 'assets/image/rain.png'
        },
        'night' : {
            'background' : MIST_NIGHT,
            'accent' : MIST_NIGHT_ACCENT,
            'image' : 'assets/image/rain.png'
        }
    }
}


# This maps the code ranges
weather_code_range = [
    (range(200,233), 'thunderstorm'),
    (range(300, 322), 'shower rain'),
    (range(500, 532), 'rain'),
    (range(600, 622), 'snow'),
    (range(701,782), 'mist'),
    ([800], 'clear sky'),
    ([801], 'few clouds'),
    ([802], 'scattered clouds'),
    ([803,804], 'broken clouds')
]
