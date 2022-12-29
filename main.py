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
            "push" : [
                "`git push`",
                "Pushes comitted changes to origin on current branch",
                ],
            "pull" : [
                "`git pull`",
                "Pulls the most recent snapshot of the current branch",
                "from the remote repo",
                ],
            "branches" : [
                "`git branch --list`",
                "Displays the list of existing branches"
                ],
            "status" : [
                "`git status`",
                "Displays current index"
                ]
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

class IncompatibleTagException(Exception):
    def __init__(self, subcmd, tag):
        usage()
        msg = f"The tag `{tag}` is not compatible with the subcommand `{subcmd}`"
        super().__init__(msg)

# Classes
class Gutils:
    # Class attibutes
    default_message = 'No message provided'

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
        msg = Gutils.default_message 
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
        self.clear()
        if scmd == "add":
            if flags not in ["m"] and flags is not None: 
                raise IncompatibleTagException("add", flags)
            add = "." 
            if msg != Gutils.default_message:
                add = msg.split()
            self.git_add(add)
        elif scmd == "commit":
            if flags == "a":
                self.git_add()
            self.git_commit(msg)
        elif scmd == "status":
            self.git_status()
        elif scmd == "push":
            self.git_push()
        elif scmd == "pull":
            self.git_pull()
        elif scmd == "branches":
            self.git_branches()
        else:
            assert False, f'Subcommand `{scmd}` not implemented'
        self.git_status()
        line(20)
        print(f"scmd = {scmd}\nflags = {flags}\nmsg = {msg}")
        line(20)
        
    def git_add(self, files = ["."]):
        st = " ".join(files)
        syscall(f"git add {st}")

    def git_status(self):
        syscall("git status", False)
    
    def clear(self):
        syscall("clear", False)

    def git_commit(self, msg):
        cm = f'git commit -m "{msg}"'
        syscall(cm)

    def git_push(self):
        syscall("git push", False)

    def git_pull(self):
        syscall("git pull", False)
    
    def git_branches(self):
        syscall("git branches --list", False)



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
            messages.append(f"{tab*2}{k:>8} - {v[0]}")
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

def syscall(cmd, echo = True):
    if echo:
        print(f"RUNNING `{cmd}`")
    os.system(cmd)


# -=- program testing -=-
ob = Gutils(args)
print(ob)
ob.run()
