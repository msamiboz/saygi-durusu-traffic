"""Build compact cell-day and city-hour panels in data/interim/ from the monthly files."""

from saygi import panel

if __name__ == "__main__":
    panel.build()
    print("panels written to", panel.DERIVED)
