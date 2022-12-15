from astropy.io import fits

files = input("file names : ")

a = fits.open(files)

fits.writeto(files, a[1].data, a[1].header, overwrite=True)
