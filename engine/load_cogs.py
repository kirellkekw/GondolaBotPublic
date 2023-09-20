import os
from nextcord.ext.commands import Bot
from config import VERSION, NAME, cogs_to_load


def tree_print(category:str = None, cog:str = None, last_category:bool = False, last_cog:bool = False):
    """
    Usage:

    tree_print(category, cog, last_category, last_cog)
    """

    no_branch = "│  "
    branch = "├──"
    last_branch = "└──"
    space = "   "

    if category != None:
        # print category
    
        category_indent = last_branch if last_category else branch

        print(f"{category_indent}{category}")

    else:
        # print the cog goddamn
        category_indent = space if last_category else no_branch

        cog_indent = last_branch if last_cog else branch

        print(f"{category_indent}{cog_indent}{cog}")

def load_cogs(bot):

    load_core_cogs(bot)
    load_other_cogs(bot)


def load_core_cogs(bot: Bot):
    cog_names = []

    print(f"Loading {NAME} v{VERSION}...\n")

    print(F"{NAME} v{VERSION}")

    tree_print(category="core")

    for file in os.listdir("core/"):
        if file.endswith(".py"):
            cog_names.append(file[:-3])
    
    cogs_imported = 0
    for cog in cog_names:
        bot.load_extension(f"core.{cog}")
        cogs_imported += 1
        tree_print(cog=cog, last_cog=cogs_imported == len(cog_names))


def load_other_cogs(bot:Bot):
    
    categories = []
    category_imported = 0
    for category in cogs_to_load:
        categories.append(category)


    for category in cogs_to_load:
        category_cogs = 0
        category_imported += 1

        tree_print(category=category, last_category=category_imported == len(categories))

        for _ in cogs_to_load[category]:
            category_cogs += 1


        for cog_name, opts in cogs_to_load[category]:
            bot.load_extension(f"cogs.{category}.{cog_name}", extras=opts)
            category_cogs -= 1
            tree_print(cog=cog_name, last_cog=category_cogs == 0, last_category=category_imported == len(categories))

            

                

    

    


"├──"
"└──"
