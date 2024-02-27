[
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:89:45",
    "name": "IMG_Linked_Version",
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
    "fields": [
      {
        "name": "IMG_INIT_JPG",
        "tag": "field",
        "value": 1
      },
      {
        "name": "IMG_INIT_PNG",
        "tag": "field",
        "value": 2
      },
      {
        "name": "IMG_INIT_TIF",
        "tag": "field",
        "value": 4
      },
      {
        "name": "IMG_INIT_WEBP",
        "tag": "field",
        "value": 8
      },
      {
        "name": "IMG_INIT_JXL",
        "tag": "field",
        "value": 16
      },
      {
        "name": "IMG_INIT_AVIF",
        "tag": "field",
        "value": 32
      }
    ],
    "id": 281,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:94:9",
    "name": "",
    "ns": 0,
    "tag": "enum"
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:102:3",
    "name": "IMG_InitFlags",
    "ns": 0,
    "tag": "typedef",
    "type": {
      "id": 281,
      "name": "",
      "tag": ":enum"
    }
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:166:29",
    "name": "IMG_Init",
    "ns": 0,
    "parameters": [
      {
        "name": "flags",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:191:30",
    "name": "IMG_Quit",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:252:39",
    "name": "IMG_LoadTyped_RW",
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
        "name": "type",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:294:39",
    "name": "IMG_Load",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:347:39",
    "name": "IMG_Load_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:385:39",
    "name": "IMG_LoadTexture",
    "ns": 0,
    "parameters": [
      {
        "name": "renderer",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "SDL_Renderer"
          }
        }
      },
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
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Texture"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:432:39",
    "name": "IMG_LoadTexture_RW",
    "ns": 0,
    "parameters": [
      {
        "name": "renderer",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "SDL_Renderer"
          }
        }
      },
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
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Texture"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:487:39",
    "name": "IMG_LoadTextureTyped_RW",
    "ns": 0,
    "parameters": [
      {
        "name": "renderer",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "SDL_Renderer"
          }
        }
      },
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
        "name": "type",
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
      "tag": ":pointer",
      "type": {
        "tag": "SDL_Texture"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:532:29",
    "name": "IMG_isAVIF",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:575:29",
    "name": "IMG_isICO",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:618:29",
    "name": "IMG_isCUR",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:661:29",
    "name": "IMG_isBMP",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:704:29",
    "name": "IMG_isGIF",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:747:29",
    "name": "IMG_isJPG",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:790:29",
    "name": "IMG_isJXL",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:833:29",
    "name": "IMG_isLBM",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:876:29",
    "name": "IMG_isPCX",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:919:29",
    "name": "IMG_isPNG",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:962:29",
    "name": "IMG_isPNM",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1005:29",
    "name": "IMG_isSVG",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1048:29",
    "name": "IMG_isQOI",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1091:29",
    "name": "IMG_isTIF",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1134:29",
    "name": "IMG_isXCF",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1177:29",
    "name": "IMG_isXPM",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1220:29",
    "name": "IMG_isXV",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1263:29",
    "name": "IMG_isWEBP",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1297:39",
    "name": "IMG_LoadAVIF_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1331:39",
    "name": "IMG_LoadICO_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1365:39",
    "name": "IMG_LoadCUR_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1399:39",
    "name": "IMG_LoadBMP_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1433:39",
    "name": "IMG_LoadGIF_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1467:39",
    "name": "IMG_LoadJPG_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1501:39",
    "name": "IMG_LoadJXL_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1535:39",
    "name": "IMG_LoadLBM_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1569:39",
    "name": "IMG_LoadPCX_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1603:39",
    "name": "IMG_LoadPNG_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1637:39",
    "name": "IMG_LoadPNM_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1671:39",
    "name": "IMG_LoadSVG_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1705:39",
    "name": "IMG_LoadQOI_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1739:39",
    "name": "IMG_LoadTGA_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1773:39",
    "name": "IMG_LoadTIF_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1807:39",
    "name": "IMG_LoadXCF_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1841:39",
    "name": "IMG_LoadXPM_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1875:39",
    "name": "IMG_LoadXV_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1909:39",
    "name": "IMG_LoadWEBP_RW",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1930:39",
    "name": "IMG_LoadSizedSVG_RW",
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
        "name": "width",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      },
      {
        "name": "height",
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
        "tag": "SDL_Surface"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1949:39",
    "name": "IMG_ReadXPMFromArray",
    "ns": 0,
    "parameters": [
      {
        "name": "xpm",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": ":pointer",
            "type": {
              "bit-alignment": 8,
              "bit-size": 8,
              "tag": ":char"
            }
          }
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1968:39",
    "name": "IMG_ReadXPMFromArrayToRGB888",
    "ns": 0,
    "parameters": [
      {
        "name": "xpm",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": ":pointer",
            "type": {
              "bit-alignment": 8,
              "bit-size": 8,
              "tag": ":char"
            }
          }
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:1985:29",
    "name": "IMG_SavePNG",
    "ns": 0,
    "parameters": [
      {
        "name": "surface",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "SDL_Surface"
          }
        }
      },
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:2002:29",
    "name": "IMG_SavePNG_RW",
    "ns": 0,
    "parameters": [
      {
        "name": "surface",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "SDL_Surface"
          }
        }
      },
      {
        "name": "dst",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "SDL_RWops"
          }
        }
      },
      {
        "name": "freedst",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:2021:29",
    "name": "IMG_SaveJPG",
    "ns": 0,
    "parameters": [
      {
        "name": "surface",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "SDL_Surface"
          }
        }
      },
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
        "name": "quality",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:2038:29",
    "name": "IMG_SaveJPG_RW",
    "ns": 0,
    "parameters": [
      {
        "name": "surface",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "SDL_Surface"
          }
        }
      },
      {
        "name": "dst",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "SDL_RWops"
          }
        }
      },
      {
        "name": "freedst",
        "tag": "parameter",
        "type": {
          "bit-alignment": 32,
          "bit-size": 32,
          "tag": ":int"
        }
      },
      {
        "name": "quality",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:2050:3",
    "name": "IMG_Animation",
    "ns": 0,
    "tag": "typedef",
    "type": {
      "bit-alignment": 64,
      "bit-size": 256,
      "fields": [
        {
          "bit-alignment": 32,
          "bit-offset": 0,
          "bit-size": 32,
          "name": "w",
          "tag": "field",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        },
        {
          "bit-alignment": 32,
          "bit-offset": 32,
          "bit-size": 32,
          "name": "h",
          "tag": "field",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        },
        {
          "bit-alignment": 32,
          "bit-offset": 64,
          "bit-size": 32,
          "name": "count",
          "tag": "field",
          "type": {
            "bit-alignment": 32,
            "bit-size": 32,
            "tag": ":int"
          }
        },
        {
          "bit-alignment": 64,
          "bit-offset": 128,
          "bit-size": 64,
          "name": "frames",
          "tag": "field",
          "type": {
            "tag": ":pointer",
            "type": {
              "tag": ":pointer",
              "type": {
                "tag": "SDL_Surface"
              }
            }
          }
        },
        {
          "bit-alignment": 64,
          "bit-offset": 192,
          "bit-size": 64,
          "name": "delays",
          "tag": "field",
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
      "id": 282,
      "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:2044:9",
      "name": "",
      "ns": 0,
      "tag": "struct"
    }
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:2065:41",
    "name": "IMG_LoadAnimation",
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
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "IMG_Animation"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:2086:41",
    "name": "IMG_LoadAnimation_RW",
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
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "IMG_Animation"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:2116:41",
    "name": "IMG_LoadAnimationTyped_RW",
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
        "name": "type",
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
      "tag": ":pointer",
      "type": {
        "tag": "IMG_Animation"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "inline": false,
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:2131:30",
    "name": "IMG_FreeAnimation",
    "ns": 0,
    "parameters": [
      {
        "name": "anim",
        "tag": "parameter",
        "type": {
          "tag": ":pointer",
          "type": {
            "tag": "IMG_Animation"
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:2151:41",
    "name": "IMG_LoadGIFAnimation_RW",
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
      }
    ],
    "return-type": {
      "tag": ":pointer",
      "type": {
        "tag": "IMG_Animation"
      }
    },
    "storage-class": "extern",
    "tag": "function",
    "variadic": false
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:2158:9",
    "name": "IMG_SetError",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    }
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:2165:9",
    "name": "IMG_GetError",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    }
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:69:9",
    "name": "SDL_IMAGE_COMPILEDVERSION",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 2603
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:45:9",
    "name": "SDL_IMAGE_MINOR_VERSION",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 6
  },
  {
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:46:9",
    "name": "SDL_IMAGE_PATCHLEVEL",
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
    "location": "/gnu/store/9p78my901z4sfzpn39m9l9vi02sah6zy-profile/include/SDL2/SDL_image.h:44:9",
    "name": "SDL_IMAGE_MAJOR_VERSION",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 64,
      "bit-size": 64,
      "tag": ":long"
    },
    "value": 2
  }
]
