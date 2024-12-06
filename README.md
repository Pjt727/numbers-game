# Premise
- Computer Society audience driven game
## Basic game starting concept
- the concept of this game was adapted from this [steam game](https://store.steampowered.com/app/3043740/Calculate_It/)
- there are rounds
- if you fail a round the game ends
- object is to stay alive for as many rounds
- you're given an inventory of mathematical symbols (numbers, operations, etc)
- each round
    - you must get to a target value by creating a mathematical expression with your symbols
    - you comsume the symbols use use in your expression
    - if you don't get the target value you fail
## Meeting Organization
- members write down an **ANY** addition to the game (i.e. adding another operation)
- the note will be folded up and placed up front
- once we have some amount of suggestions we'll pick one at random
    - this will then be live implemented as fast as possible

## ideas from club members not implemented
- colors
- lootboxes
- choose items
- power ups (could be in lootboxes)
    - draw three items for inventory
    - you can fail a round
- add a streak message (encouragement)
- difficulty
    - select difficulty
    - higher range of targets
    - fewer numbers and operators
- make every target possible
    - easier to generate all possible then choose
- add a help command for the game
- change the way the scoring works
    - using fewer symbols gives more points?
    - using more symbols gives more points?
    - certain symbols are worth more?
    - calculate the percent of your total symbols?
- mode where there are two target
    - anyone in your expression evals to bonus you get it

# Setup instructions
## short
- install dependencies in `requirements.txt` and run `main.py` with python
## verbose
- set up a python environment (optional)
    - create environment: `python -m venv venv`
    - python might be `python3` on your path as well
    - activate (windows): `venv\Scripts\activate`
        - if you get a "Scripts are disabled on this system" (powershell error) you can run the follow command
        - you may want to revert this for security reasons
        - `Set-ExecutionPolicy Unrestricted`
    - activate (mac/ linux): `source venv/bin/activate`
- run these next commands in your shell/ terminal in the root directory of this project
- install dependencies 
    - `pip install -r requirements.txt`
- if you dont have pip in your path (command not found) but you have python you can use
    - `python -m pip install -r requirements.txt`
    - python might be `python3` on your path
- run the program
    - `python main.py`
    - python might be `python3` on your path

