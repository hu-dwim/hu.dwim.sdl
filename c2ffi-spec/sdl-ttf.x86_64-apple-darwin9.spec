[
  {
    "inline": false,
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:85:45",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:95:30",
    "name": "TTF_ByteSwappedUNICODE",
    "ns": 0,
    "parameters": [
      {
        "name": "swapped",
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
    "bit-alignment": 0,
    "bit-size": 0,
    "fields": [],
    "id": 0,
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:98:16",
    "name": "_TTF_Font",
    "ns": 0,
    "tag": "struct"
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:98:26",
    "name": "TTF_Font",
    "ns": 0,
    "tag": "typedef",
    "type": {
      "bit-alignment": 0,
      "bit-size": 0,
      "fields": [],
      "id": 0,
      "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:98:16",
      "name": "_TTF_Font",
      "ns": 0,
      "tag": "struct"
    }
  },
  {
    "inline": false,
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:101:29",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:107:36",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:108:36",
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
          "bit-alignment": 64,
          "bit-size": 64,
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:109:36",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:110:36",
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
          "bit-alignment": 64,
          "bit-size": 64,
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:118:29",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:119:30",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:120:29",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:121:30",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:128:29",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:129:30",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:132:29",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:137:29",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:142:29",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:145:29",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:148:29",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:149:30",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:152:30",
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
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:155:29",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:156:32",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:157:32",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:160:29",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:166:29",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:171:29",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:172:29",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:173:29",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:181:39",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:183:39",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:185:39",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:195:39",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:203:39",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:205:39",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:207:39",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:217:39",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:224:39",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:226:39",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:228:39",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:238:39",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:240:39",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:242:39",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:251:39",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:263:30",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:266:30",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:269:29",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:277:21",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:280:21",
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
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:126:9",
    "name": "TTF_HINTING_MONO",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 2
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:125:9",
    "name": "TTF_HINTING_LIGHT",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 1
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:127:9",
    "name": "TTF_HINTING_NONE",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 3
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:124:9",
    "name": "TTF_HINTING_NORMAL",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 0
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:117:9",
    "name": "TTF_STYLE_STRIKETHROUGH",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 8
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:114:9",
    "name": "TTF_STYLE_BOLD",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 1
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:113:9",
    "name": "TTF_STYLE_NORMAL",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 0
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:116:9",
    "name": "TTF_STYLE_UNDERLINE",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 4
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:115:9",
    "name": "TTF_STYLE_ITALIC",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 2
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:284:9",
    "name": "TTF_GetError",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    }
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:283:9",
    "name": "TTF_SetError",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    }
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:88:9",
    "name": "UNICODE_BOM_NATIVE",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 65279
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:67:9",
    "name": "SDL_TTF_COMPILEDVERSION",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 2015
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:89:9",
    "name": "UNICODE_BOM_SWAPPED",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 65534
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:46:9",
    "name": "SDL_TTF_PATCHLEVEL",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 15
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:45:9",
    "name": "SDL_TTF_MINOR_VERSION",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 0
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:44:9",
    "name": "SDL_TTF_MAJOR_VERSION",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 2
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:61:9",
    "name": "TTF_PATCHLEVEL",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 15
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:59:9",
    "name": "TTF_MAJOR_VERSION",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 2
  },
  {
    "location": "/nix/store/p1a950vn35gafaix4z8hmq5cc9hsw71a-SDL2_ttf-2.0.15/include/SDL2/SDL_ttf.h:60:9",
    "name": "TTF_MINOR_VERSION",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 0
  }
]
