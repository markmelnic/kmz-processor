from kmz_processor import KMZ

kmz = KMZ()
item = kmz.coords_item((52.370216, 4.895168))
image = kmz.load_images(item[1], single=True, neighbours=True)
