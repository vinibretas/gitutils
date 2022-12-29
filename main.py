# Script to automate some git utils
# Imports
import sys
import re
import os

# Command line args
cmdline = sys.argv
fname = re.findall("\w*\.py$", cmdline[0])[0]

args = cmdline[1:]

# Constants
DETAIL = { 
        "subcommands" : { 
            "add" : [
                "`git add .`",
                ],

            "commit" : [
                "`git commit -m [message]`",
                "Default message = 'No message provided'",
                ],
            },


        "flags" : {
            "a": [
                "`git add .` folowed by `git commit -m [message]`",
                "This flag is used alongside with `git commit`",
                ],
            "m": [
                "`git commit -m`",
                "This flag is used alongside with `git commit` too",
                "but you don't have to put the message inside quotes"
                ]
            },

        }

# Exception classes
class EmptyArgsException(Exception):
    def __init__(self):
        usage()
        super().__init__("NO PARAMETERS WERE GIVEN")


class InvalidSubcommandException(Exception):
    def __init__(self, sub):
        usage()
        super().__init__(f"INVALID SUBCOMMAND `{sub}`")

class InvalidTagException(Exception):
    def __init__(self, tag):
        usage()
        super().__init__(f"INVALID TAG `{tag}`")

# Classes
class Gutils:
    # Magic methods
    def __init__(self,args = None):
        self.subcommand, self.flags, self.message = self.parse_args(args)
    
    def __repr__(self):
        result = "Gutils("
        dic = self.__dict__
        count,size = 0,len(dic) - 1
        for k,v in dic.items():
            if type(v) == str: v = f"'{v}'"
            if count != size:
                result += f"{k} = {v}, "
            else:
                result += f"{k} = {v}"
            count += 1
        result += ")"
        return result

    # Methods
    def parse_args(self, args):
        # Set message to default, if its not updated, thats what
        # it will be
        msg = 'No message provided'
        flags = None
        
        # Handle empty arg
        if not args: 
            raise EmptyArgsException

        # Handle invalid subcommand
        subcommand = args.pop(0)
        if subcommand not in DETAIL["subcommands"]: 
            raise InvalidSubcommandException(subcommand)

        rest = len(args)
        if rest > 0:
            # Check if the first is a flag
            first = args[0]
            if first.startswith("-"):
                first = first[1:]
                if first in DETAIL["flags"]:
                    flags = first
                    args.pop(0)
                else:
                    raise InvalidTagException(first)
            if args:
                msg = " ".join(args)
        return (subcommand, flags, msg)
    def run(self):
        scmd = self.subcommand
        flags = self.flags
        msg = self.message
        run = "echo hello world"
        
        if scmd == "add":
            run = "git add ."
            pass
        elif scmd == "commit":
            pass
        line(20)
        print("self.run() call")
        print(f"scmd = {scmd}\nflags = {flags}\nmsg = {msg}")
        line(20)
        os.system(run)
        



    # Independent functions aliases
    @staticmethod
    def usage():
        return usage()



# Independent functions:
def usage():
    tab = " "*4
    messages = [f" Usage: python3 {fname} <subcommand> [-flags] [message]"]
    # add subcommands and flags to list
    for key,value in DETAIL.items():
        messages.append(f"\n{tab}{key}:")
        for k,v in value.items():
            messages.append(f"{tab*2}{k:>6} - {v[0]}")
            for k2 in v[1:]:
                messages.append(f"{tab*4}{k2}")

    larger = get_larger(messages)
    line(larger)
    for k in messages:
        if k:
            print(k)
    line(larger)

# Helper functions
def get_larger(lst):
    max_ = 0
    for k in lst:
        sz = len(k)
        if sz > max_: max_ = sz
    return max_


def line(n, offset = 1):
    n += 2*offset
    n = n // 2 
    print("-="*n)



# -=- program testing -=-
ob = Gutils(args)
print(ob)
ob.run()
