import cv2
import datetime
import glob
import img2pdf
import numpy as np
import os
from PyPDF2 import PdfFileMerger
from PIL import Image
import sys


now = datetime.datetime.now()
d_name = now.strftime('%Y-%m-%d-%H-%M-%S')
os.mkdir(d_name)

args = sys.argv
length = len(args)

for i in range(1, length):
    img = cv2.imread(args[i], cv2.IMREAD_GRAYSCALE)
    name = args[i]

    if img is None:
        print('can\'t open file')
        sys.exit()

    ksize = 51
    blur = cv2.blur(img, (ksize, ksize))
    rij = img / blur
    index_1 = np.where(rij >= 0.91)
    index_0 = np.where(rij < 0.91)
    rij[index_0] = 0
    rij[index_1] = 255
    cv2.imwrite(d_name + '//' + str(i) + name, rij)

    os.chdir(d_name)
    pdf_name = str(i) + '.pdf'
    img = Image.open(str(i) + name)
    pp = img2pdf.convert(img.filename)
    file = open(pdf_name, "wb")
    file.write(pp)
    file.close()

    os.chdir('../')

os.chdir(d_name)
pdf_file_merger = PdfFileMerger()

for filename in glob.glob('*.pdf'):
    pdf_file_merger.append(filename)

pdf_file_merger.write('merge.pdf')
pdf_file_merger.close()
