#!/usr/bin/env python3

import random
from enum import Enum

ACKNOWLEDGEMENTS = """
    cowsay for GNU/Linux was initially written in perl by Tony Monroe (tony@nog.net), with suggestions from
    Shannon Appel (appel@CSUA.Berkeley.EDU) and contributions from Anthony Polito (aspolito@CSUA.Berkeley.EDU).
    
    This code was originally written by: Vaasu Devan S
                                         https://pypi.org/project/cowsay/
                                         https://github.com/VaasuDevanS/cowsay-python
                                         All base characters, newline logic is from his code!
                                
    The code was updated by: Rashid NHM
                             https://github.com/rashid-nhm/cowsay
"""

__author__ = "Rashid NHM"
__name__ = "cowsay"
__version__ = 1.0

max_line_len = 50


class Characters(Enum):
    beavis = """
     __------~~-,
   ,'            ,
   /               \\
  /                :
 |                  '
 |                  |
 |                  |
  |   _--           |
  _| =-.     .-.   ||
  o|/o/       _.   |
  /  ~          \\ |
(____\@)  ___~    |
   |_===~~~.`    |
_______.--~     |
\\________       |
         \\      |
       __/-___-- -__
      /            _ \\      
    """

    cheese = """
    
     /     \\_/         |
    |                 ||
    |                 ||
   |    ###\\  /###   | |
   |     0  \\/  0    | |
  /|                 | |
 / |        <        |\\ \\
| /|                 | | |
| |     \\_______/   |  | |
| |                 | / /
/||                 /|||
   ----------------|
        | |    | |
        ***    ***
       /___\\  /___\\
       
    """

    daemon = """
    
            /- _  `-/  '
           (/\\/ \\ \\   /\\
           / /   | `    \\
           O O   ) /    |
           `-^--'`<     '
          (_.)  _  )   /
           `.___/`    /
             `-----' /
<----.     __ / __   \\
<----|====O)))==) \\) /====
<----'    `--' `.__,' \\
             |        |
              \\       /
        ______( (_  / \\______
      ,'  ,-----'   |        \\
      `--{__________)        \\/

    """

    cow = """    
^__^                             
(oo)\_______                   
(__)\       )\/\             
    ||----w |           
    ||     ||  
    """

    dragon = """
                              / \\  //\\
           |\\___/|      /   \\//  \\\\
           /0  0  \\__  /    //  | \\ \\    
          /     /  \\/_/    //   |  \\  \\  
          \@_^_\@'/   \\/_   //    |   \\   \\ 
          //_^_/     \\/_ //     |    \\    \\
       ( //) |        \\///      |     \\     \\
     ( / /) _|_ /   )  //       |      \\     _\\
   ( // /) '/,_ _ _/  ( ; -.    |    _ _\\.-~        .-~~~^-.
 (( / / )) ,-{        _      `-.|.-~-.           .~         `.
(( // / ))  '/\\      /                 ~-. _ .-~      .-~^-.  \\
(( /// ))      `.   {            }                   /      \\  \\
 (( / ))     .----~-.\\        \\-'                 .~         \\  `. \\^-.
            ///.----..>        \\             _ -~             `.  ^-`  ^-_
              ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~
                                                                 /.-~
    """

    ghostbusters = """
                          __---__
                   _-       /--______
              __--( /     \\ )XXXXXXXXXXX\\v.
            .-XXX(   O   O  )XXXXXXXXXXXXXXX-
           /XXX(       U     )        XXXXXXX\\
         /XXXXX(              )--_  XXXXXXXXXXX\\
        /XXXXX/ (      O     )   XXXXXX   \\XXXXX\\
        XXXXX/   /            XXXXXX   \\__ \\XXXXX
        XXXXXX__/          XXXXXX         \\__---->
---___  XXX__/          XXXXXX      \\__         /
  \\-  --__/   ___/\\  XXXXXX            /  ___--/=
   \\-\\    ___/    XXXXXX              '--- XXXXXX
      \\-\\/XXX\\ XXXXXX                      /XXXXX
        \\XXXXXXXXX   \\                    /XXXXX/
         \\XXXXXX      >                 _/XXXXX/
           \\XXXXX--__/              __-- XXXX/
            -XXXXXXXX---------------  XXXXXX-
               \\XXXXXXXXXXXXXXXXXXXXXXXXXX/
                 ""VXXXXXXXXXXXXXXXXXXV""
    """

    kitty = """
      ("`-'  '-/") .___..--' ' "`-._
      ` *_ *  )    `-.   (      ) .`-.__. `)
      (_Y_.) ' ._   )   `._` ;  `` -. .-'
   _.. `--'_..-_/   /--' _ .' ,4
( i l ),-''  ( l i),'  ( ( ! .-'  
    """

    meow = """
                   _ ___.--'''`--''//-,-_--_.
   \\`"' ` || \\\\ \\ \\\\/ / // / ,-\\\\`,_
  /'`  \\ \\ || Y  | \\|/ / // / - |__ `-,
 /\@"\\  ` \\ `\\ |  | ||/ // | \\/  \\  `-._`-,_.,
/  _.-. `.-\\,___/\\ _/|_/_\\_\\/|_/ |     `-._._)
`-'``/  /  |  // \\__/\\__  /  \\__/ \\
     `-'  /-\\/  | -|   \\__ \\   |-' |
       __/\\ / _/ \\/ __,-'   ) ,' _|'
      (((__/(((_.' ((___..-'((__,'
    """

    milk = """
       ____________ 
       |__________|
      /           /\\
     /           /  \\
    /___________/___/|
    |          |     |
    |  ==\\ /== |     |
    |   O   O  | \\ \\ |
    |     <    |  \\ \\|
   /|          |   \\ \\
  / |  \\_____/ |   / /
 / /|          |  / /|
/||\\|          | /||\\/
    -------------|   
        | |    | | 
       <__/    \\__>
    """

    stegosaurus = """  
                                / `.   .' " 
                        .---.  <    > <    >  .---.
                        |    \\  \\ - ~ ~ - /  /    |
    _____          ..-~             ~-..-~
   |     |   \\~~~\\.'                    `./~~~/
  ---------   \\__/                        \\__/
 .'  O    \\     /               /       \\  " 
(_____,    `._.'               |         }  \\/~~~/
 `----.          /       }     |        /    \\__/
       `-.      |       /      |       /      `. ,~~|
           ~-.__|      /_ - ~ ^|      /- _      `..-'   
                |     /        |     /     ~-.     `-. _  _  _
                |_____|        |_____|         ~ - . _ _ _ _ _>
    """

    stimpy = """
   .    _  .    
  |\\_|/__/|    
  / / \\/ \\  \\  
 /__|O||O|__ \\ 
|/_ \\_/\\_/ _\\ |  
| | (____) | ||  
\\/\\___/\\__/  // 
(_/         ||
 |          ||
 |          ||\\   
  \\        //_/  
   \\______//
  __ || __||
 (____(____)
    """

    turkey = """
                                        ,+*^^*+___+++_
                              ,*^^^^              )
                           _+*                     ^**+_
                         +^       _ _++*+_+++_,         )
     _+^^*+_    (     ,+*^ ^          \\+_        )
    {       )  (    ,(    ,_+--+--,      ^)      ^\\
   { (\@)    } f   ,(  ,+-^ __*_*_  ^^\\_   ^\\       )
  {:;-/    (_+*-+^^^^^+*+*<_ _++_)_    )    )      /
 ( /  (    (        ,___    ^*+_+* )   <    <      \\
  U _/     )    *--<  ) ^\\-----++__)   )    )       )
   (      )  _(^)^^))  )  )\\^^^^^))^*+/    /       /
 (      /  (_))_^)) )  )  ))^^^^^))^^^)__/     +^^
(     ,/    (^))^))  )  ) ))^^^^^^^))^^)       _)
 *+__+*       (_))^)  ) ) ))^^^^^^))^^^^^)____*^
 \\             \\_)^)_)) ))^^^^^^^^^^))^^^^)
  (_             ^\\__^^^^^^^^^^^^))^^^^^^^)
    ^\\___            ^\\__^^^^^^))^^^^^^^^)\\\\
         ^^^^^\\uuu/^^\\uuu/^^^^\\^\\^\\^\\^\\^\\^\\^\\
            ___) >____) >___   ^\\_\\_\\_\\_\\_\\_\\)
           ^^^//\\\\_^^//\\\\_^       ^(\\_\\_\\_\\)
             ^^^ ^^ ^^^ ^             
    """

    turtle = """
                                ___-------___
                            _-~~             ~~-_
                         _-~                    /~-_
   /^\\__/^\\        /~  \\                   /    \\
 /|  O|| O|        /      \\_______________/        \\
| |___||__|      /       /                \\          \\
|          \\    /      /                    \\          \\
|   (_______) /______/                        \\_________ \\
|         / /         \\                      /            \\
 \\         \\^\\\\         \\                  /               \\     /
   \\         ||           \\______________/      _-_       //\\__//
     \\       ||------_-~~-_ ------------- \\ --/~   ~\\    || __/
       ~-----||====/~     |==================|       |/~~~~~
        (_(__/  ./     /                    \\_\\      \\.
               (_(___/                         \\_____)_)
    """

    tux = """
    .--.
   |o_o |
   |:_/ |
  //   \\ \\
 (|     | )
/'\\_   _/`\\
\\___)=(___/    
    """


