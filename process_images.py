import rasterio

def process_image(image_path):
    with rasterio.open(image_path) as src:
        print(f'Number of bands: {src.count}')
        print(f'Bands: {src.indexes}')

        red = src.read(1)
        nir = src.read(2)

        ndvi = (nir.astype(float) - red.astype(float)) / (nir + red)

        ndvi_image_path = 'NDVI_outputs/ndvi_output.tif'
        with rasterio.open(
            ndvi_image_path, 'w',
            driver='GTiff',
            height=ndvi.shape[0],
            width=ndvi.shape[1],
            count=1,
            dtype=ndvi.dtype,
            crs=src.crs,
            transform=src.transform
        ) as dst:
            dst.write(ndvi, 1)

        print(f'NDVI image saved as {ndvi_image_path}')

if __name__ == '__main__':
    image_path = 'image_input/Satellite_image.tif'
    process_image(image_path)
