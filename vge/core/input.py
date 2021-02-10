import pygame


class MouseInput:
    mouse_pos = pygame.mouse.get_pos()
    mouse_buttons = pygame.mouse.get_pressed()
    pressed = [0, 0, 0]

    @staticmethod
    def _update():
        MouseInput.mouse_pos = pygame.mouse.get_pos()
        MouseInput.mouse_buttons = pygame.mouse.get_pressed()

        for i in range(3):
            if MouseInput.mouse_buttons[i]:
                MouseInput.pressed[i] += 1
            else:
                MouseInput.pressed[i] = 0
    
    @staticmethod
    def is_pressed(index):
        return MouseInput.pressed[index] > 0
    
    @staticmethod
    def is_released(index):
        return MouseInput.pressed[index] == 0
    
    @staticmethod
    def is_pressed_once(index):
        return MouseInput.pressed[index] == 1
    
    @staticmethod
    def get_pos():
        return MouseInput.mouse_pos
    
    @staticmethod
    def get_x():
        return MouseInput.mouse_pos[0]
    
    @staticmethod
    def get_y():
        return MouseInput.mouse_pos[1]


class Keys:
    KEYS_QUANTITY = 132

    pygame_keys = [
        pygame.K_BACKSPACE,
        pygame.K_TAB,
        pygame.K_CLEAR,
        pygame.K_RETURN,
        pygame.K_PAUSE,
        pygame.K_ESCAPE,
        pygame.K_SPACE,
        pygame.K_EXCLAIM,
        pygame.K_QUOTEDBL,
        pygame.K_HASH,
        pygame.K_DOLLAR,
        pygame.K_AMPERSAND,
        pygame.K_QUOTE,
        pygame.K_LEFTPAREN,
        pygame.K_RIGHTPAREN,
        pygame.K_ASTERISK,
        pygame.K_PLUS,
        pygame.K_COMMA,
        pygame.K_MINUS,
        pygame.K_PERIOD,
        pygame.K_SLASH,
        pygame.K_0,
        pygame.K_1,
        pygame.K_2,
        pygame.K_3,
        pygame.K_4,
        pygame.K_5,
        pygame.K_6,
        pygame.K_7,
        pygame.K_8,
        pygame.K_9,
        pygame.K_COLON,
        pygame.K_SEMICOLON,
        pygame.K_LESS,
        pygame.K_EQUALS,
        pygame.K_GREATER,
        pygame.K_QUESTION,
        pygame.K_AT,
        pygame.K_LEFTPAREN,
        pygame.K_BACKSLASH,
        pygame.K_RIGHTBRACKET,
        pygame.K_CARET,
        pygame.K_UNDERSCORE,
        pygame.K_BACKQUOTE,
        pygame.K_a,
        pygame.K_b,
        pygame.K_c,
        pygame.K_d,
        pygame.K_e,
        pygame.K_f,
        pygame.K_g,
        pygame.K_h,
        pygame.K_i,
        pygame.K_j,
        pygame.K_k,
        pygame.K_l,
        pygame.K_m,
        pygame.K_n,
        pygame.K_o,
        pygame.K_p,
        pygame.K_q,
        pygame.K_r,
        pygame.K_s,
        pygame.K_t,
        pygame.K_u,
        pygame.K_v,
        pygame.K_w,
        pygame.K_x,
        pygame.K_y,
        pygame.K_z,
        pygame.K_DELETE,
        pygame.K_KP0,
        pygame.K_KP1,
        pygame.K_KP2,
        pygame.K_KP3,
        pygame.K_KP4,
        pygame.K_KP5,
        pygame.K_KP6,
        pygame.K_KP7,
        pygame.K_KP8,
        pygame.K_KP9,
        pygame.K_KP_PERIOD,
        pygame.K_KP_DIVIDE,
        pygame.K_KP_MULTIPLY,
        pygame.K_KP_MINUS,
        pygame.K_KP_PLUS,
        pygame.K_KP_ENTER,
        pygame.K_EQUALS,
        pygame.K_UP,
        pygame.K_DOWN,
        pygame.K_RIGHT,
        pygame.K_LEFT,
        pygame.K_INSERT,
        pygame.K_HOME,
        pygame.K_END,
        pygame.K_PAGEUP,
        pygame.K_PAGEDOWN,
        pygame.K_F1,
        pygame.K_F2,
        pygame.K_F3,
        pygame.K_F4,
        pygame.K_F5,
        pygame.K_F6,
        pygame.K_F7,
        pygame.K_F8,
        pygame.K_F9,
        pygame.K_F10,
        pygame.K_F11,
        pygame.K_F12,
        pygame.K_F13,
        pygame.K_F14,
        pygame.K_F15,
        pygame.K_NUMLOCK,
        pygame.K_CAPSLOCK,
        pygame.K_SCROLLOCK,
        pygame.K_RSHIFT,
        pygame.K_LSHIFT,
        pygame.K_RCTRL,
        pygame.K_LCTRL,
        pygame.K_RALT,
        pygame.K_LALT,
        pygame.K_RMETA,
        pygame.K_LMETA,
        pygame.K_LSUPER,
        pygame.K_RSUPER,
        pygame.K_MODE,
        pygame.K_HELP,
        pygame.K_PRINT,
        pygame.K_SYSREQ,
        pygame.K_BREAK,
        pygame.K_MENU,
        pygame.K_POWER,
        pygame.K_EURO
    ]

    K_BACKSPACE = 0
    K_TAB = 1
    K_CLEAR = 2
    K_RETURN = 3
    K_PAUSE = 4
    K_ESCAPE = 5
    K_SPACE = 6
    K_EXCLAIM = 7
    K_QUOTEDBL = 8
    K_HASH = 9
    K_DOLLAR = 10
    K_AMPERSAND = 11
    K_QUOTE = 12
    K_LEFTPAREN = 13
    K_RIGHTPAREN = 14
    K_ASTERISK = 15
    K_PLUS = 16
    K_COMMA = 17
    K_MINUS = 18
    K_PERIOD = 19
    K_SLASH = 20
    K_0 = 21
    K_1 = 22
    K_2 = 23
    K_3 = 24
    K_4 = 25
    K_5 = 26
    K_6 = 27
    K_7 = 28
    K_8 = 29
    K_9 = 30
    K_COLON = 31
    K_SEMICOLON = 32
    K_LESS = 33
    K_EQUALS = 34
    K_GREATER = 35
    K_QUESTION = 36
    K_AT = 37
    K_LEFTBRACKET = 38
    K_BACKSLASH = 39
    K_RIGHTBRACKET = 40
    K_CARET = 41
    K_UNDERSCORE = 42
    K_BACKQUOTE = 43
    K_A = 44
    K_B = 45
    K_C = 46
    K_D = 47
    K_E = 48
    K_F = 49
    K_G = 50
    K_H = 51
    K_I = 52
    K_J = 53
    K_K = 54
    K_L = 55
    K_M = 56
    K_N = 57
    K_O = 58
    K_P = 59
    K_Q = 60
    K_R = 61
    K_S = 62
    K_T = 63
    K_U = 64
    K_V = 65
    K_W = 66
    K_X = 67
    K_Y = 68
    K_Z = 69
    K_DELETE = 70
    K_KP0 = 71
    K_KP1 = 72
    K_KP2 = 73
    K_KP3 = 74
    K_KP4 = 75
    K_KP5 = 76
    K_KP6 = 77
    K_KP7 = 78
    K_KP8 = 79
    K_KP9 = 80
    K_KP_PERIOD = 81
    K_KP_DIVIDE = 82
    K_KP_MULTIPLY = 83
    K_KP_MINUS = 84
    K_KP_PLUS = 85
    K_KP_ENTER = 86
    K_KP_EQUALS = 87
    K_UP = 88
    K_DOWN = 89
    K_RIGHT = 90
    K_LEFT = 91
    K_INSERT = 92
    K_HOME = 93
    K_END = 94
    K_PAGEUP = 95
    K_PAGEDOWN = 96
    K_F1 = 97
    K_F2 = 98
    K_F3 = 99
    K_F4 = 100
    K_F5 = 101
    K_F6 = 102
    K_F7 = 103
    K_F8 = 104
    K_F9 = 105
    K_F10 = 106
    K_F11 = 107
    K_F12 = 108
    K_F13 = 109
    K_F14 = 110
    K_F15 = 111
    K_NUMLOCK = 112
    K_CAPSLOCK = 113
    K_SCROLLOCK = 114
    K_RSHIFT = 115
    K_LSHIFT = 116
    K_RCTRL = 117
    K_LCTRL = 118
    K_RALT = 119
    K_LALT = 120
    K_RMETA = 121
    K_LMETA = 122
    K_LSUPER = 123
    K_RSUPER = 124
    K_MODE = 125
    K_HELP = 126
    K_PRINT = 127
    K_SYSREQ = 128
    K_BREAK = 129
    K_MENU = 130
    K_POWER = 131
    K_EURO = 132


class KeyInput:
    keys = pygame.key.get_pressed()
    keys_count = []

    for i in range(Keys.KEYS_QUANTITY):
        keys_count.append(0)

    @staticmethod
    def _update():
        KeyInput.keys = pygame.key.get_pressed()

        for i in range(Keys.KEYS_QUANTITY):
            if KeyInput.keys[Keys.pygame_keys[i]]:
                KeyInput.keys_count[i] += 1
            else:
                KeyInput.keys_count[i] = 0

    @staticmethod
    def is_pressed(key_index):
        return KeyInput.keys_count[key_index] >= 1
    
    @staticmethod
    def is_pressed_once(key_index):
        return KeyInput.keys_count[key_index] == 1
        
    @staticmethod
    def is_released(key_index):
        return KeyInput.keys_count[key_index] == 0


class EventInput:
    pass
