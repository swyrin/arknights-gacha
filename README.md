# Welcome to `arknights-gacha` repository
This is my shameless attempt of simulating Arknights gacha.

Current supported banner types (with potential bugs):
  - Standard banner
  - Debut banner
  - Limited banner
  - Limited banner with comeback operator (e.g. `Nian - Hidden Moon`, `W - Deep Drown Lament`)
  - Joint Operation

Helps are welcome! :tada:

# How to use
1. API way
The API implementation for this repo is hosted on [`https://api.swyrin.me/arknights`](https://api.swyrin.me/arknights)

| Endpoints                           | Description                                            | Note| 
| ----                                | ----                                                   | --- |
| 1. General Endpoints                |                                                        | 
| `/rates`                            | Check gacha rates                                      |
| `/operators`                              | Check all available operators                         |
|2. Banner-specific Endpoints         |                                                        | `banner_id`: ID of the banner (e.g. `standard`, `deep-drown-lament`).Will be the banner's name most of the time.
| `banners/`                                 | Check all available banners
| `banners/{banner_id}`                      | See infomation of specified banner
| `banners/{banner_id}/roll?count=[number]`   | Gambling Industry                                      | `count`: Number of rolls
| `banners/{banner_id}/rates`                | Check banner's rate-up rates for rarities              |
| `banners/{banner_id}/operators`            | Check banner's rate-up operators                       |

 
2. Normal way
If you are lazy to install the entire Python just to run this, you can use the `Embeddeable Package` installation of Python.
```
gacha.py [banner_id] [roll count]
example: gacha.py deep-drown-lament 300
```

# TODOs
- [x] Operators list
- [x] Rate-ups
    - [x] 6* rate ups
      - [ ] Rate up for 6* comeback operator(s)
    - [x] 5* rate ups
    - [x] 4* rate ups
- [x] More banner types support
- [ ] Better code quality
- [ ] Extending to customizable gacha?
