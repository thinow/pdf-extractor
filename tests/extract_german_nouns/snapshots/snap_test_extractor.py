# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_extract_nouns_from_sample[sample-0.txt] 1'] = '''Ablenkung\tdie
Ablenkungsmanöver\tdas
Ableser\tder
Handlung\tdie
Ableserin\tdie
Ablesung\tdie
Ablieferung\tdie
Ablöse\tdie
Ableugnung\tdie
Ablichtung\tdie
Ablieferungstermin\tder
Ablösesumme\tdie
Ablösung\tdie
Ablösungssumme\tdie
Abluft\tdie
Ablufttrockner\tder
Abmachung\tdie
Abmagerung\tdie
Abmahnung\tdie
Abmagerungskur\tdie
Abmarsch\tder
Abmeldung\tdie
Abmelkwirtschaft\tdie
Abmessung\tdie
Abmilderung\tdie
Abmoderation\tdie
'''

snapshots['test_extract_nouns_from_sample[sample-1.txt] 1'] = '''Aufbietung\tdie
Aufblähung\tdie
Aufblende\tdie
Aufblick\tder
Aufbauschule\tdie
Aufbauspiel\tdas
Aufbauspieler\tder
Aufbauspielerin\tdie
Aufbaustudium\tdas
Aufbaustufe\tdie
Aufbautraining\tdas
Aufbereitung\tdie
Aufbereitungsanlage\tdie
Aufbesserung\tdie
Aufbewahrung\tdie
Aufbewahrungsort\tder
Aufbewahrungsraum\tder
'''
