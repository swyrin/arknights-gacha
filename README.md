# Welcome to `arknights-gacha` repository
This is my shameless attempt of simulating Arknights gacha.

Current supported banner types (with potential bugs):
  - Standard banner
  - Debut banner
  - Limited banner
  - Limited banner with comeback operator (e.g. `Nian - Hidden Moon`, `W - Deep Drown Lament`)

Helps are welcome! :tada:

# How to use
1. API way
```
api.py
```
Then head to `127.0.0.1:8000` to use the API.

Available endpoints:

| Endpoints                           | Description                                            | Note| 
| ----                                | ----                                                   | --- |
| 1. General Endpoints                |                                                        | 
| `/`                                 | Index page, just say "Hello world!"                    |
| `/docs`                             | Having problems when remembering? Just use this        |
| `/operators`                        | Check operator list                                    |
| `/rates`                            | Check gacha rates                                      |
| `/ids`                              | Check all available banner IDs                         |
|2. Banner-specific Endpoints         |                                                        | `banner_id`: ID of the banner (e.g. `standard`, `deep-drown-lament`). Will be the banner's name most of the time.
| `/{banner_id}`                      | See infomation of banner
| `/{banner_id}/roll?count[number]`   | Gambling Industry                                      | `count`: Number of rolls
| `/{banner_id}/rates`                | Check banner's rate-up rates for rarities              |
| `/{banner_id}/operators`            | Check banner's rate-up operators                       |

 
2. Normal way
```
gacha.py [banner_id] [roll count]
example: gacha.py deep-drown-lament 300
```

# TODOs
- [x] Operators list
- [x] Rate-ups
    - [x] 6* rate ups
    - [x] 5* rate ups
    - [x] 4* rate ups
- [x] More banner types support
- [ ] Better code quality
- [x] API???
- [ ] Extending to customizable gacha?