#  Copyright (C) 2017  Volkan Gezer <volkangezer@gmail.com>

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Prise en main
#
# 1. Spécifiez la valeur des paramètres ci-dessous :
origLang = "fr-FR" # langue source
targetLang = "en-GB" # langue cible
tmxfile = "tmx2tbx-sample.tmx" # nom du fichier .tmx
title = "Fiches terminologiques" # nom de la collection terminologique
note = "Fichier résultant d'une conversion TMX" # Note descriptive du contenu du fichier
term = "<seg>" # ne pas modifier
saveAs = "termes.tbx" # nom souhaité pour le fichier .tbx
index = 0 # id de la première entrée (pas d'incrémentation = 2)

# 2. Exécuter le script :
# python tmx2tbx3-fr.py



with open(tmxfile, "r") as f:
    searchfor = f.readlines()


with open(saveAs, 'w') as terms:
    terms.write('<?xml version=\'1.0\' encoding=\'UTF-8\'?>' + '\n')
    terms.write('<?xml-model href=\'TBX-Basic_dialect/DCA/TBXcoreStructV03_TBX-Basic_integrated.rng\' type=\'application/xml\' schematypens=\'http://relaxng.org/ns/structure/1.0\'?>' + '\n')
    terms.write('<?xml-model href=\'TBX-Basic_dialect/DCA/TBX-Basic_DCA.sch\' type=\'application/xml\' schematypens=\'http://purl.oclc.org/dsdl/schematron\'?>' + '\n')
    terms.write('<tbx style=\'dca\' type=\'TBX-Basic\' xml:lang=\'en-US\' xmlns=\'urn:iso:std:iso:30042:ed-2\'>' + '\n')
    terms.write(' <tbxHeader>' + '\n')
    terms.write('  <fileDesc>' + '\n')
    terms.write('   <titleStmt>' + '\n')
    terms.write('    <title>' + title + '</title>' + '\n')
    terms.write('    <note>' + note + '</note>' + '\n')
    terms.write('   </titleStmt>' + '\n')
    terms.write('  </fileDesc>' + '\n')
    terms.write(' </tbxHeader>' + '\n')
    terms.write(' <text>' + '\n')
    terms.write('  <body>' + '\n')
    for i, line in enumerate(searchfor):
        if term in line:
            if index % 2:
                activeLang = targetLang
            else:
                activeLang = origLang
                terms.write('   <conceptEntry id="' + str(index) + '">' + '\n')
            wordBeg = line.find('>') + 1
            wordEnd = line.find('<', wordBeg + 1)
            terms.write('     <langSec xml:lang="' + activeLang + '">' + '\n')
            terms.write('       <termSec>' + '\n')
            terms.write('         <term>' + line[wordBeg:wordEnd] + '</term>' + '\n')
            terms.write('       </termSec>' + '\n')
            terms.write('     </langSec>' + '\n')
            index = index + 1
            if activeLang == targetLang:
                terms.write('   </conceptEntry>' + '\n')
    terms.write('  </body>' + '\n')
    terms.write(' </text>' + '\n')
    terms.write('</tbx>' + '\n')
