from nextcord.ext.commands import Bot
from config import VERSION, NAME, COGS_TO_LOAD


def tree_print(category: str = None, cog: str = None, last_category: bool = False, last_cog: bool = False):
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


def load_cogs(bot: Bot):

    print(f"Loading {NAME} v{VERSION}...\n")
    print(F"{NAME} v{VERSION}")

    categories = []
    category_imported = 0
    for category in COGS_TO_LOAD:
        categories.append(category)

    for category in COGS_TO_LOAD:
        category_cogs = 0
        category_imported += 1

        tree_print(category=category,
                   last_category=category_imported == len(categories))

        for _ in COGS_TO_LOAD[category]:
            category_cogs += 1

        for cog_name, opts in COGS_TO_LOAD[category]:
            bot.load_extension(f"cogs.{category}.{cog_name}", extras=opts)
            category_cogs -= 1
            tree_print(cog=cog_name, last_cog=category_cogs == 0,
                       last_category=category_imported == len(categories))


"├──"
"└──"
