from cmd import Cmd


class Application(Cmd):
    intro = (
        """Welcome to your cat shell. Start your tracing by executing `cat doggy.py`!"""
    )

    prompt = "(yourcat) "

    def do_cat(self, arg: str):
        "Print the contents of a file to the screen"
        try:
            with open(arg, "r") as f:
                print(f.read())
        except:
            print("Error: could not open file")

    def do_story(self, arg: str):
        "Something you may want to know"
        with open("story.md", "r") as f:
            print(f.read())


try:
    Application().cmdloop()
except KeyboardInterrupt:
    print("\nGoodbye!")
