# Dynamic Wallpapers For Gnome 42 Generator
* This is a python script and bash script for generating xml files for Gnome 42 Light/Dark Wallpapers.
* The main idea of this script is to Generate XML files for Light/Dark Wallpapers that are inside a directory and have 
their subdirectory with the respective wallpapers.

## Instructions to use
 1. Execute the script in the root directory where the subdirectories with the wallpapers are located.
 2. Make sure that you are not going to move/delete/modify the directory if you do you need to execute the script after 
    that.
 3. The subdirectories names are going to be used as XML filename and theme name, use descriptive names in the case you 
    need to modify it. 
 4. Make sure that the name of your files have an alphabetical order, it is recommended to use names like:

        - 01-light.png, 02-night.png
        - wallpaper-1.png, wallpaper-2.png
    To ensure alphabetical order avoid names like:

        * 5-light.png, 15-night.png
        * wallpaper-2.png, wallpaper-13.png
    The order that will be followed will be those with the number 1 first, that is, an ascending order for numbers in 
    the file name are not fulfilled.
 5. After generating the XML files use the bash script **copy_xml_to_system_dir.sh** as root in the current directory to move
    all the generated files to the system directory(/usr/share/gnome-background-properties/) or do it manually
 6. Enjoy

## Especial thanks to [@suchinton](https://github.com/suchinton) beceause this code was inspired by the script [WallC](https://github.com/suchinton/WallC)
 