def character_names():
    return [character.name for character in Characters]


def character_functions():
    return [beavis, cheese, daemon, cow, dragon,
            ghostbusters, kitty, meow, milk, stegosaurus,
            stimpy, turkey, turtle, tux]


def process_string(func):
    def string_processor(txt, *args, **kwargs):
        txt = str(txt)
        lines = [i.strip() for i in txt.split("\n") if len(i.strip()) != 0]

        if len(lines) == 1:
            line_len = len(lines[0])
            if line_len <= max_line_len:
                ret_txt = f"  {'_'*line_len}\n /{' '*line_len}\\\n< {lines[0]}{' '*(line_len - len(lines[0]) + 1)}>\n "\
                    f"{'='*line_len}\n"
            else:
                lines = list("".join(lines[0]))
                for i, line in enumerate(lines):
                    if i and i % max_line_len == 0:
                        lines.insert(i, "\n")
                return string_processor("".join(lines), *args, **kwargs)
        else:
            line_len = len(max(lines, key=len))
            if all(len(line) <= max_line_len for line in lines):
                ret_txt = f" {'_'*line_len}\n /{' '*line_len}\\\n"
                for line in lines:
                    ret_txt = f"| {line}{' '*(line_len-len(line)+1)}|\n"
                ret_txt += f" \\{' '*line_len}/\n {'='*line_len}\n"
            else:
                new_lines = []
                for line in lines:
                    if len(line) > max_line_len:
                        joined_line = list("".join(line))
                        for i, char in enumerate(joined_line):
                            if i and i % max_line_len == 0:
                                joined_line.insert(i, "\n")
                        new_lines.append("".join(joined_line))
                    else:
                        new_lines.append(line + "\n")
                return string_processor("".join(new_lines), *args, **kwargs)
        return func(ret_txt, *args, max_line=line_len, **kwargs)
    return string_processor


