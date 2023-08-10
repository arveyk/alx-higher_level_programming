#!/usr/bin/python3
if __name__=="__main__":
    import hidden_4
    for var in list(dir(hidden_4)):
            if not var.startswith('__'):
                print("{:s}".format(var))
