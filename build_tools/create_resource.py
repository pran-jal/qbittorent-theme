

def create_resource_file(files, path = None):

    if not path:
        path = "resource.qrc"

    with open(path, 'w') as res_file:
        res_file.write('<!DOCTYPE RCC><RCC version="1.0">\n')
        res_file.write('\t<qresource>\n')

        if files:
            for file in files:
                if file.get("alias"):
                    res_file.write(f"\t\t<file alias='{file['alias']}'>{file['name']}</file>\n")
                else:
                    res_file.write(f"\t\t<file>{file['name']}</file>\n")

        res_file.write('\t</qresource>\n')
        res_file.write('</RCC>\n')