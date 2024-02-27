[
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:113:45",
    "name": "TTF_Linked_Version",
    "ns": 0,
    "parameters": [],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_version"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:128:30",
    "name": "TTF_GetFreeTypeVersion",
    "ns": 0,
    "parameters": [
      {
        "name": "major",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      },
      {
        "name": "minor",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      },
      {
        "name": "patch",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      }
    ],
    "return-type": {
      "tag": ":void"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:141:30",
    "name": "TTF_GetHarfBuzzVersion",
    "ns": 0,
    "parameters": [
      {
        "name": "major",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      },
      {
        "name": "minor",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      },
      {
        "name": "patch",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      }
    ],
    "return-type": {
      "tag": ":void"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:159:30",
    "name": "TTF_ByteSwappedUNICODE",
    "ns": 0,
    "parameters": [
      {
        "name": "swapped",
        "tag": "parameter",
        "type": {
          "tag": "SDL_bool"
        }
      }
    ],
    "return-type": {
      "tag": ":void"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "bit-alignment": 0,
    "bit-size": 0,
    "fields": [],
    "id": 0,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:164:16",
    "name": "_TTF_Font",
    "ns": 0,
    "tag": "struct"
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:164:26",
    "name": "TTF_Font",
    "ns": 0,
    "tag": "typedef",
    "type": {
      "bit-alignment": 0,
      "bit-size": 0,
      "fields": [],
      "id": 0,
      "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:164:16",
      "name": "_TTF_Font",
      "ns": 0,
      "tag": "struct"
    }
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:186:29",
    "name": "TTF_Init",
    "ns": 0,
    "parameters": [],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:205:36",
    "name": "TTF_OpenFont",
    "ns": 0,
    "parameters": [
      {
        "name": "file",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "ptsize",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "TTF_Font"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:229:36",
    "name": "TTF_OpenFontIndex",
    "ns": 0,
    "parameters": [
      {
        "name": "file",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "ptsize",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      },
      {
        "name": "index",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":long"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "TTF_Font"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:254:36",
    "name": "TTF_OpenFontRW",
    "ns": 0,
    "parameters": [
      {
        "name": "src",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "SDL_RWops"
          }
        }
      },
      {
        "name": "freesrc",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      },
      {
        "name": "ptsize",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "TTF_Font"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:284:36",
    "name": "TTF_OpenFontIndexRW",
    "ns": 0,
    "parameters": [
      {
        "name": "src",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "SDL_RWops"
          }
        }
      },
      {
        "name": "freesrc",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      },
      {
        "name": "ptsize",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      },
      {
        "name": "index",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":long"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "TTF_Font"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:307:36",
    "name": "TTF_OpenFontDPI",
    "ns": 0,
    "parameters": [
      {
        "name": "file",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "ptsize",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      },
      {
        "name": "hdpi",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":unsigned-int"
        }
      },
      {
        "name": "vdpi",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":unsigned-int"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "TTF_Font"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:335:36",
    "name": "TTF_OpenFontIndexDPI",
    "ns": 0,
    "parameters": [
      {
        "name": "file",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "ptsize",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      },
      {
        "name": "index",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":long"
        }
      },
      {
        "name": "hdpi",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":unsigned-int"
        }
      },
      {
        "name": "vdpi",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":unsigned-int"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "TTF_Font"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:364:36",
    "name": "TTF_OpenFontDPIRW",
    "ns": 0,
    "parameters": [
      {
        "name": "src",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "SDL_RWops"
          }
        }
      },
      {
        "name": "freesrc",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      },
      {
        "name": "ptsize",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      },
      {
        "name": "hdpi",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":unsigned-int"
        }
      },
      {
        "name": "vdpi",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":unsigned-int"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "TTF_Font"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:398:36",
    "name": "TTF_OpenFontIndexDPIRW",
    "ns": 0,
    "parameters": [
      {
        "name": "src",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "SDL_RWops"
          }
        }
      },
      {
        "name": "freesrc",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      },
      {
        "name": "ptsize",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      },
      {
        "name": "index",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":long"
        }
      },
      {
        "name": "hdpi",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":unsigned-int"
        }
      },
      {
        "name": "vdpi",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":unsigned-int"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "TTF_Font"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:411:29",
    "name": "TTF_SetFontSize",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "ptsize",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:426:29",
    "name": "TTF_SetFontSizeDPI",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "ptsize",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      },
      {
        "name": "hdpi",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":unsigned-int"
        }
      },
      {
        "name": "vdpi",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":unsigned-int"
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:455:29",
    "name": "TTF_GetFontStyle",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:477:30",
    "name": "TTF_SetFontStyle",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "style",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      }
    ],
    "return-type": {
      "tag": ":void"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:489:29",
    "name": "TTF_GetFontOutline",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:501:30",
    "name": "TTF_SetFontOutline",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "outline",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      }
    ],
    "return-type": {
      "tag": ":void"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:531:29",
    "name": "TTF_GetFontHinting",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:553:30",
    "name": "TTF_SetFontHinting",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "hinting",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      }
    ],
    "return-type": {
      "tag": ":void"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:578:29",
    "name": "TTF_GetFontWrappedAlign",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:596:30",
    "name": "TTF_SetFontWrappedAlign",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "align",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      }
    ],
    "return-type": {
      "tag": ":void"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:608:29",
    "name": "TTF_FontHeight",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:620:29",
    "name": "TTF_FontAscent",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:632:29",
    "name": "TTF_FontDescent",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:642:29",
    "name": "TTF_FontLineSkip",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:652:29",
    "name": "TTF_GetFontKerning",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:667:30",
    "name": "TTF_SetFontKerning",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "allowed",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      }
    ],
    "return-type": {
      "tag": ":void"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:677:30",
    "name": "TTF_FontFaces",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:693:29",
    "name": "TTF_FontFaceIsFixedWidth",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:709:38",
    "name": "TTF_FontFaceFamilyName",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "bit-alignment": 8,
        "bit-size": 8,
        "tag": ":char"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:725:38",
    "name": "TTF_FontFaceStyleName",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "bit-alignment": 8,
        "bit-size": 8,
        "tag": ":char"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:747:29",
    "name": "TTF_GlyphIsProvided",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "ch",
        "tag": "parameter",
        "type": {
          "tag": "Uint16"
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:763:29",
    "name": "TTF_GlyphIsProvided32",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "ch",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:788:29",
    "name": "TTF_GlyphMetrics",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "ch",
        "tag": "parameter",
        "type": {
          "tag": "Uint16"
        }
      },
      {
        "name": "minx",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      },
      {
        "name": "maxx",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      },
      {
        "name": "miny",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      },
      {
        "name": "maxy",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      },
      {
        "name": "advance",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:809:29",
    "name": "TTF_GlyphMetrics32",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "ch",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      },
      {
        "name": "minx",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      },
      {
        "name": "maxx",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      },
      {
        "name": "miny",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      },
      {
        "name": "maxy",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      },
      {
        "name": "advance",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:837:29",
    "name": "TTF_SizeText",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "w",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      },
      {
        "name": "h",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:857:29",
    "name": "TTF_SizeUTF8",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "w",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      },
      {
        "name": "h",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:882:29",
    "name": "TTF_SizeUNICODE",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "Uint16"
          }
        }
      },
      {
        "name": "w",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      },
      {
        "name": "h",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:911:29",
    "name": "TTF_MeasureText",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "measure_width",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      },
      {
        "name": "extent",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      },
      {
        "name": "count",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:935:29",
    "name": "TTF_MeasureUTF8",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "measure_width",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      },
      {
        "name": "extent",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      },
      {
        "name": "count",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:964:29",
    "name": "TTF_MeasureUNICODE",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "Uint16"
          }
        }
      },
      {
        "name": "measure_width",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      },
      {
        "name": "extent",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      },
      {
        "name": "count",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:998:39",
    "name": "TTF_RenderText_Solid",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1029:39",
    "name": "TTF_RenderUTF8_Solid",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1063:39",
    "name": "TTF_RenderUNICODE_Solid",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "Uint16"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1096:39",
    "name": "TTF_RenderText_Solid_Wrapped",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "wrapLength",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1125:39",
    "name": "TTF_RenderUTF8_Solid_Wrapped",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "wrapLength",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1158:39",
    "name": "TTF_RenderUNICODE_Solid_Wrapped",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "Uint16"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "wrapLength",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1192:39",
    "name": "TTF_RenderGlyph_Solid",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "ch",
        "tag": "parameter",
        "type": {
          "tag": "Uint16"
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1224:39",
    "name": "TTF_RenderGlyph32_Solid",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "ch",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1260:39",
    "name": "TTF_RenderText_Shaded",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "bg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1290:39",
    "name": "TTF_RenderUTF8_Shaded",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "bg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1325:39",
    "name": "TTF_RenderUNICODE_Shaded",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "Uint16"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "bg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1359:39",
    "name": "TTF_RenderText_Shaded_Wrapped",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "bg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "wrapLength",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1389:39",
    "name": "TTF_RenderUTF8_Shaded_Wrapped",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "bg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "wrapLength",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1423:39",
    "name": "TTF_RenderUNICODE_Shaded_Wrapped",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "Uint16"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "bg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "wrapLength",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1458:39",
    "name": "TTF_RenderGlyph_Shaded",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "ch",
        "tag": "parameter",
        "type": {
          "tag": "Uint16"
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "bg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1491:39",
    "name": "TTF_RenderGlyph32_Shaded",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "ch",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "bg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1526:39",
    "name": "TTF_RenderText_Blended",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1555:39",
    "name": "TTF_RenderUTF8_Blended",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1589:39",
    "name": "TTF_RenderUNICODE_Blended",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "Uint16"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1622:39",
    "name": "TTF_RenderText_Blended_Wrapped",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "wrapLength",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1651:39",
    "name": "TTF_RenderUTF8_Blended_Wrapped",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "wrapLength",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1684:39",
    "name": "TTF_RenderUNICODE_Blended_Wrapped",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "Uint16"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "wrapLength",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1718:39",
    "name": "TTF_RenderGlyph_Blended",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "ch",
        "tag": "parameter",
        "type": {
          "tag": "Uint16"
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1750:39",
    "name": "TTF_RenderGlyph32_Blended",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "ch",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1786:39",
    "name": "TTF_RenderText_LCD",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "bg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1816:39",
    "name": "TTF_RenderUTF8_LCD",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "bg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1851:39",
    "name": "TTF_RenderUNICODE_LCD",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "Uint16"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "bg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1886:39",
    "name": "TTF_RenderText_LCD_Wrapped",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "bg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "wrapLength",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1917:39",
    "name": "TTF_RenderUTF8_LCD_Wrapped",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "bg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "wrapLength",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1952:39",
    "name": "TTF_RenderUNICODE_LCD_Wrapped",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "text",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "Uint16"
          }
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "bg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "wrapLength",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:1987:39",
    "name": "TTF_RenderGlyph_LCD",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "ch",
        "tag": "parameter",
        "type": {
          "tag": "Uint16"
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "bg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:2019:39",
    "name": "TTF_RenderGlyph32_LCD",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "ch",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      },
      {
        "name": "fg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      },
      {
        "name": "bg",
        "tag": "parameter",
        "type": {
          "tag": "SDL_Color"
        }
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:2055:30",
    "name": "TTF_CloseFont",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      }
    ],
    "return-type": {
      "tag": ":void"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:2075:30",
    "name": "TTF_Quit",
    "ns": 0,
    "parameters": [],
    "return-type": {
      "tag": ":void"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:2097:29",
    "name": "TTF_WasInit",
    "ns": 0,
    "parameters": [],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:2118:36",
    "name": "TTF_GetFontKerningSize",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "prev_index",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      },
      {
        "name": "index",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:2141:21",
    "name": "TTF_GetFontKerningSizeGlyphs",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "previous_ch",
        "tag": "parameter",
        "type": {
          "tag": "Uint16"
        }
      },
      {
        "name": "ch",
        "tag": "parameter",
        "type": {
          "tag": "Uint16"
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:2158:21",
    "name": "TTF_GetFontKerningSizeGlyphs32",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "previous_ch",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      },
      {
        "name": "ch",
        "tag": "parameter",
        "type": {
          "tag": "Uint32"
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:2177:21",
    "name": "TTF_SetFontSDF",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "on_off",
        "tag": "parameter",
        "type": {
          "tag": "SDL_bool"
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:2190:26",
    "name": "TTF_GetFontSDF",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      }
    ],
    "return-type": {
      "tag": "SDL_bool"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "fields": [
      {
        "name": "TTF_DIRECTION_LTR",
        "tag": "field",
        "value": 0
      },
      {
        "name": "TTF_DIRECTION_RTL",
        "tag": "field",
        "value": 1
      },
      {
        "name": "TTF_DIRECTION_TTB",
        "tag": "field",
        "value": 2
      },
      {
        "name": "TTF_DIRECTION_BTT",
        "tag": "field",
        "value": 3
      }
    ],
    "id": 199,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:2211:9",
    "name": "",
    "ns": 0,
    "tag": "enum"
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:2217:3",
    "name": "TTF_Direction",
    "ns": 0,
    "tag": "typedef",
    "type": {
      "id": 199,
      "name": "",
      "tag": ":enum"
    }
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:2241:44",
    "name": "TTF_SetDirection",
    "ns": 0,
    "parameters": [
      {
        "name": "direction",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:2264:44",
    "name": "TTF_SetScript",
    "ns": 0,
    "parameters": [
      {
        "name": "script",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:2287:29",
    "name": "TTF_SetFontDirection",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "direction",
        "tag": "parameter",
        "type": {
          "tag": "TTF_Direction"
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:2306:29",
    "name": "TTF_SetFontScriptName",
    "ns": 0,
    "parameters": [
      {
        "name": "font",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "TTF_Font"
          }
        }
      },
      {
        "name": "script",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "bit-alignment": 8,
            "bit-size": 8,
            "tag": ":char"
          }
        }
      }
    ],
    "return-type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":int"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:558:9",
    "name": "TTF_WRAPPED_ALIGN_LEFT",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 0
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:146:9",
    "name": "UNICODE_BOM_NATIVE",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 65279
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:433:9",
    "name": "TTF_STYLE_ITALIC",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 2
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:431:9",
    "name": "TTF_STYLE_NORMAL",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 0
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:51:9",
    "name": "SDL_TTF_MINOR_VERSION",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 20
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:511:9",
    "name": "TTF_HINTING_LIGHT_SUBPIXEL",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 4
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:50:9",
    "name": "SDL_TTF_MAJOR_VERSION",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 2
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:510:9",
    "name": "TTF_HINTING_NONE",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 3
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:508:9",
    "name": "TTF_HINTING_LIGHT",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 1
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:147:9",
    "name": "UNICODE_BOM_SWAPPED",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 65534
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:434:9",
    "name": "TTF_STYLE_UNDERLINE",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 4
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:68:9",
    "name": "TTF_MAJOR_VERSION",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 2
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:69:9",
    "name": "TTF_MINOR_VERSION",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 20
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:560:9",
    "name": "TTF_WRAPPED_ALIGN_RIGHT",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 2
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:52:9",
    "name": "SDL_TTF_PATCHLEVEL",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 2
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:435:9",
    "name": "TTF_STYLE_STRIKETHROUGH",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 8
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:83:9",
    "name": "SDL_TTF_COMPILEDVERSION",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 4002
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:559:9",
    "name": "TTF_WRAPPED_ALIGN_CENTER",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 1
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:507:9",
    "name": "TTF_HINTING_NORMAL",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 0
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:70:9",
    "name": "TTF_PATCHLEVEL",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 2
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:509:9",
    "name": "TTF_HINTING_MONO",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 2
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:432:9",
    "name": "TTF_STYLE_BOLD",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 1
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:2204:9",
    "name": "TTF_GetError",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    }
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_ttf.h:2197:9",
    "name": "TTF_SetError",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    }
  }
]
