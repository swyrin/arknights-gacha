# Welcome to `arknights-gacha` repository
This is my shameless attempt of simulating Arknights gacha.

Currently, we are supporting these banner types (with potential bugs):
  - [x] Standard
  - [x] Debut
  - [x] Limited
    - [x] Even with comeback operator(s) (e.g. `Nian - Hidden Moon`, `W - Deep Drown Lament`)
  - [x] Joint Operation banner

Helps are welcome! :tada:

# How to use
### 1. API way

Under reconstruction, so not available yet.
 
### 2. Normal way

If you are lazy to install the entire Python just to run this, you can use the `Embeddeable Package` installation of Python.
```
cli.py -i=[banner-id] -c=100 -r=glb

arguments:
  --id|-i=[banner-id]: Banner ID.
  --count|-c=[count]: How many times you want to draw. (Default: 100)
  --region|-r=[region]: Region. Only "glb" and "chn" are supported. (Default: glb)

example: cli.py -i=deep-drown-lament -c=300 -r=glb
```

# TODOs
- Core components:
  - [x] Operators list
  - [x] Rate-ups
      - [x] 6* rate ups
        - [x] Rate up for 6* comeback operator(s)
      - [x] 5* rate ups
      - [x] 4* rate ups
      - [x] 3* rate ups
  - [x] More banner types support
    - [x] Standard banner
    - [x] Debut operator banner
    - [x] Limited operator banner
      - [x] With comeback operator(s)
    - [ ] Analytics
- CLI:
  - [ ] Add more useful options
- API:
  - [ ] Soon:tm:
- General:
  - [ ] Better code
  - [ ] Extending to customizable gacha?
  - [ ] Extending to other regions?
  - [ ] Better documentation
