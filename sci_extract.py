from astropy.io import fits
import argparse

parser = argparse.ArgumentParser(description='Extract SCI image')
parser.add_argument('file', type=str, help='File name')
args = parser.parse_args()

file = args.file
file_out = f'{file}_sci.fits'

hdu = fits.open(file)

fits.writeto(file_out, hdu['SCI'].data, hdu['SCI'].header, overwrite=True)
