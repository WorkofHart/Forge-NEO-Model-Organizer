import argparse


def preload(parser: argparse.ArgumentParser):
    parser.add_argument("--forge-neo-mo-debug", action='store_true', help="Enable Forge NEO Model Organizer Debug Mode")
    parser.add_argument("--forge-neo-mo-database-dir", type=str, help="Path to directory with database", default=None)
    parser.add_argument("--forge-neo-mo-models-dir", type=str, help="Path to models directory", default=None)