def apologize_if_fail_for(character_name):
    def apologize(func):
        def apology(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                if not str(args[0]).strip():
                    return func(f"You didn't actually give {character_name} anything to say...")
                return func(f"I was not able to parse and say what you wanted. Please give {character_name} something "
                            f"easier or different")
        return apology
    return apologize


@process_string
def __say(txt, base_character, max_line=max_line_len, left_pad=0):
    for i in range(5, 9):
        txt += " " * (max_line + i) + "\\\n"

    base_char_lines = [line for line in base_character.value.split("\n") if len(line) != 0]
    for line in base_char_lines:
        txt += " " * (max_line + left_pad) + line + "\n"

    return txt


@apologize_if_fail_for("beavis")
def beavis(txt):
    return __say(txt, Characters.beavis, left_pad=7)


@apologize_if_fail_for("cheese")
def cheese(txt):
    return __say(txt, Characters.cheese, left_pad=3)


@apologize_if_fail_for("daemon")
def daemon(txt):
    return __say(txt, Characters.daemon, left_pad=-2)


@apologize_if_fail_for("cow")
def cow(txt):
    return __say(txt, Characters.cow, left_pad=10)


@apologize_if_fail_for("dragon")
def dragon(txt):
    return __say(txt, Characters.dragon, left_pad=0)


@apologize_if_fail_for("ghostbusters")
def ghostbusters(txt):
    return __say(txt, Characters.ghostbusters, left_pad=0)


@apologize_if_fail_for("kitty")
def kitty(txt):
    return __say(txt, Characters.kitty, left_pad=3)


@apologize_if_fail_for("meow")
def meow(txt):
    return __say(txt, Characters.meow, left_pad=3)


@apologize_if_fail_for("milk")
def milk(txt):
    return __say(txt, Characters.milk, left_pad=3)


@apologize_if_fail_for("stegosaurus")
def stegosaurus(txt):
    return __say(txt, Characters.stegosaurus, left_pad=0)


@apologize_if_fail_for("stimpy")
def stimpy(txt):
    return __say(txt, Characters.stimpy, left_pad=7)


@apologize_if_fail_for("turkey")
def turkey(txt):
    return __say(txt, Characters.turkey, left_pad=2)


@apologize_if_fail_for("turtle")
def turtle(txt):
    return __say(txt, Characters.turtle, left_pad=5)


@apologize_if_fail_for("tux")
def tux(txt):
    return __say(txt, Characters.tux, left_pad=5)


def random_character(txt):
    return random.choice(character_functions())(txt)
