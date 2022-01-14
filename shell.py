if __name__ == '__main__' or __name__ == "main":
    import config,getpass,socket,os,sys,multiprocessing
    Hello="""
    __  __          ____  _          _ _ 
    \ \/ /         / ___|| |__   ___| | |
    \  /   _____  \___ \| '_ \ / _ \ | |
    /  \  |_____|  ___) | | | |  __/ | |
    /_/\_\         |____/|_| |_|\___|_|_|
    """
    print(Hello)
    print(f"Version {config.version},Python {sys.version}\n")
    def get_prompt():
        return f"Xsh:{getpass.getuser()}@{socket.gethostname()}:{os.getcwd()}# "
    def run_command(cmdstr):
        args=cmdstr[1:]
        cmd=cmdstr[0]
    while True:
        command=input(get_prompt())
        if command == "exit":
            break
        else:
            p=multiprocessing.Process(target=os.system,args=(command,))
            p.start()
            p.join()

