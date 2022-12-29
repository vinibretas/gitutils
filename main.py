import sys
cmdline = sys.argv
fname = cmdline[0]
args = cmdline[1:]
DETAIL = { 
        "subcommands: " : { 
            "add" : [
                "`git add [message]`",
                "If no message are given, `.` is used",
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
                ]
            },

        }
            


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

    def parse_args(self, args):
        if not args: 
            print("\n   !ERROR: No parameters were given")
            usage()
            exit(True)
        subcommand, flags, msg = None, None, "No message provided"
        return (subcommand, flags, msg)
    
        



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
        messages.append(f"{tab}{key}:")
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
