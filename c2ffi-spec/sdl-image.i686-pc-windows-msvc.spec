[
  {
    "inline": false,
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:68:45",
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
      }
    ],
    "id": 187,
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:70:9",
    "name": "",
    "ns": 0,
    "tag": "enum"
  },
  {
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:76:3",
    "name": "IMG_InitFlags",
    "ns": 0,
    "tag": "typedef",
    "type": {
      "id": 187,
      "name": "",
      "tag": ":enum"
    }
  },
  {
    "inline": false,
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:82:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:85:30",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:95:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:97:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:98:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:103:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:104:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:105:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:109:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:110:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:111:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:112:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:113:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:114:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:115:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:116:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:117:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:118:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:119:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:120:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:121:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:122:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:123:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:126:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:127:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:128:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:129:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:130:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:131:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:132:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:133:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:134:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:135:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:136:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:137:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:138:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:139:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:140:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:141:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:143:39",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:146:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:147:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:148:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:149:29",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:40:9",
    "name": "SDL_IMAGE_PATCHLEVEL",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 5
  },
  {
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:38:9",
    "name": "SDL_IMAGE_MAJOR_VERSION",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:153:9",
    "name": "IMG_GetError",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    }
  },
  {
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:39:9",
    "name": "SDL_IMAGE_MINOR_VERSION",
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
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:152:9",
    "name": "IMG_SetError",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    }
  },
  {
    "location": "/nix/store/gc7ra22lf3x41i02klfqy1d8mr9adgrm-SDL2_image-2.0.5/include/SDL2/SDL_image.h:55:9",
    "name": "SDL_IMAGE_COMPILEDVERSION",
    "ns": 0,
    "tag": "const",
    "type": {
      "bit-alignment": 32,
      "bit-size": 32,
      "tag": ":long"
    },
    "value": 2005
  }
]
