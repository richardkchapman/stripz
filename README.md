# stripz
Strip unnecessary Z moves from gcode

Very simple Python code to remove unnecessary Z moves from a gcode program.
V-Carve often adds these between depth passes when cutting a pocket. This
program will remove any Z move that is immediately followed by another Z move.

Probably not advized to use on a script that includes pecking drill operations.

