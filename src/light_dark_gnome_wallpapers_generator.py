import os

curr = os.getcwd()
my_list = os.listdir(curr)
welcome_message = """Hello User, this script will generate the xml for Light/Dark Wallpapers for Gnome 42+,
The following steps are recommended to be followed:
 1. Execute the script in the root directory where the subdirectories with the wallpapers are located.
 2. Make sure that you are not going to move/delete/modify the directory if you do you need to execute the script after 
    that.
 4. The subdirectories names are going to be used as XML filename and theme name, use descriptive names in the case you 
    need to modify it. 
 3. Make sure that the name of your files have an alphabetical order, it is recommended to use names like:
        * 01-light.png, 02-night.png
        * wallpaper-1.png, wallpaper-2.png
    To ensure alphabetical order avoid names like:
        * 5-light.png, 15-night.png
        * wallpaper-2.png, wallpaper-13.png
    The order that will be followed will be those with the number 1 first, that is, an ascending order for numbers in 
    the file name are not fulfilled.
 4. After generating the XML files use the bash script copy_xml_to_system_dir.sh as root in the current directory to move
    all the generated files to the system directory(/usr/share/gnome-background-properties/) or do it manually
 5. Enjoy"""

print(welcome_message)
for directory in my_list:
    sub_directory = os.path.join(curr, directory)
    if not os.path.isfile(sub_directory):
        files = os.listdir(sub_directory)
        files.sort()
        if len(files) == 2:
            xml_to_generate = """<?xml version="1.0"?><!DOCTYPE wallpapers SYSTEM "gnome-wp-list.dtd"><wallpapers><wallpaper deleted="false"><name>"""+directory+"""</name><filename>""" + os.path.join(sub_directory,files[0]) + """</filename><filename-dark>""" + os.path.join(sub_directory,files[1]) + """</filename-dark><options>zoom</options><shade_type>solid</shade_type><pcolor>#3465a4</pcolor><scolor>#000000</scolor></wallpaper></wallpapers>"""
            with open(directory+".xml","w") as new_file:
                new_file.write(xml_to_generate)

